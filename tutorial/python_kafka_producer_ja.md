# Python Kafkaプロデューサー

## 仕様

## データ

[HASC(Human Activity Sensing Consortium)](http://hasc.jp/)が提供するオープンデータ「[2010corpus](http://hasc.jp/hc2010/HASC2010corpus/hasc2010corpus.html)」を利用します。

HASCは、人間行動理解のための装着型センサによる大規模データベース構築を目的とする

加速度データ(*.csv)
データの構成
csv形式
[時刻(sec)],[X軸(G)],[Y軸(G)],[Z軸(G)]
1.0(G)≒9.80665(m/s2)
学習データ：20秒分,シーケンスデータ：120秒分
サンプリングレート：10~100(Hz)

## kafka-pythonパッケージ


## 実装解説

### kafka-pythonパッケージ


### メッセージＩＤと送信時刻
```
```
### センサー情報
```
```

### Aiven Kafka接続情報

### Producerクラス

## 実行と終了
