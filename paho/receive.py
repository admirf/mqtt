import paho.mqtt.client as mqtt
import time

timestamps = []


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    client.subscribe("test")


def on_message(client, userdata, msg):
    global timestamps
    diff = time.time() - float(msg.payload)
    timestamps.append(diff)

    print('Average is: ' + str(sum(timestamps) / len(timestamps)))


def main():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect("localhost", 1883)
    client.loop_forever()


if __name__ == '__main__':
    main()
