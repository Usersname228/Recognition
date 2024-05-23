import requests
from deepface import DeepFace
import os

url_one = 'https://gas-kvas.com/grafic/uploads/posts/2023-09/1695805189_gas-kvas-com-p-kartinki-garri-potter-18.jpg'
url_two = 'https://fikiwiki.com/uploads/posts/2022-02/1644856862_27-fikiwiki-com-p-kartinki-garri-pottera-na-avu-32.jpg'


response_one = requests.get(url_one)
response_two = requests.get(url_two)

# current_path = os.path.dirname(os.path.abspath(__file__))
# photos_path = os.path.join(current_path, "photos")

# photo1 =os.path.join(photos_path, 'photo_one.jpg')
# photo2 =os.path.join(photos_path, 'photo_two.jpg')

with open('img1', 'wb') as file:
    file.write(response_one.content)

with open('img2.jpg', 'wb') as file:
    file.write(response_two.content)


result = DeepFace.verify('img1.jpg', 'img2.jpg')
print(result)