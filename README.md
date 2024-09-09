# Rubik-Cube-Solver

# Step 2

Solve lighting conditions:
1. Non-ML Approaches (Traditional Computer Vision)
    a. Color Normalization (Lighting Compensation)

        Adaptive Histogram Equalization: You can use this technique to improve contrast and normalize the lighting in images. OpenCV's CLAHE (Contrast Limited Adaptive Histogram Equalization) can be useful.
        White Balance Adjustment: Correcting white balance helps standardize the color distribution across different lighting environments.
    b. Dynamic HSV Thresholding

    You can make your color detection more adaptive by adjusting the HSV thresholds based on the average brightness of the image. This technique involves recalculating the ranges for the HSV channels dynamically based on the lighting of the image.
    c. Contour Detection & Grid Mapping

    For un-cropped images, you can use contour detection and image segmentation to detect the Rubik's Cube face in the image. Once the cube's face is detected, you can apply a perspective transform to isolate the face and divide it into a 3x3 grid.

        Detecting the Cube: Use edge detection (e.g., Canny Edge) and contour detection to find the largest square shape (the cube face).
        Perspective Transform: Once you detect the square, apply a perspective transform to warp it into a flat, 2D 3x3 grid.

    d. Lighting Invariant Features

    Instead of relying purely on color, you can use texture-based features (e.g., SIFT, ORB) to assist in identifying stickers, combined with color information. This reduces the algorithm’s reliance on lighting.

2. ML approach:

    If the traditional methods don't provide sufficient robustness, ML-based methods can be very effective. Here are two main approaches you could explore:
    a. Color Classification with ML

    You can train a machine learning model (e.g., SVM, Decision Trees, or even a simple Neural Network) to classify colors under varying lighting conditions. For this, you would need to create a labeled dataset of Rubik's Cube stickers in various lighting conditions. Features can be based on the RGB or HSV values of each sticker's region.

    Steps:

        Data Collection: Capture many images of the Rubik's Cube under different lighting conditions.
        Label the Data: Label each sticker with its correct color.
        Train a Classifier: Train an ML model to classify the stickers' colors based on the HSV or RGB values.

    Libraries like scikit-learn can be used to implement this.
    b. Deep Learning with CNNs (Convolutional Neural Networks)

    A more advanced approach is to use Convolutional Neural Networks (CNNs). This would be a robust solution, especially if you want to handle various lighting, occlusion, and perspective changes.

        Dataset: You'd need a dataset with labeled Rubik’s Cube faces under different lighting and positions.
        Network Architecture: A simple CNN can classify each of the 9 regions into one of the 6 possible colors. You can use pre-trained models (like ResNet or MobileNet) and fine-tune them on your dataset.

