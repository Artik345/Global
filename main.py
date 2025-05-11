from flask import Flask, render_template, request
from app import get_random_answer

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')          
@app.route("/answer")  
def answer():
    top = request.args.get("top","")
    result = get_random_answer(top)
    return render_template('answer.html', answer = result)


if __name__ == "__main__":
    app.run(debug=True)