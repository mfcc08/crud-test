from flask import Flask,render_template,request,redirect
from models import db,PedidosModel
from datetime import datetime
from utils import commit_pedido


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/data")
def retrieve_pedidos():
    pedidos = PedidosModel.query.all()
    return render_template("datalist.html",pedidos = pedidos)

@app.route("/data/create",methods=["GET","POST"])
def create():
    if request.method == "GET":
        return render_template("createpage.html")
    
    if request.method == "POST":
        commit_pedido(request, db)
        return redirect("/data")

@app.route("/data/update",methods = ["GET","POST"])
def update():
    id, n_item =  request.args.get("id"), request.args.get("n_item")
    pedido = PedidosModel.query.get((id,n_item))
    if request.method == "POST":
        if pedido:
            db.session.delete(pedido)
            db.session.commit()

            commit_pedido(request, db)
            return redirect(f"/data")
        return f"Pedido com id = {id}{n_item} nao existe"
 
    return render_template("update.html")

app.run(debug=True, host="localhost", port=5000)