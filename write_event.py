import datetime
from dotenv import load_dotenv
import os
from azure.core.credentials import AzureKeyCredential
from azure.eventgrid import EventGridPublisherClient, EventGridEvent
import json
import time


def create_data() -> str:
    data = {}
    data['producer'] = 'python app-1'
    data['subscriber'] = 'python app-2'
    data['timestamp'] = datetime.datetime.now().isoformat()
    return json.dumps(data)


load_dotenv('.env')

azure_event_key = os.environ['azure_event_key']
azure_event_endpoint = os.environ['azure_event_endpoint']


def send_event(event):
    endpoint = azure_event_endpoint
    credential = AzureKeyCredential(azure_event_key)
    client = EventGridPublisherClient(endpoint, credential)
    client.send(event)
    print(".")


def create_event(event_data: str) -> EventGridEvent:
    return EventGridEvent(
        data=event_data,
        subject="spider-1",
        event_type="SpiderEvent",
        data_version="1.0"
    )


if __name__ == '__main__':
    while True:
        send_event(create_event(create_data()))
        time.sleep(4)  # sleep for 4 seconds
