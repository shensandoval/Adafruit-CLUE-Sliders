from adafruit_clue import clue
import paho.mqtt.client as mqtt
import ast

def display_text(clueData):
  
    clue_data[0].text = "Accel: {} {} {} m/s^2".format(*clueData["accelerometer"])
    clue_data[1].text = "Gyro: {} {} {} dps".format(*clueData["gyro"])
    clue_data[2].text = "Magnetic: {} {} {} uTesla".format(*clueData["magnetometer"])
    clue_data[3].text = "Pressure: {} hPa".format(clueData["pressure"])
    clue_data[4].text = "Altitude: {:.0f} m".format(clue.altitude)
    clue_data[5].text = "Temperature: {} C".format(clueData["temperature"])
    clue_data[6].text = "Humidity: {} %".format(clueData["humidity"])
    clue_data[7].text = "Proximity: {}".format(clue.proximity)
    clue_data[8].text = "Color: R: {} G: {} B: {} C: {}".format(*clueData["color"])
    clue_data.show()

data = {
    'accelerometer': (0,0,0),
    'gyro': (0,0,0),
    'temperature': 0,
    'pressure': 1013,
    'magnetometer': (0,0,0),
    'humidity':0,
    'proximity': 0,
    'color': (0,0,0,0)
}

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.subscribe("clue-slider")
        display_text(data)

def on_message(client, userdata, msg):
    # display_text(int(msg.payload.decode()))
    dataFromHtml = ast.literal_eval(msg.payload.decode())
    data["accelerometer"] = (int(dataFromHtml["accelerometerX"]), int(dataFromHtml["accelerometerY"]), int(dataFromHtml["accelerometerZ"]))
    data["gyro"] = (int(dataFromHtml["gyroX"]), int(dataFromHtml["gyroY"]), int(dataFromHtml["gyroZ"]))
    data["temperature"] = int(dataFromHtml["temperature"])
    data["pressure"] = int(dataFromHtml["pressure"])
    data["magnetometer"] = (int(dataFromHtml["magnetometerX"]), int(dataFromHtml["magnetometerY"]), int(dataFromHtml["magnetometerZ"]))
    data["humidity"] = int(dataFromHtml["humidity"]),
    data["proximity"] = int(dataFromHtml["proximity"]),
    data["color"] = (int(dataFromHtml["colorR"]), int(dataFromHtml["colorG"]), int(dataFromHtml["colorB"]),int(dataFromHtml["colorC"]))
  
    display_text(data)


# clue.sea_level_pressure = 1020

clue_data = clue.simple_text_display(text_scale=2)
# 
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.eclipse.org", 1883, 60)

client.loop_forever()