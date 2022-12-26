from tkinter import*
from PIL import ImageTk, Image

import tkinter.font 
from gpiozero import LED

import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM) 
import time
import serial

import speech_recognition as sr
from datetime import date
from gpiozero import LED
from time import sleep

r = sr.Recognizer()
mic = sr.Microphone()

ser = serial.Serial('/dev/ttyACM1',9600, timeout=1) # or ACM1/0
ser.flush()



## hardware
Led = LED (14)

## GUI DEFINITIONS ##z
win = Tk()
win.title("EMPERICAL SYSTEM")
win.geometry("1300x800")
myFont = tkinter.font. Font(family = 'Helvetica', size = 12, weight = "bold")


### EVENT FUNCTIONS ###
def placeholder():
    popup = Toplevel()
    popup.title("placeholder")
    # Fill the popup window with Canvas() example image
    C = Canvas(popup, bg ="aqua" , height = 250 , width = 300)
    coord = 10 ,50 , 240, 210
    arc = C.create_arc(coord, start = 0, extent = 150, fill = "blue")
    C.pack()
    popup.mainloop()

def displayLed():
    Led.on()
    time.sleep(0.5)
    Led.off()
    time.sleep(0.5)

# Code required for information display of Capitals    
def Amarvati():
    popup = Toplevel()
    popup.title("Amarvati")
    text = Text(popup)
    text.insert(INSERT, "Description: ")  
    text.insert(END, "CAPITAL OF ANDRA PRADESH \nAmaravati was founded by the former chief minister of Andhra Pradesh, N. Chandrababu Naidu in 2014.\nIt is roughly located in the geographical center of Andhra Pradesh.")  
    text.pack() 
    ser.write(b"Amarvation\n")
    def closepopup():
        ser.write(b"Amarvatioff\n")
        popup.destroy()
    popup.protocol("WM_DELETE_WINDOW", closepopup)
    popup.mainloop()

def Itanagar():
    popup = Toplevel()
    popup.title("Itanagar")
    text = Text(popup)
    text.insert(INSERT, "Description: ")  
    text.insert(END, "CAPITAL OF ARUNACHAL PRADESH \n* Itanagar was named after the Ita fort (fort made of bricks) located in the city.\n* The average annual precipitation in Itanagar is quite high. There are more than 120 rainy days in a year. ")  
    text.pack()
    ser.write(b"Itanagaron\n") 
    displayLed()
    def closepopup():
        ser.write(b"Itanagaroff\n") 
        popup.destroy()
    popup.protocol("WM_DELETE_WINDOW", closepopup)
    popup.mainloop()

def Dispur():
    popup = Toplevel()
    popup.title("Dispur")
    text = Text(popup)
    text.insert(INSERT, "Description: ")  
    text.insert(END, "CAPITAL OF ASSAM \n* Dispur is a locality within Guwahati city. \nThe legislative assembly is located in Dispur.")  
    text.pack() 
    ser.write(b"Dispuron\n") 
    def closepopup():
        ser.write(b"Dispuroff\n") 
        popup.destroy()
    popup.protocol("WM_DELETE_WINDOW", closepopup)
    popup.mainloop()

def Patna():
    popup = Toplevel()
    popup.title("Patna")
    text = Text(popup)
    text.insert(INSERT, "Description: ")  
    text.insert(END, "CAPITAL OF BIHAR \n* Patna is one of the oldest cities in the world.\nFormerly known as Pataliputra, Patna was founded in 490 BCE.")  
    text.pack() 
    ser.write(b"Patnaon\n") 
    def closepopup():
        ser.write(b"Patnaoff\n") 
        popup.destroy()
    popup.protocol("WM_DELETE_WINDOW", closepopup)
    popup.mainloop()

