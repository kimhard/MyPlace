from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello'

if __name__ == '__main__':
    app.run(host = '127.0.0.1', port='5000')
    
# 실행 코드(terminal에 작성)
# python -m test.py
