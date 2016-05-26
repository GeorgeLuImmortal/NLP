import nltk
from nltk.corpus import names
import random
import numpy

def gender_features1(word):                                      #extract the last two words
    return {'last_two_letter_and_first_word': word[-2]+word[-1]}
# gender_features('Shrek') = {'last_letter': 'k'}

accuracys=[]
for i in range(100):
    male_names = [(name, 'male') for name in names.words('male.txt')]
    female_names = [(name, 'female') for name in names.words('female.txt')]
    labeled_names = male_names + female_names
    random.shuffle(labeled_names)
    featuresets = [(gender_features1(n), gender) for (n, gender) in labeled_names]
    #entries are    ({'last_letter': 'g'}, 'male')
    train_set, test_set = featuresets[5000:], featuresets[:5000]


    classifier = nltk.NaiveBayesClassifier.train(train_set)

    ans1 = classifier.classify(gender_features1('Mark'))
    ans2 = classifier.classify(gender_features1('Precilla'))
    ans3 = classifier.classify(gender_features1('George'))

    #print("Mark is:", ans1)
    #print("Precilla is:", ans2)
    #print("George is:", ans3)
    accuracys.append(nltk.classify.accuracy(classifier, test_set))
    # classifier.show_most_informative_features(5)
    #print(nltk.classify.accuracy(classifier, test_set))

print(accuracys)
print('The mean accuracy of new feature is '+str(numpy.mean(accuracys)))




