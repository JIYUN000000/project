from flask import Flask
import random

app = Flask(__name__)

number = random.randint(0,9)
print(number)

@app.route("/")
def hello_world():
    return ("<h1>Guess a number between 0 and 9</h1>"
            "<img src = 'https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExbGRwOXRuNzhma2drazFubTNtanlxNXF0YjltcTViemtibGMxd2hhdSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7aCSPqXE5C6T8tBC/giphy.gif'>")

@app.route("/<int:user_num>")
def check_number(user_num):
    if number == user_num:
        return "You found me!"
    elif number < user_num:
        return "Too high, try again!"
    else:
        return "Too low, try again!"



if __name__ == "__main__":
    app.run(debug=True)
