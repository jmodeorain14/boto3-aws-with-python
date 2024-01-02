import boto3
import time

def runRemoteShellCommands(InstanceId):
    # Create an SSM client
    ssm_client = boto3.client("ssm")

    # Send the command(s) to the EC2 instance
    response = ssm_client.send_command(
        InstanceIds=[InstanceId],
        DocumentName="AWS-RunShellScript",
        Parameters={"commands": ["cd /home/ubuntu/jtl-reporter", "sudo docker-compose up -d"]},
    )

    # Get command status and output
    CommandId = response["Command"]["CommandId"]
    time.sleep(5) # Wait for 5 seconds before trying again
    output = ssm_client.get_command_invocation(
        CommandId=CommandId, InstanceId=InstanceId
    )

    # Wait for command to finish
    while output["Status"] == ["Pending", "InProgress"]:
        output = ssm_client.get_command_invocation(
            CommandId=CommandId, InstanceId=InstanceId
        )
    
    # Print the output of the executed command(s)
    print(output["StandardOutputContent"])

# Pass the EC2 instance ID to the function
runRemoteShellCommands("i-09f8e38adcf744509")
