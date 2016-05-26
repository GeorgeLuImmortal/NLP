__author__ = 'user'
# http://pythonprogramming.net/support-vector-machine-svm-example-tutorial-scikit-learn-python/

import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn import svm

digits = datasets.load_digits()

classifier = svm.SVC(gamma=0.01, C=100)

print(len(digits.data))

x, y = digits.data[:-20], digits.target[:-20]
classifier.fit(x, y)
print[digits.data]
print[digits.target]
print('Prediction: data[-15] is ', classifier.predict(digits.data[-15]))
print('Prediction: data[-14] is ', classifier.predict(digits.data[-14]))
print('Prediction: data[-13] is ', classifier.predict(digits.data[-13]))
print('Prediction: data[-12] is ', classifier.predict(digits.data[-12]))
print('Prediction: data[-11] is ', classifier.predict(digits.data[-11]))
print('Prediction: data[-10] is ', classifier.predict(digits.data[-10]))
print('Prediction: data[-9] is ', classifier.predict(digits.data[-9]))
print('Prediction: data[-8] is ', classifier.predict(digits.data[-8]))
print('Prediction: data[-7] is ', classifier.predict(digits.data[-7]))
print('Prediction: data[-6] is ', classifier.predict(digits.data[-6]))

print('Reality: data[-15] is ', digits.target[-15])
print('Reality: data[-15] is ', digits.target[-14])
print('Reality: data[-15] is ', digits.target[-13])
print('Reality: data[-15] is ', digits.target[-12])
print('Reality: data[-15] is ', digits.target[-11])
print('Reality: data[-15] is ', digits.target[-10])
print('Reality: data[-15] is ', digits.target[-9])
print('Reality: data[-15] is ', digits.target[-8])
print('Reality: data[-15] is ', digits.target[-7])
print('Reality: data[-15] is ', digits.target[-6])




plt.imshow(digits.images[-6], cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()