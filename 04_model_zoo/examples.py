#!/usr/bin/python3

# load data
import sklearn.datasets
data = sklearn.datasets.load_breast_cancer()
X = data.data   # shape = (569, 30)
Y = data.target # shape = (569,)

# import classifiers
# MLP = Multilayer Perceptron = neural network
from sklearn.neural_network import MLPClassifier
mlp1 = MLPClassifier(
        hidden_layer_sizes = [100]          # VCdim = 30 * 100**2 = 300,000
        )
mlp2 = MLPClassifier(
        hidden_layer_sizes = [10,10]        # VCdim = 30 * 10**2 * 10**2 = 300,000
        )
mlp3 = MLPClassifier(
        hidden_layer_sizes = [10,10,10]     # VCdim = 30 * 10**2 * 10**2 * 10**2 = 30,000,000
        )

from sklearn.tree import DecisionTreeClassifier
stump = DecisionTreeClassifier(
        max_depth = 1,              # k = 1, VCdim <= 2**1 = 2
        min_samples_split = 2,
        min_samples_leaf = 1,
        )
tree3 = DecisionTreeClassifier(
        max_depth = 3,              # k = 3, VCdim <= 2**3 = 8
        min_samples_split = 25,
        min_samples_leaf = 10,
        )
tree7 = DecisionTreeClassifier(
        max_depth = 7,              # k = 7, VCdim <= 2**7 = 128
        min_samples_split = 15
        min_samples_leaf = 10,
        )

# the larger value for min_samples_*, the more pruning will happen, so the fewer leaf nodes

from sklearn.ensemble import AdaBoostClassifier
boosted_mlp1 = AdaBoostClassifier(
        base_estimator = mlp1,
        n_estimators = 500,             # VCdim = 300,000 * 500 = 1.5 10**8
        )
boosted_mlp2 = AdaBoostClassifier(
        base_estimator = mlp2,
        n_estimators = 50,
        )
boosted_mlp3 = AdaBoostClassifier(
        base_estimator = mlp3,
        n_estimators = 11,
        )

boosted_stump = AdaBoostClassifier(
        base_estimator = stump,         # VCdim(stump) <= 2
        n_estimators = 30,              # T = 30
        )                               # VCdim(boosted_stump) ~= 60
boosted_tree3 = AdaBoostClassifier(
        base_estimator = tree3,
        n_estimators = 50,              # 8 * 50 = 400
        )
boosted_tree7 = AdaBoostClassifier(
        base_estimator = tree7,         # B = 128
        n_estimators = 11,              # T = 11
        )

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier()

# train model
model = mlp3
model.fit(X,Y)

# get training error
acc = model.score(X,Y)
print("acc=",acc)
