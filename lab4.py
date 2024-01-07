import pandas as pd
import numpy as np
from collections import Counter
from pprint import pprint

def entropy(probs):
    return -np.sum(probs * np.log2(probs))

def entropylist(arr):
    return entropy(np.array(list(Counter(arr).values())) / len(arr))

def gain(df, sp, target):
    total = entropylist(df[target])
    group = df.groupby(sp)[target].apply(lambda x: entropylist(x) * len(x) / len(df))
    return total - group.sum()

def id3(df, target, attrs):
    if np.all(df[target] == df[target].iloc[0]):
        return df[target].iloc[0]
    if not attrs or df.empty:
        return Counter(df[target]).most_common(1)[0][0]
    best = max(attrs, key=lambda attr: gain(df, target, attr))
    tree = {best: {}}
    for val, data in df.groupby(best):
        rem = [attr for attr in attrs if attr != best]
        tree[best][val] = id3(data, target, rem)
    return tree

def classify(instance, tree):
    while isinstance(tree, dict):
        attribute = next(iter(tree))
        tree = tree[attribute].get(instance.get(attribute))
    return tree

df = pd.read_csv('datasets/4.csv')
names = list(df.columns)
print("List of attrs:", names)
names.remove('PlayTennis')
tree = id3(df, 'PlayTennis', names)

test_data = pd.read_csv('datasets/4_test.csv')
test_data['predicted2'] = test_data.apply(lambda row: classify(row, tree), axis=1)

print("Predicting attrs:", names)
pprint(tree)
print(test_data[['predicted2']])
