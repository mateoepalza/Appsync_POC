import time

def lambda_handler(event, context):
    print("EVENT", event)
    print("CONTEXT", context)

    time.sleep(2)

    return {
        "median": 5.5,
        "dataPoints": [
            {
                "date": 2024,
                "value": 2.5,
            },
            {
                "date": 2023,
                "value": None,
            },
            {
                "date": 2022,
                "value": 2.0,
            },
        ],
    }