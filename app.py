from flask import Flask, render_template, jsonify, request
import requests
from pymongo import MongoClient
from datetime import datetime, timedelta

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/project', methods=['POST'])
def post_project():

    title_receive = request.form['title_give']
    start_date = request.form['start_date']
    end_date = request.form['end_date']
    task2_name = request.form['task2_name']
    task1_name = request.form['task1_name']
    task3_name = request.form['task3_name']
    task4_name = request.form['task4_name']
    task5_name = request.form['task5_name']
    task1_progress = request.form['task1_progress']
    task2_progress = request.form['task2_progress']
    task3_progress = request.form['task3_progress']
    task4_progress = request.form['task4_progress']
    task5_progress = request.form['task5_progress']

    doc = {
        'title': title_receive,
        'start_day': start_date,
        'end_day': end_date,
        'task1_name': task1_name,
        'task1_progress': task1_progress,
        'task2_name': task2_name,
        'task2_progress': task2_progress,
        'task3_name': task3_name,
        'task3_progress': task3_progress,
        'task4_name': task4_name,
        'task4_progress': task4_progress,
        'task5_name': task5_name,
        'task5_progress': task5_progress
    }

    db.myprojects.insert_one(doc)

    # time_present = datetime.now()
    # # end_time = datetime() #end_date를 datetime 패키지 안에 변환
    # left_day = end_date - time_present
    #
    # progress = [task1_progress, task2_progress, task3_progress, task4_progress, task5_progress]
    # for score in progress:
    #     total += score
    # average = progress / len(progress)

    print(title_receive)

    return jsonify({'result': 'success', 'msg': '저장 완료!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
