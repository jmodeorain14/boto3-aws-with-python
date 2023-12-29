import boto3

# Create a Boto3 EC2 client object
ec2 = boto3.client("ec2")

# Define the Jtl Reporter EC2 Instance ID
instance_id = "i-09f8e38adcf744509"

# Start the Jtl Reporter EC2 instance
response = ec2.start_instances(InstanceIds=[instance_id])
