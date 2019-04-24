import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
# from sklearn.ensemble import BaggingClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

dataset = pd.read_csv("parsed_results/boardgame_data.csv")
target = dataset.iloc[:,0].values

data = dataset.iloc[:,1:4]
data_training, data_test, target_training, target_test = train_test_split(data, target, test_size=0.2,random_state=1)

random_forest_machine = RandomForestClassifier(n_estimators=20)
random_forest_machine.fit(data_training, target_training)

predictions = random_forest_machine.predict(data_test)
print(accuracy_score(target_test, predictions))

