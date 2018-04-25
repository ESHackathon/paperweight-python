from flask import Flask, jsonify, request
from rake_nltk import Rake


app = Flask(__name__)

@app.route('/', methods=["POST"])
def extract_keyword():
    if request.method == "POST":
        json_dict = request.get_json()

        abstracts = [publication["abstract"] for publication in json_dict["publications"]]
        abstracts = list(filter(None, abstracts))

        data = extract_keywords(abstracts)
        data = [array[:5] for array in data]
        data = [item for sublist in data for item in sublist]
        data = {"keywords": data}

        return jsonify(data)
    else:
        return """<html><body>
        Something went horribly wrong
        </body></html>"""

def extract_keywords(abstracts):
    # Takes in an array of abstracts and performs keyword extraction on each
    processed = []
    for abstract in abstracts:
        rake = Rake()
        rake.extract_keywords_from_text(abstract)
        processed.append(rake.get_ranked_phrases())
    return processed


