# YOLO Object Detection with PPE (Personal Protective Equipment) Detection

This is a Python script that uses the YOLO (You Only Look Once) object detection algorithm to detect various classes of objects in a video or webcam feed. Specifically, it focuses on detecting Personal Protective Equipment (PPE) such as hardhats, masks, safety vests, safety cones, machinery, and vehicles.

# Construction Site Safety: YOLO Object Detection with PPE (Personal Protective Equipment) Detection

This is a Python script that uses the YOLO (You Only Look Once) object detection algorithm to detect various classes of objects related to construction site safety in a video or webcam feed. Specifically, it focuses on detecting Personal Protective Equipment (PPE) such as hardhats, masks, safety vests, safety cones, machinery, and vehicles.


## Requirements

- Python 3.x
- `ultralytics` library
- `cv2` (OpenCV) library
- `cvzone` library
- Pre-trained YOLO model file (`ppe-50.pt`)
- Video file or webcam for input

## Installation

1. Clone the repository or download the code files.
2. Install the required Python libraries using pip:

pip install ultralytics
pip install opencv-python
pip install cvzone

markdown
Copy code

3. Download the pre-trained YOLO model file (`ppe-50.pt`) and place it in the same directory as the script.

## Usage

1. Open the script in a Python IDE or text editor.
2. Modify the path of the video file or uncomment the webcam-related lines if you want to use the webcam instead.
3. Run the script.

## Training

The YOLO model used in this project has been trained with fifty epochs using a dataset specifically curated for construction site safety. The training process involved feeding the model with annotated images of construction sites, ensuring the model learns to accurately detect and classify various safety-related objects.


## Output

The script will open a window showing the input video or webcam feed. It will draw bounding boxes around the detected objects and display the confidence and class name for each detected object using the `cvzone` library.

## License

[MIT License](LICENSE)

Feel free to use and modify this code for your own projects.

## Author

Nikhil Shendge

## Acknowledgments

- YOLO Algorithm: [YOLO: Real-Time Object Detection](https://pjreddie.com/darknet/yolo/)
- `ultralytics` library: [Ultralytics/YOLO](https://github.com/ultralytics/yolov5)
- `cvzone` library: [cvzone](https://github.com/cvzone/cvzone)
- OpenCV Library: [OpenCV](https://opencv.org/)

![Object Detection with PPE](results\output.png)