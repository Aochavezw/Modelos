# imports
from src.make_data import make_data
from src.knn import euclidean_distance, manhattan_distance, cosine_distance, KNNRegressor
import matplotlib as plt

# get data
X, y = make_data(n_features=2, n_pts=300, noise=0.1)

# separate into training and test
X_train = X[5:]
y_train = y[5:]
X_test = X[:5]
y_test = y[:5]

# perform a KNN Regression using multiple distance functions
for f in [euclidean_distance, manhattan_distance, cosine_distance]:
    knn = KNNRegressor(k=3, distance=f)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)

    print(f.__name__)
    print("Predictions", y_pred)
    print("Actual", y_test)
    print('*' * 50)

    plt.figure(figsize=(10,10))
    plt.scatter(y_test, y_pred, c='crimson')
    
    p1 = max(max(y_pred), max(y_test))
    p2 = min(min(y_pred), min(y_test))
    plt.plot([p1, p2], [p1, p2], 'b-')
    plt.xlabel('True Values', fontsize=15)
    plt.ylabel('Predictions', fontsize=15)
    plt.axis('equal')
    plt.show()