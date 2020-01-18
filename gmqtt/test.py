import asyncio
import signal
import time

from gmqtt import Client as MQTTClient


STOP = asyncio.Event()

timestamps = []


def on_connect(client, flags, rc, properties):
    print('Connected')
    client.subscribe('TEST/#', qos=0)


def on_message(client, topic, payload, qos, properties):
    global timestamps
    diff = time.time() - float(payload)
    timestamps.append(diff)

    # offset 6
    print('Average is: ' + str(sum(timestamps) / len(timestamps) - 6))


def on_disconnect(client, packet, exc=None):
    print('Disconnected')


def on_subscribe(client, mid, qos):
    print('SUBSCRIBED')


def ask_exit(*args):
    STOP.set()


async def main(broker_host):
    client = MQTTClient('client-id')

    client.on_connect = on_connect
    client.on_message = on_message
    client.on_disconnect = on_disconnect
    client.on_subscribe = on_subscribe

    await client.connect(broker_host, 1883)

    for x in range(100):
        client.publish('TEST/TIME', time.time(), qos=1)

    await STOP.wait()
    await client.disconnect()


if __name__ == '__main__':
    host = 'localhost'

    loop = asyncio.get_event_loop()

    loop.run_until_complete(main(host))
