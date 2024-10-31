
import time

def lambda_handler(event, context):
    print("EVENT", event)
    print("CONTEXT", context)


    return {
        "median": 6.5,
        "dataPoints": [
            {
                "date": "2024-10",
                "value": 1.8
            },
            {
                "date": "2024-09",
                "value": 2.5
            },
            {
                "date": "2024-08",
                "value": None
            },
            {
                "date": "2023-11",
                "value": None
            },
        ],
    }