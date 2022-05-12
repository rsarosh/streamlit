import os
import json
from azure.eventgrid import EventGridEvent
from azure.servicebus import ServiceBusClient
from dotenv import load_dotenv
#
# https://docs.microsoft.com/en-us/azure/service-bus-messaging/service-bus-python-how-to-use-queues

load_dotenv('.env')
# all types of EventGridEvents below produce same DeserializedEvent
connection_str = os.environ['azure_servicebus_conection_str']
queue_name = os.environ['azure_servicebus_queue_name']


if __name__ == '__main__':
    try:
        with ServiceBusClient.from_connection_string(connection_str) as sb_client:
            receiver = sb_client.get_queue_receiver(queue_name=queue_name)
            with receiver:
                for message in receiver:

                    event = json.loads(str(message))
                    print(f"Event: {event['data']}")
                    receiver.complete_message(message)  # mark message as complete

    except:
        print("Error: No message received")
