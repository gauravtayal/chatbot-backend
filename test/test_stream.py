import requests


url = "http://127.0.0.1:8000/api/v1/chat/hr/stream"

payload = {
    "message": "What is the maternity leave policy?",
    "session_id": "stream-demo-001"
}


with requests.post(
    url,
    json=payload,
    stream=True
) as response:

    for line in response.iter_lines():

        if line:

            print(
                line.decode("utf-8")
            )