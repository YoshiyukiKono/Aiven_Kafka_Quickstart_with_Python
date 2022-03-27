### メッセージ確認

ここで、Aiven Kafkaへのデータフィードが実行されている状態で、どのようにWebコンソールから状況を確認できるかを見ていきます。

#### トピックリスト

Kafkaのデータフィードは、特定の「トピック」を介して、送信側(Producer)と受信側(Consumer)との間でやりとりされます。

Kafkaサービスの詳細画面(サービスビュー)を開きます。
[Topics]タブから、以下の様にトピックのリストとステータス情報等を確認できます。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/176567/4774dc73-570d-bd9f-f0ba-9ea173563bb4.png)

#### トピック情報

特定のトピックを選択して、詳細情報を確認することができます。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/176567/ce11ab83-06d6-3887-b189-2b384f706cbc.png)


#### メッセージ内容確認

上掲のトピック詳細画面右上の[Messages]ボタンを押下することで、そのトピックに送信されたメッセージの内容を表示することができます。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/176567/de49479f-b42b-d07c-38ec-a89fa241c964.png)

適宜フィルター設定を変更し(ここではデフォルトのまま試しています)、右上の[Produce Messages]を押下します。

下記のように、メッセージが表示されます（メッセージは複数行に渡って表示されますが、煩雑にならないよう、ここでは1行目のみを切り取っています）。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/176567/41f4b4c2-74bf-83f2-42ee-301844249959.png)

[Docode from base64]トグルボタンをオンにするとメッセージの内容が確認できます。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/176567/bb70e7be-bd38-03cd-acea-5043329896de.png)


