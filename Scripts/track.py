# track_yolov8.py

import argparse
from ultralytics import YOLO
import cv2

def main(input_video_path, output_video_path):
    # Load the trained YOLOv8 model
    model = YOLO("config/best.pt")  # Path to the trained model

    # Initialize video capture
    cap = cv2.VideoCapture(input_video_path)

    # Get video properties
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    # Initialize video writer
    out = cv2.VideoWriter(output_video_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (frame_width, frame_height))

    # Run object tracking on each frame of the video
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Perform prediction and tracking
        results = model.track(frame, conf=0.3, iou=0.5, persist=True)

        # Get annotated frame
        annotated_frame = results[0].plot()  # Extract the first frame result for visualization

        # Display frame with annotations
        cv2.imshow('Tracking', annotated_frame)
        out.write(annotated_frame)  # Save frame to output video

        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources
    cap.release()
    out.release()
    cv2.destroyAllWindows()

    print(f"Tracking completed. Output video saved to {output_video_path}")

if __name__ == "__main__":
    # Setup argument parser
    parser = argparse.ArgumentParser(description="Track objects in a video using YOLOv8")
    parser.add_argument('--input', type=str, required=True, help="Path to the input video file")
    parser.add_argument('--output', type=str, required=True, help="Path to save the output video file")

    # Parse the arguments
    args = parser.parse_args()

    # Run the main function with the provided arguments
    main(args.input, args.output)
