# K-Nearest Neighbors


import math
from collections import Counter


def get_neighbors(training_set, test_instance, k):
  """ Get k nearest neighbors for a test instance using math.dist
  """
  distances = [(item, math.dist(item[:-1], item[:-1])) for item in training_set]

  # Sort by distance and get k nearest neighbors
  return [instance for instance, _ in sorted(distances, key=lambda x: x[1])[:k]]


def predict_classification(training_set, test_instance, k):
  """ Make a prediction using KNN
  """
  neighbors = get_neighbors(training_set, test_instance, k)

  # Get all class values from neighbors
  output_values = [neighbor[-1] for neighbor in neighbors]

  # Return the most common class
  return Counter(output_values).most_common(1)[0][0]


# ---------------------------------------------------------

if __name__ == "__main__":

  # Example usage
  # Sample dataset: [feature1, feature2, ..., class_label]
  dataset = [
    [2.78, 2.55, 0],
    [1.46, 2.36, 0],
    [3.39, 4.40, 0],
    [1.38, 1.85, 0],
    [3.06, 3.00, 0],
    [7.62, 2.75, 1],
    [5.33, 2.08, 1],
    [6.92, 1.77, 1],
    [8.67, -0.24, 1],
    [7.67, 3.50, 1]]

  # Test instance (without class label)
  test_instance = [5.70, 2.50]

  # Number of neighbors to consider
  k = 3

  # Make prediction (adding None as placeholder for class label)
  prediction = predict_classification(dataset, test_instance + [None], k)
  print(f"Predicted class for {test_instance}: {prediction}")

