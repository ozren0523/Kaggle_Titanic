import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

df = pd.read_csv()
df = df.dropna(subset = ["Embarked"])
df["Age"] = df["Age"].fillna(df["Age"].median())

mapping1 = {"male": 0, "female": 1}
df["Sex_num"] = df["Sex"].map(mapping1)

mapping2 = {"S": 0, "C": 1, "Q": 2}
df["Embarked_num"] = df["Embarked"].map(mapping2)

X = df[["Pclass", "Sex_num", "Age", "SibSp", "Parch", "Fare", "Embarked_num"]]
y = df["Survived"]

model = LogisticRegression(max_iter=1000)
model.fit(X, y)

test_set = pd.read_csv()

test_set["Sex_num"] = test_set["Sex"].map(mapping1)
test_set["Embarked_num"] = test_set["Embarked"].map(mapping2)
test_set["Age"] = test_set["Age"].fillna(test_set["Age"].median())
test_set["Fare"] = test_set["Fare"].fillna(df["Fare"].mode()[0])

X_test = test_set[["Pclass", "Sex_num", "Age", "SibSp", "Parch", "Fare", "Embarked_num"]]

y_pred = model.predict(X_test)

output_path = 
output = pd.DataFrame({"PassengerId": test_set["PassengerId"], "Survived":y_pred})
output.to_csv(output_path, index=False)

print("make csvfile")