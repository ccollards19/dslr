#!/usr/bin/env python3
import csv
import time 
import argparse 
import pandas as pd
import matplotlib.pyplot as plt

HOUSES = ["Ravenclaw", "Hufflepuff", "Slytherin", "Gryffindor"]
COLORS = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"]

class Dataset:

    def __init__(self, file_path : str):
        self.df = pd.read_csv(file_path, index_col=0)

    def plot(self):
        _, axes = plt.subplots(3, 5,figsize=(15, 10))
        i = 0
        for course in self.df.loc[:, "Arithmancy":]: 
            for house, color in zip(HOUSES, COLORS):
                temp_df = self.df[self.df["Hogwarts House"] == house]
                axes[i//5,i%5].hist(temp_df[course], color=color, alpha=0.5, edgecolor='black', label=house)
            axes[i//5,i%5].legend(title="House")
            axes[i//5,i%5].set_title(f"{course}")
            i+=1
        plt.tight_layout()
        plt.savefig("hist")
        plt.show()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input', type=Dataset, help='input file')
    args = parser.parse_args()
    if args.input :
        args.input.plot()

if __name__ == "__main__" :
    main()
