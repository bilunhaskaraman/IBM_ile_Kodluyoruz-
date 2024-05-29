import numpy 
import pandas
import math

# Phyton Uygulama 2 
# Minimum Öklid Mesafesinin Hesaplanması 

def euclideanDistance(x1,y1,x2,y2): #Öklid Mesafesini Bulan Fonksiyon
    
  euclidian_distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)     
  
  return euclidian_distance


def min_distances(distances): #Mesafeler Arasındaki Minimum Değeri Döndüren Fonksiyon
    
    minimum_euclidian_distance = min(distances)
    
    return minimum_euclidian_distance


points = [(1, 10), (3, 7), (5, 6), (7, 23), (9, 56)]

distances = []

for i in range(len(points)): #Range 0,5 iken 
    for j in range(i + 1, len(points)): #Range 1,5 olur. 
        dist = euclideanDistance(points[i][0], points[i][1], points[j][0], points[j][1]) #1,10,3,7 sırası ile verir.
        distances.append(dist) #Append fonksiyonu ile listeye ekleme yapılır. 

    
min_euclidian_dis = min_distances(distances) #Fonksiyona oluşturulan distances listesi verildi. 
  
print("Minimum Öklid Mesafesi : ", min_euclidian_dis)
    
