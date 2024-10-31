import time

def lambda_handler(event, context):
    print("EVENT", event)
    print("CONTEXT", context)

    time.sleep(2)

    return {
        "median": 90,
        "dataPoints": [
            {
                "start": "2024-10-25",
                "end": "2024-10-31",
                "value": 4.5
            },
            {
                "start": "2024-10-18",
                "end": "2024-10-24",
                "value": 3.5
            },
            {
                "start": "2024-10-11",
                "end": "2024-10-17",
                "value": None
            },
            {
                "start": "2024-10-01",
                "end": "2024-10-10",
                "value": None
            }
        ]
    }