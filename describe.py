#!/usr/bin/env python3
import csv
import argparse 
import pandas as pd


ASKED = ['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max']


class Dataset:

    def __init__(self, file_path : str):
        self.df = pd.read_csv(file_path, index_col=0)
        try :
            self.num_df = self.df.select_dtypes(include='number')
            self.num_df = self.num_df.dropna(axis=1, how='all')
            self.desc_df = self.get_desc_df()
        except Exception as e:
            print(f"||||||||{e}|||||||||")
            raise argparse.ArgumentTypeError("failed to process data")

    def get_desc_df(self):
        desc = pd.DataFrame(index=self.num_df.columns, columns=ASKED)
        for col in self.num_df.columns:
            feature = self.num_df[col]
            count = 0
            total = 0
            min =  float('+inf')
            max = float('-inf')
            for val in feature:
                if pd.isna(val): continue 
                count += 1
                total += val
                if val > max: max = val
                if val < min: min = val
            mean = total / count 
            std = 0
            total = 0
            for val in feature:
                if pd.isna(val): continue 
                total += (mean-val)**2
            std = (total / count)**0.5
            feature = feature.sort_values()
            quart_1 = feature.iloc[int((count - 1) * 0.25)]
            quart_2 = feature.iloc[int((count - 1) * 0.50)]
            quart_3 = feature.iloc[int((count - 1) * 0.75)]
            desc.loc[col] = [count, mean, std, min, quart_1, quart_2, quart_3, max]
        return desc

    def __str__(self) -> str:
        return self.desc_df.to_string()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input', type=Dataset, help='input file')
    args = parser.parse_args()
    if args.input :
        print(args.input)
        #print('|||||||||||||||||||||||||||||||||||||||||||||||||||||||')
        #desc = args.input.num_df.describe()
        #quantile = args.input.num_df.quantile([0.25, 0.5, 0.75], interpolation='lower', numeric_only=True)
        #quantile.index = ['25%', '50%', '75%']
        #desc.loc[['25%', '50%', '75%']] = quantile 
        #print(desc.T)
if __name__ == "__main__" :
    main()
