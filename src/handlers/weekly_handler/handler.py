
import time

def lambda_handler(event, context):
    print("EVENT", event)
    print("CONTEXT", context)

    time.sleep(2)

    return {
        "median": 90,
        "dataPoints": [
            {
                "date": "2024-10-16",
                "value": 1.8
            },
            {
                "date": "2024-10-15",
                "value": 2.5
            },
            {
                "date": "2024-10-14",
                "value": None
            }
        ]
    }