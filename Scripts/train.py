from ultralytics import YOLO

# Load a YOLOv8 model (can be 'yolov8n', 'yolov8s', 'yolov8m', etc.)
model = YOLO('config/yolov8n.pt')  # Use a small YOLOv8 model for custom training

# Define the path to your dataset in YOLO format
data_path = '../Intern_project/Dataset/M_Dataset/data.yaml'  # Make sure this YAML points to train/valid images

# Train the model on custom dataset
model.train(data=data_path, epochs=25, imgsz=640, batch=16)