def Raipur():
    popup = Toplevel()
    popup.title("Raipur")
    text = Text(popup)
    text.insert(INSERT, "Description: ")  
    text.insert(END, "CAPITAL OF CHHATTISGARH \n* Raipur is famous for its premier educational institutions. \nThe city is home to an IIM, an NIT, an NLU, an AIIMs, and an IIIT.")  
    text.pack() 
    ser.write(b"Raipuron\n") 
    def closepopup():
        ser.write(b"Raipuroff\n") 
        popup.destroy()
    popup.protocol("WM_DELETE_WINDOW", closepopup)
    popup.mainloop()

def Panaji():
    popup = Toplevel()
    popup.title("Panaji")
    text = Text(popup)
    text.insert(INSERT, "Description: ")  
    text.insert(END, "CAPITAL OF GOA \n* According to the 2011 census, Panaji had an average literacy rate of 90.98 %.")  
    text.pack() 
    ser.write(b"Panajion\n") 
    def closepopup():
        ser.write(b"Panajioff\n") 
        popup.destroy()
    popup.protocol("WM_DELETE_WINDOW", closepopup)
    popup.mainloop()

def Gandhinagar():
    popup = Toplevel()
    popup.title("Gandhinagar")
    text = Text(popup)
    text.insert(INSERT, "Description: ")  
    text.insert(END, "CAPITAL OF GUJRAT \n* The city of Gandhinagar is famous as a “green city”. \nThe green cover in the city is around (54%) of its land area.")  
    text.pack() 
    ser.write(b"Gandhinagaron\n") 
    def closepopup():
        ser.write(b"Gandhinagaroff\n") 
        popup.destroy()
    popup.protocol("WM_DELETE_WINDOW", closepopup)
    popup.mainloop()

def Chandigarh():
    popup = Toplevel()
    popup.title("Chandigarh")
    text = Text(popup)
    text.insert(INSERT, "Description: ")  
    text.insert(END, "CAPITAL OF HARYANA AND PUNJAB \n* The city is the capital of both Haryana and Punjab. \nIt is also a union territory.")  
    text.pack() 
    ser.write(b"Chandigarhon\n")
    def closepopup():
        ser.write(b"Chandigarhoff\n")
        popup.destroy()
    popup.protocol("WM_DELETE_WINDOW", closepopup)
    popup.mainloop()

def Shimla():
    popup = Toplevel()
    popup.title("Shimla")
    text = Text(popup)
    text.insert(INSERT, "Description: ")  
    text.insert(END, "CAPITAL OF HIMACHAL PRADESH(Summer) \n* Shimla is a famous tourist destination. \nThe city is also the last station of the Kalka-Shimla railway line, a UNESCO world heritage site.")  
    text.pack() 
    ser.write(b"Shimlaon\n")
    def closepopup():
        ser.write(b"Shimlaoff\n")
        popup.destroy()
    popup.protocol("WM_DELETE_WINDOW", closepopup)
    popup.mainloop()

def Dharamshala():
    popup = Toplevel()
    popup.title("Dharamshala")
    text = Text(popup)
    text.insert(INSERT, "Description: ")  
    text.insert(END, "CAPITAL OF HIMACHAL PRADESH(Winter) \n* In March 2017, Dharamshala was declared the second capital of Himachal Pradesh. \n* Surrounded by cedar forests on the edge of the Himalayas, this hillside city is home to the Dalai Lama and the Tibetan government-in-exile. ")  
    text.pack() 
    ser.write(b"Dharamshalaon\n")
    def closepopup():
        ser.write(b"Dharamshalaoff\n")
        popup.destroy()
    popup.protocol("WM_DELETE_WINDOW", closepopup)
    popup.mainloop()

def Ranchi():
    popup = Toplevel()
    popup.title("Ranchi")
    text = Text(popup)
    text.insert(INSERT, "Description: ")  
    text.insert(END, "CAPITAL OF JHARKHAND \n* Ranchi is also known as the “city of waterfalls”. \nDassam Falls, Hundru Falls, and Hirni Falls are some famous waterfalls in Ranchi.")  
    text.pack() 
    ser.write(b"Ranchion\n")
    def closepopup():
        ser.write(b"Ranchioff\n")
        popup.destroy()
    popup.protocol("WM_DELETE_WINDOW", closepopup)
    popup.mainloop()

