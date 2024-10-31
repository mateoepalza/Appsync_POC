import boto3
import random
import datetime
import boto3.session
from tqdm import tqdm  # To show progress of insertion

# Initialize Timestream write client
session = boto3.Session(profile_name='lab', region_name="us-east-1")
timestream = session.client('timestream-write')

DATABASE_NAME = 'PetMetricsDB'
TABLE_NAME = 'PetMetricsTable'

# Function to generate a random record
def generate_record(user_id, pet_id, timestamp_ns):
    weight = round(random.uniform(5.0, 50.0), 2)  # Random weight between 5 and 50 kg
    visits = random.randint(1, 10)  # Random number of visits between 1 and 10
    record = [
        {
            'Dimensions': [
                {'Name': 'userId', 'Value': user_id},
                {'Name': 'petId', 'Value': pet_id},
            ],
            'MeasureName': 'weight',
            'MeasureValue': str(weight),
            'MeasureValueType': 'DOUBLE',
            'Time': str(timestamp_ns),
            'TimeUnit': 'NANOSECONDS'
        },
        {
            'Dimensions': [
                {'Name': 'userId', 'Value': user_id},
                {'Name': 'petId', 'Value': pet_id},
            ],
            'MeasureName': 'visits',
            'MeasureValue': str(visits),
            'MeasureValueType': 'BIGINT',
            'Time': str(timestamp_ns+1),
            'TimeUnit': 'NANOSECONDS'
        }
    ]
    return record

# Function to batch insert records into Timestream
def batch_insert_records(records_batch):
    try:
        response = timestream.write_records(
            DatabaseName=DATABASE_NAME,
            TableName=TABLE_NAME,
            Records=records_batch
        )
        return response
    except timestream.exceptions.RejectedRecordsException as e:
        print(f"Error inserting records: {e}")
        if 'RejectedRecords' in e.response:
            for rejected_record in e.response['RejectedRecords']:
                print(f"Rejected record: {rejected_record}")
        else:
            print("No details available for rejected records.")
    except Exception as e:
        print(f"Unexpected error inserting records: {e}")

if __name__ == '__main__':
    total_records = 100000
    batch_size = 25  # AWS Timestream can handle 100 records per batch
    user_ids = [f"user_{i}" for i in range(1, 20)]  # Generate user IDs

    # Generate timestamps spread over one year
    start_date = datetime.datetime(2024, 9, 30, 21)  # Start from this date
    end_date = datetime.datetime(2024, 10, 1, 20)  # End date after one year

    # Calculate the time difference between each record based on total records
    total_seconds_in_year = (end_date - start_date).total_seconds()
    seconds_per_record = total_seconds_in_year / total_records  # Spread evenly over one year

    inserted_records = 0
    current_time = start_date

    print(f"Inserting {total_records} records into Timestream...")

    for i in tqdm(range(0, total_records, batch_size)):
        records_batch = []

        for j in range(batch_size):
            # Generate random user, pet, and type
            user_id = random.choice(user_ids)
            pet_id = f"pet_{user_id}_{random.randint(1, 5)}"

            # Calculate timestamp for each record, spread over one year
            timestamp_ns = int(current_time.timestamp() * 1e9)  # Nanoseconds precision
            # Generate and append records for this timestamp
            records_batch.extend(generate_record(user_id, pet_id, timestamp_ns))

            # Increment the time for the next record
            current_time += datetime.timedelta(seconds=seconds_per_record)


        # Insert the batch of 100 records
        batch_insert_records(records_batch)
        inserted_records += batch_size

    print(f"Successfully inserted {inserted_records} records into Timestream.")