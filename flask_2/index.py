from flask import Flask, render_template

app = Flask(__name__, template_folder='template')  # still relative to module

@app.route('/')
def index():
    return render_template('/index.html')

 
if __name__ == '__main__':
    app.debug = True
    app.run(host="localhost", port=5000)