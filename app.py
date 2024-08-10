from flask import Flask, request, jsonify
import pandas as pd
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

# 仮のデータとモデル
data = pd.DataFrame({'task': ['task1', 'task2'], 'duration': [5, 3]})
model = LinearRegression().fit(data[['duration']], [1, 2])  # ダミーのモデル

@app.route("/schedule", methods=["POST"])
def generate_schedule():
    tasks = request.json.get("tasks", [])
    # ここでAIやアルゴリズムを使ってスケジュールを生成
    schedule = [{"task": task, "time": model.predict([[1]])[0]} for task in tasks]
    return jsonify(schedule)

if __name__ == "__main__":
    app.run()
