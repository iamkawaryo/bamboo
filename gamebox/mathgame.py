import random,time
from flask import render_template, session
import node_list

def mathgame_logic(num1, num2, user_ans, count):

# user_ansを整数に変換
    try:
        user_ans = int(user_ans)
    except ValueError:
        return render_template("mathgame.html", num1=num1, num2=num2, count=count, message="数値を入力してください！")

    ans = num1 + num2 #答えの生成

    if ans == user_ans:
        count += 1
        if count < 10:
            num1 = random.randint(1, 30)
            num2 = random.randint(1, 30)
            return render_template("mathgame.html", num1=num1, num2=num2, count=count, message="正解！")
        else:
            end_time = time.time()  # タイマーストップ
            start_time = session.get('start_time',0)#スタート時間の取得
            score = end_time - start_time  # スコアの計算
            formated_score =  f"{score:.5f}"#スコアを小数点第5位までに指定

            name = session.get('name')#名前の取得

            return render_template("mathgame_result.html", score = formated_score, name = name)  # 結果を表示するテンプレート
    else:
        return render_template("mathgame.html", num1=num1, num2=num2, count=count, message="間違い！")
