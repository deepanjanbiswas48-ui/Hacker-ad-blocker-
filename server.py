from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/status')
def status():
    return jsonify({
        "status": "Active",
        "threats_blocked": 1346,
        "engine": "Beast Mode ON"
    })

if __name__ == '__main__':
    # সার্ভারটি ৮০০০ পোর্টে চলবে
    app.run(host='0.0.0.0', port=8000)
