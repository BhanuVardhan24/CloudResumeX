from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    return render_template_string(open("index.html").read())

if __name__ == "__main__":
    app.run()
