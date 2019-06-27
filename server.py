from flask import Flask, request, jsonify
import pickle
import pandas as pd


app = Flask(__name__)

nmf_features = pd.read_csv('nmf_features').set_index('wine_id')


@app.route('/api', methods=['POST'])
def predict():

    # get wine_id to compute similarity
    wine_id_map = request.get_json(force=True)

    # extract wine_id from nmf_features
    wine = nmf_features.loc[wine_id_map['wine_id']]

    # compute similarity of wine with other wines
    similarities = nmf_features.dot(wine)

    # return the 5 largest wines with highest cosine similarity
    return jsonify(similarities.nlargest().to_dict())


if __name__ == '__main__':
    app.run(debug=True)






