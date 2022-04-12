"""Storage module for app"""
import logging
from uuid import uuid4

import requests
from flask import Flask, render_template, url_for, request

app = Flask(__name__)


@app.route("/home/")
@app.route("/")
def main_page() -> str:
    """
    Main page rout
    """
    return render_template("welcome_page.html")


@app.route("/add_data/", methods=["POST", "GET"])
def add_data() -> str:
    """
    Rout send data for save
    :return: render template
    """
    if request.method == "POST":
        send_data = {key: value for key, value in
                     zip(["_id", "name", "weight", "color"],
                         [str(uuid4()), request.form["name"], request.form["weight"], request.form["color"]])}
        try:
            response = requests.post(
                url="http://172.16.238.5:5001/save-data/",
                json=send_data)
            return render_template("after_filling.html", value=send_data.get("_id"))
        except KeyError as ex:
            logging.error(ex)
    return render_template("add_data_page.html")


if __name__ == '__main__':
    app.run(host='172.16.238.10', port=5000)
