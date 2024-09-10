# Video Object Detection and Tracking Pipeline
This project is designed to detect and track children and therapists in videos to analyze behaviors and engagement levels. The pipeline leverages a custom-trained YOLOv8 model for object detection and uses a tracking algorithm to identify and track individuals throughout the video.

## Setup and Running the Project

1. requirements.txt
Contains a list of all necessary Python packages to run the project, including packages for training, object detection, tracking, and video processing.
How to use:
bash
Copy code
pip install -r requirements.txt
2. download_videos.py
Purpose: Downloads videos from YouTube using the pytube library.
Explanation: This script is used to fetch videos that will be used for training and testing the object detection model. It downloads videos from a given YouTube URL and saves them to a specified output directory.
How to use: No input is required when running the script directly.
3. auto_annotate.py
Purpose: Automatically annotates bounding boxes around persons detected in videos using the AutoDistill framework.
Explanation: This script automatically generates annotations for videos, labeling detected persons with bounding boxes. All detected persons are initially labeled as "person."
How to use: No input is required when running the script directly.
4. Manual Annotation Correction
Purpose: Corrects the labels manually to distinguish between "child" and "adult."
Explanation: After auto-annotation, use tools like Roboflow or LabelImg to manually correct and differentiate between children and adults. This step is crucial for creating accurate annotations for training.
How to perform:
Open the auto-annotated files in Roboflow or LabelImg.
Change labels from "person" to "child" or "adult" as appropriate.
Save the corrected annotations.
5. train.py
Purpose: Trains a custom YOLOv8 model on the manually corrected dataset.
Explanation: This script is used to train the YOLOv8 model to detect "child" and "adult" classes. The model is trained for 25 epochs on the dataset, and the trained weights are saved for later use in the tracking process.
How to use: No input is required when running the script directly.
6. track.py
Purpose: Tracks objects in the input video using the trained YOLOv8 model and generates an output video with tracked objects.
Explanation: This script takes an input video, runs object detection and tracking, and outputs a video with bounding boxes and unique IDs assigned to each detected person (child or adult).
How to use:
This is the only script that takes input arguments.
Command to run:
bash
Copy code
python track.py --input <input_video_path> --output <output_video_path>
Arguments:
--input: Path to the input video file.
--output: Path where the output video file with tracking results will be saved.

## Expected Output
The track.py script will output a video file with detected children and therapists annotated with bounding boxes and unique IDs.
Conclusion
By following these steps, you will be able to download, annotate, train, and track objects in videos using the custom-trained YOLOv8 model. This pipeline is designed to help analyze behaviors and engagement levels of children with Autism Spectrum Disorder and therapists.

