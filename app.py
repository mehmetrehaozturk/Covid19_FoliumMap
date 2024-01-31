import os
from flask import Flask, send_file

curr_workdir = os.getcwd()
html_file_path = os.path.join(curr_workdir, "CoronaWorldMap.html")

app = Flask(__name__)

@app.route('/')
def get_html():
    return send_file(html_file_path)

if __name__ == '__main__':
    app.run(debug=True)
