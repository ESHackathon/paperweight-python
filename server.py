from flask import Flask, jsonify, request
from rake_nltk import Rake
from keyword_extraction import calculate_keywords
from textrank import text_rank
import nltk


app = Flask(__name__)
nltk.download('averaged_perceptron_tagger')

@app.route('/', methods=["POST"])
def extract_keyword():
    if request.method == "POST":
        json_dict = request.get_json()

        abstracts = [publication["abstract"] for publication in json_dict["publications"]]
        abstracts = list(filter(None, abstracts))

        keywords_data = extract_keywords(abstracts)
        text_rank_data = text_rank(json_dict)
        #  data = [array[:5] for array in data]
        #  data = [item for sublist in data for item in sublist]
        data = {"keywords": keywords_data, "text_rank": text_rank_data}

        return jsonify(data)
    else:
        return """<html><body>
        Something went horribly wrong
        </body></html>"""

def extract_keywords(abstracts):
    # Takes in an array of abstracts and performs keyword extraction on each
    all_abstracts = " ".join(abstracts)
    return calculate_keywords(all_abstracts)
