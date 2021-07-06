from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/profile/<string:user_name>')
def profile(user_name):
    return '{name}さんのプロフィール画面です'.format(name=user_name)

@app.route('/info')
def info():
    return 'This Web site is for test.'

if __name__ == '__main__':
    app.run()