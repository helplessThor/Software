from machine import Pin, PWM
from time import sleep
# Create a dictionary of Morse Code. s is for Short (or dots), l is for Long (or dashes)
MorseCodes = {
    ' ': '',
    'a': 'sl',
    'b': 'lsss',
    'c': 'lsls',
    'd': 'lss',
    'e': 's',
    'f': 'ssls',
    'g': 'lls',
    'h': 'ssss',
    'i': 'ss',
    'j': 'slll',
    'k': 'lsl',
    'l': 'slss',
    'm': 'll',
    'n': 'ls',
    'o': 'lll',
    'p': 'slls',
    'q': 'llsl',
    'r': 'sls',
    's': 'sss',
    't': 'l',
    'u': 'ssl',
    'v': 'sssl',
    'w': 'sll',
    'x': 'lssl',
    'y': 'lsll',
    'z': 'llss',
    '1': 'sllll',
    '2': 'sslll',
    '3': 'sssll',
    '4': 'ssssl',
    '5': 'sssss',
    '6': 'lssss',
    '7': 'llsss',
    '8': 'lllss',
    '9': 'lllls',
    '0': 'lllll'}

# button = Pin(10, Pin.IN, Pin.PULL_UP)
shortled = Pin(8, Pin.OUT)
longled = Pin(8, Pin.OUT)
speaker = PWM(Pin(13))

fast = 0.1
slow = 0.2

sound = True
light = True
pitch = 500
volume = 512
speaker.freq(500) #pitch of sound. Higher number is higher pitch

shortled.low()
longled.low()

def letterlookup(stringvalue):
    for k in MorseCodes:
        if MorseCodes[k] == stringvalue:
            return k
    return " "

def blinkletter(letter):

    if letter != "":
        currentletter = MorseCodes[letter]
    if letter == " ":
        sleep(0.6)
        return
    
    print(letter + " : " + currentletter)
    for c in currentletter:
        if (c == 'l'):
            blinkspeed = slow
        if (c =='s'):
            blinkspeed = fast      
        if light : shortled.value(1)
        if sound :
            speaker.freq(pitch)
            speaker.duty_u16(volume)
        sleep(blinkspeed)
        if light : shortled.value(0)
        if sound : speaker.duty_u16(0)
        sleep(blinkspeed)
        
    sleep(0.6)
    
def playmessage(message):           
    for c in message:
        blinkletter(str.lower(c))
