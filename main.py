from flask import Flask,render_template,request,redirect
from models import db,PedidosModel
from datetime import datetime


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
        id = request.form["id"]
        n_item = request.form["n_item"]
        data = datetime.strptime(request.form["data"],"%Y-%m-%d")
        data_etiqueta = datetime.strptime(request.form["data_etiqueta"],"%Y-%m-%d")
        prioridade = request.form["prioridade"]
        express = request.form["express"]
        valor_pedido = request.form["valor_pedido"]
        valor_frete = request.form["valor_frete"]
        pagamento = request.form["pagamento"]
        status = request.form["status"]
        produto = request.form["produto"]
        tipo_couro = request.form["tipo_couro"]
        cor = request.form["cor"]
        personalizacao = request.form["personalizacao"]
        impressao = request.form["impressao"]
        endereco = request.form["endereco"]
        estado = request.form["estado"]
        etiqueta = request.form["etiqueta"]
        obs = request.form["obs"]

        pedido = PedidosModel(id, n_item, data, data_etiqueta, prioridade, express, valor_pedido, valor_frete, pagamento, status, produto, tipo_couro, cor, personalizacao, impressao, endereco, estado, etiqueta, obs)

        db.session.add(pedido)
        db.session.commit()

        return redirect('/data')

app.run(debug=True, host="localhost", port=5000)