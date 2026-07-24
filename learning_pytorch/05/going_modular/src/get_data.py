import os
import requests
import zipfile
from pathlib import Path

data_path = Path("/data")
image_path = data_path / "pizza_steak_sushi"

if image_path.is_dir():
    print(f"{image_path} directory exists.")
