
Chicken Parts Detection using YOLOv4
This project implements a deep learning-based approach to detect and classify chicken parts using the YOLOv4 object detection model. The model identifies parts such as back, breast, leg, neck, and wing with high accuracy.

Table of Contents
Overview
Features
Installation
Usage
Dataset Preparation
Model Configuration
Output and Results
Troubleshooting
Contributing
License
Overview
Efficient chicken part detection is essential for the poultry industry to streamline processing tasks. This project utilizes YOLOv4 to detect chicken parts from whole carcasses, providing precise localization and classification. The results are visualized with bounding boxes and can be exported for further analysis.

Features
Detection of five chicken parts: back, breast, leg, neck, and wing.
High accuracy and efficiency using YOLOv4.
Easy-to-use command-line interface for processing images.
Configurable parameters for dataset and model optimization.
Visualization of results with bounding boxes and metadata.
Installation
Prerequisites
Ensure the following are installed:

Python 3.8 or later
pip (Python package installer)
Steps
Clone the repository:

bash
Copy code
git clone https://github.com/MohammadRezaNamvarNejad/Chicken-Meat-Parts
cd Chicken-Meat-Parts
Install required dependencies:

bash
Copy code
pip install -r requirements.txt
Usage
Prepare Input Images:

Move the images to be processed into the img folder.
Run the Model: Execute the following command to process the images:

bash
Copy code
python ./run.py
View Results:

Processed results, including visualized bounding boxes and metadata, will be saved to the output directory.
Additional logs and metrics will be displayed in the terminal.
Dataset Preparation
Annotation: Use tools like CVAT to annotate images.

Supported labels: back, breast, leg, neck, wing.
Folder Structure: Organize your dataset as follows:

Copy code
dataset/
├── train/
│   ├── images/
│   └── labels/
├── valid/
│   ├── images/
│   └── labels/
Data Augmentation: Enhance dataset diversity using rotation, scaling, and flipping.

Model Configuration
The model parameters are specified in the chicken_parts.yaml file. Update as needed:

yaml
Copy code
train: ./data/train/images
val: ./data/valid/images
nc: 5
names: ['back', 'breast', 'leg', 'neck', 'wing']
Key Parameters:
Epochs: Adjust training epochs (default: 30).
Image Size: Resize images to 640x640 (default) for a balance of speed and accuracy.
Device: GPU recommended for faster training (CPU is supported but slower).
Output and Results
Visualization: Each processed image will have bounding boxes and class labels drawn on it.

Example output:
python
Copy code
OUTPUT/
├── combined_image_1.jpg
├── combined_image_2.jpg
...
Metrics: Performance metrics include:

IoU (Intersection over Union)
Precision, Recall, and F1-Score
True Positives, False Positives, and False Negatives
Troubleshooting
Dependency Issues: Ensure pip is updated:

bash
Copy code
pip install --upgrade pip
Missing Results:

Verify paths in run.py and chicken_parts.yaml are correct.
Check the img folder contains valid image files.
Low Accuracy:

Ensure the dataset is balanced and properly annotated.
Experiment with different augmentation techniques or training epochs.
Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

License
This project is licensed under the MIT License.
