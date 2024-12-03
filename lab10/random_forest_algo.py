import math
import pandas as pd
import random

def calculate_entropy(data, target_col):
    value_counts = data[target_col].value_counts()
    entropy = 0
    total_data = len(data)
    for count in value_counts:
        prob = count / total_data
        entropy -= prob * math.log2(prob)
    return entropy

def calculate_information_gain(data, attribute, target_col):
    entropy_before = calculate_entropy(data, target_col)
    unique_values = data[attribute].unique()
    weighted_entropy = 0
    total_data = len(data)
    for value in unique_values:
        subset = data[data[attribute] == value]
        weighted_entropy += (len(subset) / total_data) * calculate_entropy(subset, target_col)
    info_gain = entropy_before - weighted_entropy
    return info_gain

def build_tree(data, attributes, target_col, depth=0, max_depth=3):
    if len(data[target_col].unique()) == 1:
        return data[target_col].iloc[0]
    
    if depth >= max_depth or len(attributes) == 0:
        return data[target_col].mode()[0]
    
    info_gains = {attribute: calculate_information_gain(data, attribute, target_col) for attribute in attributes}
    best_attribute = max(info_gains, key=info_gains.get)
    tree = {best_attribute: {}}
    
    unique_values = data[best_attribute].unique()
    remaining_attributes = [attribute for attribute in attributes if attribute != best_attribute]
    
    for value in unique_values:
        subset = data[data[best_attribute] == value]
        tree[best_attribute][value] = build_tree(subset, remaining_attributes, target_col, depth + 1, max_depth)
    
    return tree

def predict(tree, data_point):
    
    if not isinstance(tree, dict): 
        return tree
    
    root_attribute = list(tree.keys())[0]
    attribute_value = data_point.get(root_attribute)
    
    if attribute_value not in tree[root_attribute]:
        return tree[root_attribute].get('default', 'Unknown')  
    
    return predict(tree[root_attribute][attribute_value], data_point)

def build_random_forest(data, attributes, target_col, n_trees=2):
    forest = []
    for _ in range(n_trees):
        bootstrap_sample = data.sample(frac=1, replace=True)
        tree = build_tree(bootstrap_sample, attributes, target_col)
        forest.append(tree)
    return forest

def predict_random_forest(forest, data_point):
    
    predictions = [predict(tree, data_point) for tree in forest]
    return pd.Series(predictions).mode()[0] 

def main():
    data = {
        'Weather': ['Sunny', 'Sunny', 'Overcast', 'Rainy', 'Rainy'],
        'Temperature': ['Hot', 'Hot', 'Hot', 'Mild', 'Mild'],
        'Play?': ['No', 'Yes', 'Yes', 'Yes', 'No']
    }

    df = pd.DataFrame(data)
    target_col = 'Play?'  
    attributes = ['Weather', 'Temperature']  

    forest = build_random_forest(df, attributes, target_col, n_trees=2)
    
    print("Random Forest (Multiple Trees):")
    for i, tree in enumerate(forest, 1):
        print(f"Tree {i}:")
        print(tree)
        print()
    
    data_point = {'Weather': 'Sunny', 'Temperature': 'Mild'}
    prediction = predict_random_forest(forest, data_point)
    print(f"Prediction for {data_point}: {prediction}")

main()
