import boto3

# Create a Boto3 EC2 resource object
ec2 = boto3.resource("ec2")

# Print relevant details of all existing EC2 instances
for instance in ec2.instances.all():
    instance_id = instance.id
    instance_type = instance.instance_type
    # If the instance does not have a name, provide a default value of 'N/A'
    instance_name = next((tag['Value'] for tag in instance.tags if tag['Key'] == 'Name'), 'N/A')
    instance_status = instance.state['Name']
    
    print(f"Instance ID {instance_id} of type {instance_type} with name name {instance_name} is currently {instance_status}.")
