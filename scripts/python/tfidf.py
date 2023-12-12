import argparse
from pathlib import Path
import numpy as np
import json
import pandas as pd

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', required=True, help='Path to tsv input file')
    parser.add_argument('-o', '--output', required=True, help='Path to json output file')
    args = parser.parse_args()

    df = pd.read_csv(Path(args.input), sep='\t')
    df = df[['title', 'description', 'final movie', 'final topic']]
    # drop last row since it's empty for our specific input file
    df = df[:-1]
    
    # drop rows where final movie is NR or NM as these do not contain a topic as defined in our typology
    df = df[df['final movie'] != 'NR']
    df = df[df['final movie'] != 'NM']
    N = len(df) # numbers of articles with a valid topic

    # get all topics
    topics = df['final topic'].unique()

    punctuations = "()[]/,-.?!:;#&"
    with open('stopwords.txt') as f:
            stopwords = f.read().splitlines()
    article_text = pd.DataFrame() # to store the words of each article
    word_counts = {}
    for t in topics:
        word_counts[t] = {}

        words = df[df['final topic'] == t]['description'].str.lower() + " " + df[df['final topic'] == t]['title'].str.lower()
        # Remove punctuation
        for punct in punctuations:
            words = words.str.replace(punct, '')
        # replace single quotes with a space
        words = words.str.replace("'", ' ')
        # also replace double quotes
        words = words.str.replace('"', '')
        # still need to remove the \u2018 and \u2019
        words = words.str.replace('\u2018', '')
        words = words.str.replace('\u2019', '')

        # Split the words into a list
        words = words.str.split()
        # append words to article_text
        article_text = pd.concat([article_text, words], axis=0, ignore_index=True)

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
        # word needs count at least 2
        word_counts[t] = {k:v for (k,v) in word_counts[t].items() if v >= 2}


    # now compute tf-idf
    tf_idf = {}
    for t in topics:
        tf_idf[t] = {}
        for word in word_counts[t]:
            # need to calculate in how many articles the word appears
            num_articles = sum([1 for article in article_text[0] if word in article])
            tf_idf[t][word] = word_counts[t][word] * np.log(N / num_articles)
    # sort by tf-idf
    for t in topics:
        tf_idf[t] = {k: v for k, v in sorted(tf_idf[t].items(), key=lambda item: item[1], reverse=True)}

    # get top 10 words with tf-idf values
    for t in topics:
        tf_idf[t] = list(tf_idf[t].keys())[:10]

    # to get the values as well, need to comment out above
    #tf_idf = {k: dict(list(v.items())[:10]) for k, v in tf_idf.items()}

    # save in json file
    with open(Path(args.output), 'w') as outfile:
        json.dump(tf_idf, outfile)

    
    

if __name__ == '__main__':
    main()
