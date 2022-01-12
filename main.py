import json

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def welcome():
    return "Hello Word"


# 解析GET请求
@app.route("/get")
def compute():
    a = request.args.get("a")
    b = request.args.get("b")
    c = int(a) + int(b)
    if c > 100:
        d = jsonify(code=400, type="null")
        return d
    else:
        d = jsonify(code=200, type=c)
        return d


# 解析POST请求
@app.route("/data1", methods=["POST"])
def check():
    a = request.form["a"]
    b = request.form["b"]
    c = int(a) + int(b)
    return str(c)


# 同时解析GET和POST
@app.route("/gather", methods=["GET", "POST"])
def gather():
    if request.method == "POST":
        print("request.form=",request.form)
        a = request.form.get("a")
        b = request.form.get("b")
        return "POST"
    else:
        print("request.form=", request.form)
        a = request.args.get("a")
        b = request.args.get("b")
        return "GET"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
