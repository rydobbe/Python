#Imports
from flask import Flask, redirect, render_template, request, url_for
from models import db, Client



#Configure Flask
app = Flask(__name__)
app.secret_key = "hehehe"


# DB Connection/Config
db_name = "sqlite_database.db"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db.app = app
db.init_app(app)


@app.route("/")
def index():
    return render_template("index.html", title = "New Client")


@app.route("/register", methods=['POST'])
def register():
    firstName = request.form['firstName']
    lastName = request.form['lastName']
    address = request.form['address']
    city = request.form['city']
    state = request.form['state']
    email = request.form['email']
    phone = request.form['phone']
    socialSecurity = request.form['socialSecurity']
    dateOfBirth = request.form['dateOfBirth']
    annualIncome = request.form['annualIncome']
    monthlyRent = request.form['monthlyRent']
    zipCode = request.form['zipCode']
    country = request.form['country']
    client = Client(firstName=firstName, lastName=lastName, address=address,
                    city=city, state=state, email=email, phone=phone,
                    socialSecurity=socialSecurity, dateOfBirth=dateOfBirth,
                    annualIncome=annualIncome, monthlyRent=monthlyRent, zipCode=zipCode,
                    country=country)
    db.session.add(client)
    db.session.commit()
    return redirect(url_for("registered_clients"))


@app.route("/registered_clients")
def registered_clients():
    return render_template("registered.html",title="View All Clients", clients=Client.query.all())


@app.route("/view_clients", methods=['POST'])
def view_clients():
    return redirect(url_for("registered_clients"))


@app.route("/add", methods=['POST'])
def add():
    return redirect(url_for("index"))

@app.route("/drop", methods=['POST'])
def drop():
    db.drop_all()
    db.create_all()
    db.session.commit()
    return redirect(url_for("index"))


@app.route("/<int:client_id>/<client_lastName>/edit", methods=['GET', 'POST'])
def client_edit(client_id, client_lastName):
    client = Client.query.get_or_404(client_id)
    if request.method == 'POST':
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        address = request.form['address']
        city = request.form['city']
        state = request.form['state']
        email = request.form['email']
        phone = request.form['phone']
        socialSecurity = request.form['socialSecurity']
        dateOfBirth = request.form['dateOfBirth']
        annualIncome = request.form['annualIncome']
        monthlyRent = request.form['monthlyRent']
        zipCode = request.form['zipCode']
        country = request.form['country']
        
        client.firstName = firstName
        client.lastName = lastName
        client.address = address
        client.city = city
        client.state = state
        client.email = email
        client.phone = phone
        client.socialSecurity = socialSecurity
        client.dateOfBirth = dateOfBirth
        client.annualIncome = annualIncome
        client.monthlyRent = monthlyRent
        client.zipCode = zipCode
        client.country = country 
        
        db.session.add(client)
        db.session.commit()
        return redirect(url_for('registered_clients'))
    return render_template('client_edit.html', client=client, title="Edit Client")


@app.post('/<int:client_id>/delete/')
def delete_client(client_id):
    client = Client.query.get_or_404(client_id)
    db.session.delete(client)
    db.session.commit()
    return redirect(url_for('registered_clients'))


@app.route("/<int:client_id>/<client_lastName>/view", methods=['GET', 'POST'])
def client_view(client_id, client_lastName):
    client = Client.query.get_or_404(client_id)
    return render_template('client_view.html', client=client, title="Client View")
   


# __name__ is set to __main__ at runtime when running app directly
if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
    