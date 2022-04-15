import boto3

# create ec2 instance
ec2_client = boto3.client('ec2')

response = ec2_client.run_instances(
        ImageId = 'ami-08e4e35cccc6189f4',
        InstanceType = 't2.micro',
        MaxCount = 1,
        MinCount = 1,
        KeyName = 'vockey'
)
print(response)


# create s3 bucket
import boto3 

bucket_name = 's3-bucket-1928046' 
s3 = boto3.resource('s3')
try:
    s3.create_bucket(Bucket=bucket_name)
    print('S3 bucket created successfully')
except Exception as e:
    print('S3 error: ',e)

# create sns topic
import boto3

client = boto3.client('sns')
response = client.create_topic(
    Name='sns-topic-1928046',
    # Attributes={
    #     'string': 'string'
    # },
    # Tags=[
    #     {
    #         'Key': 'Name',
    #         'Value': 'myTopic'
    #     }
    # ]
)

# # create sns subscription
# response = client.subscribe(
#         TopicArn='arn:aws:sns:us-east-1:289479200412:sns-topic-1928046',
#         Protocol='sms',
#         Endpoint='07555565472'
# )

# print(response)

# create sqs queue 
# >>>>> REMEMBER TO ENABLE RAW MESSAGE DELIVERY IN AWS CONSOLE <<<<<<
# sqs = boto3.resource('sqs')
# queue = sqs.Queue('url')  # <-------- add URL

# response = client.create_queue(
#     QueueName='sqs-queue-1928046',
#     Attributes={
#         'SqsManagedSseEnabled': True
#     },
#     tags={
#         'string': 'string'
#     }
# )
