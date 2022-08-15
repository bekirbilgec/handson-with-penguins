from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello'

@app.route('/second')
def second():
    return 'Hello Penguins'

@app.route('/third/subthird')
def third():
    return 'Hello subthird'    


@app.route('/forth/<float:id>')
def forth(id):
    return f'merhaba{id}'



if __name__ == '__main__':
    app.run(debug=True, port=2000) # default 5000
    
    
    