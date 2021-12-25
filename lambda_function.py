# This is a lambda function to integrate dynamo-db from lambda
# This function is built using the following ref doc - https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html
'''
Steps to run 
Install the packages in the requirements.txt using the following command - pip install -r requirements.txt -t .
Test the function locally on your machine by running python lambda_function.py after configuring aws
After validating it locally convert it to a zip file and upload it to lambda
'''
import boto3
import json
def lambda_handler(event,context):
    client = boto3.client('dynamodb')
    table_name = "Mello"
    # converting the json event to a dictionary
    event = json.loads(event)
    response = client.put_item(
        TableName=table_name,
        Item={'id':{'S':str(event['id'])},"name":{'S':event['name']}}
    )
    # Note N and S means the attribute type String and Number in dynamodb table
    print(response)
    return (response)

'''
if __name__ == "__main__":
    event = '{"id":1,"name":"firsttournament"}'
    lambda_handler(event,2)
'''

