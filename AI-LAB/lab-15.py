import numpy as np
from sklearn.neural_network import MLPClassifier

# Input data
X = np.array([[0, 0], [0, 1],
              [1, 0], [1, 1]])

y = np.array([0, 1, 1, 1])

# Create Neural Network
model = MLPClassifier(hidden_layer_sizes=(4,),
                      max_iter=5000,
                      random_state=1)

# Train the model
model.fit(X, y)

# Test the model
result = model.predict([[1, 1]])

print("Neural Network Prediction:", result[0])
