# ECS-CloudFormation
Create an ECS Cluster using CloudFormation

## Before you begin
Make sure you have an AWS Account to be able to run these Scripts on the CloudFormation Service.

## Requirements
* Public S3 bucket to upload the Scripts.
* URL of the Docker image of the application that you are going to run.

### Upload your image to ECR
You can find an app.py file on the project as an example of the application to run on the ECS Cluster and a DockerFile to create the applications Docker image.
## Build the Docker Image
* Create a new Folder to download the Application Files.
* Download the app.py and the Dockerfile files.
* Go to the folder where the application files where downloaded.
* Run the following command (You need to have Docker installed)
```
docker build -t name-of-your-image .
```
## Create an ECR Repository and push your Docker Image
* Go to the ECS Service on the AWS Console.
* Go to the Repositories option.
* Click on Create repository and fill the Repository Name field with the Name of your docker image (previous step).
* Follow the push command instructions to push your Docker image.

### Upload your Scripts to S3
Upload the following Scripts to S3.
* ALB.yml
* ElastiCache.yml
* IAMRole.yml
* SecurityGroups.yml
* ECSCluster.yml

### Modify the main Script
Replace the TemplateURL Property in the Resources of the MainTemplate.yml file, with the URLs of your own S3 bucket.
```
IAMRoleTemplate:
    Type: AWS::CloudFormation::Stack
    Properties:
      TemplateURL: https://s3.amazonaws.com/cloudformation-hrou/IAMRole.yml
```

```
SecurityGroupTemplate:
    Type: AWS::CloudFormation::Stack
    Properties:
      TemplateURL: https://s3.amazonaws.com/cloudformation-hrou/SecurityGroups.yml
```

```
ElastiCacheTemplate:
    Type: AWS::CloudFormation::Stack
    Properties:
      TemplateURL: https://s3.amazonaws.com/cloudformation-hrou/ElastiCache.yml
```

```
  ALBTemplate:
    Type: AWS::CloudFormation::Stack
    Properties:
      TemplateURL: https://s3.amazonaws.com/cloudformation-hrou/ALB.yml
```

```
  ECSClusterTemplate:
    Type: AWS::CloudFormation::Stack
  Properties:
      TemplateURL: https://s3.amazonaws.com/cloudformation-hrou/ECSCluster.yml
```
## Create the Stack on CloudFormation
Follow the next steps to create your Stack on the CloudFormation Service on AWS.
* Login into the AWS console.
* Upload the modified MainTemplate.yml Script to S3.
* Go to the CloudFormation Service.
* Click on "Create new Stack".
* Specify your MainTemplate.yml Script URL.
### Filling the Parameters
```
You will be prompted with the following required parameters.
* AppContainerPort: It's the port on the container where the application runs.
* AppName: The Name of your application for the ECS Cluster.
* AppSubnets: The Subnets that the AutoScaling Group will use to launch the EC2 Instances.
* ClusterName: The Name of the ECS Cluster.
* DesiredCapacity: The Number of EC2 Instances desired on the Cluster.
* DesiredCount: The Number of Containers desired to be running on the Cluster.
* Image: The URL of the image that the containers will use.
* InstanceType: The EC2 Instance type that the cluster will use.
* KeyName: The KayPair to use to ssh into the EC2 instances.
* MaxSize: The MaxSize of EC2 instances to be launched into the Cluster.
* ServiceName: The Name of the Service that will run the tasks under the Cluster.
* VPC: The VPC where everything will run.
```
* Fill the parameters info.
* Click Next.
* Click Create.
### Access the application.
Go to the EC2 Service on the AWS Console.
Click on the Load Balancers.
Copy the DNS name of the load balancer into a web browser.
You should be able to see your application running.
* You can go to the Target Groups option into the EC2 Service to see your containers status.
### Delete Everything
Go to the CloudFormation Service.
* Select the stack.
* Click Delete on the Stack Actions menu.
