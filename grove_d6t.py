# coding: utf-8
# Driver for D6T.
# Please execute the following command before use "pigpio"
# $ sudo pigpiod

import time
import pigpio

class GroveD6t:
    I2C_ADDR = 0x0a
    pi = pigpio.pi()
    handle = None

    def __init__(self,address=0x0a):
        self.I2C_ADDR = address
        try:
            self.handle = self.pi.i2c_open(1, 0x0a)
        except AttributeError:
            print('If you have not executed the "sudo pigpiod" command, please execute it.')
            raise

    def __del__(self):
        if self.handle is not None:
            self.pi.i2c_close(self.handle)
            self.handle = None
         
    def readData(self):
        try:
            self.pi.i2c_write_device(self.handle, [0x4c])
            data = self.pi.i2c_read_device(self.handle, 35)
        except pigpio.error:
            print('Failed to read data.')
            return None,None
        
        tp = []
        tptat = 0

        try:
            tp.append((data[1][3] * 256 + data[1][2]) / 10.0)
            tp.append((data[1][5] * 256 + data[1][4]) / 10.0)
            tp.append((data[1][7] * 256 + data[1][6]) / 10.0)
            tp.append((data[1][9] * 256 + data[1][8]) / 10.0)
            tp.append((data[1][11] * 256 + data[1][10]) / 10.0)
            tp.append((data[1][13] * 256 + data[1][12]) / 10.0)
            tp.append((data[1][15] * 256 + data[1][14]) / 10.0)
            tp.append((data[1][17] * 256 + data[1][16]) / 10.0)
            tp.append((data[1][19] * 256 + data[1][18]) / 10.0)
            tp.append((data[1][21] * 256 + data[1][20]) / 10.0)
            tp.append((data[1][23] * 256 + data[1][22]) / 10.0)
            tp.append((data[1][25] * 256 + data[1][24]) / 10.0)
            tp.append((data[1][27] * 256 + data[1][26]) / 10.0)
            tp.append((data[1][29] * 256 + data[1][28]) / 10.0)
            tp.append((data[1][31] * 256 + data[1][30]) / 10.0)
            tp.append((data[1][33] * 256 + data[1][32]) / 10.0)

            tptat = (data[1][1] * 256 + data[1][0]) / 10.0
        except IndexError:
            print('got an incorrect index.')
            return None,None
        
        return tp, tptat
