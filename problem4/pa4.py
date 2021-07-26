# -*- coding: utf-8 -*-
"""
PA4

1. Reads a training and test file of spam/not-spam emails.
2. Fits a BernoulliNB to training data.
3. Predicts the labels of the test emails.
4. Prints statistics about the test emails and their predictions.

"""
import csv
import numpy as np
from sklearn.metrics import confusion_matrix
from sklearn.naive_bayes import BernoulliNB
import sys

if __name__ == '__main__':

    train_file = sys.argv[1]
    test_file = sys.argv[2]

    def read_X_y(filename):
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            next(reader) # header
            D=np.asarray(list(reader))

        X = (D[:, :-1] == 'True')
        y = D[:, -1]
        return X, y

    # Read the files
    X_train, y_train = read_X_y(train_file)
    X_test, y_test = read_X_y(test_file)

    # Create a BernoulliNB
    bn = BernoulliNB(alpha=1, binarize=None, fit_prior=True)

    # Fit BernoulliNB to the training data
    bn.fit(X_train, y_train)

    # Predict labels on the test data
    # This prediction uses the default threshold for assigning classes
    # i.e., in this case, 0.5
    y_pred = bn.predict(X_test)

    # IMPLEMENT BELOW
    # Change the code but do not change the variable names
    # Your final code should not have any print print statements
    # other than the ones already included at the bottom.
    # Count how many spam and not-spam emails are in the test (y_test)
    s_c = 0 # The number of spam emails in the test. Update this.
    ns_c = 0 # The number of not-spam emails in the test. Update this.
    for x in y_test:
        if (x == 'spam'):
            s_c += 1
        else:
            ns_c += 1

    # Confusion matrix
    cm = confusion_matrix(y_test, y_pred, labels=['spam', 'not-spam'])
    metrics = cm.ravel()
    tn, fp, fn, tp = metrics[0], metrics[1], metrics[2], metrics[3]
    as_ps = tn # Actual spam, predicted spam. Update this.
    as_pns = fp # Actual spam, predicted not-spam. Update this.
    ans_ps = fn # Actual not-spam, predicted spam. Update this.
    ans_pns = tp# # Actual not-spam, predicted not-spam. Update this.

    accuracy = (tp+tn)/(tp+tn+fp+fn) # Accuracy. Update this.
    precision = tn/(tn+fn) # Precision. The positive class is 'spam.' Update this.
    recall = tn/(tn+fp) # Recall. The positive class is 'spam.' Update this.
    f1 = 2*(precision*recall)/(precision+recall) # F1. The positive class is 'spam.' Update this.

    # Scikit-learn has methods for calculating the above metrics.
    # I recommend you to use the confusion marix and your
    # counts (as_ps, as_pns, ...) to compute accuracy, precision, ...
    # See the learning-4 slide deck.

    # DO *NOT* CHANGE THE CODE BELOW

    print("In the test set, there are"\
          " {:d} spam emails and"\
          " {:d} not-spam emails.".format(
              s_c, ns_c))

    print()

    print("Of the {:d} spam emails,"\
          " {:d} were delivered to the spam folder"\
          " and {:d} were delivered to Inbox.".format(
              s_c, as_ps, as_pns))

    print("Of the {:d} not-spam emails,"\
      " {:d} were delivered to the spam folder"\
      " and {:d} were delivered to Inbox.".format(
          ns_c, ans_ps, ans_pns))

    print()


    print("{:<10} {:.2f}".format("Accuracy", accuracy))
    print("{:<10} {:.2f}".format("Precision", precision))
    print("{:<10} {:.2f}".format("Recall", recall))
    print("{:<10} {:.2f}".format("F1", f1))
