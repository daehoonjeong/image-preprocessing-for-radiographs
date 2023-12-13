import os
import numpy as np
import cv2
import matplotlib.pyplot as plt
from tqdm import tqdm

image_folder = "../(4)CFA82_1As_cooling_100fps"
start = 2200 # full_melt_point right before the phenomenon starts

def sum_upper_half(image):
    height, width = image.shape[:2]
    upper_half = image[height // 2:2000, :]
    return upper_half.sum()

def process_images_and_plot(input_folder):
    all_image_files = [f for f in os.listdir(input_folder) if f.endswith(".tif")]
    image_files = all_image_files[start:start+30]
    sequence = []
    sums = []

    for filename in sorted(image_files):
        image_path = os.path.join(input_folder, filename)
        image = cv2.imread(image_path)

        if image is not None:
            upper_half_sum = sum_upper_half(image)
            sequence.append(image_files.index(filename))
            sums.append(upper_half_sum)
            
    mean_sum = np.ones(len(sequence))
    mean_sum = mean_sum * np.mean(sums)
    font = {'family':'arial','color':'black','size':18, 'weight':'bold'}
    title = {'family':'arial','color':'black','size':20}
    # Plot the results
    plt.figure(figsize=(10, 6))
    plt.plot(sequence, sums, marker='o')
    plt.plot(sequence, mean_sum)
    plt.title("Sum of Upper Half of Images", fontdict = title)
    plt.xlabel("Image Sequence", fontdict = font)
    plt.ylabel("Sum of Pixel Values", fontdict = font)
    plt.xticks(fontsize = 18)
    plt.yticks(fontsize = 18)
    #plt.tight_layout()
    plt.show()
    
process_images_and_plot(image_folder)
