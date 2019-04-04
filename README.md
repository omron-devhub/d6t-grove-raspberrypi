# d6t-grove-raspberrypi
It is a module for evaluating Omron sensor D6T with Raspberry Pi 3 Model B and a sample program when using a module.

D6T is an infrared sensor that can measure the surface temperature of an object noncontactly by receiving radiant heat energy from the object with a thermopile element.
It can be used as a highly sensitive human sensor that can also detect stationary people.

## language
- [English](./README.md)
- [Japanase](./README_ja.md)

## Description
- grove_d6t.py  
Driver module for acquiring data from D6T via GrovePi+.

- sample_d6t.py  
It is a sample program that allows you to check the data acquired via the driver module on the console.

- sample_gui_d6t.py  
It is a sample program that enables you to visualize and check the data acquired via the driver module with graphs.

***DEMO:***  
When you run sample_gui_d6t.py, you can see the following graph.  

![Graph_D6T](Graph_D6T.png)

## Installation
1. It is necessary to install dependency software beforehand.  
    [Dependencies](#link)
2. Open Terminal and execute the following command.    
    ```
    $ mkdir omron_sensor
    $ cd omron_sensor
    $ git clone https://github.com/omron-devhub/d6t-grove-raspberrypi.git
    ```

## Usage
Procedure to operate the sample program.  
Please execute the following command before use "pigpio".
```
$ sudo pigpiod
```

-  sample_2smpb_02e.py  
Open Terminal and execute the following command.  
    ```
    $ cd omron_sensor
    $ sudo python3 sample_d6t.py
    ```
- sample_gui_2smpb_02e.py  
Open Terminal and execute the following command.  
    ```
    $ cd omron_sensor
    $ sudo python3 sample_gui_d6t.py
    ```

## <a name="link"></a>Dependencies
d6t-grove-raspberrypi requires the following dependencies.
- [Python3](https://www.python.org/)
- [GrovePi+](http://wiki.seeedstudio.com/GrovePi_Plus/)
- [matplotlib](https://matplotlib.org/)
- [pigpio](http://abyz.me.uk/rpi/pigpio/download.html)

## Licence
Copyright (c) OMRON Corporation. All rights reserved.

Licensed under the MIT License.
