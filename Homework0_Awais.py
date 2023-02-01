import argparse
from collections import Counter
import re
# import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

def Homework0_awais(file, lower=False, stem=False, stop=False, specialchars=False, numeric=False, removepunct=False):
    with open(file, 'r') as f:
        text = f.read()

    # Case folding
    if lower:
        text = text.lower() # convert the text into lower case
        
    # Tokenize
    tokens = text.split() # extract the words as tokens from the text file.
   
    # Stopword removal
    if stop:
        # mystops = ["a","an","the","for","but","so","on"]  # for using own stop words.
        mystops= stopwords.words('english') # use nltk corpus for stopwords.
        stop_words = set(mystops)
        tokens = [token for token in tokens if token not in stop_words]

    # Stemming
    if stem:
    #    tokens = [token[:-1] if token.endswith('s') else token for token in tokens] # remove the words ending with 's' or we can set our own ending with 'ing' and 'ed'
         stemmer = PorterStemmer()
         tokens = [stemmer.stem(token) for token in tokens]
    
    # Remove punctuation   
    if removepunct:
        tokens = re.sub(r'[^\w\s]', '', text)
    
    # Remove numeric values    
    if numeric:
        tokens = re.sub(r'\d+', '', text)
     
    # Remove special characters    
    if specialchars:
        tokens = re.sub(r'[^a-zA-Z0-9]', '', text)

    # Normalize
    tokens = [re.sub(r'\W+', '', token) for token in tokens]
    tokens = [token for token in tokens if token]

    # Count tokens
    token_counts = Counter(tokens)

    # Sort by frequency
    sorted_tokens = sorted(token_counts.items(), key=lambda x: x[1], reverse=True)

    return sorted_tokens

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Normalize text file')
    parser.add_argument('file', type=str)
    parser.add_argument('--lower', action='store_true')
    parser.add_argument('--stem', action='store_true')
    parser.add_argument('--stop', action='store_true')
    parser.add_argument('--removepunct', action='store_true')
    parser.add_argument('--numeric', action='store_true')
    parser.add_argument('--specialchars', action='store_true')   
    
    
    args = parser.parse_args()

    sorted_tokens = Homework0_awais(args.file, lower=args.lower, stem=args.stem, stop=args.stop)
    for token, count in sorted_tokens:
        print(f'{token} {count}')