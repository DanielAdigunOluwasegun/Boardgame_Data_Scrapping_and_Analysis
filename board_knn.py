import pandas as pd 
from sklearn.neighbors import KNeighborsClassifier

data = pd.read_csv("parsed_results/boardgame_data.csv")
print(data.head())

target = data.iloc[:,0].values

print(target)
data = data.iloc[:,2:4]

print(data.head())


#learn the api for sklearn

knn = KNeighborsClassifier(n_neighbors=6)

knn.fit(data, target)

X = [
	[7.0,15367],
	[7.7,50235],
	[6.5,7842],
]

print(X)

results = knn.predict(X)

print(results)






