from ultralytics import YOLO

# Load the YOLO model (pre-trained weights)
model = YOLO("yolo11n.pt")

# Train the model on your custom dataset
results = model.train(
    data="chicken_parts.yaml",
    epochs=30,
    imgsz=640,
    device="cpu"
)
