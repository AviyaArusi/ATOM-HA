# Sharp Frame Selector for Orthophoto Creation

   
## Introduction
This repository contains a Python application designed to select the sharpest frames from a video file, using an adaptive thresholding method. The selected frames are ideal for creating high-quality orthophotos, particularly useful in geographic information systems (GIS), construction planning, and environmental studies.

## Features
- **Adaptive Sharpness Thresholding:** Dynamically adjusts the sharpness threshold based on the content of the video to ensure optimal frame selection.
- **Automatic Frame Selection:**  Automates the process of selecting frames based on calculated sharpness, reducing manual effort and increasing efficiency.
- **Easy Integration:** Designed to be integrated with additional image processing or GIS workflows for creating orthophotos.

## Prerequisites
Before you run this application, make sure you have the following installed:
- Python 3.6+
- OpenCV library
- NumPy library

You can install the necessary Python libraries using pip:
~> pip install flask opencv-python


## How to run the project:
1. Open the terminal and run the command: ~> python app.py
2. On your browser go to the http://127.0.0.1:5000/ address.
3. Choose any mp4 video that you like and click on upload.

## License
The project is released under the [LICENSE](LICENSE). By using or contributing to the project, you agree to the terms and conditions of this license.

## Contact
For support or any questions related to the project, please contact me at [aviyaarusi@gmail.com](mailto:aviyaarusi@gmail.com).


