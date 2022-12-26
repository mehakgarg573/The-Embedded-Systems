import speech_recognition as sr
from datetime import date
from gpiozero import LED
from time import sleep
import serial

r = sr.Recognizer()
mic = sr.Microphone()

ser = serial.Serial('/dev/ttyACM1',9600, timeout=1) # or ACM1/0
ser.flush()

print("hello")
while True:
    with mic as source:
        audio = r.listen(source)
    words = r.recognize_google(audio)
    print(words)

    if words == "today":
        print(date.today())

    if words == "Amarawati":
        ser.write(b"Amarawati\n")

    if words == "Itanagar":
        ser.write(b"Itanagar\n")

    if words == "Dispur":
        ser.write(b"Dispur\n")
        
    if words == "Patna":
        ser.write(b"Patna\n")

    if words == "Raipur":
        ser.write(b"Raipur\n")

    if words == "Panaji":
        ser.write(b"Panaji\n")

    if words == "Gandhinagar":
        ser.write(b"Gandhinagar\n")

    if words == "Chandigarh":
        ser.write(b"Chandigarh\n")
        
    if words == "Shimla":
        ser.write(b"Shimla\n")
        
    if words == "Srinagar":
        ser.write(b"Srinagar\n")
        
    if words == "Ranchi":
        ser.write(b"Ranchi\n")
        
    if words == "Bengaluru":
        ser.write(b"Bengaluru\n")
        
    if words == "Trivandrum":
        ser.write(b"Trivandrum\n")
        
    if words == "Bhopal":
        ser.write(b"Bhopal\n")
        
    if words == "Mumbai":
        ser.write(b"Mumbai\n")
        
    if words == "Imphal":
        ser.write(b"Imphal\n")
        
    if words == "Shillong":
        ser.write(b"Shillong\n")
        
    if words == "Aizawl":
        ser.write(b"Awzawl\n")
        
    if words == "Kohima":
        ser.write(b"Kohima\n")
        
    if words == "Bhubaneswar":
        ser.write(b"Bhubaneswar\n")
        
    if words == "Jaipur":
        ser.write(b"Jaipur\n")
        
    if words == "Gangtok":
        ser.write(b"Gangtok\n")
        
    if words == "Chennai":
        ser.write(b"Chennai\n")
        
    if words == "Hyderabad":
        ser.write(b"Hyderabad\n")
        
    if words == "Agartala":
        ser.write(b"Agartala\n")
        
    if words == "Lucknow":
        ser.write(b"Lucknow\n")
        
    if words == "Dheradun":
        ser.write(b"Dheradun\n")
        
    if words == "Kolkata":
        ser.write(b"Kolkate\n")
    

    if words == "exit":
        print("...")
        sleep(1)
        print("...")
        sleep(1)
        print("...")
        sleep(1)
        print("Goodbye")
        break
