import sys
sys.path.append(".")
# import PyCapture2
from multiprocessing import Process
from MainWindow import start_main_win
from Utilities.IO.IOHelper import create_config_file, create_configt_file, create_camconfig_file
#modi
# global StackNum
# StackNum = 0
# global StorageNum
# StorageNum = 0

if __name__ == '__main__':
    create_config_file()
    create_configt_file()
    create_camconfig_file()

    p = Process(target=start_main_win)
    p.start()
    p.join()
    #start_main_win()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def print_camera_info(cam):
    cam_info = cam.getCameraInfo()
    print('\n*** CAMERA INFORMATION ***\n')
    print('Serial number - %d' % cam_info.serialNumber)
    print('Camera model - %s' % cam_info.modelName)
    print('Camera vendor - %s' % cam_info.vendorName)
    print('Sensor - %s' % cam_info.sensorInfo)
    print('Resolution - %s' % cam_info.sensorResolution)
    print('Firmware version - %s' % cam_info.firmwareVersion)
    print('Firmware build time - %s' % cam_info.firmwareBuildTime)
    print()
