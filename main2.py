import numpy as np
import pandas as pd

# Excel dosyasını okuyun
# Aşağıda belirtiler excell dosyasının yoludur.Sistemden sisteme değişiklilik gösterebilir. 
df = pd.read_excel(r'C:\Users\ilyqs\Downloads\soru3_data.xlsx', header=None)
image = df.values
# Gauss filtresi kerneli
kernel = np.array([[1, 2, 1],
                   [2, 4, 2],
                   [1, 2, 1]]) * (1/16)
output_image_size = (30, 30)
output_image = np.zeros(output_image_size)
for i in range(1, image.shape[0] - 1):
    for j in range(1, image.shape[1] - 1):
        output_image[i-1, j-1] = np.sum(image[i-1:i+2, j-1:j+2] * kernel)
print(output_image)
