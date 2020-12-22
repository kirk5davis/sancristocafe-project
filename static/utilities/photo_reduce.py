from io import BytesIO
from PIL import Image as Img
import os
import glob



# INPUT_IMG = r"C:\projects\sancristocafe\sancristocafe-project\sancristocafe\static\images\wet_mill_reception.jpg"
# OUTPUT_IMG = r"C:\projects\sancristocafe\sancristocafe-project\sancristocafe\static\images\wet_mill_reception_reduced.jpg"
# OUT_WIDTH = 1500

def reduce_img(input_img):
    output_img = input_img.replace(".jpg", "_rcopy.jpg")
    img_obj = open(input_img, 'rb').read()
    img = Img.open(BytesIO(img_obj))
    #width, height = img.size
    #if img.mode != 'RGB':
    #    img = img.convert('RGB')
    #img.thumbnail((OUT_WIDTH, OUT_WIDTH * height / width), Img.ANTIALIAS)
    #output = BytesIO()
    img.save(output_img, format='JPEG', quality=80)

test_dir = r"C:\Users\Lenovo\Downloads\pics_from_20200510"
for pic in glob.glob(test_dir + "\\*.jpg"):
    print("reducing pic: - ".format(pic))
    reduce_img(pic)
    