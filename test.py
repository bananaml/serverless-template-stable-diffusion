# This file is used to verify your http server acts as expected
# Run it with `python3 test.py``

import requests
import base64
from io import BytesIO
from PIL import Image

model_inputs = {'seed': 789, 'prompt': 'Ragdoll cat king wearing a golden crown, intricate, elegant, highly detailed, centered, digital painting, artstation, concept art, smooth, sharp focus, illustration, artgerm, Tomasz Alen Kopera, Peter Mohrbacher, donato giancola, Joseph Christian Leyendecker, WLOP, Boris Vallejo'}

res = requests.post('http://localhost:8000/', json = model_inputs)

image_byte_string = res.json()["images_base64"][0]

image_encoded = image_byte_string.encode('utf-8')
image_bytes = BytesIO(base64.b64decode(image_encoded))
image = Image.open(image_bytes)
image.save("output.jpg")