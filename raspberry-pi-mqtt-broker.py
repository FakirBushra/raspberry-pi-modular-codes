# This Module for Raspberry Pi MQTT broker with subscribe, unsubscribe and publish actions explained
# www.fakirbushra.com
# www.github.com/FakirBushra

# Import libraries
# Paho MQTT Library
import paho.mqtt.client as mqtt
# TkInter Library for UI
from tkinter import *
from tkinter.font import *

# Setting the UI
win = Tk()
myfont = Font(family ='Helvetica',size = 66,weight ='bold')
win.title("Raspberry Pi MQTT Broker")
win.geometry("300x300")


# functions will be called when MQTT events happen such as
# connecting to the server or receiving data from a subscribed feed. 
def on_connect(client, userdata, flags, rc):
    # Connection renewed when lost.
    print("Connected with result code " + str(rc))
    client.subscribe("home/pi/topic")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))
    # Check if this is a message for the Pi.
    if msg.topic == 'home/pi/topic':
        # Look at the message data and perform the appropriate action.
        if msg.payload == b'Subscribe':
            # Subscribe to topic
            client.subscribe("home/pi/topic")
            print('Subscribed to topic')
        elif msg.payload == b'Unsubscribe':
            # Subscribe to topic
            client.unsubscribe("home/pi/topic")
            print('Unsubscribed from home/pi/topic')


# Create MQTT client and connect to localhost "Raspberry Pi"
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("localhost", 1883, 60)
# client.connect("mqtt.eclipseprojects.io", 1883, 60)
# Connect to the MQTT server and process messages in a background thread.
client.loop_start()
# Main loop to listen for button presses.
print('Script is running, press Ctrl-C to quit...')


# Define Functions Starts
# Subscribe to topic
def subscribe():
    client.subscribe('home/pi/topic')


# unsubscribe from topic
def unsubscribe():
    client.unsubscribe('home/pi/topic')


# Publish messages ... Do Action 1
def action1():
    client.publish('home/pi/topic', 'DoAction1')


# Publish messages ... Do Action 2
def action2():
    client.publish('home/pi/topic', 'DoAction2')


# Define Function Ends


# Defining buttons start
Label(win, text="Broker").grid(row=2, column=2)

# Subscribe
BuAction1 = Button(win, text="Subscribe", command=subscribe, height=2, width=10)
BuAction1.grid(row=1, column=1)

# Unsubscribe
BuAction2 = Button(win, text="Unsubscribe", command=unsubscribe, height=2, width=10)
BuAction2.grid(row=1, column=2)

# Action 1
BuAction1 = Button(win, text="Action 1", command=action1, height=2, width=10)
BuAction1.grid(row=2, column=1)

# Action 2
BuAction2 = Button(win, text="Action 2", command=action2, height=2, width=10)
BuAction2.grid(row=2, column=2)
# Defining buttons end


# Start Loop
mainloop()
