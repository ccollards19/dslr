import pandas as pd
import numpy as np

def normalised_sigmoid_function(x):
    if x >= 0:
        z = np.exp(-x)
        return 1 / (1 + z)
    else:
        z = np.exp(x)
        return z / (1 + z)

class LogisticRegression:

    def __init__(self, weights=None):
        self.weights = weights
        
    def train(self, dataset, results, epochs, lrates):
        results = pd.get_dummies(results).astype(int)
        if self.weights is None:
            self.weights = pd.DataFrame(index=results.columns, columns=dataset.columns)
            self.weights = self.weights.fillna(0.0)
        print(self.weights)
        for i in range(epochs):
            logits = dataset.dot(self.weights.T)
            probs = logits.map(normalised_sigmoid_function)
            loss = results * np.log(probs) + (1 - results) * np.log(1 - probs)
            error = probs - results
            gradient = error.T.dot(dataset) / len(dataset) * lrates
            self.weights -= gradient
            self.loss = loss.mean()
            #print(f"===Loss===\n{self.loss}\n===Weights===\n{self.weights}")
        return self.weights

    def predict(self, dataset):
        dataset["Bias"] = 1
        logits = dataset.dot(self.weights.T)
        probs = logits.map(normalised_sigmoid_function)
        results = probs.T.idxmax()
        return(results)

