from flask import Flask,request,session,url_for,render_template

from flask_socketio import SocketIO

app=Flask(__name__)

app.secret_key="hie"

socketio=SocketIO(app)

@app.route("/",methods=["POST","GET"])

def main():
    if request.method=="POST":
        print(request.form["username"])
    return render_template("index.html")

if __name__=="__main__":
    socketio.run(app,debug=True)

