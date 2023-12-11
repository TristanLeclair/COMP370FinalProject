import argparse
from pathlib import Path
import numpy as np
import json
import pandas as pd

def main():
    df = pd.read_csv(Path('complete.tsv'), sep='\t')
    df = df[['title', 'description', 'final movie', 'final topic']]
    # drop last row since it's empty
    df = df[:-1]
    N = len(df) # for idf we use the original number of articles collected
    # drop rows where final movie is NR or NM as these do not contain a topic as defined in our typology
    df = df[df['final movie'] != 'NR']
    df = df[df['final movie'] != 'NM']

    # get all topics
    topics = df['final topic'].unique()

    punctuations = "()[],-.?!:;#&"
    with open('stopwords.txt') as f:
            stopwords = f.read().splitlines()
    word_counts = {}
    for t in topics:
        word_counts[t] = {}

        words = df[df['final topic'] == t]['description'].str.lower() + " " + df[df['final topic'] == t]['title'].str.lower()
        # Remove punctuation
        for punct in punctuations:
            words = words.str.replace(punct, '')
        # Split the words into a list
        words = words.str.split()
        # Loop through the words
        for line in words:
            for word in line:
                # If the word is already in the dictionary, add 1 to its count
                if word in word_counts[t]:
                    word_counts[t][word] += 1
                # If the word is not in the dictionary, set its count to 1
                else:
                    word_counts[t][word] = 1
        # Remove stopwords
        for stopword in stopwords:
            if stopword in word_counts[t]:
                del word_counts[t][stopword]

    # now compute tf-idf
    tf_idf = {}
    for t in topics:
        tf_idf[t] = {}
        for word in word_counts[t]:
            tf_idf[t][word] = word_counts[t][word] * np.log(N / (sum([1 for topic in topics if word in word_counts[topic]])))
    # sort by tf-idf
    for t in topics:
        tf_idf[t] = {k: v for k, v in sorted(tf_idf[t].items(), key=lambda item: item[1], reverse=True)}
    #print(tf_idf)
    # get top 10 words with tf-idf values
    for t in topics:
        tf_idf[t] = list(tf_idf[t].keys())[:10]

    # to get the values as well
    #tf_idf = {k: dict(list(v.items())[:10]) for k, v in tf_idf.items()}

    # save in json file
    # change file output name if outputting values as well
    with open('tfidf_words.json', 'w') as outfile:
        json.dump(tf_idf, outfile)

    
    

if __name__ == '__main__':
    main()