import json
import os
import copy
import cv2


class CocoTrainDataset:
    def __init__(self, labels_file, images_folder, stride=8, sigma=7, paf_sigma=7, paf_thickness=1):
        with open(labels_file, 'r') as f:
            self._labels = json.load(f)
        self._images_folder = images_folder
        self._stride = stride
        self._sigma = sigma
        self._paf_sigma = paf_sigma
        self._paf_thickness = paf_thickness

        self.annotations = self._labels['annotations']
        self.images = {img['id']: img for img in self._labels['images']}

        print(f"Loaded {len(self.annotations)} annotations from {labels_file}")
        print(f"Loaded {len(self.images)} images from {labels_file}")

    def __getitem__(self, idx):
        if idx >= len(self.annotations):
            raise IndexError(f"Index {idx} is out of bounds for annotations with length {len(self.annotations)}")

        annotation = copy.deepcopy(self.annotations[idx])
        image_id = annotation['image_id']

        if image_id not in self.images:
            raise KeyError(f"Image ID {image_id} not found in images")

        image_info = self.images[image_id]
        image_path = os.path.join(self._images_folder, image_info['file_name'])

        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image file {image_path} not found")

        image = cv2.imread(image_path, cv2.IMREAD_COLOR)
        if image is None:
            raise ValueError(f"Failed to read image {image_path}")

        print(f"Accessing index: {idx}, Image ID: {image_id}, Image Path: {image_path}")
        return image, annotation

    def __len__(self):
        return len(self.annotations)


# 调试代码，检查数据集是否正确加载
labels_file = 'json/dataset.json'
images_folder = './pic'

dataset = CocoTrainDataset(labels_file, images_folder)
print(f"Dataset length: {len(dataset)}")

for i in range(len(dataset)):
    try:
        image, annotation = dataset[i]
        print(f"Image shape: {image.shape}, Annotation: {annotation}")
    except Exception as e:
        print(f"Error accessing index {i}: {e}")
import os
import json

# 检查图片文件夹
import json
import os
import copy
import cv2


class CocoTrainDataset:
    def __init__(self, labels_file, images_folder, stride=8, sigma=7, paf_sigma=7, paf_thickness=1):
        with open(labels_file, 'r') as f:
            self._labels = json.load(f)
        self._images_folder = images_folder
        self._stride = stride
        self._sigma = sigma
        self._paf_sigma = paf_sigma
        self._paf_thickness = paf_thickness

        self.annotations = self._labels['annotations']
        self.images = {img['id']: img for img in self._labels['images']}

        print(f"Loaded {len(self.annotations)} annotations from {labels_file}")
        print(f"Loaded {len(self.images)} images from {labels_file}")

    def __getitem__(self, idx):
        if idx >= len(self.annotations):
            raise IndexError(f"Index {idx} is out of bounds for annotations with length {len(self.annotations)}")

        annotation = copy.deepcopy(self.annotations[idx])
        image_id = annotation['image_id']

        if image_id not in self.images:
            raise KeyError(f"Image ID {image_id} not found in images")

        image_info = self.images[image_id]
        image_path = os.path.join(self._images_folder, image_info['file_name'])

        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image file {image_path} not found")

        image = cv2.imread(image_path, cv2.IMREAD_COLOR)
        if image is None:
            raise ValueError(f"Failed to read image {image_path}")

        print(f"Accessing index: {idx}, Image ID: {image_id}, Image Path: {image_path}")
        return image, annotation

    def __len__(self):
        return len(self.annotations)


# 调试代码，检查数据集是否正确加载
labels_file = 'json/dataset.json'
images_folder = './pic'

dataset = CocoTrainDataset(labels_file, images_folder)
print(f"Dataset length: {len(dataset)}")

for i in range(len(dataset)):
    try:
        image, annotation = dataset[i]
        print(f"Image shape: {image.shape}, Annotation: {annotation}")
    except Exception as e:
        print(f"Error accessing index {i}: {e}")
