import json

def create_stream_event(event_type: str, content: str = "") -> str:
    """
    Create a stream event in the format expected by the client.
    """
    return json.dumps({"type": event_type, "content": content}) + "\n\n"