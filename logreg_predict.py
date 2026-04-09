#!/usr/bin/env python3
import argparse 
import math 
import pandas as pd
from sklearn.metrics import accuracy_score
from logistic_regression import LogisticRegression as lr


class Dataset:

    def __init__(self, file_path : str):
        self.df = pd.read_csv(file_path, index_col=0)
        try :

            self.num_df = self.df.drop( "Hogwarts House", axis=1)
            self.num_df = self.num_df.select_dtypes(include='number')
            print(self.num_df.shape)
            self.num_df = self.num_df.fillna(self.num_df.mean())
            self.num_df = (self.num_df - self.num_df.mean()) / self.num_df.std()
            self.num_df["Bias"] = 1
        except Exception as e:
            print(f"||||||||{e}|||||||||")
            raise argparse.ArgumentTypeError("failed to process dataset")


class Weights:

    def __init__(self, file_path : str):
        self.df = pd.read_csv(file_path, index_col=0)

def main():
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('input', type=Dataset, help='input file')
        parser.add_argument('weights', type=Weights, help='weight file')
        args = parser.parse_args()
        if args.input and args.weights:
            # print(args.input.num_df)
            # print(args.weights.df)
            model = lr(weights=args.weights.df)
            ret = model.predict(args.input.num_df)
            ret.index.name = "student"
            ret.name = "House Prediction"
            # print(ret)
            # print(f"Accuracy: {accuracy_score(args.input.df['Hogwarts House'], ret)}")
            ret.to_csv("houses.csv")
    except Exception as e:
        print(e)


if __name__ == "__main__" :
    main()

