"""
<describe what this module has/does>

Created on Oct 19, 2016.
Written by: galluzzi.
"""
import time
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

def LEDOn():
    return makebytearray(0x03, 0x00, 0x00)

def LEDOff():
    return makebytearray(0x03, 0x00, 0x01)

def main():
    s = mysocket()
    s.open(ROBOTNUMBER)
    print("response: ", s.read())
    tests = [LEDOn(), LEDOff(), LEDOn(), LEDOff(), LEDOn(), LEDOff(), LEDOn(), LEDOff()]
    for i in tests:
        print(i)
        s.write(i)
        print("one: ", s.read())
        time.sleep(1)
    cmd = input("Enter a command: ")
    while cmd != 'q':
        pin = input("Enter a pin: ")
        value = input("Enter a value: ")
        s.write(makebytearray(int(cmd, 16), int(pin, 16), int(value, 16)))
        print("response: ", str(s.read()))

        # if (cmd == '0x00') or (cmd == '0x02'):
        #    print("value is: ", s.read())
        cmd = input("Enter a command: ")



#-----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#-----------------------------------------------------------------------
if __name__ == '__main__':
    main()