def Bengaluru():
    popup = Toplevel()
    popup.title("Bengaluru")
    text = Text(popup)
    text.insert(INSERT, "Description: ")  
    text.insert(END, "CAPITAL OF KARNATAKA \n* Known as the “Silicon Valley of India“, Bengaluru is an important city in India. \n* It is the third most populous city in India. \n* The city enjoys a pleasant climate throughout the year.")  
    text.pack() 
    ser.write(b"Bengaluruon\n")
    def closepopup():
        ser.write(b"Bengaluruoff\n")
        popup.destroy()
    popup.protocol("WM_DELETE_WINDOW", closepopup)
    popup.mainloop()

def Thiruvananthapuram():
    popup = Toplevel()
    popup.title("Thiruvananthapuram")
    text = Text(popup)
    text.insert(INSERT, "Description: ")  
    text.insert(END, "CAPITAL OF KERALA \n* The Padmanabhaswamy temple, located in Thiruvananthapuram, is one of the richest religious structures in the world. \n* It has treasures worth billions of dollars stored in its vaults.")  
    text.pack() 
    ser.write(b"Thiruvananthapuramon\n")
    def closepopup():
        ser.write(b"Thiruvananthapuramoff\n")
        popup.destroy()
    popup.protocol("WM_DELETE_WINDOW", closepopup)
    popup.mainloop()

def Bhopal():
    popup = Toplevel()
    popup.title("Bhopal")
    text = Text(popup)
    text.insert(INSERT, "Description: ")  
    text.insert(END, "CAPITAL OF MADHYA PRADESH \n* The infamous Bhopal Gas Tragedy which took place in December 1984 claimed the lives of thousands of people. The exact death toll is still unknown. \n* Bhopal was ranked the 14th cleanest city in the 2021 Swachh Survekshan.")  
    text.pack() 
    ser.write(b"Bhopalon\n")
    def closepopup():
        ser.write(b"Bhopaloff\n")
        popup.destroy()
    popup.protocol("WM_DELETE_WINDOW", closepopup)
    popup.mainloop()

def Mumbai():
    popup = Toplevel()
    popup.title("Mumbai")
    text = Text(popup)
    text.insert(INSERT, "Description: ")  
    text.insert(END, "CAPITAL OF MAHARASTRA \n* Mumbai is the financial capital of India. \nThe city is also the home of Hindi and Marathi cinema.")  
    text.pack() 
    ser.write(b"Mumbaion\n")
    def closepopup():
        ser.write(b"Mumbaioff\n")
        popup.destroy()
    popup.protocol("WM_DELETE_WINDOW", closepopup)
    popup.mainloop()

def Imphal():
    popup = Toplevel()
    popup.title("Imphal")
    text = Text(popup)
    text.insert(INSERT, "Description: ")  
    text.insert(END, "CAPITAL OF MANIPUR \n* Interestingly, Imphal city’s area falls under both Imphal East and Imphal West districts of Manipur.")  
    text.pack() 
    ser.write(b"Imphalon\n")
    def closepopup():
        ser.write(b"Imphaloff\n")
        popup.destroy()
    popup.protocol("WM_DELETE_WINDOW", closepopup)
    popup.mainloop()

def Shillong():
    popup = Toplevel()
    popup.title("Shillong")
    text = Text(popup)
    text.insert(INSERT, "Description: ")  
    text.insert(END, "CAPITAL OF MEGHALAYA \n* The British used to call Shillong the “Scotland of the East“.\n* Like most of Meghalaya, Shillong also receives a lot of precipitation with more than 110 average rainy days in a year.")  
    text.pack() 
    ser.write(b"Shillongon\n")
    def closepopup():
        ser.write(b"Shillongoff\n")
        popup.destroy()
    popup.protocol("WM_DELETE_WINDOW", closepopup)
    popup.mainloop()

