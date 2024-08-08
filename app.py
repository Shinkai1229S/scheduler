from flask import Flask, request, jsonify

# Flaskアプリケーションのインスタンスを作成
app = Flask(__name__)

# ルートエンドポイントを定義
@app.route('/')
def index():
    return 'Hello, World!'

# スケジューリング用のエンドポイントを定義
@app.route('/schedule', methods=['POST'])
def schedule():
    data = request.get_json()
    tasks = data.get('tasks', [])
    # スケジューリングロジックをここに記述
    return jsonify({'message': 'Schedule created', 'tasks': tasks})

# メインスクリプトとして実行されたときの処理
if __name__ == '__main__':
    app.run()