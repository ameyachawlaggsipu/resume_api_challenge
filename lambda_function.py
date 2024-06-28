import json
import boto3

#Initialize DynamoDB resourceS
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Resume')

def lambda_handler(event, context):

    #extract id from query parameters

    id = event['queryStringParameters']['id']

    try:
        response = table.get_item(Key = {'id' : id})
        item = response.get('Item')

        if item:
            # Successfull response
            return {
                'statusCode' : 200,
                'body' : json.dumps(item)
            }
    
        else:
            return {
                'statuscode' : 404,
                'body' : json.dumps({'error' : 'resume not found'})
            }
    except Exception as e:
        # Return 500 Internal Server Error if any exception occurs
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }