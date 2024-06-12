import numpy as np
yoğunluk_degerleri = np.array([100, 101, 102, 104, 105, 106, 107, 108, 109, 110, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150])
piksel_sayilari = np.array([12, 10, 32, 52, 65, 55, 42, 32, 16, 10, 5, 18, 25, 32, 40, 65, 43, 32, 20, 10, 4])
def otsu_esikleme(yogunluk_degerleri, piksel_sayilari):
    tümü = np.sum(piksel_sayilari)
    sumB = 0
    wB = 0
    maksimum = 0.0
    optimal_esik_degeri = 0 
    sum1 = np.dot(yogunluk_degerleri, piksel_sayilari)
    for i in range(len(yogunluk_degerleri)):
        wB += piksel_sayilari[i]
        wF = tümü - wB
        if wB == 0 or wF == 0:
            continue
        sumB += yogunluk_degerleri[i] * piksel_sayilari[i]
        mB = sumB / wB
        mF = (sum1 - sumB) / wF
        between = wB * wF * ((mB - mF) ** 2)
        if between > maksimum:
            maksimum = between
            optimal_esik_degeri = yogunluk_degerleri[i]  
    return optimal_esik_degeri
optimal_esik_degeri = otsu_esikleme(yoğunluk_degerleri, piksel_sayilari)
print(f"Optimal eşik değeri: {optimal_esik_degeri}")
