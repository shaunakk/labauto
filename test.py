import matplotlib.pyplot as plt
import requests
from PIL import Image
from io import BytesIO
url = 'http://192.168.0.85:31950/camera/picture'

r = requests.post(url,headers={'Opentrons-Version':'2'})
# print(r.content)
im = Image.open(BytesIO(r.content))
 
plt.imshow(im)
plt.show()