"""
<describe what this module has/does>

Created on Oct 20, 2016.
Written by: galluzzi.
"""

import tkinter
from tkinter import ttk
import socket

ROBOTNUMBER = 21

class mysocket(object):
    def __init__(self):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.rnum = 0

    def open(self, addr):
        self.rnum = addr
        addr = "r" + str(addr) + ".wlan.rose-hulman.edu"
        self.connection.connect((addr, 2000))

    def write(self, out):
        self.connection.sendall(out)

    def read(self, buffersz=4096):
        return self.connection.recv(buffersz)

def makebytearray(command, pin, value):
    b = bytearray()
    b.append(command)
    b.append(pin)
    b.append(value)
    return b

def ledoff(s):
    s.write(makebytearray(0x03, 0x00, 0x00))
    print("off: ", s.read())

def ledon(s):
    s.write(makebytearray(0x03, 0x00, 0x01))
    print("on: ", s.read())

def tone(s):
    s.write(makebytearray(0x05, 0x00, s.rnum))
    print("singing: ", s.read())

def toneoff(s):
    s.write(makebytearray(0x05, 0x00, 0x00))
    print("stopping: ", s.read())


def main():
    s = mysocket()
    s.open(ROBOTNUMBER)
    root = tkinter.Tk()

    frame1 = ttk.Frame(root, padding=10)
    frame1.grid()

    on_button = ttk.Button(frame1, text='LED On')
    on_button['command'] = (lambda:ledon(s))
    on_button.grid()

    off_button = ttk.Button(frame1, text='LED Off')
    off_button['command'] = (lambda:ledoff(s))
    off_button.grid()

    tone_on_button = ttk.Button(frame1, text='Tone On')
    tone_on_button['command'] = (lambda:tone(s))
    tone_on_button.grid()

    tone_off_button = ttk.Button(frame1, text='Tone Off')
    tone_off_button['command'] = (lambda:toneoff(s))
    tone_off_button.grid()


    root.mainloop()


# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
