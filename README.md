# HealthIssuesFromNail

~~I've been known to struggle a bit when it comes to naming things. Let's just say my creativity takes a coffee break sometimes.~~

This is a university-level course project. The aim is to inform users of potential health issues based on the classification of their nail disease.

The project makes use of TensorFlow and Keras high-level APIs and utilizes transfer learning with the MobileNetV3 model because of the compact size and reasonable performance. The dataset is taken from Roboflow Universe, you can read more about it on the [Dataset](#dataset) section.

This project does not guarantee its correctness or reliability. Please use the information provided with caution.


# Dataset

You may download the dataset from the provided [OneDrive](https://1drv.ms/u/s!AsGDCQXYI6yYgbIGAXt1h7tsuj3dSA?e=0JpNt1) link for convenience. However, if the OneDrive link is not available, I recommend accessing the official source of the data, the [Nail Disease Detection Dataset](https://universe.roboflow.com/knm/nail-disease-detection-mxoqy), on Roboflow Universe.

There are several versions of the dataset available from OneDrive, as follows:
* v1: the raw dataset, which is the same as the official version
* v2: the dataset after running organizer.py and performing some manual organization
* v3: the same as v2, but with the Lindsay's nail class removed due to having only two images
* v4: the dataset with a few additional images that we have added

Here is the BibTeX information provided by the official source:

```bibtex
@misc{ nail-disease-detection-mxoqy_dataset,
    title = { Nail Disease Detection Dataset },
    type = { Open Source Dataset },
    author = { KNM },
    howpublished = { \url{ https://universe.roboflow.com/knm/nail-disease-detection-mxoqy } },
    url = { https://universe.roboflow.com/knm/nail-disease-detection-mxoqy },
    journal = { Roboflow Universe },
    publisher = { Roboflow },
    year = { 2022 },
    month = { jan },
    note = { visited on 2023-03-12 },
}
```


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


# How to Run
If you do not wish to train a model from scratch, you may use the pre-trained model provided in a `saved_models` directory. Simply load the model using `tensorflow.keras.models.load_model(path)`, for example, a path could be `"saved_models/model_{test_accuracy}"`. Please note that `{...}` is a placeholder and should not be included in the actual file name.

To prevent any errors, I recommend running the notebooks in the latest version from top to bottom. If you encounter any errors, I suggest reviewing the code and ensuring that all necessary dependencies have been installed. Furthermore, it is recommended that you verify that the dataset path is correct before running the notebooks, as some of them may contain outdated dataset paths.


# What Types of Images Are Preferred for This Project?
Please note that this project does not provide any preprocessing utility for images. Therefore, you will need to crop the picture of your nail yourself, preferably in a square or close-to-square aspect ratio. It is best if there is only one nail in the cropped image. While it is not necessary to be perfect, you can refer to the dataset for example images if you are unsure.
