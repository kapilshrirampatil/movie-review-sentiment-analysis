# -*- coding: utf-8 -*-
from pathlib import Path
import pandas as pd
import numpy as np
import re
import contractions
import sys




def read_data(data_path):
    df = pd.read_csv(data_path)
    return df

def remove_html_tags(x):
    text = re.sub('<.+>','',x)
    return text

def remove_links(x):
    pattern = 'https?://\S*|www\.\S*'
    text = re.sub(pattern,'',x)
    return text

def perform_data_cleaning(df):
    df.drop_duplicates(inplace=True)
    df['text'] = df['text'].apply(remove_html_tags)
    df['text'] = df['text'].apply(remove_links)
    df['text'] = df['text'].str.lower()
    df['text'] = df['text'].apply(lambda x:contractions.fix(x))
    return df

def save_data(df,output_path):
    df.to_csv(output_path +'/cleaned_reviews.csv',index=False)

def main():
    current_dir = Path(__file__)
    home_dir = current_dir.parent.parent.parent
    input_file = sys.argv[1]
    data_path = home_dir.as_posix() + input_file
    output_path = home_dir.as_posix() + '/data/cleaned_data'
    
    data = read_data(data_path)
    df = perform_data_cleaning(data)
    save_data(df,output_path)

if __name__ == '__main__':
    main()
