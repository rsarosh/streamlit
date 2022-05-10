from dotenv import load_dotenv
import os
from azure.core.credentials import AzureKeyCredential
from azure.eventgrid import EventGridPublisherClient, EventGridEvent

event = EventGridEvent(
    data={"team": "Analyst"},
    subject="Start Scrapping",
    event_type="Scrapping",
    data_version="1.0"
)

load_dotenv('.env')

azure_event_key = os.environ['azure_event_key']
azure_event_endpoint = os.environ['azure_event_endpoint']


if __name__ == '__main__':
    endpoint = azure_event_endpoint
    credential = AzureKeyCredential(azure_event_key)
    client = EventGridPublisherClient(endpoint, credential)
    client.send(event)
    print("Event sent")
