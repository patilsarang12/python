import boto3
import sys
aws_con=boto3.session.Session(profile_name="student001")
ec2_con_re=aws_con.resource(service_name="ec2",region_name="us-east-1")
print(dir(ec2_con_re))
print("***************")
print(dir(ec2_con_re.meta))
# convert your resource object (higher level) into client object (lower level processing is required) using meta
print(dir(ec2_con_re.meta.client)) # now you can use all functions from client using resource object!
"""
ec2_con_cl=aws_con.client(service_name="ec2",region_name="us-east-1")

while True:
    print("1.start 2.stop 3.terminate 4.exit on ec2 instance\n")
    choice=int(input("Enter your choice "))
    if choice==1:
        instance_id=input("Enter ec2 instance id: ")
        instance_obj=ec2_con_re.Instance(instance_id)
        instance_obj.start()
        print(f"{instance_id} is running!")
    elif choice==2:
        instance_id = input("Enter ec2 instance id: ")
        instance_obj = ec2_con_re.Instance(instance_id)
        instance_obj.stop()
        print(f"{instance_id} is stopped!")
    elif choice==3:
        instance_id = input("Enter ec2 instance id: ")
        instance_obj = ec2_con_re.Instance(instance_id)
        instance_obj.terminate()
        print(f"{instance_id} is terminated!")
    elif choice==4:
        sys.exit(0)
    else:
        print("Invalid choice!")
"""


