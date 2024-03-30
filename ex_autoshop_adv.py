import os
import time
import keyboard
from PIL import ImageGrab

def screenshot():
    curr_time = time.strftime("_%Y%m%d_%H%M%S")
    img = ImageGrab.grab()
    img_file_path = file_path + "/image{0}.png".format(curr_time)
    img.save(img_file_path)

curr_dir_path = os.path.dirname(os.path.abspath(__file__))
file_path = curr_dir_path + '/userlib_result'

# keyboard.add_hotkey("F9", screenshot)
keyboard.add_hotkey("ctrl+shift+s", screenshot)
keyboard.wait("esc")