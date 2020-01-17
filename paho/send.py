import paho.mqtt.client as mqtt
import time


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    client.subscribe("test")


def on_message(client, userdata, msg):
    print(msg.topic + ' ' + msg.payload)


def main():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.username_pw_set('ctnmhqle', 'KsDbKxfSoJmU')
    client.connect("hairdresser.cloudmqtt.com", 18694)
    for x in range(100):
        client.publish('test', time.time())


if __name__ == '__main__':
    main()
