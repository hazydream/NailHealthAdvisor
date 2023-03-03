import shutil
from pathlib import Path

import pandas as pd


def preprocess_class_name(class_name):
    return class_name.strip()


input_dirs = ["test", "valid", "train"]
output_dir = "categorized"


base_dir = Path.cwd()
output_dir = base_dir / output_dir

for directory in input_dirs:
    input_dir = base_dir / directory

    df = pd.read_csv(input_dir / "_classes.csv")
    _, *classes = df.columns

    # make a directory for each class
    for class_name in classes:
        class_folder = output_dir / preprocess_class_name(class_name)
        class_folder.mkdir(parents=True, exist_ok=True)

    # copy each image into its corresponding class directory
    for i, row in df.iterrows():
        filename = row["filename"]
        for class_name in classes:
            if row[class_name] == 1:
                src = input_dir / filename
                dst = output_dir / preprocess_class_name(class_name) / filename
                shutil.copy(src, dst)
