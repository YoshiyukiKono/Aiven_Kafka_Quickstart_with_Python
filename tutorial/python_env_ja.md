## Pythonプログラミング環境

チュートリアルで使う、Pythonプログラミング環境について説明します。

今回のチュートリアルの確認済みの依存関係は以下の通りです。

- Python: 3.10.0
- kafka-python: 2.0.2

Pythonプログラミングについて詳しい方は、次のステップに進むこともできます。

なお、以降の記述は、Windows環境で確認された内容に基づいています。
既知の環境による違いについては注釈しています。


### 仮想環境

Anacondaがインストールされた環境でcondaを使った仮想環境のセットアップについて説明します。
Anacondaのインストールについては[ドキュメント](https://docs.anaconda.com/anaconda/install/index.html)を参照ください。

以下の様に、仮想環境を作成します。

```
>conda create -n aiven python=3
```

作成された仮想環境を起動します。

```
>activate aiven
```

MacOSの時は、以下のようになります。

```
$ source activate aiven
```

### パッケージインストール

仮想環境上でkafka-pythonをインストールします。

```
(aiven) ...>pip install kafka-python
```


[目次へ戻る](./contents_ja.md)
