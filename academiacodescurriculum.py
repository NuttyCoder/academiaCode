# -*- coding: utf-8 -*-
"""academiaCodesCurriculum.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1O-Pn6bIuUMy9smIppBQDiOIJ330pfnWz
"""



"""# Week 1: Introduction to Genertative AI

Day 1-2: Overview of AI and Generative AI
Lecture: Understanding AI and its Evolution



*   Artificial Intelligence (AI): AI is the simulation of human intelligence in machines designed to think and learn like humans. It encompasses a wide range of technologies, from simple rule-bases systems to complexed neural networks.
*   Generative AI: A sunset of AI focused on creating new content - be it text, images or sounds. Unlike traditional AI, which often classifies or predicts based on input data, generative AI produces novel outputs.

Key Concepts:

*   Machine Learning (ML): A method of data analysis that automates analytical model building. It's a subset of AI based on the idea that systems can learn from data, identify patterns, and make decisions with minimal human intervention.
*   Deep Learning(DL): A subset of ML involving neural networks with three or more layers. These neural networks attempt to simulate the behavior of the human brain to solve complex data-driven problems.
*   Neural Networks: Systems of algorithms that attempt to recognize underlying relationships in a set of data through a process that mimics the way the human brain operates.

Activity: Discussion and Research

*   Discussion: What are some real-world applications of AI and generative AI? Examples include chatbots, recommendation systems, content creation tools, and more.
*   Research: Find and summerize an example of generative AI in action. Present your findings to the class.

Day 3-4 Introduction to Python Programming

Lecture: Python Fundamentals

*   Python Basics: Python is a high-level, interpreted programming language known from its readability and simplicity. Key features include:
*   Data Types: Integer, float, string, list, tuple, dictionary, etc.
*   Variables: Containers for storing data values.
*   Operators: Arithmetic, comparison, logical, etc.

Hello World:
"""



"""# Hands-On Exercise:"""

print("Hello, World!")

"""Basic Arithmetic:"""

a=10
b=20
print(a+b)
print(a-b)
print(a*b)
print(a/b)

"""Data Structures:"""

#Lists
fruits=["apple","banana","cherry"]
print(fruits)
print(fruits[1])
fruits.append("orange")
print(fruits)

# Dictionary
person={"name":"John","age":30}
print(person["name"])
person["age"]=35
print(person)

#Tuple
coordinates=(10,20)
print(coordinates[0])
#coordinates[0]=5

#Set
unique_numbers={1,2,3,4,5}
print(unique_numbers)
unique_numbers.add(6)
print(unique_numbers)

"""# Day 5-6: Setting Up the Development Environment
Lecture: Environment Setup

*   Tools Required:
*   Python: Ensure Python is installed. Use version 3.6 or later.
*   IDE/Code Edior; Install a code editor Like Visual Studio Code, PyCharm, or Jupyter Notebook, Google CoLab.
*   Libraries: Install necessary libraries for AI programming:
"""

pip install numpy pandas matplotlib scikit-learn tensorflow torch

"""Hands-On Exercise:

-Create a Virtual Environment
"""

python -m venv myenv
source myenv/bin/activate # On Windows: myenv\Scripts\activate

"""Install Libraries:"""

pip install numpy pandas matplotlib scikit-learn tensorflow torch

"""# Day 7: Hands-On Project: Creating a Simple Chatbot
Lecture: Basics of Building a Chatbot

*   Chatbot: A program designed to simulate conversation with human users, especially over the internet.
*   Rule-based Chatbopt: Uses predefined rules and patterns to understand and respond to user input.

Project Code:

*   Simple Rule-based Chatbot:




"""

def  chatbot_response(user_input):
  responses = {
      "hello": "Hello! How can I assist you today?",
      "how are you": "I'm just a computer program, but I'm here to help!",
      "bye": "Goodbye! Have a great day!",
  }
  return responses.get(user_input.lower(), "I'm sorry, I don't understand that.")

while True:
  user_input = input("You: ")
  if user_input.lower() == "exit":
    break
  response = chatbot_response(user_input)
  print("Chatbot:", response)

