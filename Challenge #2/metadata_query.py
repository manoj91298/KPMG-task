# The Python script that queries the AWS EC2 instance metadata and provides JSON-formatted output
# 
# prerequities:
# Boto3 library installed using pip
# 
# "pip install boto3"

import json
import boto3

def get_instance_metadata():
    # Create a Boto3 EC2 client
    ec2_client = boto3.client('ec2')

    # Get the instance metadata
    response = ec2_client.describe_instances()
    instance_metadata = response['Reservations'][0]['Instances'][0]

    return instance_metadata

def get_metadata_json():
    instance_metadata = get_instance_metadata()
    return json.dumps(instance_metadata, indent=2)

def get_metadata_key(key):
    instance_metadata = get_instance_metadata()
    data = instance_metadata
    for k in key.split('/'):
        if k in data:
            data = data[k]
        else:
            return None
    return json.dumps(data, indent=2)

if __name__ == "__main__":
    # Retrieve all metadata as JSON
    print("All metadata:")
    print(get_metadata_json())

    # Retrieve a particular data key
    key = "InstanceType"
    print(f"\nMetadata for key '{key}':")
    print(get_metadata_key(key))

# To execute the script and retrieve all metadata as JSON

# "python metadata_query.py"

# The script will fetch the instance metadata and display it in JSON format with proper indentation.

# If we want Retrieve a Specific Data Key 

# For example, to retrieve the value of the InstanceType key:

# python metadata_query.py InstanceType

