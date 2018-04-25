import nltk

def model_titles(titles):
    # Pass in an array of titles
    joined_titles = ' '.join(titles)
    tokenized_titles = nltk.word_tokenize(joined_titles)



