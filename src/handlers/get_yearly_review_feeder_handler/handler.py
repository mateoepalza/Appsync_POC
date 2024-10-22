
import time

def lambda_handler(event, context):
    print("EVENT", event)
    print("CONTEXT", context)

    time.sleep(4)

    return {
        "total": 90
    }