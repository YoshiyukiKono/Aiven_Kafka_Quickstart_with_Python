# Article: Aiven Kafka and Observability

## Introduction

### Goal of this article

Apache Kafka is widely used as a key component of data streaming technology.

In this article, we'll look at how easy it is to visualize Kafka's data with Aiven's services.

In this article, trademark notation etc. are omitted.

### What is Aiven?

Aiven offers fully managed services for popular open source projects such as Apache Kafka, Cassandra, Elasticsearch, M3 and PostgreSQL in a variety of public clouds.

### Aiven Kafka

Aiven offers Kafka as a managed service.



### Aiven's technology stack for system monitoring

Aiven offers the widely used system monitoring dashboard Grafana service. This time, I will use this.

InfluxDB and PostgresQL are the metrics data displayed on the Grafana dashboard, but this time we are using the InfluxDB service.

### What are Service Integrations?
 
Service integration provides additional functionality by interconnecting various Aiven services.

Metrics integration allows Aiven users to send advanced telemetry data to the InfluxDB metrics database for visualization in Grafana. Telemetry data is currently supported by Aiven for Apache Kafka, Aiven for PostgreSQL, Aiven for MySql, Aiven for Cassandra, Aiven for ElasticSearch, Aiven for Redis, and more.

This article uses Kafka as an example, but the same functionality works for other services.

In addition to metric integration, log integration is also supported. Log consolidation allows any Aiven service to send logs to Aiven for Elasticsearch and use the Kibana front end to search the logs.

Finally, the following points and information regarding the use of the service integration function are shown.

--The service integration feature is only available in each service's startup, business, and premium plans (that is, not in the hobbyist service tier).
――In addition, it goes without saying that costs will be incurred for each of the services to be integrated, and no additional costs will be charged for using the service integration function itself.

### About metrics in Aiven

Aiven automatically provides basic host-level resource metrics (CPU, memory, disk, and network) for all services on the Metrics tab of the Services view of the Aiven web console.

Advanced telemetry capabilities provide Aiven users with much more detailed service-specific metrics that allow Aiven users to drill down into service behavior and identify problem and performance bottlenecks.

### Aiven Trial

A 30-day free trial is available. 300 $ worth of credit will be given automatically.

https://console.aiven.io/signup



## Aiven usage step by step
## Step by step

In the following, we will explain from building a Kafka cluster to setting up a system monitoring environment, including actual screen operation images.

Here, the following services will appear.

--Aiven for Apache Kafka: A service that generates telemetry data
--Aiven for InfluxDB: A database where telemetry data is stored and can be queried from it.
--Aiven for Grafana: Telemetry Data Dashboard

### Aiven Sign up

### Kafka cluster construction

## Service construction

The Aiven service is managed by the Aiven web console.
When you log in to the console with the credentials (email address and password) you created when you signed up, you will first see the Services view.
If it has already been created, you will see a list of services.

Create a Kafka service. Service setup has much in common with other services, so

Select Kafka as the service type. You can also select the version you want to use.

Select the cloud provider and region where you want to run the service.
Prices may vary by provider and region. The service summary on the right side of the console shows the pricing for the selected option.

Select a service plan. It defines the number of servers and the types of memory, CPU, and disk resources allocated to the service.

Enter the name of the service. Random names are provided by default.
You can change the name to something that is easy to recognize. Here, it is replaced with "test".

Click Create Service under the overview on the right side of the console. This will return you to the service view. A new service appears in the list with a status indicator indicating that it is being created.

While building the service, you can access the service's Overview tab and see the status change from "REBUILDING" to "RUNNING".

After building, you can see that the new service has been added as shown below.

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/176567/ec303810-7b79-3eb3-0883-96923d0393bb.png)

### Kafka Data Feed Simulation

A data feed to Kafka is required to see the actual operation of the cluster.

This is a technically different topic, so I will omit it in this article, but the simulation program and construction procedure used here are published below, so if you are interested, please do not hesitate to contact us. Please look.

https://github.com/YoshiyukiKono/Aiven_Kafka_Quickstart_with_Python

## Kafka settings

### Check connection information

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/176567/4279227d-8149-535d-73c9-b934598c34b9.png)

Here, it is the following URL.

>kafka-test-yoshiyuki-e281.aivencloud.com:10779

Advanced settings. Enabling `auto_create_topics_enable`.

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/176567/446d43c7-cad7-1bec-2eef-f45ae9ce90ed.png)



![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/176567/833d3bc7-e366-4810-92f2-db3b5dd127ea.png)

Topic list.

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/176567/3206ff70-b744-5b84-dd50-7e92d8dd7b54.png)

Topic information.

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/176567/c5b36885-4472-fb3c-6a2a-22f852279c01.png)

REST enabled.

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/176567/35ef6756-0bb1-df61-319c-66caa4f3737a.png)

Confirm message content.

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/176567/ac98303f-8861-d8fc-8165-b6588148ddfe.png)



### Launching InfluxDB and Grafana services

### Service integration settings

"Service integration" is a characteristic function of Aiven managed services that provide various services.



The following is the service integration setting screen of InfluxDB.
Set Metrics (Kafka) as the data source to InfluxDB and Dashboard (Grafana) as the data source of InfluxDB.

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/176567/1a551dad-f806-ed1a-dff2-931ecde883b8.png)

The screen after the setting is completed is as follows.

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/176567/d3936c12-289e-7e77-43e8-994a0a3fa24e.png)

That's all you need to do to see your Kafka cluster metrics in your Grafana dashboard.

### Grafana Dashboard Check

Log in to the Grafana dashboard to see the results of your setup so far.

Go back to the service list and select the Grafana service.

In the Connection Parameters section, click the password icon to see the information you need to log in to Grafana.
The default user name for Grafana is "avnadmin".
Copy the password so you can paste it into the Grafana login dialog.

Click the link next to the host to open a browser page to the Grafana login dialog.

Enter avnadmin as your username and paste your Grafana password into the password field to log in to Grafana.


![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/176567/ceba3f22-90e1-c597-7ea0-e6f9ab114576.png)


If you just enabled the integration, you may not have started getting the data to the dashboard view.

In less than a few minutes, the dashboard "Aiven Kafka --kafka-test --Resource" will be created automatically as shown below. In addition to the Overview, it is closed to show the whole picture, but System metrics (15 panels), Kafka metrics (17 panels), and Java metrics (3 panels) are automatically added.

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/176567/c8e19c3a-eb9b-9510-256d-00b0143b1888.png)

### Custom dashboard definition


Of course, as a basic feature of Grafana, you can add custom dashboards that aren't predefined.
Alternatively, you may want to edit a predefined dashboard.
Any changes you make to the predefined dashboards will eventually be overwritten automatically by the system.
Save it with a different name to avoid overwriting.
It's important to give it a different name that doesn't start with "Aiven", as dashboards whose title starts with "Aiven" are considered auto-managed.

### Service stop

If you do not use it, you can stop the service as shown below and you will not be charged.

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/176567/704e4619-c7e2-7ebc-1bba-51678fcfaf28.png)



When the service is stopped (power-off), information such as topics will be cleared.

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/176567/decf29aa-0213-32dd-01d2-ae0d0e1c31f9.png)


>WARNING
>All data on the cluster and all topic data and configuration will be lost on power off.



### Reference information

https://developer.aiven.io/docs/products/grafana/get-started.html











### Reference information

In writing this article, I referred to the following articles.

https://help.aiven.io/en/articles/1456441-getting-started-with-service-integrations

