from flask import *
import random

application = Flask(__name__)


@application.route('/', methods=['GET', 'POST'])
def Calculator():
    if request_method == "POST":
        friendship_percent = random.randint(1, 101)
        friendship_percent = str(friendship_percent)
        return render_template('calculator.html', friendship=(friendship_percent + "%"))
    else:
        return render_template('calculator.html')


if __name__ == "__main__":
    application.run(debug=True)
