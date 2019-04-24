import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn import tree 
from sklearn.metrics import accuracy_score

from sklearn.metrics import confusion_matrix

dataset = pd.read_csv("parsed_results/boardgame_data.csv")

print(dataset.head())

target = dataset.iloc[:,0].values

print(target)

data = dataset.iloc[:,2:4]

print(data.head())
data_training, data_test, target_training, target_test = train_test_split(data, target, test_size=0.2,random_state=1)

print("data_training")
print("data_test")
print("target_training")
print("target_test")

decision_tree_machine = tree.DecisionTreeClassifier(criterion="gini", max_depth=10)
decision_tree_machine.fit(data_training, target_training)

predictions = decision_tree_machine.predict(data_test)
print(predictions)
accuracy_score(target_test, predictions)
print(accuracy_score(target_test, predictions))
