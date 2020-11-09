from flask import Flask, render_template, jsonify, request
import requests
from pymongo import MongoClient

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/project', methods=['POST'])
def post_project():
    title_receive = request.form['title_give']
    print(title_receive)
    return jsonify({'result': 'success', 'msg': '저장 완료!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)