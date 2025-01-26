import tkinter as tk
from tkinter import messagebox
from tkinter import Menu
import requests
import time
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.basemap import Basemap

lon = 0
lon_absolut = 0
lon_direction = ""
lat = 0
lat_absolut = 0
lat_direction = ""
timestamp = 0
status = "nicht aktiv"

# Versions-Meldung
def showVersion():
    messagebox.showinfo("Version",
<<<<<<< Updated upstream
                        "4.1.0 vom 20.01.2025")
=======
                        "4.2.2 vom 26.01.2025")
>>>>>>> Stashed changes


# Copyright-Meldung
def showCopyright():
    messagebox.showinfo("Copyright",
                        "Torge Hauschild")

# Hilfe-Meldung
def showHelp():
    messagebox.showinfo("Hilfe",
    "Dieses Programm ermittelt die aktuelle Position der Internationalen Raumstation (ISS) \nin Echtzeit auf Grundlage der NASA-API \n  http://api.open-notify.org/iss-now.json")


# Programm beenden
def quitProgram():
    decision = messagebox.askyesno("Beenden",
                            "Möchten Sie das Programm beenden?")
    if decision:
        exit()


# Fehler-Meldung V00
def showErrorV00():
    messagebox.showerror("Fehler V00",
                        "Es ist ein Verbindungsfehler zur API aufgetreten!")

<<<<<<< Updated upstream
=======
# Einstellungsmenü
def Einstellungen():
    messagebox.showinfo("Einstellungen",
                        "API-URL: http://api.open-notify.org/iss-now.json")                        

>>>>>>> Stashed changes

# Daten von API ISS-now laden
def loadData():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    if response.status_code == 200:
        data = response.json()
        iss_position = data["iss_position"]
        return iss_position
    else:
        return None


# Daten aus der json-response auslesen
def getDataResponse():
    try:
        iss_position = loadData()
        status = "Daten wurden verarbeitet"
        if iss_position:
            lon = float(iss_position["longitude"])
            lat = float(iss_position["latitude"])
            timestamp = time.strftime("%d.%m.%Y %H:%M:%S")
            return lon, lat, timestamp, status
    except:
        status = "Verbindungsfehler"
        timestamp = time.strftime("%d.%m.%Y %H:%M:%S")
        showErrorV00()
        return 0, 0, timestamp, status


# Ergänze Richtungsdaten
def addDataResponse():
    lon, lat, timestamp, status = getDataResponse()
    
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
<<<<<<< Updated upstream
    return lon, lon_direction, lon_absolut, lat, lat_direction, lat_absolut, timestamp, status


# Update GUI
def refreshGui():
    lon, lon_direction, lon_absolut, lat, lat_direction, lat_absolut, timestamp, status = addDataResponse()
    
    label_status.config(text="Status: " + str(status))
    label_result1.config(text="Längengrad = " + str(lon_absolut) + " " + str(lon_direction))
    label_result2.config(text="Breitengrad = " + str(lat_absolut) + " " + str(lat_direction))
    label_result3.config(text="Zeitpunkt = " + str(timestamp))


# Erstelle GUI
def gui():
    # globale Variablen definieren
    global label_result1, label_result2, label_result3, label_status
=======
    return lon_direction, lon_absolut, lat_direction, lat_absolut, timestamp, status


# Update GUI
def refreshGui():
    lon_direction, lon_absolut, lat_direction, lat_absolut, timestamp, status = addDataResponse()
    
    label_status_0.config(text="Status: ")
    label_status_1.config(text=str(status))
    label_result1_0.config(text="Längengrad = ")
    label_result1_1.config(text=str(lon_absolut) + " " + str(lon_direction))
    label_result2_0.config(text="Breitengrad = ")
    label_result2_1.config(text=str(lat_absolut) + " " + str(lat_direction))
    label_result3_0.config(text="Zeitpunkt = ")
    label_result3_1.config(text=str(timestamp))


# Zeichne Karte
def map():
    refreshGui()
    iss_position = loadData()
    if iss_position: 
        try:
            plt.clf()
        finally:
            lon = float(iss_position['longitude'])
            lat = float(iss_position['latitude'])
        
            karte = Basemap(projection='ortho', lat_0=lat, lon_0=lon)
            karte.drawcoastlines()
            karte.drawmapboundary(fill_color='aqua')
            karte.fillcontinents(color='coral',lake_color='aqua')
            karte.drawparallels(np.arange(-90.,120.,30.))
            karte.drawmeridians(np.arange(0.,360.,60.))
        
            x, y = karte(lon, lat)
            karte.plot(x, y, 'ro', markersize=10)
            plt.title("Aktuelle Position der ISS")
            plt.show()

