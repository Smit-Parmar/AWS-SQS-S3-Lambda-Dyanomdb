# Project to Insert CSV data into dynamodb 

### AWS services used in this project
- S3 (To store csv file)
- SQS (To handle message while csv is uploaded into s3)
- AWS Lambda (To read message from SQS , Read data from CSV and insert data into dynamodb)
- Dynamodb (Store the data)

