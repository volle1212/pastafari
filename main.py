from holidays import my_holidays
from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def index():
    day_of_year = datetime.now().timetuple().tm_yday
    if day_of_year == "60" and str(datetime.now().month) == "2":
        return render_template('index.html', holiday=my_holidays[str(400)].replace("th ", "th\n"))
    else:
        return render_template('index.html', holiday=my_holidays[str(day_of_year)].replace("th ", "th\n"))


if __name__ == "__main__":
    print(datetime.now().month)
    app.run(debug=True)
