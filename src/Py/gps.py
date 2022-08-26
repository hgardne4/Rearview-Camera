"""
Henry Gardner
Rear-view Camera for any car

GPS file to get location of moving vehicle
"""

from tkinter import *
from tkinter import ttk
import time
from datetime import datetime
import json
import gpsd

# make sure the usb gps dongle is connected
test = {}

# function  polling gpsd data
def get_gps_data():
    # obtain the current() location values:
    packet = gpsd.get_current()
    lat, lon = packet.position()
    elevation = packet.altitude()
    format(lat, lon, elevation)

# function to format the output for both a .json file and standard output:
def format(lat, lon, elevation):
    global test
    # saving location to file
    f = open("data/locations.json", "a")
    # get the current date and time (show only 3 decimals in the microseconds):
    date, time = datetime.now().strftime("%m/%d/%Y %H:%M:%S.%f")[:-3].split(" ")
    result = {"date": date, "time": time, "lat": str(lat) + " N", "lon": str(lon) + " W", "elevation": str(elevation) + " m or " + "%.3f" % (elevation*3.28084) + " ft"}
    # write to both the json file and the standard output
    json.dump(result, f)
    print(json.dumps(result, indent=2)) 
    test = result

# initialize the window:
root = Tk()
root.geometry("700x700")
frame = ttk.Frame(root, padding=10)
frame.pack()

mmenu = Menu(frame)
mmenu.add_command(label="Exit", command=root.destroy)
root.config(menu=mmenu)

# the current json contains all the elements we wish to display, this updates each iteration
gpsd.connect()

current = get_gps_data()
ttk.Label(frame, text="Date: " + str(test['date'])).grid(column=0,row=0)
ttk.Label(frame, text="Time: " + str(test['time'])).grid(column=0,row=1)
ttk.Label(frame, text="Latitude: " + str(test['lat'])).grid(column=0,row=2)
ttk.Label(frame, text="Longitude: " + str(test['lon'])).grid(column=0,row=3)
ttk.Label(frame, text="Elevation: " + str(test['elevation'])).grid(column=0,row=4)
root.mainloop()
