import os
import shutil
import random

# Define the classes
classes = ["cats", "dogs", "birds"]

# Define the total number of images for each class
total_images_per_class = {"cats": 40, "dogs": 30, "birds": 30}

# Define the proportions for training, validation, and testing sets
proportions = {"train": 0.7, "validation": 0.15, "test": 0.15}

# Define the directory where the images will be stored
base_dir = "dataset"

# Create directories for training, validation, and testing sets
for split in ["train", "validation", "test"]:
    os.makedirs(os.path.join(base_dir, split), exist_ok=True)
    for class_name in classes:
        os.makedirs(os.path.join(base_dir, split, class_name), exist_ok=True)

# Generate dummy image paths
image_paths = []
for class_name, total_images in total_images_per_class.items():
    for i in range(total_images):
        image_paths.append((class_name, f"dummy_{class_name}_{i}.jpg"))

# Shuffle the image paths
random.shuffle(image_paths)

# Split the image paths into training, validation, and testing sets
split_points = {
    "train": int(len(image_paths) * proportions["train"]),
    "validation": int(
        len(image_paths) * (proportions["train"] + proportions["validation"])
    ),
}
splits = {
    "train": image_paths[: split_points["train"]],
    "validation": image_paths[split_points["train"] : split_points["validation"]],
    "test": image_paths[split_points["validation"] :],
}

# Move images to their respective directories
for split, images in splits.items():
    for class_name, image_path in images:
        source_path = os.path.join(base_dir, class_name, image_path)
        destination_path = os.path.join(base_dir, split, class_name, image_path)
        shutil.copy(source_path, destination_path)

print("Prototype dataset generated successfully!")
