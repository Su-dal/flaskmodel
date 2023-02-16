 # -- coding: utf-8 --
from flask import Flask # Flask
from flask import request,render_template,jsonify
from flask_restx import Api,Resource
import json
import re
from flask_cors import CORS
#import numpy as np
import os
import sys
import urllib.request
import urllib.parse
from model import summarizer 
from crawler import getapi

app = Flask(__name__)
CORS(app)
api=Api(app, version='1.0', title='API 문서', description='Swagger 문서', doc="/api-docs")
app.config['JSON_AS_ASCII'] = False

test_api = api.namespace('news', description='조회 API')
#test_api.config['JSON_AS_ASCII'] = False
@test_api.route('/<string:name>')
class NewsCrawler(Resource):
    def get(self,name):
        titles,dates,urls,contents=getapi(name,1,1)
        temp=[]
        temp.append(titles)
        temp.append(dates)
        temp.append(urls)
        temp.append(contents)
        keys=['titles','dates','urls','contents']
        ans=dict(zip(keys,temp))
        return jsonify(ans)
#sum_api=api.namespace('summ')
@test_api.route('')
class Summarizer(Resource):
    @test_api.expect({
  "input": {
    "text": "tl즌의 38.8%만 뛰었는데, 연봉이 4배로 뛰었다. 하지만 타선 전반에 걸쳐 큰 우산을 펼쳐줬던 '빅 보이'가 더이상 없다.롯데 자이언츠 외국인 타자 잭 렉스가 처한 입장이다. 올해야말로 팀 타선의 중심 역할을 해줘야한다.팀은 메이저리그 대신 KBO리그에서의 2년차를 택한 그에게 확실한 연봉을 안겨줬다. 시즌 도중에 합류해 연봉 31만 달러에 불과했던 그는 올해 총액 130만 달러에 도장을 찍었다.지난 시즌 성적은 56경기 동안 타율 3할3푼 8홈런 34타점, OPS(출루율+장타율) 0.905. 롯데 관계자는 렉스의 연봉 조건에 대해  마지막 도전에 실패한 뒤 롯데로 돌아온 스트레일리와는 입장이 다른 셈."
  }
})
    def post(self):
        if request.method=='POST':
            request_data=json.loads(request.data)
            print(request_data)
            answ=(request_data['input'])
            to_sum=answ['text']
            res=summarizer(to_sum)
            print(res)
            ##res={"number":answ}
        return  jsonify(res)

@app.route('/summary', methods=["POST"])
def make_prediction():
    if request.method=='POST':
        request_data=json.loads(request.data)
        print(request_data)
        answ=(request_data['input'])
        to_sum=answ['text']
        res=summarizer(to_sum)
        print(res)
        ##res={"number":answ}
    return  jsonify(res)
if __name__ == "__main__":
    app.run(debug = True, host="0.0.0.0",port=5000)