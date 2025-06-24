import cv2
from PIL import Image

def preprocess_image(image_path, size=(512, 512), low=100, high=200):
    image = cv2.imread(image_path)
    image = cv2.resize(image, size)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, low, high)
    edges_rgb = cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)
    return Image.fromarray(edges_rgb)
