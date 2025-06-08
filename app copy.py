from flask import Flask,request,redirect,session,url_for,render_template

from flask_socketio import SocketIO

app=Flask(__name__)

app.secret_key="hie"

socketio=SocketIO(app)

@app.route("/",methods=["POST","GET"])

def main():
    if request.method=="POST":
        session['username']=(request.form["username"])
        return render_template("chat.html")

    return render_template("index.html")
@app.route("/chat",methods=["POST","GET"])
def chat():
    if(session.get('username')!=None):
        if request.method=="POST":
            session['message']=request.form['message']
            print(session['message'])
        return render_template("chat.html")


    else:
        print(session.get("username"))
        return redirect(url_for("main"))
if __name__=="__main__":
    socketio.run(app,debug=True)

