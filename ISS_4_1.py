import tkinter as tk
from tkinter import messagebox
from tkinter import Menu
import requests
import time

lon = 0
lon_absolut = 0
lon_direction = ""
lat = 0
lat_absolut = 0
lat_direction = ""
timestamp = 0
status = "Deaktiviert"

# Versions-Meldung
def showVersion():
    messagebox.showinfo("Version",
                        "4.1.0 vom 20.01.2025")


# Copyright-Meldung
def showCopyright():
    messagebox.showinfo("Copyright",
                        "Torge Hauschild")


# Programm beenden
def quitProgram():
    decision = messagebox.askyesno("Beenden",
                            "Möchten Sie das Programm beenden?")
    if decision:
        exit()


# Fehler-Meldung
def showError():
    messagebox.showerror("Fehler",
                        "Es ist ein Verbindungsfehler zur API aufgetreten!")


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
        showError()
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
    label_status = tk.Label(main,
                            text="Status: " + str(status),
                            font=("Arial,12"))

    label_result1 = tk.Label(main,
                            text="Längengrad = " + str(lon_absolut) + " " + str(lon_direction),
                            font=("Arial,12"))
    
    label_result2 = tk.Label(main,
                            text="Breitengrad = " + str(lat_absolut) + " " + str(lat_direction),
                            font=("Arial,12"))
    
    label_result3 = tk.Label(main,
                            text="Zeitpunkt = " + str(timestamp),
                            font=("Arial,12"))
    
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
    
    main.mainloop()

# Hauptprogramm
if __name__ == "__main__":
    gui()