import json
import boto3
import csv

def lambda_handler(event, context):
    # TODO implement
    s3=boto3.client("s3")
    for record in event['Records']:
        #pull the body out & json load it
        jsonmaybe=(record["body"])
        jsonmaybe=json.loads(jsonmaybe)
        #now the normal stuff works
        bucket_name = jsonmaybe["Records"][0]["s3"]["bucket"]["name"]
        key=jsonmaybe["Records"][0]["s3"]["object"]["key"]
        csv_file=s3.get_object(Bucket=bucket_name,Key=key)
        
        record_file=csv_file["Body"].read().decode("utf-8").splitlines()
        # print(record_file)
        csv_reader=csv.reader(record_file,delimiter=",",quotechar='"')
        
        dynamodb = boto3.resource('dynamodb')
        #table name
        table = dynamodb.Table('csv_table')
        #inserting values into table

        for row in csv_reader:
            duration=row[0]
            pulse=row[1]
            maxpulse=row[2]
            calories=row[3]
            response = table.put_item(
            Item={
                'duration': duration,
                'maxpulse':maxpulse,
                'pulse':pulse,
                'calories':str(calories)
                
             }
            )
        
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }


    
