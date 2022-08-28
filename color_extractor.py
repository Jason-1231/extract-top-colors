import numpy as np
import pandas as pd
from PIL import Image
import math


class Extractor:
    def __init__(self, image_path):
        self.image_path = image_path
        self.top10_colors_rgb = []
        self.top10_colors_hex = []
        self.extract_rgb()
        self.rgb_to_hex()

    def extract_rgb(self):
        img = Image.open(self.image_path)
        img_arr = np.array(img)

        r = []
        g = []
        b = []
        for row in img_arr:
            for array in row:
                for _ in array:
                    r.append(array[0])
                    g.append(array[1])
                    b.append(array[2])

        d = {'r': np.array(r),
             'g': np.array(g),
             'b': np.array(b)}
        df = pd.DataFrame(d)

        color_count_series = df.value_counts()
        color_count_df = color_count_series.reset_index()
        top_10 = math.ceil(len(color_count_series) * 0.1)
        c_indices = np.linspace(0, top_10, num=10, dtype=int)

        for i in c_indices:
            rgb_color = color_count_df.iloc[i]
            self.top10_colors_rgb.append((int(rgb_color.r), int(rgb_color.g), int(rgb_color.b)))

    def rgb_to_hex(self):
        for rgb in self.top10_colors_rgb:
            color_hex = '#%02x%02x%02x' % rgb
            self.top10_colors_hex.append(color_hex)




