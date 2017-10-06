from natto import MeCab
from sklearn.feature_extraction.text import TfidfVectorizer
import json


def tokenize(text):
    tokens = []
    with MeCab() as nm:
        for n in nm.parse(text, as_nodes=True):
            # ignore any end-of-sentence nodes
            if not n.is_eos() and n.is_nor():
                # pick up the class of word and lematized word
                klass, word = n.feature.split(",")[0], n.feature.split(",")[-3]
                # if klass in ['名詞', '形容詞', '形容動詞', '動詞']:
                if klass in ['名詞']:
                    tokens.append(word)

    return tokens


def is_bigger_than_min_tfidf(term, terms, tfidfs):
    if tfidfs[terms.index(term)] > 0.03 and term.isdigit() is False and len(
            term) > 1:
        return True
    return False


def featured_words(json_data):
    train_data = []
    # Only accept the response json from Azure Search
    for value in json_data["value"]:
        train_data.append(value["content"])
    # Apply mecab and calculate tf-idf for each word and each document
    vectorizer = TfidfVectorizer(tokenizer=tokenize)
    train_matrix = vectorizer.fit_transform(train_data)
    # Get the name from number
    terms = vectorizer.get_feature_names()
    # Calculate the mean tf-idf value for each word from all documents
    tfidfs = train_matrix.mean(axis=0).tolist()
    word_and_score = []
    for term in terms:
        if is_bigger_than_min_tfidf(term, terms, tfidfs[0]):
            word_and_score.append({
                "word": term,
                "score": tfidfs[0][terms.index(term)]
            })
    sorted_word_and_score = sorted(
        word_and_score, key=lambda x: x['score'], reverse=True)
    return sorted_word_and_score
