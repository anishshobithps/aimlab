from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report

iris = load_iris()

print("Class : number")
[print(f"{label} : {target}") for target, label in enumerate(iris.target_names)]

X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.3)
knn = KNeighborsClassifier(n_neighbors=1).fit(X_train, y_train)

y_pred = knn.predict(X_test)

print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred, target_names=iris.target_names))