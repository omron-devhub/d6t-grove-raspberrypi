# coding: utf-8
# Sample to draw graph values acquired with D6T.
# Please execute the following command before use "pigpio"
# $ sudo pigpiod

from __future__ import print_function

import time
import datetime

import numpy as np
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt

import grove_d6t

sensor = grove_d6t.GroveD6t()

def main():
    plt.ion()
    fig = plt.figure()
    x = range(5)
    y = range(5)
    visibleColorBar = False
    print('start')
    
    while True:
            tpn, tptat = sensor.readData()
            if tpn != None and tptat != None:
                print(datetime.datetime.today().strftime("[%Y/%m/%d %H:%M:%S]"),"temperature=%.1f[degC]" %tptat)
                print(tpn[0:4])
                print(tpn[4:8])
                print(tpn[8:12])
                print(tpn[12:16])
                
                Z = np.array([tpn[0:4],
                          tpn[4:8],
                          tpn[8:12],
                          tpn[12:16]])

                X,Y = np.meshgrid(x, y)
                
                plt.clf()
                plt.pcolor(X,Y,Z,cmap="coolwarm",vmax=35,vmin=25)
                
                if visibleColorBar == False:
                    plt.colorbar()
                    visibleColorBar = True

                plt.xticks(x)
                plt.yticks(y)
                fig.tight_layout()
                fig.canvas.draw()
                plt.show()

if __name__ == '__main__':
  main()
