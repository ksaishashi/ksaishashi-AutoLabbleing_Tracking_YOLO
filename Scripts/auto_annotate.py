import os
import cv2
import supervision as sv
from autodistill_grounding_dino import GroundingDINO
from autodistill.detection import CaptionOntology

# Set your directories for images and the G_dataset
HOME = "../Intern_project/Dataset"
IMAGE_DIR_PATH = f"{HOME}/Images"
DATASET_DIR_PATH = f"{HOME}/G_dataset"

# Ensure that 'jpg' and 'png' files are properly listed
image_paths = sv.list_files_with_extensions(
    directory=IMAGE_DIR_PATH,
    extensions=["png", "jpg"]
)

print('Image count:', len(image_paths))

# Set the class ontology for annotation (e.g., 'person' class with 'adult' label)
base_model = GroundingDINO(
    ontology=CaptionOntology({
        "person": "adult"
    })
)

# Automatically annotate images and save the G_dataset
G_dataset = base_model.label(
    input_folder=IMAGE_DIR_PATH,
    extension=".jpg",  # Annotating JPEG images
    output_folder=DATASET_DIR_PATH
)   

# Save the annotations, images, and data.yaml to the G_dataset folder
ANNOTATIONS_DIRECTORY_PATH = f"{HOME}/G_dataset/train/labels"
IMAGES_DIRECTORY_PATH = f"{HOME}/G_dataset/train/images"
DATA_YAML_PATH = f"{HOME}/G_dataset/data.yaml"

# Function to create YAML file for YOLO format
def create_data_yaml(data_yaml_path, train_dir, val_dir, class_list):
    data_yaml_content = f"""
train: {train_dir}
val: {val_dir}

nc: {len(class_list)}
names: {class_list}
"""
    with open(data_yaml_path, 'w') as f:
        f.write(data_yaml_content)

# Create directories for storing annotations and images if not exist
os.makedirs(ANNOTATIONS_DIRECTORY_PATH, exist_ok=True)
os.makedirs(IMAGES_DIRECTORY_PATH, exist_ok=True)

# Create a list of class names
class_list = ['adult']  # For now, 'adult' is the only class

# Create the data.yaml file
create_data_yaml(
    data_yaml_path=DATA_YAML_PATH,
    train_dir=IMAGES_DIRECTORY_PATH,
    val_dir=IMAGES_DIRECTORY_PATH,  # You can set a different val directory if needed
    class_list=class_list
)

# No need to display or plot the images, just save them and their annotations
print(f"Dataset saved in {DATASET_DIR_PATH}")
