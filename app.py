import time
import pandas as pd
import numpy as np
import redis

from flask import Flask, render_template

app = Flask(__name__)
cache = redis.Redis(host="redis", port=6379)


@app.route("/")
def home():
    dates = pd.date_range("20130101", periods=6)
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
    return render_template(
        "home.html", tables=[df.to_html(classes="data", header="true")]
    )


if __name__ == "__main__":
    app.run(debug=True)
