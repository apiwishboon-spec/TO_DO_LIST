from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory task list
tasks = []

@app.route("/")
def index():
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add_task():
    task = request.form.get("task")
    deadline = request.form.get("deadline")  # optional HH:MM
    if task:
        tasks.append({"task": task, "deadline": deadline})
    return redirect(url_for("index"))

@app.route("/delete/<int:index>")
def delete_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
