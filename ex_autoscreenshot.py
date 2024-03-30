import os
import time
from PIL import ImageGrab

curr_dir_path = os.path.dirname(os.path.abspath(__file__))
file_path = curr_dir_path + '/userlib_result'
time.sleep(2)
print(file_path)

for i in range(1, 11):
    img = ImageGrab.grab()
    img_file_path = file_path + "/image{0}.png".format(i)
    print(img_file_path)
    img.save(img_file_path)
    time.sleep(2)
