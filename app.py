import psutil
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    Message = None
    if cpu > 80 or mem > 80:
        Message = "Alert! CPU or MEM usage is over 80%"

    return render_template("index.html", cpu=cpu, mem=mem, message=Message)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
