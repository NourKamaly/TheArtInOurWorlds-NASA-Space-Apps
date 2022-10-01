from flask import Flask, render_template, render_template_string,request
import joblib
import pandas as pd
from datetime import datetime
import numpy as np
import pandas as pd
import warnings
import joblib
from datetime import datetime
warnings.filterwarnings("ignore")


app = Flask(__name__)


@app.route('/',methods=['GET'])
def home():
    return render_template('index.html')




searchKeyword='null'
Documents = { 
          'key1': {'name': 'value_1'},
          'key2': {'name': 'value_2'}
           }
@app.route('/predict',methods=['GET'])
def SearchResult():
    searchKeyword=request.args.get('searchkeyword')
    #use this searchKeyword in your models
    #Write your code here
    #pass one or more Dictionary as i did in this function in the next line
    return render_template('index.html',Documents=Documents)
    
if __name__=='__main__':
    app.run(debug=True)




