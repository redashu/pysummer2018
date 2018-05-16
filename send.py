#!/usr/bin/python2

import  socket 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.sendto("hiiii",("192.168.10.177",9999))



 