# Erstelle GUI
def gui():
    # globale Variablen definieren
    global label_result1_0, label_result1_1
    global label_result2_0, label_result2_1 
    global label_result3_0, label_result3_1
    global label_status_0, label_status_1
>>>>>>> Stashed changes

    # Fenster
    main = tk.Tk()
    main.title("ISS - Internationale Raumstation")

    # Menüleiste
    menubar = Menu(main)
    main.config(menu=menubar)
    info_menu = Menu(menubar, tearoff=0)
    exit_menu = Menu(menubar, tearoff=0)

    info_menu.add_command(label="Version", command=showVersion)
    info_menu.add_separator() # Fügt eine Trennlinie hinzu
    info_menu.add_command(label="Copyright", command=showCopyright)
    info_menu.add_separator() # Fügt eine Trennlinie hinzu
<<<<<<< Updated upstream
=======
    info_menu.add_command(label="Einstellungen", command=Einstellungen)
    info_menu.add_separator() # Fügt eine Trennlinie hinzu
>>>>>>> Stashed changes
    info_menu.add_command(label="Hilfe", command=showHelp)

    exit_menu.add_command(label="Beenden", command=quitProgram)

    menubar.add_cascade(label="Info", menu=info_menu)
    menubar.add_cascade(label="Beenden", menu=exit_menu)

    main.config(menu=menubar)  

    # Fenster-Abmessungen
    main.geometry("800x400")
    main.minsize(400,200)

    # Fenster-Inhalt
    label_headline = tk.Label(main, 
                            text="Aktuelle Position der ISS",
                            font=("Arial,20"))
<<<<<<< Updated upstream
    label_status = tk.Label(main,
                            text="Status: " + str(status),
                            font=("Arial,12"))

    label_result1 = tk.Label(main,
                            text="Längengrad = " + str(lon_absolut) + " " + str(lon_direction),
=======
    label_status_0 = tk.Label(main,
                            text="Status: ",
>>>>>>> Stashed changes
                            font=("Arial,12"))
    
    label_status_1 = tk.Label(main,
                            text=str(status),
                            font=("Arial,12"))

    label_result1_0 = tk.Label(main,
                            text="Längengrad = ",
                            font=("Arial,12"))
    
    label_result1_1 = tk.Label(main,
                            text=str(lon_absolut) + " " + str(lon_direction),
                            font=("Arial,12"))
    
<<<<<<< Updated upstream
    button_ermittle = tk.Button(main,
                               text=("POSITIONSERMITTLUNG"),
                               command=refreshGui)

    
    # Fenster erstellen
    label_headline.pack(pady=25)
    label_status.pack()
    label_result1.pack()
    label_result2.pack()
    label_result3.pack()
    button_ermittle.pack(pady=25)
=======
    label_result2_0 = tk.Label(main,
                            text="Breitengrad = ",
                            font=("Arial,12"))
    
    label_result2_1 = tk.Label(main,
                            text=str(lat_absolut) + " " + str(lat_direction),
                            font=("Arial,12"))
    
    label_result3_0 = tk.Label(main,
                            text="Zeitpunkt = ",
                            font=("Arial,12"))
    
    label_result3_1 = tk.Label(main,
                            text=str(timestamp),
                            font=("Arial,12"))
    
    button_ermittle = tk.Button(main,
                               text=("D A T E N"),
                               command=refreshGui)
    
    button_map = tk.Button(main,
                           text=("K A R T E"),
                           command=map)

    
    # Fenster erstellen
    main.columnconfigure(0, weight=1)
    main.columnconfigure(1, weight=5)
    label_headline.grid(row=0, sticky=tk.N, pady=50, padx=150)
    label_status_0.grid(row=2, column=0, sticky=tk.W, padx=100)
    label_status_1.grid(row=2, column=1, sticky=tk.W)
    label_result1_0.grid(row=3, column=0, sticky=tk.W, padx=100)
    label_result1_1.grid(row=3, column=1, sticky=tk.W)
    label_result2_0.grid(row=4, column=0, sticky=tk.W, padx=100)
    label_result2_1.grid(row=4, column=1, sticky=tk.W)
    label_result3_0.grid(row=5, column=0, sticky=tk.W, padx=100)
    label_result3_1.grid(row=5, column=1, sticky=tk.W)
    button_ermittle.grid(row=7, column=0, pady=40)
    button_map.grid(row=7, column=0, sticky=tk.E)
>>>>>>> Stashed changes
    
    main.mainloop()

# Hauptprogramm
if __name__ == "__main__":
    gui()