def Aizawl():
    popup = Toplevel()
    popup.title("Aizawl")
    text = Text(popup)
    text.insert(INSERT, "Description: ")  
    text.insert(END, "CAPITAL OF MIZORAM \n* According to the 2011 census, 93.63 % population of Aizawl is Christian.")  
    text.pack() 
    ser.write(b"Aizawlon\n")
    def closepopup():
        ser.write(b"Aizawloff\n")
        popup.destroy()
    popup.protocol("WM_DELETE_WINDOW", closepopup)
    popup.mainloop()

def Kohima():
    popup = Toplevel()
    popup.title("Kohima")
    text = Text(popup)
    text.insert(INSERT, "Description: ")  
    text.insert(END, "CAPITAL OF NAGALAND \n* Just like Aizawl, Kohima also has a majority Christian population.")  
    text.pack() 
    ser.write(b"Kohimaon\n")
    def closepopup():
        ser.write(b"Kohimaoff\n")
        popup.destroy()
    popup.protocol("WM_DELETE_WINDOW", closepopup)
    popup.mainloop()

def Bhubaneswar():
    popup = Toplevel()
    popup.title("Bhubaneswar")
    text = Text(popup)
    text.insert(INSERT, "Description: ")  
    text.insert(END, "CAPITAL OF ODISHA \n* Known as the “temple city“, Bhubaneswar has many famous Hindu, Buddhist, and Jain temples.\n* The literacy rate of Bhubaneshwar (91.87 %) is much higher than the national average literacy rate (74.04 ℅).")  
    text.pack() 
    ser.write(b"Bhubaneswaron\n")
    def closepopup():
        ser.write(b"Bhubaneswaroff\n")
        popup.destroy()
    popup.protocol("WM_DELETE_WINDOW", closepopup)
    popup.mainloop()

def Jaipur():
    popup = Toplevel()
    popup.title("Jaipur")
    text = Text(popup)
    text.insert(INSERT, "Description: ")  
    text.insert(END, "CAPITAL OF RAJASTHAN \n* Known as the “pink city“, Jaipur is the 10th most populous city in India.\n* Jaipur is a part of the Golden Triangle (Delhi, Agra, Jaipur), the foremost tourist circuit in India.")  
    text.pack() 
    ser.write(b"Jaipuron\n")
    def closepopup():
        ser.write(b"Jaipuroff\n")
        popup.destroy()
    popup.protocol("WM_DELETE_WINDOW", closepopup)
    popup.mainloop()

def Gangtok():
    popup = Toplevel()
    popup.title("Gangtok")
    text = Text(popup)
    text.insert(INSERT, "Description: ")  
    text.insert(END, "CAPITAL OF SIKKIM \n* Gangtok is a popular tourist destination. For a capital city, Gangtok has a very low population of only around 1 lakh.\n* On clear days, the third highest mountain in the world, the Kanchenjunga is easily visible from Gangtok")  
    text.pack() 
    ser.write(b"Gangtokon\n")
    def closepopup():
        ser.write(b"Gangtokoff\n")
        popup.destroy()
    popup.protocol("WM_DELETE_WINDOW", closepopup)
    popup.mainloop()

def Chennai():
    popup = Toplevel()
    popup.title("Chennai")
    text = Text(popup)
    text.insert(INSERT, "Description: ")  
    text.insert(END, "CAPITAL OF TAMIL NADU \n* Known as the “health capital” of India, Chennai is the sixth most populous city in India.\n* Chennai is also referred to as “the Detroit of India” as the majority of the Indian automobile industry is based in Chennai.")  
    text.pack() 
    ser.write(b"Chennaion\n")
    def closepopup():
        ser.write(b"Chennaioff\n")
        popup.destroy()
    popup.protocol("WM_DELETE_WINDOW", closepopup)
    popup.mainloop()

