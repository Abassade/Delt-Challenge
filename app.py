from flask import Flask, jsonify, request, abort
from flask_pymongo import PyMongo
from nltk.tokenize.treebank import TreebankWordDetokenizer
import requests
import json
import os
from utils import Response, Constant

app = Flask(__name__)
DB_URL = os.environ.get('DATABASE_URL')
app.config["MONGO_URI"] = DB_URL
mongo = PyMongo(app)

response = Response()
constant = Constant()

@app.route('/')
def home():
    """
    This is the base endpoint (GET) HTTP
    """

    return response.success(data='welcome to deltai search engine')

@app.route('/api/news', methods=['POST'])
def search_news():
    """
    This endpoint is a (POST) HTTP method, it takes a json that consists
    of a key value pair - keywords that holds an array of non empty
    keyword of type string. sample is shown below
    {
        "keywords": [ "one", "two", "three" ]
    }
    """
 
    query_input = request.get_json()
    array_input = query_input['keywords']
    
    if(not query_input or not array_input):
        return response.bad_request(message='not a valid input')
        
    if(type(array_input) != list):
        return response.bad_request(message='the keywords is of type array')
    
    if(array_input[0].strip() == ''):
        return response.bad_request(message='array must contain a non empty string')
    
    detokenized_words = TreebankWordDetokenizer().detokenize(array_input)
    identifier = '_'.join(array_input)
    identifier = identifier.lower()
    news_holder = []
    identifier = str(identifier)
    query = { "identifier": identifier }
    not_included = { "_id": 0, "identifier": 0}
    try:
        news_from_db = mongo.db.news.find(query, not_included)
        if news_from_db:
            for obj in news_from_db:
                news_holder.append(obj)
            if len(news_holder) > 0:
                news_holder.sort(key=constant.get_my_key, reverse=True)
                print('!!!!!!! got data from db !!!!!!!')
                return response.success(data=news_holder)
    except Exception as err:
        print(err)
        return response.internal_server_error(message=f'error occured while querying from db - {err}')
    print('!!!!!!!! got data from internet !!!!!!!!!!!')
    return get_news_from_internet(detokenized_words, identifier, array_input)

def get_news_from_internet(keywords, identifier, array_input):
    """
    This function gets news from the third party API (https://newsapi.org/)
    It recieves the keywords to search and returns a json which includes the respone
    """

    API_KEY=os.environ.get('API_KEY')
    news_api = f'https://newsapi.org/v2/everything?q={keywords}&apiKey={API_KEY}'
    filtered_news = []
    try:
        resp = requests.get(news_api)
        resp = resp.json()
        if resp['status'] == 'ok':
            needed_news = resp['articles'][0:3]
            if not len(needed_news) < 1:
                for each_news in needed_news:
                    rank = constant.get_ranking(each_news['content'], array_input)
                    each_news['rank'] = rank
                    obj = constant.news_temp(each_news)
                    try:
                        data = {
                            'identifier': identifier, 
                            'title': obj['title'],
                            'ranking': obj['ranking'],
                            'reference': obj['reference'],
                            'content':obj['content']
                        }
                        mongo.db.news.insert_one(data)
                        print('!!! added news in db !!!!')
                    
                    except Exception as e:
                        print(e)
                        return response.internal_server_error(message=f'cant save to db - {e}')
                    filtered_news.append(obj)
                    filtered_news.sort(key=constant.get_my_key, reverse=True)
                return response.success(data=filtered_news)
            return response.not_found(message='no news found')
        return response.internal_server_error(message='finding it hard to retrive news')
                
    except ConnectionError as error:
        return response.internal_server_error(message=error)
    
    
if __name__ == '__main__':
    app.run(host='localhost', port=3000, debug=True)