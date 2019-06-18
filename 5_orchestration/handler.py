def validate_temperature(event, context):
    temperature = int(event["temperature"])
    if temperature < -20:
        raise ValueError("Too cold!")
    if temperature > 30:
        raise ValueError("Too warm!")

    return event

def enrich_location(event, context):
    event["location"] = "Berlin"
    return event