def Hyderabad():
    popup = Toplevel()
    popup.title("Hyderabad")
    text = Text(popup)
    text.insert(INSERT, "Description: ")  
    text.insert(END, "CAPITAL OF TELANGANA \n* Hyderabad is the fourth most populous city in India. \n* It is one of the fastest-growing IT cities in India.")  
    text.pack() 
    ser.write(b"Hyderabadon\n")
    def closepopup():
        ser.write(b"Hyderabadoff\n")
        popup.destroy()
    popup.protocol("WM_DELETE_WINDOW", closepopup)
    popup.mainloop()

def Agartala():
    popup = Toplevel()
    popup.title("Agartala")
    text = Text(popup)
    text.insert(INSERT, "Description: ")  
    text.insert(END, "CAPITAL OF TRIPURA \n* Bengali is the most spoken language in Agartala.\n* Agartala is just a few kilometers from the eastern Indo-Bangladesh border.")  
    text.pack() 
    ser.write(b"Agartalaon\n")
    def closepopup():
        ser.write(b"Agartalaon\n")
        popup.destroy()
    popup.protocol("WM_DELETE_WINDOW", closepopup)
    popup.mainloop()

def Lucknow():
    popup = Toplevel()
    popup.title("Lucknow")
    text = Text(popup)
    text.insert(INSERT, "Description: ")  
    text.insert(END, "CAPITAL OF UTTAR PRADESH \n* Located in the Awadh region of Uttar Pradesh, Lucknow is a major Indian city. The city is among the “happiest” Indian cities.")  
    text.pack() 
    ser.write(b"Lucknowon\n")
    def closepopup():
        ser.write(b"Lucknowoff\n")
        popup.destroy()
    popup.protocol("WM_DELETE_WINDOW", closepopup)
    popup.mainloop()

def Dehradun():
    popup = Toplevel()
    popup.title("Dehradun")
    text = Text(popup)
    text.insert(INSERT, "Description: ")  
    text.insert(END, "CAPITAL OF UTTARAKHAND(Winter) \n* The city of Dehradun lies in the Doon valley with the famous hill station Mussoorie just 30 kilometers from the city center.")  
    text.pack() 
    ser.write(b"Dehradunon\n")
    def closepopup():
        ser.write(b"Dehradunoff\n")
        popup.destroy()
    popup.protocol("WM_DELETE_WINDOW", closepopup)
    popup.mainloop()

def Gairsain():
    popup = Toplevel()
    popup.title("Gairsain")
    text = Text(popup)
    text.insert(INSERT, "Description: ")  
    text.insert(END, "CAPITAL OF UTTARAKHAND(Summer) \n* Gairsain is announced as the summer capital of Uttarakhand. However, its infrastructure is still in a developmental phase.")  
    text.pack() 
    ser.write(b"Gairsainon\n")
    def closepopup():
        ser.write(b"Gairsainoff\n")
        popup.destroy()
    popup.protocol("WM_DELETE_WINDOW", closepopup)
    popup.mainloop()

def Kolkata():
    popup = Toplevel()
    popup.title("Kolkata")
    text = Text(popup)
    text.insert(INSERT, "Description: ")  
    text.insert(END, "CAPITAL OF WEST BENGAL \n* Kolkata is known as the “cultural capital of India“. It was the capital of British India for a long time.\n* Kolkata is the seventh most populous city in the country.")  
    text.pack() 
    ser.write(b"Kolkataon\n")
    def closepopup():
        ser.write(b"Kolkataoff\n")
        popup.destroy()
    popup.protocol("WM_DELETE_WINDOW", closepopup)
    popup.mainloop()

