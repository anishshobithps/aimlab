import numpy as np

X = np.array([[2, 9], [1, 5], [3, 6]], dtype=float)
X /= np.amax(X, axis=0)
Y = np.array([[92], [86], [89]], dtype=float) / 100

# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

epochs, learning_rate = 5000, 0.1
input_neurons, hidden_neurons, output_neurons = 2, 3, 1

input_hidden_weights = np.random.uniform(size=(input_neurons, hidden_neurons))
hidden_biases = np.random.uniform(size=(1, hidden_neurons))
hidden_output_weights = np.random.uniform(size=(hidden_neurons, output_neurons))
output_biases = np.random.uniform(size=(1, output_neurons))

for _ in range(epochs):
    # Forward Propagation
    hidden_layer_output = sigmoid(np.dot(X, input_hidden_weights) + hidden_biases)
    predicted_output = sigmoid(np.dot(hidden_layer_output, hidden_output_weights) + output_biases)

    # Backpropagation
    output_error = (Y - predicted_output) * predicted_output * (1 - predicted_output)
    hidden_layer_error = output_error.dot(hidden_output_weights.T) * hidden_layer_output * (1 - hidden_layer_output)

    # Update weights and biases
    hidden_output_weights += hidden_layer_output.T.dot(output_error) * learning_rate
    input_hidden_weights += X.T.dot(hidden_layer_error) * learning_rate

print("Input:\n", X)
print("Actual Output:\n", Y)
print("Predicted Output:\n", predicted_output)
