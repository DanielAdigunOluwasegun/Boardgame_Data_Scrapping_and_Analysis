import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
from sklearn import metrics



dataset = pd.read_csv("parsed_results/boardgame_data.csv",header=None)
# pd.to_numeric(dataset, errors = 'coerce')
int(dataset)
print(dataset.info())
# print(dataset.head())
# plt.scatter(dataset[2],dataset[3])
# plt.savefig("scatter.png")


# for i in range (4):
# 	n = i + 2
# 	print(n)
# 	kmeans_predictions = KMeans(n_clusters=n).fit_predict(dataset)
# 	plt.scatter(dataset[0],dataset[1], c=kmeans_predictions)
# 	plt.savefig("scatterkmean" + str(n)+ ".png")
# 	print("kmeas" + str(n)+ "clusters")
# 	print(metrics.silhouette_score(dataset,kmeans_predictions))

# for i in range (4):
# 	n = i + 2
# 	print(n)
# 	gaussian_predictions = GaussianMixture(n_components=n).fit(dataset).predict(dataset)
# 	plt.scatter(dataset[0],dataset[1], c=gaussian_predictions)
# 	print("guass" + str(n)+ "components")
# 	plt.savefig("scattergaussian" + str(n)+ ".png")
# 	print(metrics.silhouette_score(dataset,gaussian_predictions))