# Code required for the details of Rivers 
def NARMADA():
    popup = Toplevel()
    popup.title("NARMADA")
    text = Text(popup)
    text.insert(INSERT, "Description: ")  
    text.insert(END, "source- narmada khund - vindhyachal parvat amarkantak plateau , MP \nelevation - 1048 m (3438 ft) \ndischarge - 1447 m^3/s \nsoil type - black cotton soil type ")  
    text.pack() 
    displayLed()
    def closepopup():
        Led.off()
        popup.destroy()
    popup.protocol("WM_DELETE_WINDOW", closepopup)
    popup.mainloop()

def GANGES():
    popup = Toplevel()
    popup.title("GANGES")
    text = Text(popup)
    text.insert(INSERT, "Description: ")  
    text.insert(END, "source - confluence at devprayag, uk of alakanda river, ganges delta \nelevation - 7,000 m above mean sea level \ndischarge - 12,020 m³/s  \nsoil type - submontane soils and alluvial soils, covering (58%) of the basin area, have very high erodibility; \nred soils covering (12%) of the basin area have high erodibility \nred & yellow soils and mixed red and black soils covering an area of (8%) have moderate erodibility \ndeep black soils and medium black soils covering")  
    text.pack() 
    displayLed()
    def closepopup():
        Led.off()
        popup.destroy()
    popup.protocol("WM_DELETE_WINDOW", closepopup)
    popup.mainloop()

def LUNI():
    popup = Toplevel()
    popup.title("LUNI")
    text = Text(popup)
    text.insert(INSERT, "Description: ")  
    text.insert(END, "source - aravalli range, nagri-sihawa, dhamtari,dandakaranya, chattisgarh \nelevation - 890m above sea level \ndischarge- 496kms \nsoil type - Saline Sodic soils are seen in the far flood plains of river Ghaggar and in Luni Basin")  
    text.pack() 
    displayLed()
    def closepopup():
        Led.off()
        popup.destroy()
    popup.protocol("WM_DELETE_WINDOW", closepopup)
    popup.mainloop()

def TAPTIRIVER():
    popup = Toplevel()
    popup.title("TAPTI RIVER")
    text = Text(popup)
    text.insert(INSERT, "Description: ")  
    text.insert(END, "source- multai, madhya pradesh - dumas, surat, gujarat \nelevation - 752 m \ndischarge- avg - 489 m^3/s \nsoil type - black soils")  
    text.pack() 
    displayLed()
    def closepopup():
        Led.off()
        popup.destroy()
    popup.protocol("WM_DELETE_WINDOW", closepopup)
    popup.mainloop()
    
def GODAWRI():
    popup = Toplevel()
    popup.title("GODAWRI")
    text = Text(popup)
    text.insert(INSERT, "Description: ")  
    text.insert(END, "source - brahmagiri mountain, trimbakeshwar,nashik, maharashtra \nelevation - 920 m \ndischarge - 3505 m^3/s \nsoil type - The Godavari basin consists of large undulating plains divided by low flat topped hill ranges. \nThe important soil types found in the basins are black soils, red soils, lateritic soils, alluvium, mixed soils and saline and alkaline soils.")  
    text.pack() 
    displayLed()
    def closepopup():
        Led.off()
        popup.destroy()
    popup.protocol("WM_DELETE_WINDOW", closepopup)
    popup.mainloop()

def PALAR():
    popup = Toplevel()
    popup.title("PALAR")
    text = Text(popup)
    text.insert(INSERT, "Description: ")  
    text.insert(END, "source - on	Kolar District in Karnataka, India \nelevation - 800 m above MSL \ndischarge - 6000 cusecs of water \nsoil type- The predominant soil order found in this river basin is Inceptisol, Alfisol, Entisol, Ultisols and Vertisol")  
    text.pack() 
    displayLed()
    def closepopup():
        Led.off()
        popup.destroy()
    popup.protocol("WM_DELETE_WINDOW", closepopup)
    popup.mainloop()

