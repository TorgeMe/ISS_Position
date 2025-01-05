### ISS ##################################
# Version 4.0.3                          #
#                                        #
# vom 05.01.2025                         #
#                                        #
# @author: Torge Hauschild               #
##########################################

import tkinter as tk
import requests
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import time

lon = 0
lon_absolut = 0
lon_direction = ""
lat = 0
lat_absolut = 0
lat_direction = ""
timestamp = 0

def iss_location():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    if response.status_code == 200:
        data = response.json()
        iss_position = data["iss_position"]
        return iss_position
    else:
        return None


def where():
    iss_position = iss_location()
    if iss_position:
        lon = float(iss_position["longitude"])
        lat = float(iss_position["latitude"])
        #timestamp = time.localtime()
        timestamp = time.strftime("%d.%m.%Y %H:%M:%S")
        return lon, lat, timestamp
    else:
        print("Fehler beim Abrufen der ISS-Position!")
    
    
def refresh_gui():
    lon, lat, timestamp = where()
    
    if lon < 0:
        lon_direction = "West"
    else:
        lon_direction = "Ost"
    lon_absolut = abs(lon)
    
    if lat < 0:
        lat_direction = "Süd"
    else:
        lat_direction = "Nord"
    lat_absolut = abs(lat)
    
    print(lon, lon_absolut, lon_direction, lat, 
          lat_absolut, lat_direction, 
          timestamp)
    gui(lon, lon_absolut, lon_direction, lat, lat_absolut, lat_direction, timestamp)
    
    
def gui(lon, lon_absolut, lon_direction, lat, lat_absolut, lat_direction, timestamp):
    main = tk.Tk()
    main.title("ISS - Internationale Raumstation")
    
    main.geometry("800x400")
    main.minsize(400,200)
    label_headline = tk.Label(main, 
                     text="Aktuelle Position der ISS",
                     font=("Arial,20"))
    
    label_result1 = tk.Label(main,
                            text="Längengrad = " + str(lon_absolut) + " " + str(lon_direction),
                            font=("Arial,12"))
    
    label_result2 = tk.Label(main,
                            text="Breitengrad = " + str(lat_absolut) + " " + str(lat_direction),
                            font=("Arial,12"))
    
    label_result3 = tk.Label(main,
                            text="Zeitpunkt = " + str(timestamp),
                            font=("Arial,12"))
    
    button_Ermittle = tk.Button(main,
                               text=("Positionsermittlung"),
                               command=refresh_gui)
    
    #label_result1.config(text="Längengrad = " + str(lon_absolut) + " " + str(lon_direction))
    
    label_headline.pack(pady=50)
    label_result1.pack()
    label_result2.pack()
    label_result3.pack()
    button_Ermittle.pack(pady=50)
    
    main.mainloop()
    
    
    
if __name__ == "__main__":
    gui(lon, lon_absolut, lon_direction, lat, lat_absolut, lat_direction, timestamp)
