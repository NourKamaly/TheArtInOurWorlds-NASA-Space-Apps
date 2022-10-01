from flask import Flask, render_template, render_template_string, request
import joblib
import pandas as pd
from datetime import datetime
import numpy as np
import pandas as pd
import warnings
import joblib
from datetime import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import time
cred = credentials.Certificate("Backend/NaSa/privatekey.json")
firebase_admin.initialize_app(cred)
warnings.filterwarnings("ignore")


app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


searchKeyword = 'null'
Documents = {
    'key1': {'name': 'value_1'},
    'key2': {'name': 'value_2'}
}


@app.route('/predict', methods=['GET'])
def SearchResult():
    searchKeyword = request.args.get('searchkeyword')
    # use this searchKeyword in your models
    # Write your code here
    db = firestore.client()
    doc_id = db.collection('Search').document().id
    doc_ref = db.collection(u'search').document(doc_id).set({
        u'searchKeyword': searchKeyword,
        u'result': None
    })

    doc = db.collection(u'search').document(doc_id).get().to_dict()
    while doc['result'] == None:
        time.sleep(5)
        doc = db.collection(u'search').document(doc_id).get().to_dict()
    else:
        return render_template('index.html', Documents=doc)

    # pass one or more Dictionary as i did in this function in the next line


if __name__ == '__main__':
    app.run(debug=True)
