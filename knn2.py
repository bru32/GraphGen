# KNN using numpy

import math
import numpy as np
from collections import Counter

def euclidean_distance(p1, p2):
  return np.sqrt(np.sum((p1 - p2)**2))

def knn_predict(training_data, training_labels, test_point, k):
  distances = []
  for i in range(len(training_data)):
    dist = np.linalg.norm(test_point-training_data[i])
    distances.append((dist, training_labels[i]))
  distances.sort(key=lambda x: x[0])
  k_nearest_labels = [label for _, label in distances[:k]]
  return Counter(k_nearest_labels).most_common(1)[0][0]


# ---------------------------------------------------------

def test1():
  p1 = np.array([2,4,6,8])
  p2 = np.array([1,2,3,4])
  x = math.sqrt(30)
  print(x)
  x = euclidean_distance(p1, p2)
  print(x)
  x = np.linalg.norm(p1-p2)
  print(x)

def test2():
  training_data = np.array([[1, 2], [2, 3], [3, 4], [6, 7], [7, 8]])
  training_labels = ['A', 'A', 'A', 'B', 'B']
  test_point = np.array([4, 5])
  k = 3
  prediction = knn_predict(training_data, training_labels, test_point, k)
  print(prediction)


# ---------------------------------------------------------


test1()
test2()
