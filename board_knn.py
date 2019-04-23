import pandas as pd 
from sklearn.neighbors import KNeighborsClassifier

data = pd.read_csv("parsed_results/boardgame_data.csv", header=None)
print(data.head())

data = data.iloc[:,3:5]

print(data.head())

target = data.iloc[:,2].values

print(target)
#learn the api for sklearn

knn = KNeighborsClassifier(n_neighbors=6)

knn.fit(data, target)

X = [
	[8.9,5566],
	[7.7,5023],
	[6.5,7844],
]

print(X)

results = knn.predict(X)

print(results)






