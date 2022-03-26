# Aivenで体験するKafkaクラスター構築と監視

## はじめに

Apache Kafkaは、データストリーミング技術の主要な構成要素として、広く使われています。

本稿では、Kafkaクラスターの構築と監視が、Aivenのサービスを利用することでいかに容易に達成できるかを、ご覧に入れます。

### Aivenとは何か？

Aivenは、Apache KafkaやCassandra、Elasticsearch、M3、PostgreSQLといった人気の高いオープンソースプロジェクトのフルマネージドサービスを、様々なパブリッククラウドで提供します。

### Aiven Kafka


### Aivenで利用できる監視用テクノロジースタック

Aivenは、広く使われているシステム監視ダッシュボードGrafanaサービスを提供しています。今回、これを利用します。

Grafanaダッシュボードで表示するメトリックスデータとして、InfluxDBとPostgresQLがありますが、今回はInfluxDBサービスを利用しています。


## ステップバイステップ

以下では、実際の画面操作イメージを交えながら、

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/176567/ec303810-7b79-3eb3-0883-96923d0393bb.png)

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/176567/4279227d-8149-535d-73c9-b934598c34b9.png)

kafka-test-yoshiyuki-e281.aivencloud.com:10779

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/176567/1a551dad-f806-ed1a-dff2-931ecde883b8.png)

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/176567/d3936c12-289e-7e77-43e8-994a0a3fa24e.png)

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/176567/ceba3f22-90e1-c597-7ea0-e6f9ab114576.png)

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/176567/c8e19c3a-eb9b-9510-256d-00b0143b1888.png)

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/176567/704e4619-c7e2-7ebc-1bba-51678fcfaf28.png)

#### Kafka

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/176567/446d43c7-cad7-1bec-2eef-f45ae9ce90ed.png)

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/176567/833d3bc7-e366-4810-92f2-db3b5dd127ea.png)

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/176567/3206ff70-b744-5b84-dd50-7e92d8dd7b54.png)

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/176567/c5b36885-4472-fb3c-6a2a-22f852279c01.png)

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/176567/35ef6756-0bb1-df61-319c-66caa4f3737a.png)

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/176567/ac98303f-8861-d8fc-8165-b6588148ddfe.png)

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/176567/decf29aa-0213-32dd-01d2-ae0d0e1c31f9.png)


>WARNING
>All data on the cluster and all topic data and configuration will be lost on power off.

### Aivenトライアル

30日間の無料トライアルが用意されています。300$分のクレジットが自動的に与えられます。

https://console.aiven.io/signup

### Kafkaプロデューサー

実演には、Kafkaへのデータのフィードが必要です。

今回は、私が作成したデモ用プログラムを利用します。プログラムは、以下で公開しています。

リポジトリには、プログラムの利用手順の解説を含んでいます。

## Aiven利用ステップバイステップ

### 参考情報

https://developer.aiven.io/docs/products/grafana/get-started.html

## サービス統合(Service Integrations)とは
 
https://help.aiven.io/en/articles/1456441-getting-started-with-service-integrations

サービス統合は、さまざまなAivenサービスを相互に接続することにより、追加の機能を提供します。

メトリクスの統合により、Aivenユーザーは高度なテレメトリデータをInfluxDBメトリクスデータベースに送信し、Grafanaで視覚化できます。テレメトリデータは現在、Aiven for Apache Kafka、Aiven for PostgreSQL 、Aiven for MySql、Aiven for Cassandra、Aiven for ElasticSearch、Aiven for Redisなどでサポートされています。

この記事では例としてKafkaを使用していますが、同じ機能が他のサービスでも機能します。 。  

メトリックの統合に加えて、ログの統合もサポートされています。ログ統合により、任意のAivenサービスからAiven for Elasticsearchにログを送信し、Kibanaフロントエンドを使用してログを検索できます。

### 利点

Aivenは、Aiven Webコンソールのサービスビューの[メトリック]タブで、すべてのサービスの基本的なホストレベルのリソースメトリック（CPU、メモリ、ディスク、およびネットワーク）を自動的に提供します。 

高度なテレメトリ機能は、Aivenユーザーにはるかに詳細なサービス固有のメトリックを提供し、Aivenユーザーはサービスの動作にドリルダウンして、問題とパフォーマンスのボトルネックを特定できます。

以下に概説する手順に従うことで、高度なテレメトリ統合の使用を開始するのは非常に簡単です。始めましょう！

## 入門
開始するには、次の3つのサービスが必要です。

Aiven forApache Kafka-テレメトリデータを生成するサービス

Aiven for InfluxDB / PostgreSQL-テレメトリデータが保存され、そこからクエリできるデータベース

Aiven for Grafana-テレメトリデータのダッシュボード

注1：現在、これらのサービスは同じAivenプロジェクトで実行する必要がありますが、この制限は将来削除され、たとえば、異なるプロジェクトの複数のKafkaサービスを同じInfluxDB/PostgreSQLおよびGrafanaに接続できるようになります。インスタンス。

注2：この例では、テレメトリデータの収集ポイントとしてInfluxDBを使用します。PostgreSQLを使用する場合も同じ手順が適用されます。

Kafkaから始めて、3つのサービスを開始しましょう。


