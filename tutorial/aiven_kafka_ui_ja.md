Aiven Kafka UI解説

### Kafkaクラスター構築

## サービス構築

Aivenサービスは、Aiven Webコンソールで管理されます。
サインアップで作成した認証情報(メールアドレスとパスワード)で、コンソールにログインすると、まず[サービス]ビューが表示されます。
すでに作成されている場合は、サービスのリストが表示されます。

Kafkaサービスを作成します。サービスのセットアップは、他のサービスと共通の部分が多いため、

サービスタイプとしてKafkaを選択します。使用するバージョンを選択することもできます。

サービスを実行するクラウドプロバイダーとリージョンを選択します。
料金は、プロバイダーや地域によって異なる場合があります。コンソールの右側にあるサービスの概要には、選択したオプションの料金が表示されます。

サービスプランを選択します。これは、サーバーの数と、サービスに割り当てられるメモリ、CPU、およびディスクリソースの種類を定義します。

サービスの名前を入力します。デフォルトではランダムな名前が提供されます。
認識しやすい名前に変更できます。ここでは、「test」に置き換えています。

コンソールの右側にある概要の下にある[サービスの作成]をクリックします。これにより、サービスビューに戻ります。作成中であることを示すステータスインジケータとともに新しいサービスが、リストに表示されます。

サービスの構築中に、サービスの[Overview(概要)]タブにアクセスして、ステータスが「REBUILDING」から「RUNNING」に変化することを確認できます。

構築後下記のように、新しいサービスが追加されたのが分かります。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/176567/ec303810-7b79-3eb3-0883-96923d0393bb.png)

### Kafkaデータフィードシミュレーション

クラスターの実際の動作を確認するには、Kafkaへのデータフィードが行われることが必要です。

これについては、技術的にまた別のトピックとなるため、本稿では割愛しますが、ここで利用しているシミュレーション用のプログラムと構築手順を下記で公開していますので、興味のある方は、ご覧ください。

https://github.com/YoshiyukiKono/Aiven_Kafka_Quickstart_with_Python

## Kafka設定

### 接続情報確認

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/176567/4279227d-8149-535d-73c9-b934598c34b9.png)

ここでは、以下のＵＲＬです。

>kafka-test-yoshiyuki-e281.aivencloud.com:10779

高度な設定。`auto_create_topics_enable`の有効化。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/176567/446d43c7-cad7-1bec-2eef-f45ae9ce90ed.png)



![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/176567/833d3bc7-e366-4810-92f2-db3b5dd127ea.png)

トピックリスト。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/176567/3206ff70-b744-5b84-dd50-7e92d8dd7b54.png)

トピック情報。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/176567/c5b36885-4472-fb3c-6a2a-22f852279c01.png)

REST有効化。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/176567/35ef6756-0bb1-df61-319c-66caa4f3737a.png)

メッセージ内容確認。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/176567/ac98303f-8861-d8fc-8165-b6588148ddfe.png)



