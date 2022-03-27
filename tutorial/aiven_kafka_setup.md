## Aiven Kafka setup

### Aiven Web Console login

Aiven users can use Aiven web console to manage Aiven services.

When you log in to the console with the credentials (email address and password) that you created when you signed up, you will see the Services list first.
Initially the list is empty, but if it has already been created, you will see a list of services as shown below (Only Kafka service is used for this tutorial).


<img src = "https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/176567/8b0e55a3-ac3d-50c7-961c-18feca9979ec.png" width = 50%>

### New service creation

Here, we will create a Kafka service.

Click the "+ Create a new service" button at the top right of the Services screen.

### Service selection

First, select the Kafka service.


<img src = "https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/176567/e64d98f5-8762-7469-06da-013b2b1e2992.png" width = 50%>

You can also select the version to use from the pull-down (use default for this tutorial).



<img src = "https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/176567/0eb9bd4e-4574-58cf-6346-3ceff0e56195.png" width = 50%>

### Cloud provider selection

Select the cloud provider for the service.
You have a wide range of options, as follows.


<img src = "https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/176567/b4114abf-0fb5-f6f0-bc73-47a7c9b5242f.png" width = 50%>

Here, we will use Google Cloud.

### Region selection

Then select a region.


<img src = "https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/176567/bab42dab-67c4-e874-9d07-f65e10588a0a.png" width = 50%>


Prices may vary by provider and region.
The service summary on the right side of the console shows the pricing for the selected option.


<img src = "https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/176567/36694952-006b-ea3f-9135-1024cfc957dc.png" width = 30%>

### Service plan selection

Next, select a service plan.

There are categories like startups, businesses, and premiums,
It presents a wide range of combinations of the number of servers and the memory, CPUs, nodes, disk resources, etc..


<img src = "https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/176567/a827fa1d-fb70-4f61-e81c-18636035ae61.png" width = 50%>

Here, select "Startup-2" on the Startup tab.

### Service name

Enter the name of the service. A random name is provided by default.
You can change the name to something that is easy to recognize. Here, it is replaced with "test".



<img src = "https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/176567/e181391e-a304-8ef3-2ea4-3cfda30180bd.png" width = 50%>

### Service creation execution and confirmation

Finally, click "+ Create Service" under the Service Summary on the right side of the console.

The new service will be added to the service list as shown below.

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/176567/ec303810-7b79-3eb3-0883-96923d0393bb.png)

It will take some time before the service is available.
The status indicator allows you to check the creation status.

While building a service, you can select a specific service screen from the service list to display the screen for that service.
Access the Overview tab, verify that the status is "RUNNING", and start using the service.

### Kafka Cluster Configuration

#### Connection information

On the Overview tab, you can check the connection information to the Aiven Kafka cluster. It is used later whan you use the Python program provided by this tutorial.


<img src = "https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/176567/4279227d-8149-535d-73c9-b934598c34b9.png" width = 50%>

Here, the following "Service URI" is displayed. You will use your own URI.

> kafka-test-yoshiyuki-e281.aivencloud.com: 10779

You can also download the Access Key, Access Certificate, and CA Certificate.

You will use these from the Python program in a later step.


#### Basic settings: REST enablement

Following the connection information, basic setting items are lined up.


<img src = "https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/176567/d0214ecb-d54b-0915-89e6-3784a9ffe2ee.png" width = 50%>

Enable the REST API to see the content of the messages fed to your Kafka cluster in a later step.



<img src = "https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/176567/35ef6756-0bb1-df61-319c-66caa4f3737a.png" width = 50%>

#### Advanced settings

At the end of the Overview screen, there is an Advanced configuration section.
Here, enable `auto_create_topics_enable` as shown below to simplify the preparation on the cluster side when executing the data feed program.


<img src = "https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/176567/446d43c7-cad7-1bec-2eef-f45ae9ce90ed.png" width = 50%>

When adding a new setting item, click the "+ Add configuration option" link, then setting candidates will be displayed as shown below.

<img src = "https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/176567/d659102e-141d-f706-686b-7c82952a1668.png" width = 50%>

You've completed the Kafka cluster setup.


[Back to Tabele of Contents](./contents_en.md)
