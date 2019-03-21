from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world"

if __name__ == '__main__':
    #デフォルトだと127.0.0.1のローカルでリッスンしているため外部からアクセスできない
    #hostに0.0.0.0を適用, ポートに80番を適用
    app.run(debug=False, host='0.0.0.0', port=80)