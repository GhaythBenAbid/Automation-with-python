import os
import shutil

def CopyFile():
    src = input("Set file path (SOURCE) :")
    dest = input("Set Destination :")
    shutil.copy(src , dest)
