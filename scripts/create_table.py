import boto3
from botocore.exceptions import ClientError

# Initialize a session using a specific profile
session = boto3.Session(profile_name='lab', region_name="us-east-1")

# Use the session to create a Timestream client
timestream_write = session.client('timestream-write')

DATABASE_NAME = 'PetMetricsDB'
TABLE_NAME = 'PetMetricsTable'

def create_database(database_name):
    try:
        timestream_write.create_database(DatabaseName=database_name)
        print(f"Database {database_name} created successfully.")
    except ClientError as e:
        if e.response['Error']['Code'] == 'ConflictException':
            print(f"Database {database_name} already exists.")
        else:
            print(f"Error creating database: {e}")

def create_table2(database_name, table_name):
    try:
        timestream_write.create_table(
            DatabaseName=database_name,
            TableName=table_name,
            RetentionProperties={
                'MemoryStoreRetentionPeriodInHours': 100,
                'MagneticStoreRetentionPeriodInDays': 1000
            },
            Schema={
                'CompositePartitionKey': [
                    {
                        'Name': 'id',
                        'Type': 'DIMENSION',  # This is the third partition key
                        'EnforcementInRecord': 'REQUIRED'
                    },
                ]
            }
        )
        print(f"Table {table_name} created successfully in database {database_name}.")
    except ClientError as e:
        if e.response['Error']['Code'] == 'ConflictException':
            print(f"Table {table_name} already exists.")
        else:
            print(f"Error creating table: {e}")

def create_table(database_name, table_name):
    try:
        timestream_write.create_table(
            DatabaseName=database_name,
            TableName=table_name,
            RetentionProperties={
                'MemoryStoreRetentionPeriodInHours': 100,
                'MagneticStoreRetentionPeriodInDays': 365
            }
        )
        print(f"Table {table_name} created successfully in database {database_name}.")
    except ClientError as e:
        if e.response['Error']['Code'] == 'ConflictException':
            print(f"Table {table_name} already exists.")
        else:
            print(f"Error creating table: {e}")

if __name__ == '__main__':
    # Step 1: Create Database and Table
    create_database(DATABASE_NAME)
    create_table(DATABASE_NAME, TABLE_NAME)
