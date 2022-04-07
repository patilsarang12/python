import boto3
# step 1 login to aws management console
aws_management_console=boto3.session.Session(profile_name="student001")
#print(dir(aws_management_console))
# step 2 create IAM console object using resource
"""
iam_console1=aws_management_console.resource(service_name="iam",region_name="us-east-1")
print(dir(iam_console))
# step 3 use the functions on the resource objects
for users in iam_console.users.all():
    print("IAM users are",users.name)
s3_console=aws_management_console.resource(service_name="s3",region_name="us-east-1")
for buckets in s3_console.buckets.all():
    print("s3 buckets are ",buckets.name)

iam_console=aws_management_console.client(service_name="iam",region_name="us-east-1")
#print(dir(iam_console))
for each_user in iam_console.list_users()['Users']:
    print(each_user['UserName'])
s3_console=aws_management_console.client(service_name="s3",region_name="us-east-1")
for buckets in s3_console.list_buckets()['Buckets']:
    print("s3 buckets are ",buckets['Name'])
#for buckets in s3_console.buckets.all():
    #print("s3 buckets are ",buckets.name)
"""
ec2_console=aws_management_console.resource(service_name="ec2",region_name="us-east-1")
for instances in ec2_console.instances.all():
    print(instances.id)

ec2_client=aws_management_console.client(service_name="ec2",region_name="us-east-1")
for instances in ec2_client.describe_instances()['Reservations']:
    for everyinstance in instances['Instances']:
        print(everyinstance['InstanceId'])