import boto3

# Replace 'your_access_key' and 'your_secret_key' with your AWS credentials
aws_access_key_id = 'your_access_key'
aws_secret_access_key = 'your_secret_key'
region_name = 'us-east-1'  # Replace with your desired AWS region

# Create a Boto3 EC2 client
ec2 = boto3.client('ec2', aws_access_key_id=aws_access_key_id,
                   aws_secret_access_key=aws_secret_access_key, region_name=region_name)

def start_instance(instance_id):
    try:
        ec2.start_instances(InstanceIds=[instance_id])
        print(f"Started instance with ID: {instance_id}")
    except Exception as e:
        print(f"Error starting instance: {str(e)}")

def stop_instance(instance_id):
    try:
        ec2.stop_instances(InstanceIds=[instance_id])
        print(f"Stopped instance with ID: {instance_id}")
    except Exception as e:
        print(f"Error stopping instance: {str(e)}")

def list_instances():
    try:
        response = ec2.describe_instances()
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                print(f"Instance ID: {instance['InstanceId']}, State: {instance['State']['Name']}")
    except Exception as e:
        print(f"Error listing instances: {str(e)}")

if __name__ == "__main__":
    while True:
        print("\nMenu:")
        print("1. Start an EC2 instance")
        print("2. Stop an EC2 instance")
        print("3. List all EC2 instances")
        print("4. Quit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            instance_id = input("Enter the instance ID to start: ")
            start_instance(instance_id)
        elif choice == '2':
            instance_id = input("Enter the instance ID to stop: ")
            stop_instance(instance_id)
        elif choice == '3':
            list_instances()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please enter a valid option.")
