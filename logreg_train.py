#!/usr/bin/env python3
import argparse 
import pandas as pd
from logistic_regression import LogisticRegression as lr

LRATES = 0.2
EPOCHS = 500


class Dataset:

    def __init__(self, file_path : str):
        self.df = pd.read_csv(file_path, index_col=0)
        try :
            self.num_df = self.df.select_dtypes(include='number')
            self.num_df = self.num_df.fillna(self.num_df.mean())
            self.num_df = (self.num_df - self.num_df.mean()) / self.num_df.std()
            self.num_df["Bias"] = 1
        except Exception as e:
            print(f"||||||||{e}|||||||||")
            raise argparse.ArgumentTypeError("failed to process dataset")


def main():
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('input', type=Dataset, help='input file')
        args = parser.parse_args()
        if args.input:
            model = lr()
            weights = model.train(args.input.num_df, args.input.df["Hogwarts House"], EPOCHS, LRATES)
            print(f"===Loss===\n{model.loss}\n===Weights===\n{weights}")
            weights.to_csv("weights.csv")
    except Exception as e:
        print(e)

if __name__ == "__main__" :
    main()


