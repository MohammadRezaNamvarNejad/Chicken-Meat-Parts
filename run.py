import os
from ultralytics import YOLO

model = YOLO('best.pt')

folder_path = './img/'

for filename in os.listdir(folder_path):
    if filename.endswith(('.jpg', '.jpeg', '.png')):
        image_path = os.path.join(folder_path, filename)

        results = model.predict(source=image_path, save=True)
