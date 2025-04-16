from flask import *
import atexit
from json import *

app = Flask(__name__)

chat_list = []

def exit_run():
    content = dumps(chat_list)
    with open("saved.json","w")as f:
        f.write(content)

@app.route('/')
def index():
    return "Welcome to Teleground"

@app.route('/chat/',methods=['GET','POST'])
def chat():
    if request.method == 'GET':
        return render_template("chat.html",chat_list=chat_list)
    else:
        content = request.form.get("content")
        print(content)
        chat_list.append(content)
        exit_run()
        return redirect("/chat/")
if __name__ == '__main__':
    app.run('0.0.0.0',8000,True)