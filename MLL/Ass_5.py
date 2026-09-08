# Import scikit-learn dataset library and model modules
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics

# Load breast cancer dataset
cancer = datasets.load_breast_cancer()

# Exploring dataset features and labels
print("Features: ", cancer.feature_names)
print("Labels: ", cancer.target_names)
print("Data Shape: ", cancer.data.shape)

# Split dataset into training set (70%) and test set (30%)
X_train, X_test, y_train, y_test = train_test_split(
    cancer.data, cancer.target, test_size=0.3, random_state=109
)

# Create a SVM Classifier object with a linear kernel
clf = svm.SVC(kernel='linear')

# Train the model using the training sets
clf.fit(X_train, y_train)

# Predict the response for test dataset
y_pred = clf.predict(X_test)

# Model Evaluation Metrics
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
print("Precision:", metrics.precision_score(y_test, y_pred))
print("Recall:", metrics.recall_score(y_test, y_pred))
