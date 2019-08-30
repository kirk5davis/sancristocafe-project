from io import BytesIO
from PIL import Image as Img



INPUT_IMG = r"C:\projects\sancristocafe\sancristocafe-project\sancristocafe\static\images\wet_mill_reception.jpg"
OUTPUT_IMG = r"C:\projects\sancristocafe\sancristocafe-project\sancristocafe\static\images\wet_mill_reception_reduced.jpg"
OUT_WIDTH = 1500

img_obj = open(INPUT_IMG, 'rb').read()
img = Img.open(BytesIO(img_obj))
width, height = img.size
if img.mode != 'RGB':
    img = img.convert('RGB')
img.thumbnail((OUT_WIDTH, OUT_WIDTH * height / width), Img.ANTIALIAS)
output = BytesIO()
img.save(OUTPUT_IMG, format='JPEG', quality=80)