def KRISHNA():
    popup = Toplevel()
    popup.title("KRISHNA")
    text = Text(popup)
    text.insert(INSERT, "Description: ")  
    text.insert(END, "source - near mahabaleshwar , jor village, dist satara \nelevation - 0 m \ndischarge - avg - 2213 m^3/s \nsoil type - black soils, red soils, laterite and lateritic soils, alluvium, mixed soils, red and black soils and saline and alkaline soils.")  
    text.pack() 
    displayLed()
    def closepopup():
        Led.off()
        popup.destroy()
    popup.protocol("WM_DELETE_WINDOW", closepopup)
    popup.mainloop()
    
def MAHANADI():
    popup = Toplevel()
    popup.title("MAHANADI")
    text = Text(popup)
    text.insert(INSERT, "Description: ")  
    text.insert(END, "source -Nagri-Sihawa, Dhamtari, Dandakaranya, Chhattisgarh, India \nelevation - 422 mts. above mean sea level \ndischarge - 2119 m ^3/s \nsoil type -The main soil types found in the basin are red and yellow soils, mixed red and black soils, laterite soils and deltaic soils.")  
    text.pack() 
    displayLed()
    def closepopup():
        Led.off()
        popup.destroy()
    popup.protocol("WM_DELETE_WINDOW", closepopup)
    popup.mainloop()

# OTHER widgets function decleration
def HowTo():
    popup = Toplevel()
    popup.title("How-To")
    text = Text(popup)
    text.insert(INSERT, "Description: ")  
    text.insert(END, "")  
    text.pack() 
    displayLed()
    def closepopup():
        Led.off()
        popup.destroy()
    popup.protocol("WM_DELETE_WINDOW", closepopup)
    popup.mainloop()

def About():
    popup = Toplevel()
    popup.title("About")
    text = Text(popup)
    text.insert(INSERT, "About Us: ")  
    text.insert(END, "\nGeography was a subject that was challenging for us to remember and comprehend when we were pupils. Students are less likely to engage their brains these days because of the availability of so much technology; instead, they are happy to just look for videos on YouTube in the belief that doing so will help them understand the concept. In order to reduce the reliance on Google and YouTube, which can be damaging to students' overall growth, we, as software engineering students, have devised this practical and entertaining method to facilitate learning and teaching for both students and professors.")  
    text.pack() 
    displayLed()
    def closepopup():
        Led.off()
        popup.destroy()
    popup.protocol("WM_DELETE_WINDOW", closepopup)
    popup.mainloop()
    
    
def close():
    RPi.GPIO.cleanup()
    win.destroy()
    
menubar = Menu(win)
menubar.config(bg="AQUA", fg="BLACK")

# Create menu entry and sub-options 
rivermenu = Menu(menubar, tearoff=0)
rivermenu.add_command(label="NARMADA", command=NARMADA) 
rivermenu.add_command(label="GANGES" , command=GANGES) 
rivermenu.add_command(label="LUNI" , command=LUNI) 
rivermenu.add_command(label="TAPTI RIVER" , command=TAPTIRIVER) 
rivermenu.add_command(label="GODAWRI" , command=GODAWRI) 
rivermenu.add_command(label="PALAR" , command=PALAR) 
rivermenu.add_command(label="KRISHNA" , command=KRISHNA) 
rivermenu.add_command(label="MAHANADI" , command=MAHANADI) 
menubar.add_cascade(label="Rivers", menu=rivermenu)

