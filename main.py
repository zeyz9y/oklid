import math

# 2D uzaydaki noktaların tanımlanması
points = [(2, 3), (5, 7), (1, 9), (4, 4), (6, 2)]

# Öklid Mesafesi Hesaplama Fonksiyonu
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# Mesafeleri saklamak için liste
distances = []

# Her nokta çifti arasındaki mesafeyi hesaplama
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        dist = euclideanDistance(points[i], points[j])
        distances.append(dist)

# Minimum mesafeyi bulma
min_distance = min(distances)

# Minimum mesafeyi ekrana yazdırma
print(f"Noktalar arasındaki minimum Öklid mesafesi: {min_distance:.2f}")
