from flask import Flask, render_template, request, session, redirect, url_for
from mysql.connector import connect, Error
from getpass import getpass
from AccountManager import AccountManager
app = Flask(__name__)

app.config["SECRET_KEY"] = 'hackathon'

HOST = 'localhost'
USER = 'root'
print(f"Connecting to [{HOST}] with user [{USER}]")
database_password = "Lego2002"
connection = None

try: 
   
    connection = connect(
        host = "localhost",
        user = "root",
        password = database_password,
        database = 'cob'
    )

except Error as e:
    print(e)

manager = AccountManager(connection)


@app.route("/")
def home():
    if session.get("user") == None:
        return render_template("index.html")
    else:
        return redirect(url_for("dashboard"))

@app.route("/dashboard")
def dashboard():
    if session.get("user") == None:
        return redirect(url_for("home"))

    else:
        print(manager.get_data_from_id(session["user"]))

        return render_template("dashboard.html", first_name = manager.get_data_from_id(session["user"])[1]["first_name"])


@app.route("/register", methods=["POST", "GET"])
def register():

    if request.method == "POST":
        f_name = request.form["first_name"]
        l_name = request.form["last_name"]
        email = request.form["email"]
        password = request.form["password"]

        status = manager.create_account(email,f_name,l_name,password)
        if (status == True):
            return redirect(url_for("home"))
        else:
            print("error")

    return render_template("register.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if session.get("user") == None:
        if request.method == "POST":
            email = request.form["email"]
            password = request.form["password"]

            acc_data = manager.get_account(email, password)
            if acc_data[0] == True:
                session["user"] = acc_data[1]
                return redirect(url_for("dashboard"))
            else:
                print("invalid")


        return render_template("login.html")
    else:
        return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)