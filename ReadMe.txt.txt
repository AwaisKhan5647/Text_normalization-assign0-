This ReadMe file contains the code explaination to perform 6 different types of normalizations including [case folding, stemming, stopword, punctuation removal, numeric removal and special character removal]  ]


Setup:
Install nltk library by using: "pip install nltk"
Download the stopwords corpus by running nltk.download('stopwords') in Python


Files:
Homework0_awais.py: Main script that normalizes the text file
file.txt: contain the text on which preprocessing/normalization needs to applied.



Examples of how to run the code:
    python Homework0_awais.py file.txt --lower: For case folding normalization only
    python Homework0_awais.py file.txt --stem:  For stemming normalization only
    python Homework0_awais.py file.txt --stop:  For stopword removal normalization only
    python Homework0_awais.py file.txt --removepunct:  For punctuation removal normalization only
    python Homework0_awais.py file.txt --numeric:  For numeric removal normalization only
    python Homework0_awais.py file.txt --specialchars:  For special character removal normalization only

Example to run more than one normalizations:
    python Homework0_awais.py myfile.txt --lower --stem : Perform case folding and stemming
    python Homework0_awais.py myfile.txt --lower --stem --stop: Perform case folding, stemming, and stopword removal

The result could contain to many values to increase the readability of the result we can store the result into text file as below: 
python Homework0_awais.py myfile.txt --lower --stem > log.txt




For further information please email @ awaiskhan@oakland.edu.