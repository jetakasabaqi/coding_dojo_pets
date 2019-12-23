from flask import Flask, render_template, request, redirect
from sqlconnection import connectToMySQL


app= Flask(__name__)

@app.route("/")
def index():
    mysql = connectToMySQL("pets")
    pets = mysql.query_db("SELECT * from pets;")
    print(pets)
    return render_template('index.html', pets = pets)


@app.route("/create_pet", methods=["POST"])
def add_friend_to_db():
    print(request.form)

    mysql = connectToMySQL('pets')
    data ={
        'pn': request.form['pname'],
        'pt': request.form['ptype']
    }
    query = "INSERT INTO pets(name, type, created_at, updated_at) VALUES(%(pn)s, %(pt)s, NOW(), NOW());"

    new_pet_id = mysql.query_db(query, data)
    return redirect('/')

if __name__== "__main__":
    app.run(debug=True)
