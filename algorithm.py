import cv2

def calculate_sharpness(image):
    """
    Calculate the sharpness of an image using the variance of the Laplacian.

    The function converts the image to grayscale and then applies the Laplacian
    operator, which measures the rate of change of pixel intensity. The variance
    of these values is used as a sharpness metric.

    Parameters:
        image (numpy.ndarray): The image on which to calculate sharpness.

    Returns:
        float: The calculated sharpness value.
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    laplacian = cv2.Laplacian(gray, cv2.CV_64F)
    sharpness = laplacian.var()
    return sharpness

# import numpy as np
# def calculate_sharpness(image):
#     """
#     Calculate the sharpness of an image using the Canny edge detector.
#
#     The function converts the image to grayscale and then applies the Canny
#     edge detector, which detects edges based on the gradients of the image.
#     The total number of edge pixels (edges detected) is used as a sharpness metric.
#
#     Parameters:
#         image (numpy.ndarray): The image on which to calculate sharpness.
#
#     Returns:
#         int: The count of edge pixels, representing sharpness.
#     """
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     edges = cv2.Canny(gray, 100, 200)  # These thresholds can be adjusted based on specific needs
#     sharpness = np.sum(edges > 0)      # Count the number of edge pixels
#     return sharpness

def select_sharp_frames(video_path, base_threshold=100.0, adaptivity_rate=0.05, window_size=30):
    """
    Select frames from a video that meet an adaptively calculated sharpness threshold.

    Parameters:
        video_path (str): The path to the video file.
        base_threshold (float): The initial sharpness threshold.
        adaptivity_rate (float): The rate at which the threshold adapits based on recent frame sharpness.
        window_size (int): The number of frames to consider for calculating the moving average sharpness.

    Returns:
        list of tuple: Each tuple contains the frame index, the frame itself, and its sharpness.
    """
    cap = cv2.VideoCapture(video_path) # Open the video file
    selected_frames = []
    recent_sharpness = []
    frame_count = 0
    adaptive_threshold = base_threshold # Only for the first 30 frames

    while True:
        ret, frame = cap.read() # Read a frame from the video
        if not ret:
            break

        sharpness = calculate_sharpness(frame)
        # Update the list of recent sharpness values
        if len(recent_sharpness) >= window_size:
            recent_sharpness.pop(0)  # Remove the oldest sharpness value
        recent_sharpness.append(sharpness)

        # Calculate adaptive threshold
        if len(recent_sharpness) == window_size:
            average_sharpness = sum(recent_sharpness) / window_size
            adaptive_threshold = base_threshold + adaptivity_rate * (average_sharpness - base_threshold)

            # Select the frame if it meets the adaptive threshold
            if sharpness > adaptive_threshold:
                selected_frames.append((frame_count, frame, sharpness))

        frame_count += 1

    cap.release() # Release the video capture object
    return selected_frames
