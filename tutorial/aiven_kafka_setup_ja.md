## Aiven Kafkaセットアップ

#### Aiven Webコンソールログイン

Aivenサービスは、Aiven Webコンソールで管理されます。
サインアップで作成した認証情報(メールアドレスとパスワード)で、コンソールにログインすると、まず[サービス]ビューが表示されます。
始めの状態ではリストは空ですが、すでに作成されている場合は、以下のようにサービスのリストが表示されます（今回は最終的にこれらの３つのサービスを利用します）。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/176567/8b0e55a3-ac3d-50c7-961c-18feca9979ec.png)

#### 新しいサービスの作成

ここでは監視対象として、Kafkaサービスを作成します。
サービスのセットアップの基本的な流れは、他のサービスでも共通です。

[サービス(Services)]画面右上の「+ Create a new service」ボタンを押下します。

#### サービスの選択

まず、サービスを選択します(ここでは、Kafkaを選択します)。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/176567/e64d98f5-8762-7469-06da-013b2b1e2992.png)

プルダウンで使用するバージョンを選択することもできます。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/176567/0eb9bd4e-4574-58cf-6346-3ceff0e56195.png)

#### クラウドプロバイダーの選択

サービスを実行するクラウドプロバイダーを選択します。
以下のように幅広い選択肢があります。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/176567/b4114abf-0fb5-f6f0-bc73-47a7c9b5242f.png)

ここではGoogle Cloudを利用します。

#### リージョンの選択

次にリージョンを選択します。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/176567/bab42dab-67c4-e874-9d07-f65e10588a0a.png)


料金は、プロバイダーや地域によって異なる場合があります。
コンソールの右側にあるサービスの概要には、選択したオプションの料金が表示されます。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/176567/36694952-006b-ea3f-9135-1024cfc957dc.png)

#### サービスプラン選択

サービスプランを選択します。

スタートアップ、ビジネス、およびプレミアムのようにカテゴライズされ、
サーバーの数と、サービスに割り当てられるメモリ、CPU、ノード数、ディスクリソース等の幅広い組み合わせが提示されます。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/176567/a827fa1d-fb70-4f61-e81c-18636035ae61.png)

ここでは、スタートアップタブの「Startup-2」を選択しました。

（Kafkaサービスの場合は存在していませんが）PostgreSQLのような他のサービスには、スタートアップ、ビジネス、プレミアムの他に、スモールテスト用のホビースト(Hobbyist)カテゴリーも提示されるものがあります。ここで、サービス統合機能利用に関して、留意点があります。サービス統合機能は、各サービスのスタートアップ、ビジネス、およびプレミアムプランでのみ使用でき、ホビーイストプランでは使用できません。

#### サービス名

サービスの名前を入力します。デフォルトではランダムな名前が提供されます。
認識しやすい名前に変更できます。ここでは、「test」に置き換えています。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/176567/e181391e-a304-8ef3-2ea4-3cfda30180bd.png)

#### サービス作成実行と確認

最後にコンソールの右側の[サービスサマリー]の下にある[サービスの作成(+ Create Service)]をクリックします。

サービスリストに下記のように、新しいサービスが追加されます。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/176567/ec303810-7b79-3eb3-0883-96923d0393bb.png)

サービスが利用できるまでには、少しだけ時間がかかります。
ステータスインジケータによって、作成状況を確認できます。

サービスの構築中にも、サービスリストから特定のサービス画面を選んで、そのサービスの画面を表示することができます。
[概要(Overview)]タブにアクセスして、ステータスが「RUNNING」であることを確認し、そのサービスを利用開始します。

### Aiven Webコンソール解説

ここからは、サービスの設定や状態確認のために、Aiven Webコンソールを利用する方法を見ていきます。

#### 接続情報確認

[Overview]タブでは、まず初めに、Aivenサービスを外部システムと連携するための、Aivenクラスターへの接続情報[Connection Information]を確認することができます。


![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/176567/4279227d-8149-535d-73c9-b934598c34b9.png)

ここでは、以下の[Service URI]が表示されています。

>kafka-test-yoshiyuki-e281.aivencloud.com:10779

また、[Access Key]、[Access Certificate]、[CA Certificate]をダウンロードすることができます。

これらを、後のステップで開設するPythonプログラムから利用します。


#### 基本設定: REST有効化

接続情報に続き、基本的な設定項目が並んでいます。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/176567/d0214ecb-d54b-0915-89e6-3784a9ffe2ee.png)

後で、Kafkaクラスターにフィードされたメッセージの内容を確認するために、REST APIを有効化します。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/176567/35ef6756-0bb1-df61-319c-66caa4f3737a.png)

#### 高度な設定

[Overview]画面の最後に、[高度な設定(Advanced configuration)]セクションがあります。
ここでは、以下のように、データフィードプログラム実行時のクラスター側の準備を簡略化するため`auto_create_topics_enable`（トピック自動作成）を有効化します。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/176567/446d43c7-cad7-1bec-2eef-f45ae9ce90ed.png)

新しい設定項目を追加する際には、[+ Add configuration option]リンクをクリックすると、以下の様に設定の候補が表示されます。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/176567/d659102e-141d-f706-686b-7c82952a1668.png)

以上で、今回のセットアップが完了しました。

[目次へ戻る](./contents_ja.md)
