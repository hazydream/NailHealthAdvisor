# NailHealthAdvisor
This is a university-level course project. The aim is to inform users of potential health issues based on the classification of their nail disease.

The project makes use of TensorFlow and Keras high-level APIs and utilizes transfer learning with the MobileNetV3 model.

Please note that there is no pre-trained model available for this project. You will need to train the model yourself. However, the model is relatively small and simple, as the dataset used for training is not very large.

This project does not guarantee its correctness or reliability. Please use the information provided with caution.


# Dataset
You can download the dataset from this [OneDrive](https://1drv.ms/u/s!AsGDCQXYI6yYgbIGAXt1h7tsuj3dSA?e=0JpNt1) link, or alternatively, you can access the official source of the data, the [Nail Disease Detection Dataset](https://universe.roboflow.com/knm/nail-disease-detection-mxoqy), on Roboflow Universe.

There are several versions of the dataset available from OneDrive, as follows:
* v1: the raw dataset, which is the same as the official version
* v2: the dataset after running organizer.py and performing some manual organization
* v3: the same as v2, but with the Lindsay's nail class removed due to having only two images
* v4: the dataset with a few additional images that we have added


# Dataset Preparation
**Case 1**: If you have downloaded the dataset from OneDrive, simply extract the archive in the same directory as the notebooks.

**Case 2**: If you have downloaded the dataset from Roboflow Universe in "Multi-Label Classification" format, follow these steps to obtain v3 of the dataset:

1. Extract the downloaded archive and navigate to the extracted directory. You should see three directories: `train`, `valid`, and `test`. (v1)
2. Copy the `organizer.py` file to the same directory and run it. This will organize the images into their respective classes and create a new directory called `organized`, which will be located at the same level as the three directories mentioned above.
3. Copy the entire `organized` directory to the same level as the notebooks.
4. Rename the `organized` directory to `dataset` or any other name that suits your preference. (v2)
5. Navigate into the `dataset` directory and delete the `Lindsay-s Nail` directory. (v3)

The expected directory structure for the dataset is as follows:
```
dataset
├── class A
├── class B
├── class C
├── ...
└── class Z
```


# What Types of Images Are Preferred for This Project?
Please note that this project does not offer any preprocessing utility. Therefore, you will need to crop the picture of your nail yourself, preferably in a square or close-to-square aspect ratio. While there is no need to be perfect, you can refer to the dataset for example images if you are unsure.


# How to Run (the Unfinished for Now)
Run the latest version of the available notebooks from top to bottom, and there should not be any errors (hopefully).

*It is important to note that the dataset paths in some of the notebooks may be outdated. Therefore, please verify that the dataset path is correct before running the notebooks.*


# Current Progress
We have decided to switch from using a CNN built from scratch to using transfer learning. The initial model has finished training, but there may be some adjustments to be made in the future. The next step is to determine how to display the output to users. Currently, we have decided to display the percentage of each class, sorted from highest to lowest, as there are only 10 classes. However, we may consider displaying only the top n classes if deemed reasonable.
