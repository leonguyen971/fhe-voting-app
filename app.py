from flask import Flask, request, render_template, redirect
import json
from fhe_utils import encrypt_vote, decrypt_vote

app = Flask(__name__)

VOTE_FILE = 'votes.json'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/vote', methods=['POST'])
def vote():
    name = request.form['candidate']
    encrypted = encrypt_vote(name)

    with open(VOTE_FILE, 'r+') as f:
        votes = json.load(f)
        votes.append(encrypted)
        f.seek(0)
        json.dump(votes, f)
    
    return redirect('/thanks')

@app.route('/thanks')
def thanks():
    return "✅ Cảm ơn bạn đã bỏ phiếu!"

@app.route('/result')
def result():
    with open(VOTE_FILE, 'r') as f:
        encrypted_votes = json.load(f)
    
    results = {}
    for ev in encrypted_votes:
        plain = decrypt_vote(ev)
        results[plain] = results.get(plain, 0) + 1

    return results

if __name__ == '__main__':
    app.run(debug=True)
