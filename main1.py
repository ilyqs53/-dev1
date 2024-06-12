import pandas as pd
import numpy as np
# Excel dosyasını okuyun
# Aşağıda belirtiler excell dosyasının yoludur.Sistemden sisteme değişiklilik gösterebilir. 
excel_dosya_yolu = r'C:\Users\ilyqs\Downloads\soru1_2_data (1).xlsx'
df = pd.read_excel(excel_dosya_yolu)
data = df.to_numpy()
M, N = data.shape
L = 256
histogram, _ = np.histogram(data.flatten(), bins=np.arange(L))
cdf = histogram.cumsum()
cdf_min = cdf[cdf > 0].min()
h_v = np.round((cdf[data.astype('int')] - cdf_min) / (M*N - cdf_min) * (L-1))
print(h_v.reshape(M, N))