"""Assignment:


*   Enhance the chatbot by adding more responses and functionalities.
*   Submit a brief report on the challenges faces and how you overcame them.

Summary
The week is all about laying the groundwork. We'll cover the basics of AI, Python programming, and environment setup, culminating in a simple yet exciting project to apply what you've learned. Next week, we'll dive deeper into neural networks and machine learning!

# Week 2: Neural Networks and Machine Learning Basics
Day 1-2: Introduction to Neural Networks
Lecture: Understanding Neural Network

Neural Network Basics:

*   Neural networks are a series of algorithms that attempt to recognize underlying relationships in a set of data through a process that mimics the way the human brain operates.
*   A neural network consists of layers of nodes (neurons), with each layer connecteds to the next. The first layer is the imput layer, the middle layers are hidden layers, and the last layer is the output layer.

Key Components:


*   Neuron: Basic  unit of a neural network. Each neuron recieves inputs, processes them, and passes the output to the next layer.
*   Activation Function: Defines the output of a neuron. Common activation functions include ReLU, Sigmoid, and Tanh.
*   Weights and Biases: Parameters that are adjusted during training to minimize the error in the network's output.
*   Forward Propagation: The process of passing inputs through the network to get the output.
*   Backward Propagation: The process of adjusting weights and biases based on the error of the output using gradient descent.

**Activity: Neural Network Visualization**
*   Visualize a Simple Neural Network:
"""

import numpy as np

def sigmoid(x):
  return 1/(1+np.exp(-x))

def sigmoid_derivative(x):
  return x*(1-x)

# Input data
inputs = np.array([[0,0], [0,1], [1,0], [1,1]])
# Expected output
output = np.array([[0], [1], [1], [0]])

# Initialize weights
input_layer_neurons = 2
hidden_layer_neurons = 2
output_layer_neurons = 1

hidden_weights = np.random.uniform(size=(input_layer_neurons, hidden_layer_neurons))
hidden_bias = np.random.uniform(size=(1, hidden_layer_neurons))
output_weights = np.random.uniform(size=(hidden_layer_neurons, output_layer_neurons))
output_bias = np.random.uniform(size=(1, output_layer_neurons))

# Training the neural network
for _ in range(10000):
  # Forward propagation
  hidden_layer_activation = np.dot(inputs, hidden_weights)
  hidden_layer_activation += hidden_bias
  hidden_layer_output = sigmoid(hidden_layer_activation)

  output_layer_activation = np.dot(hidden_layer_output, output_weights)
  output_layer_activation += output_bias
  predicted_output = sigmoid(output_layer_activation)

  # Backpropagation
  error = output - predicted_output
  d_predicted_output = error * sigmoid_derivative(predicted_output)

  error_hidden_layer = d_predicted_output.dot(output_weights.T)
  d_hidden_layer = error_hidden_layer * sigmoid_derivative(hidden_layer_output)

  # Updating weights and biases
  output_weights += hidden_layer_output.T.dot(d_predicted_output)
  output_bias += np.sum(d_predicted_output, axis=0, keepdims=True)
  hidden_weights += inputs.T.dot(d_hidden_layer)
  hidden_bias += np.sum(d_hidden_layer, axis=0, keepdims=True)

# Testing the neural network
print("Output after training:")
print(predicted_output)
print(output)
print(predicted_output - output)

"""**Day 3-4: Basic Machine Learning Concepts**

**Lecture: Introduction to Machine Learning**
**Machine Learning Basics**:
*   Machine learning is a method of data analysis that automates the building of analytical models. It's based onb the idea that systems can learn from data, identify patterns, and make decisions with minimal human intervention.

*   **Types of Machine Learning:**
**Supervised Learning:** The model is trained on on a labeled dataset, which means that each training example is paired with an input data.

**Unsupervised Learning**: The model is trained on an unlabeled dataset and must find hidden patterns or intrinsic structures in the input data.
**Reinforcement Learning**: The model learns to make decisions by taking actions in an environment to maximize cumulative reward.

**Key Concepts:**
**Training and Testing**: Splitting the dataset into a training set to training set to train the model and a testing set as evaluate its performance.
**Validation:** Using a validation set to tune the model's hyperparameters.

**Activity: Build a Simple Machine Learning Method**
**Simple Linear Regression:**



"""

import numpy as np
import matplotlib.pyplot as plt

# Generate synthetic data
np.random.seed(0)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.rand(100, 1)

# Plot the data
plt.scatter(X, y)
plt.xlabel('X')
plt.ylabel('y')
plt.show()

# Compute the optimal weights using the Normal Equation
X_b = np.c_[np.ones((100, 1)), X]
theta = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)
print("Optimal weights:", theta)

# Predict the
X_new = np.array([[0], [2]])
X_new_b = np.c_[np.ones((2, 1)), X_new]
y_predict = X_new_b.dot(theta)

# Plot the regression line
plt.scatter(X, y)
plt.plot(X_new, y_predict, 'r-')
plt.xlabel('X')
plt.ylabel('y')
plt.show()

# Compute the mean squared error
y_pred = X_b.dot(theta)
mse = np.mean((y - y_pred)**2)
print("Mean squared error:", mse)