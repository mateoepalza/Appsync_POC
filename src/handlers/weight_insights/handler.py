
def lambda_handler(event, context):
    print("EVENT", event)
    print("CONTEXT", context)

    return [
        {
            "petId": "petId-1",
            "weeklyData": None,
            "monthlyData": None,
            "yearlyData": None,
            "allData": None,
        },
        {
            "petId": "petId-2",
            "weeklyData": None,
            "monthlyData": None,
            "yearlyData": None,
            "allData": None,
        },
    ]