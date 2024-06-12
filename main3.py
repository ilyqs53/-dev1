yoğunluk_değerleri = [100, 101, 102, 104, 105, 106, 107, 108, 109, 110, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150]
piksel_sayıları = [12, 10, 32, 52, 65, 55, 42, 32, 16, 10, 5, 18, 25, 32, 40, 65, 43, 32, 20, 10, 4]
T0 = 100
epsilon = 1
while True:
    G1 = [(p, y) for p, y in zip(piksel_sayıları, yoğunluk_değerleri) if y > T0]
    G2 = [(p, y) for p, y in zip(piksel_sayıları, yoğunluk_değerleri) if y <= T0]
    if G1:
        m1 = sum(p * y for p, y in G1) / sum(p for p, y in G1)
    else:
        m1 = 0

    if G2:
        m2 = sum(p * y for p, y in G2) / sum(p for p, y in G2)
    else:
        m2 = 0
    T1 = (m1 + m2) / 2
    if abs(T1 - T0) < epsilon:
        break
    T0 = T1
print(f"Optimum eşik değeri: {T1}")

