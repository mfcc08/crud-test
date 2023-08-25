from flask_sqlalchemy import SQLAlchemy
 
db = SQLAlchemy()
 
class PedidosModel(db.Model):
    __tablename__ = "table"
 
    id = db.Column(db.Integer, primary_key=True)
    n_item = db.Column(db.Integer, primary_key=True)
    
    data = db.Column(db.Date)
    data_etiqueta = db.Column(db.Date)

    valor_pedido = db.Column(db.Numeric)
    valor_frete  = db.Column(db.Numeric)

    pagamento = db.Column(db.String)
    status =  db.Column(db.String)
    produto = db.Column(db.String)
    tipo_couro = db.Column(db.String)
    cor = db.Column(db.String)
    personalizacao = db.Column(db.String)
    impressao = db.Column(db.String)
    endereco = db.Column(db.String)
    estado = db.Column(db.String)
    etiqueta = db.Column(db.String)
    obs = db.Column(db.String)
    prioridade = db.Column(db.String)
    express = db.Column(db.String)

    def __init__(self, id, n_item, data, data_etiqueta, prioridade, express, valor_pedido, valor_frete, pagamento, status, produto, tipo_couro, cor, personalizacao, impressao, endereco, estado, etiqueta, obs):
        self.id = id
        self.n_item = n_item
        self.data = data
        self.data_etiqueta = data_etiqueta
        self.prioridade = prioridade
        self.express = express
        self.valor_pedido = valor_pedido
        self.valor_frete = valor_frete
        self.pagamento = pagamento
        self.status = status
        self.produto = produto
        self.tipo_couro = tipo_couro
        self.cor = cor
        self.personalizacao = personalizacao
        self.impressao = impressao
        self.endereco = endereco
        self.estado = estado
        self.etiqueta = etiqueta
        self.obs = obs

    def __repr__(self):
        return f"""id:     {self.id}
                   n_item: {self.n_item }
                   produto:{self.produto}"""