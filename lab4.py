from sklearn.tree import DecisionTreeClassifier, export_text
import pandas as pd

df = pd.read_csv('datasets/4.csv')
df_encoded = pd.get_dummies(df.drop('PlayTennis', axis=1))

X = df_encoded.reindex(columns=df_encoded.columns, fill_value=0).values
y = df['PlayTennis'].map({'Yes': 1, 'No': 0}).values

clf = DecisionTreeClassifier(criterion='entropy').fit(X, y)
tree_rules = export_text(clf, feature_names=list(df_encoded.columns))
print(tree_rules)

df_testing = pd.read_csv('datasets/4_test.csv')

df_testing_encoded = pd.get_dummies(df_testing)
X_test = df_testing_encoded.reindex(columns=df_encoded.columns, fill_value=0).values

predictions = clf.predict(X_test)
print("Predictions:")
print('\n'.join(['Yes' if pred == 1 else 'No' for pred in predictions]))