# Create more menus
capitalsmenu = Menu(menubar, tearoff=0)
capitalsmenu.add_command(label="Amarvati" , command=Amarvati)
capitalsmenu.add_command(label="Itanagar" , command=Itanagar)
capitalsmenu.add_command(label="Dispur" , command=Dispur)
capitalsmenu.add_command(label="Patna", command=Patna) 
capitalsmenu.add_command(label="Raipur" , command=Raipur) 
capitalsmenu.add_command(label="Panaji" , command=Panaji) 
capitalsmenu.add_command(label="Gandhinagar" , command=Gandhinagar) 
capitalsmenu.add_command(label="Chandigarh" , command=Chandigarh) 
capitalsmenu.add_command(label="Shimla" , command=Shimla)
capitalsmenu.add_command(label="Dharamshala" , command=Dharamshala) 
capitalsmenu.add_command(label="Ranchi" , command=Ranchi) 
capitalsmenu.add_command(label="Bengaluru" , command=Bengaluru) 
capitalsmenu.add_command(label="Thiruvananthapuram" , command=Thiruvananthapuram) 
capitalsmenu.add_command(label="Bhopal" , command=Bhopal) 
capitalsmenu.add_command(label="Mumbai" , command=Mumbai) 
capitalsmenu.add_command(label="Imphal" , command=Imphal) 
capitalsmenu.add_command(label="Shillong" , command=Shillong) 
capitalsmenu.add_command(label="Aizawl" , command=Aizawl) 
capitalsmenu.add_command(label="Kohima" , command=Kohima) 
capitalsmenu.add_command(label="Bhubaneswar" , command=Bhubaneswar) 
capitalsmenu.add_command(label="Jaipur" , command=Jaipur) 
capitalsmenu.add_command(label="Gangtok" , command=Gangtok) 
capitalsmenu.add_command(label="Chennai" , command=Chennai) 
capitalsmenu.add_command(label="Hyderabad" , command=Hyderabad) 
capitalsmenu.add_command(label="Agartala" , command=Agartala) 
capitalsmenu.add_command(label="Lucknow" , command=Lucknow) 
capitalsmenu.add_command(label="Dehradun" , command=Dehradun) 
capitalsmenu.add_command(label="Gairsain" , command=Gairsain) 
capitalsmenu.add_command(label="Kolkata" , command=Kolkata) 
menubar.add_cascade(label="Capitals" , menu=capitalsmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="How-To", command=HowTo)
helpmenu.add_separator()
helpmenu.add_command(label="About", command=About) 
menubar.add_cascade(label="Help", menu=helpmenu)

quitmenu = Menu(menubar, tearoff=0)
quitmenu.add_command(label="YES", command=close) 
quitmenu.add_command(label="NO") 
menubar.add_cascade(label="Quit", menu=quitmenu)

# Display the menu
win.config(menu=menubar)

### WIDGETS ###
"""
ledButton = Button (win, text = 'Blink Name', font = myFont, command = lambda: Morse_code(ledinput), bg = 'orange', height = 1)
ledButton.grid (row=0, column=2)

code = Entry(win, font=myFont, width=15)
code.grid(row=0, column=1)

exitButton = Button (win, text = 'Exit', font = myFont, command = close, bg = 'aqua', height = 1, width = 6)
exitButton.grid (row=2, column=1)
"""

#Creating Frame and Image element for Map
framemap = Frame(win, width=500, height=594)
framemap.pack()
framemap.place(anchor='center', relx=0.5, rely=0.5)

# Create an object of tkinter ImageTk
imgmap = ImageTk.PhotoImage(Image.open("capitalsmap.png"))

# Create a Label Widget to display the text or Image
labelmap = Label(framemap, image = imgmap)
labelmap.pack()

'''
#Creating Frame and Image element for Rivers
framerivers = Frame(win, width=806, height=992)
framerivers.pack()
framerivers.place(anchor='center', relx=0.5, rely=0.5)

# Create an object of tkinter ImageTk
imgrivers = ImageTk.PhotoImage(Image.open("riversmap.png"))

# Create a Label Widget to display the text or Image
labelrivers = Label(framerivers, image = imgrivers)
labelrivers.pack()
'''
win.protocol("WM_DELETE_WINDOW", close) # exit cleanly

win.mainloop() # Loop forever

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


