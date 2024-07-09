#page URL is http://127.0.0.1:8888/

from flask import Flask, render_template, request, session, redirect, url_for
import random, time
from mathgame import mathgame_logic
from node_list import Node, LinkedList

app = Flask(__name__)
app.secret_key = 'bamboo'  # セッション用の秘密鍵を設定

@app.route('/')
def start():
    return render_template("home.html")

@app.route("/home", methods=["GET"])
def home():
    return render_template("home.html")

@app.route("/mathgame_home", methods=["GET"])
def mathgame_home():
    return render_template("mathgame_home.html")

@app.route("/mathgame", methods=["GET"])
def mathgame():
    start_time = time.time()  # タイマースタート
    num1 = random.randint(1, 30)
    num2 = random.randint(1, 30)
    session['start_time'] = start_time #セッションに開始時間を保存
    session['num1'] = num1  # セッションにnum1を保存
    session['num2'] = num2  # セッションにnum2を保存
    session['count'] = 0  # 初期のカウントをセッションに保存
    session['name'] = request.args.get('name')
    return render_template("mathgame.html", num1=num1, num2=num2)

@app.route("/start_mathgame", methods=["GET"])
def start_mathgame():
    num1 = session.get('num1', 0)
    num2 = session.get('num2', 0)
    user_ans = int(request.args.get('user_ans', 0))  # ユーザー入力を取得
    count = session.get('count')  # セッションからカウントを取得

    rendered_template = mathgame_logic(num1, num2, user_ans, count)
    
    # 数値を取り出してセッションを更新
    if "正解！" in rendered_template:
        session['num1'] = random.randint(1, 30)
        session['num2'] = random.randint(1, 30)
        session['count'] = count + 1
        return redirect(url_for('start_mathgame'))
    elif "間違い！" in rendered_template:
        return rendered_template
    else:
        return rendered_template

if __name__ == "__main__":
    app.run(debug=True, port=8888)
