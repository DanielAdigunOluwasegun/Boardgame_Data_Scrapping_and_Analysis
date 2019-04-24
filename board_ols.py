from sklearn import linear_model
import pandas as pd 
dataset = pd.read_csv("parsed_results/boardgame_data.csv")

print(dataset.head())

target = dataset.iloc[:,0].values

print(target)

data = dataset.iloc[:,2:4]

print(data.head())

regression = linear_model.LinearRegression()

result = regression.fit(data, target)
print(result)

X = [
	[7.0,15367],
	[7.7,50235],
	[6.5,7842],
]

results = regression.predict(X)
print(results)


def getAccuracy(X, predictions):
    correct = 0
    for x in range(len(X)):
        if X[x][-1] is predictions[x]:
            correct += 1
    return (correct/float(len(X))) * 100.0
   
X = [
	[7.0,15367],
	[7.7,50235],
	[6.5,7842],
]
predictions = results
accuracy = getAccuracy(X, predictions)
print(accuracy)