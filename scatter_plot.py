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
        print(self.df)
        self.df.update((temp_df - temp_df.mean()) / temp_df.std())
        print(self.df)
        melt_df = self.df.melt(id_vars="Hogwarts House", value_vars=temp_df.columns, var_name="Class", value_name="Score")
        print(melt_df)
        sns.catplot(melt_df, y="Class", x="Score", hue="Hogwarts House", alpha=0.5, aspect=2.5, jitter=0.3 )
        plt.savefig("scatter")
        plt.show()


def main():
    parser = argparse.ArgumentParser("describe.py")
    parser.add_argument('input', type=Dataset, help='input file')
    args = parser.parse_args()
    if args.input :
        args.input.plot()

if __name__ == "__main__" :
    main()
