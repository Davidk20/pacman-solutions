"""
Script used to render the levels as an image so that they can be visualised.

This is a standalone script, with no connection to the application and should
only be used for development.
"""
import json
import os

import numpy as np
from PIL import Image

wall = int("1E1EC3", 16)
dot = int("F4BB9C", 16)

absolute_path = os.path.dirname(__file__)
relative_path = "../models/levels.json"
full_path = os.path.join(absolute_path, relative_path)
with open(full_path) as levels:
    data = json.load(levels)
    level = data["level1"]["map"]
    level_array = np.asarray(level)
    level_array = level_array.repeat(64, axis=0).repeat(64, axis=1)
    for row in level_array:
        print(row)
    image = Image.fromarray(level_array, "RGB")
    image.show()
