#!/usr/bin/env python3
import argparse 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class Dataset:

    def __init__(self, file_path : str):
        self.df = pd.read_csv(file_path, index_col=0)

    def plot(self):
        temp_df = self.df.loc[:, "Arithmancy":]
        self.df.update((temp_df - temp_df.mean()) / temp_df.std())
        sns.pairplot(self.df, hue="Hogwarts House")
        print(temp_df)
        print(self.df)
        plt.savefig("pair")
        plt.show()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input', type=Dataset, help='input file')
    args = parser.parse_args()
    if args.input :
        args.input.plot()

if __name__ == "__main__" :
    main()

