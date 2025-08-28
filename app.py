import sqlite3
from flask import Flask, render_template, redirect, url_for, flash, request
from dotenv import load_dotenv
import os

load_dotenv()

app: Flask = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

contacts: list = [
    {"id": 1, "nama": "Budi", "no_hp": "08123", "email": "budi@mail.com"},
    {"id": 2, "nama": "Siti", "no_hp": "08234", "email": "siti@mail.com"}
]

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html', contacts=contacts)


@app.route("/add", methods=['GET', 'POST'])
def add():

    if request.method == "POST":
        id: int = int(request.form['id'])
        nama: str = request.form['nama']
        no_hp: str = request.form['no_hp']
        email: str = request.form['email']

        contacts.append(
            {
                "id": id, 
                "nama":nama, 
                "no_hp":no_hp, 
                "email":email
            }
        )

        return redirect(url_for('index'))
    
    return render_template("add.html", contacts=contacts)

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    contacts
    if request.method == "POST":
        
        nama: str = request.form['nama']
        no_hp: str = request.form['no_hp']
        email: str = request.form['email']

        target_index: int = next((i for i, c in enumerate(contacts) if c["id"] == id), None)

        if target_index is not None:

            contacts[target_index]['nama'] = nama
            contacts[target_index]['no_hp'] = no_hp
            contacts[target_index]['email'] = email

            return redirect(url_for('index'))

    print(contacts)    
    print(id)    
    contact_by_name = [i for i in contacts if i["id"] == id]
    return render_template("edit.html", contact_by_name=contact_by_name[0])


@app.route("/delete/<int:id>", methods=["GET"])
def delete(id):

    target_index = next((i for i, c in enumerate(contacts) if c["id"] == id), None)
    contacts.pop(target_index)

    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run(debug=True)