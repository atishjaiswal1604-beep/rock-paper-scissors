from flask import Flask, render_template, request
import random

app = Flask(__name__)

choices = ["rock", "paper", "scissors"]

def get_result(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "You win!"
    else:
        return "You lose!"

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    user = None
    computer = None

    if request.method == "POST":
        user = request.form["choice"]
        computer = random.choice(choices)
        result = get_result(user, computer)

    return render_template("index.html", result=result, user=user, computer=computer)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
