# Day 2: im gonna learn ab 4 primary built-in data collections
# each servers a distinct purpose, especially when im preparing data or configuring ML models

# List: an ordered (thứ tự) and mutable (có thể thay đổi) collections
# uses square brackets: [...]
loss_values = [0.9, 1.0, 2.0, 3.0]

# Tuple: ordered but inmutable (unchangeable)
# uses parentheses: (...)
# common use in define fixed properties, such as shape or dimensions of a matrix
image_shape = (256, 256, 3)

# Dictionary: opposite of tuple, unordered but mutable
# uses curly brackets with a colon ':' to separate keys and values: {key: value}
# a standard way to store hyperparameters or to map text labels to numerical categories
hyperparameters = {
    "learning_rate" : 0.01,
    "batch_size" : 32,
    "epochs" : 100
}

# Set: an unordered collection of unique elements, it doesnt allow to duplicate values
# uses curly brackets but without the colons ':' : {...}
# perfect for data cleaning and exploration (e.g. if i have some datasets with thousands of labels, i can convert into set to remove the duplicate labels)
raw_labels = ["cat", "dog", "cat", "bird", "dog"]
unique_labels = set(raw_labels)     # Results in {"cat", "dog", "bird"}

