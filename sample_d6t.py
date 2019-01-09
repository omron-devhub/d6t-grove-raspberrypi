# coding: utf-8
# Sample that outputs the value acquired by D6T.
# Please execute the following command before use "pigpio"
#  $ sudo pigpio

import grove_d6t
import pigpio
import time

while True:
        try:
                d6t = grove_d6t.GroveD6t()
                tpn, tptat = d6t.readData()
                if tpn == None:
                        continue
                
                print(tpn,"PTAT : %.1f" %tptat)
                time.sleep(1.0)
        except IOError:
                print("IOError")
