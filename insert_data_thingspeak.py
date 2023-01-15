import serial
import urllib.request

URL = "https://api.thingspeak.com/update"

# copy the API KEY from your ThingSpeak channel
APIKEY = "TJ6OY7WNN6QI5JFS"

# copy the port from your Arduino editor
PORT = 'COM3'

ser = serial.Serial(PORT, 9600)


def upload(data):
    args = {'api_key': APIKEY}
    for i in range(len(data)):
        args["field" + str(i + 1)] = float(data[i])
        args["field" + str(i + 2)] = float(data[i + 2])
        args["field" + str(i + 3)] = float(data[i + 4])
        args["field" + str(i + 4)] = float(data[i + 6])
        query_data = urllib.parse.urlencode(args).encode("utf-8")
        query_data.decode("utf-8")
        headers = {"Content-type": "application/x-www-form-urlencoded",
                   "Accept": "text/plain"}
        req = urllib.request.Request(URL, query_data, headers)
        response = urllib.request.urlopen(req)
        return response


while True:
    message = ser.readline()
    # print(message.decode())
    print(message.strip().decode())
    upload(message.split())
