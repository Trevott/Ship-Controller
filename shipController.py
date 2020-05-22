import RPi.GPIO as GPIO
from time import sleep
from tkinter import *

#Pins for motor driver inputs
balElőre = 23
balHátra = 24
balEnged = 5

jobbElőre = 16
jobbHátra = 25
jobbEnged = 6

előreLenyomva = False
hátraLenyomva = False
jobbLenyomva = False
balLenyomva = False

def hátra(event):
    hátraLenyomva = True

    megfeleőGombotTöröl(előreLenyomva, hátraLenyomva, balLenyomva, jobbLenyomva)
    
    GPIO.output(jobbHátra, GPIO.HIGH)
    GPIO.output(balHátra, GPIO.HIGH)

def előre(event):
    előreLenyomva = True

    megfeleőGombotTöröl(előreLenyomva, hátraLenyomva, balLenyomva, jobbLenyomva)
    
    GPIO.output(jobbElőre, GPIO.HIGH)
    GPIO.output(balElőre, GPIO.HIGH)

def jobbra(event):
    jobbLenyomva = True

    megfeleőGombotTöröl(előreLenyomva, hátraLenyomva, balLenyomva, jobbLenyomva)
    
    GPIO.output(balElőre, GPIO.HIGH)

def balra(event):
    balLenyomva = True

    megfeleőGombotTöröl(előreLenyomva, hátraLenyomva, balLenyomva, jobbLenyomva)
    
    GPIO.output(jobbElőre, GPIO.HIGH)

def előreÁllj(event):
    előreLenyomva = False

    megfeleőGombotVisszaállít(előreLenyomva, hátraLenyomva, balraLenyomva, jobbraLenyomva)

    GPIO.output(jobbElőre, GPIO.LOW)
    GPIO.output(balElőre, GPIO.LOW)

def hátraÁllj(event):
    hátraLenyomva = False

    megfeleőGombotVisszaállít(előreLenyomva, hátraLenyomva, balraLenyomva, jobbraLenyomva)

    GPIO.output(jobbHátra, GPIO.LOW)
    GPIO.output(balHátra, GPIO.LOW)

def balraÁllj(event):
    balLenyomva = False

    megfeleőGombotVisszaállít(előreLenyomva, hátraLenyomva, balraLenyomva, jobbraLenyomva)

    GPIO.output(jobbElőre, GPIO.LOW)

def jobbraÁllj(event):
    jobbLenyomva = False

    megfeleőGombotVisszaállít(előreLenyomva, hátraLenyomva, balraLenyomva, jobbraLenyomva)

    GPIO.output(balElőre, GPIO.LOW)

def megfeleőGombotVisszaállít(eLenyomva, hLenyomva, bLenyomva, jLenyomva):
    if (eLenyomva == True):
        GPIO.output(jobbElőre, GPIO.HIGH)
        GPIO.output(balElőre, GPIO.HIGH)
    if (hLenyomva == True):
        GPIO.output(jobbHátra, GPIO.HIGH)
        GPIO.output(balHátra, GPIO.HIGH)
    if (bLenyomva == True):
        GPIO.output(jobbElőre, GPIO.HIGH)
    if (jLenyomva == True):
        GPIO.output(balElőre, GPIO.HIGH)

def megfeleőGombotTöröl(eLenyomva, hLenyomva, bLenyomva, jLenyomva):
    if (eLenyomva == True):
        GPIO.output(jobbElőre, GPIO.LOW)
        GPIO.output(balElőre, GPIO.LOW)
    if (hLenyomva == True):
        GPIO.output(jobbHátra, GPIO.LOW)
        GPIO.output(balHátra, GPIO.LOW)
    if (bLenyomva == True):
        GPIO.output(jobbElőre, GPIO.LOW)
    if (jLenyomva == True):
        GPIO.output(balElőre, GPIO.LOW)

if __name__ == '__main__': #program start from here
    GPIO.setmode(GPIO.BCM) #GPIO numbering
    GPIO.setup(balElőre, GPIO.OUT) #All pins as output
    GPIO.setup(balHátra, GPIO.OUT)
    GPIO.setup(balEnged, GPIO.OUT)
    
    GPIO.setup(jobbElőre, GPIO.OUT)
    GPIO.setup(jobbHátra, GPIO.OUT)
    GPIO.setup(jobbEnged, GPIO.OUT)
    
    GPIO.output(balHátra, GPIO.LOW)
    GPIO.output(balElőre, GPIO.LOW)
    GPIO.output(jobbHátra, GPIO.LOW)
    GPIO.output(jobbElőre, GPIO.LOW)
    
    GPIO.output(balEnged, GPIO.HIGH)
    GPIO.output(jobbEnged, GPIO.HIGH)
    
    ablak=Tk()
    ablak.bind('<KeyPress-Up>', előre)
    ablak.bind('<KeyRelease-Up>', előreÁllj)
    ablak.bind('<KeyPress-Down>', hátra)
    ablak.bind('<KeyRelease-Down>', hátraÁllj)
    ablak.bind('<KeyPress-Right>', jobbra)
    ablak.bind('<KeyRelease-Right>', jobbraÁllj)
    ablak.bind('<KeyPress-Left>', balra)
    ablak.bind('<KeyRelease-Left>', balraÁllj) 
    Label(ablak,text='Távirányító aktív. Használd a nyíl gombokat!').pack()
    ablak.mainloop()
