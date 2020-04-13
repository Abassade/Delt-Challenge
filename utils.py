from flask import jsonify
class Response:
    def success(self, data):
        response = jsonify({
            'error': False,
            'news': data
        })
        response.status_code = 200
        return response

    def bad_request(self, message):
        response = jsonify({
            'error': True,
            'response': message
        })
        response.status_code = 400
        return response
    
    def not_found(self, message):
        response = jsonify({
            'error': True,
            'response': message
        })
        response.status_code = 404
        return response
    
    def internal_server_error(self, message):
        response = jsonify({
            'error': True,
            'response': message
        })
        response.status_code = 500
        return response
    
class Constant:
    def news_temp(self, each_news):
        return {
            'ranking': each_news['rank'],
            'title': each_news['title'],
            'content': each_news['content'],
            'reference': each_news['url']
        }
        
    def get_ranking(self, cont, keys):
        counter = 0
        if cont is not None:
            cont = cont.lower()
            cont_arr = cont.split(' ')
            total_words = len(cont_arr)
            for k in keys:
                k = k.lower()
                for con in cont_arr:
                    if con == k:
                        counter = counter+1
                       
            rank = (counter/total_words) * 10
            return round(rank, 2)
        return 0
    
    def get_my_key(self, obj):
        return obj['ranking']