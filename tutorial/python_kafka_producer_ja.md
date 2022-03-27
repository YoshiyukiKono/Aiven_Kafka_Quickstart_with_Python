# Python Kafkaプロデューサー

## 概要

Aiven Kafkaクラスターへのデータフィードを行うシミュレーション用のプログラムを作成します。
プログラムは、Kafka Producerの役割を持ちます。今回のチュートリアルでは、AivenのKafkaトピックに送信されたデータの確認は、Aiven Webコンソールの機能を利用して行うため、Kafka Consumerの作成は行いません。

## データ

[HASC(Human Activity Sensing Consortium)](http://hasc.jp/)が提供するオープンデータを利用します。

HASCは、人間行動理解のための装着型センサによる大規模データベース構築を目的とするコンソーシアムです。

「[2010corpus](http://hasc.jp/hc2010/HASC2010corpus/hasc2010corpus.html)」ダウンロードすることのできる加速度データのひとつ(HASC1001.csv)を利用します。

## 仕様

シミュレーターは、Kafkaトピックに対して、JSON形式のメッセージを送信します。

### センサーデータ

csv形式のデータは以下の内容を持ちます（ヘッダーは含まれていません）。

```
[検測時刻(sec)],[X軸(G)],[Y軸(G)],[Z軸(G)]
```

### メタデータ

センサーデータに加えて、以下のメタデータを含めます。

- メッセージID(UUID)
- 送信時刻

## プログラム解説

チュートリアルは、Pythonプログラム([producer.py](../producer/producer.py))を提供します。

### Aiven Kafka接続情報編集

プログラムを利用する場合、Aiven Kafkaクラスターへの接続情報を編集する必要があります。

`ProducerSimilator`クラス のコンストラクターへの引数`bootstrap_servers`を適切な名前に変更します。

```
    producer_simulator = ProducerSimulator("./HASC1001.csv", 
                                     "sensor", bootstrap_servers=['YOUR_SERVICE_NAME.aivencloud.com:10779'],
                                     value_serializer=lambda x: json.dumps(x).encode('utf-8'),
                                     security_protocol="SSL",
                                     ssl_cafile=cert_folder+'/ca.pem',
                                     ssl_certfile=cert_folder+'/service.cert',
                                     ssl_keyfile=cert_folder+'/service.key',
                                    )
```

また、以前のステップで取得した下記のファイルを利用します。producer.pyと同じ場所に置きます。

- ca.pem
- service.cert
- service.key



## 実行と終了

実行すると以下の様に、コンソールに送信するメッセージが表示されます。

```
>python producer.py
Simulation running
json message: {'_id': '438e5cb9-beab-42e8-8bf8-2a1f6fce6e85', '_date': '2022-03-27T11:37:32.919642', 'sec': '9656.196248', 'X': '-0.905609', 'Y': '-0.199234', 'Z': '0.144897'}
json message: {'_id': 'c68101b0-fec4-4854-9451-2840699eb072', '_date': '2022-03-27T11:37:33.934667', 'sec': '9656.206375', 'X': '-0.905609', 'Y': '-0.163010', 'Z': '0.181122'}
json message: {'_id': '04946e55-f0c0-4eb0-96be-6ab2230d140f', '_date': '2022-03-27T11:37:34.935639', 'sec': '9656.217099', 'X': '-0.923721', 'Y': '-0.126785', 'Z': '0.217346'}
json message: {'_id': '1c056ea8-44d1-4f18-b89e-671eabc242df', '_date': '2022-03-27T11:37:35.936760', 'sec': '9656.226533', 'X': '-0.905609', 'Y': '-0.090561', 'Z': '0.144897'}
```


シミュレーションを終了するには、Ctrl+Cを入力します。

[目次へ戻る](./contents_ja.md)
