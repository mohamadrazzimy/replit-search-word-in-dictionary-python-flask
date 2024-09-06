from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_wordlist')
def get_wordlist():
    with open('1-1000.txt', 'r') as file:
        wordlist = file.read().splitlines()
    return jsonify(wordlist)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)