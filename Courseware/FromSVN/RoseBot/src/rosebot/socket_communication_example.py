"""
<describe what this module has/does>

Created on Oct 19, 2016.
Written by: galluzzi.
"""
import time
import socket

class mysocket(object):
    def __init__(self):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def open(self, addr):
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

def main():
    s = mysocket()
    s.open("r07.wlan.rose-hulman.edu")
    while True:
        s.write(bytearray([0x01, 0x00, 0x00]))
        bytes_read = s.read()
        print(len(bytes_read), bytes_read)
    m1 = makebytearray(0x01, 0x00, 0x00)
    m2 = makebytearray(0x01, 0x00, 0xFF)
    m3 = makebytearray(0x03, 0x00, 0x00)
    m4 = makebytearray(0x03, 0x00, 0x01)
    # tones
    tonesL = []
    val = 0x00
    for i in range(100):
        tonesL.append(makebytearray(0x05, 0x00, val))
        val += 1
    tonesL.append(makebytearray(0x05, 0x00, 0x00))
    tests = [m1, m2, m3, m4] + tonesL
    for i in tests:
        print(i)
        s.write(i)
        print("one: ", s.read())
        time.sleep(1)


#-----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#-----------------------------------------------------------------------
if __name__ == '__main__':
    main()
