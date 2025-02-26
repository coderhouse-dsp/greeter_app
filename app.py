from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def greet():
    if request.method == "POST":
        name = request.form["name"]
        return render_template("index.html", greeting=f"Hello, {name}!")
    return render_template("index.html", greeting="")

if __name__ == "__main__":
    app.run(debug=True)