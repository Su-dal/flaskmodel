 # -- coding: utf-8 --
from flask import Flask # Flask
from flask import request,render_template,jsonify
from flask_restx import Api,Resource
import json
import re
#import numpy as np
import os
import sys
import urllib.request
import urllib.parse
#from model import summarizer 

app = Flask(__name__)
api=Api(app, version='1.0', title='API 문서', description='Swagger 문서', doc="/api-docs")
app.config['JSON_AS_ASCII'] = False

test_api = api.namespace('news', description='조회 API')
#test_api.config['JSON_AS_ASCII'] = False
@test_api.route('/<string:name>')
class NewsCrawler(Resource):
    def get(self,name):
        client_id="rUTC2IUA7u9qhE97Azqk"
        client_secret="iCwELByHEx"
        encText=urllib.parse.quote(name)
        url="https://openapi.naver.com/v1/search/news?query="+encText
        request=urllib.request.Request(url)
        request.add_header('X-Naver-Client-Id',client_id)
        request.add_header('X-Naver-Client-Secret',client_secret)
        response=urllib.request.urlopen(request)
        rescode=response.getcode()
        keys=["id","title","link"]
        if(rescode==200):
            response_body=response.read()
            response_body=(response_body.decode('utf-8'))
            d=(json.loads(response_body))
            links=[]
            titles=[]
            tojson=[]
            for i in range(len(d['items'])):
                link = (d['items'][i]['originallink'])
                title=(d['items'][i]['title'])
                temp3=[]
                links.append(link)
                cleanr = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
                cleantext = re.sub(cleanr, '', title)
                cleantext=cleantext.replace(u'\xa0',u'')
                temp3.append(i+1)
                temp3.append(cleantext)
                temp3.append(link)
                titles.append(cleantext)
                ans=dict(zip(keys,temp3))
                tojson.append(ans)
            return jsonify(tojson)
        else:
            print("Error Code:"+rescode)
        # users 데이터를 Json 형식으로 반환한다
            return {"members": [{ "id" : 1, "name" : "yerin" },
                            { "id" : 2, "name" : "dalkong" }]}
@app.route('/summary', methods=["POST"])
def make_prediction():
    if request.method=='POST':
        request_data=json.loads(request.data)
        print(request_data)
        answ=(request_data['input'])
        to_sum=answ['text']
        #res=summarizer(to_sum)
        res={"members": [{ "id" : 1, "name" : "yerin" },
                            { "id" : 2, "name" : "dalkong" }]}
        print(res)
        ##res={"number":answ}
    return  jsonify(res)
if __name__ == "__main__":
    app.run(debug = True, port=5000)