次に、InfluxDBサービスを起動します。


そして最後に、Grafanaサービス：


数分後、3つの新しいサービスがすべて実行されます。


注：サービス統合機能は、各サービスのスタートアップ、ビジネス、およびプレミアムプランでのみ使用できます（つまり、ホビーイストサービス層では使用できません）。

サービスが起動したら、InfluxDBサービスの概要ページを開き、その中に[サービス統合]セクションを見つけます。


現在、まだアクティブ化されていないため、ステータスは「アクティブなサービス統合なし」です。[統合の管理]ボタンをクリックすると、使用可能な統合のリストが開きます。


ここでは、InfluxDBサービスで利用できるサービス統合と、有効になっているサービス統合を確認できます。


まず、InfluxDBサービスのGrafanaダッシュボードを有効にします。Grafanaアイコンをクリックして、正しいサービスを選択するだけで十分です。


これで、Grafanaダッシュボードが稼働しました。次に、Kafkaサービスからメトリックを受信できるようにします。


繰り返しになりますが、Kafkaアイコンをクリックして、正しいサービスを選択するだけで十分です。


高度なKafkaテレメトリデータをInfluxDBサービスに流すために必要なのはこれだけです。[閉じる]ボタンを押して、統合ダイアログを閉じます。

次に、Grafanaダッシュボードを開いて、サービスリストに戻り、Grafanaサービスを選択してデータを表示します。


[接続パラメータ]セクションで、パスワードアイコンをクリックして、 Grafanaへのログインに必要なパスワードを確認します。 

パスワードをコピーして、後でGrafanaログインダイアログに貼り付けることができるようにします。また、Grafanaのデフォルトのユーザー名は「avnadmin」であることに注意してください。

次に、ホストの横にあるリンクをクリックして、Grafanaログインダイアログへのブラウザページを開きます。


ユーザー名として「avnadmin」と入力し、Grafanaパスワードをパスワードフィールドに貼り付けて、Grafanaにログインします。 

Grafanaのデフォルトビューが開き、1つのダッシュボードが使用可能であることが示されます。


ダッシュボード名「AivenKafka-demo-kafka-Resources」をクリックして、Kafkaメトリックダッシュボードを開きます。


このダッシュボードは、Aivenによって自動的に維持される事前定義されたビューです。

統合を有効にしたばかりの場合は、ダッシュボードビューへのデータの取得を開始するのに1分かかる場合があることに注意してください。右上隅にあるリロードボタンを押すと、ビューを更新できます。

カスタムダッシュボードを追加するには、Grafanaで最初から定義するか、事前定義されたダッシュボードのコピーを「Aiven」で始まらない別の名前で保存します。 

注意：事前定義されたダッシュボードに加えた変更は、最終的にシステムによって自動的に上書きされます。

よくある質問
サービス統合はどのように請求されますか？何か余分な費用がかかりますか？

高度なテレメトリデータと事前定義されたダッシュボードには追加料金はかかりませんが、InfluxDBとGrafanaサービスが必要です。これらのサービスは、通常のAivenサービスとして1時間ごとに請求されます。

独自のメトリックダッシュボードを定義できますか？

はい。事前定義されたダッシュボードを開始点として使用し、それらを別の名前で保存するか、最初から作成することができます。タイトルが「Aiven」で始まるダッシュボードは自動的に管理されるため、ダッシュボードには別の名前を付けることをお勧めします。

InfluxDBでテレメトリデータに直接アクセスできますか？

はい。InfluxDBサービスは、通常のInfluxDBデータベースサービスであり、任意のInfluxDBクライアントソフトウェアまたは独自のアプリケーションやスクリプトを介してアクセスできます。データなどに対して複雑なクエリを実行できます。



## Getting Started for Kafka
Aivenサービスは、AivenWebコンソールで管理されます。メールアドレスとパスワードを使用してコンソールに最初にログインすると、[ サービス]ビューが表示され、現在選択されているプロジェクトのすべてのサービスが表示されます。

ApacheKafka®サービス用の新しいAivenを作成します。

サービスタイプとしてKafkaを選択します。使用するバージョンを選択することもできます。

サービスを実行するクラウドプロバイダーとリージョンを選択します。

ノート

同じサービスの料金は、プロバイダーや地域によって異なる場合があります。コンソールの右側にあるサービスの概要には、選択したオプションの料金が表示されます。

サービスプランを選択します。これは、サーバーの数と、サービスに割り当てられるメモリ、CPU、およびディスクリソースの種類を定義します。

サービスの名前を入力します。デフォルトではランダムな名前が提供されていますが、他のサービスと区別するために、よりわかりやすい名前を入力できます。

コンソールの右側にある概要の下にある[サービスの作成]をクリックします。これにより、サービスビューに戻ります。新しいサービスは、作成中であることを示すステータスインジケータとともに一覧表示されます。

サービスの構築中に、サービスの概要ページにアクセスして、ステータスがREBUILDINGからRUNNINGに変化することを確認できます。

次のステップ
サンプルプロジェクトをチェックして、アプリケーションを接続するためのコードサンプルを見つけてください。

サンプルデータジェネレータプロジェクトを試して、開始するためのデータを提供してください。

