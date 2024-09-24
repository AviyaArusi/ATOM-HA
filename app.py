from flask import Flask, request, render_template, send_from_directory
import os
import cv2
from algorithm import select_sharp_frames

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'output'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    """
    Route to handle file uploads and frame processing.
    Supports GET and POST methods: Displays an upload form on GET
    and processes the uploaded file on POST.
    """
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)

            # Process the video to select sharp frames using adaptive thresholding
            frames = select_sharp_frames(filepath, base_threshold=2500.0, adaptivity_rate=0.05, window_size=30)

            # Save the selected frames to the output directory
            for idx, frame_data in enumerate(frames):
                frame_idx, frame, _ = frame_data
                output_path = os.path.join(app.config['OUTPUT_FOLDER'], f'{frame_idx}.jpg')
                cv2.imwrite(output_path, frame)

            # Render a gallery view with the saved images
            return render_template('gallery.html', images=os.listdir(app.config['OUTPUT_FOLDER']))

    # Render the file upload form template on GET request
    return render_template('home.html')


@app.route('/output/<filename>')
def send_file(filename):
    """
    Route to serve files from the output directory.
    Allows the browser or users to access processed frames directly by filename.
    """
    return send_from_directory(app.config['OUTPUT_FOLDER'], filename)


if __name__ == '__main__':
    app.run()

