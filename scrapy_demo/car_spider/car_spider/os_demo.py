
import os

image_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images')
if not os.path.exists(image_path):
    os.mkdir(image_path)
else:
    print('存在')