## Checking messages on Aiven Web Console

Now let's see how you can see the status on the web console while the data feed to Aiven Kafka is running.

### Topic list

Kafka's data feeds are sent from the sender (Producer) to the receiver (Consumer) via a specific "topic".

Open the Kafka service details screen (Service View).
From the "Topics" tab, you can check the topic list and status information as shown below.


<img src = "https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/176567/4774dc73-570d-bd9f-f0ba-9ea173563bb4.png" width = 70%>


#### Topic information

You can select a specific topic for farther information.


<img src = "https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/176567/ce11ab83-06d6-3887-b189-2b384f706cbc.png" width = 70%>


#### Message content

By pressing the "Messages" button at the top right of the topic details screen above, you can display the content of the messages sent to that topic.


<img src = "https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/176567/de49479f-b42b-d07c-38ec-a89fa241c964.png" width = 70%>


Change the filter settings as appropriate (going with the defaults here), and press "Produce Messages" in the upper right.

Messages are displayed as shown below (only the first line is cut out here).



<img src = "https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/176567/41f4b4c2-74bf-83f2-42ee-301844249959.png" width = 70%>


You can check the content of the message by turning on the "Docode from base64" toggle button.


<img src = "https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/176567/bb70e7be-bd38-03cd-acea-5043329896de.png" width = 50%>


[Back to Tabele of Contents](./contents_en.md)
