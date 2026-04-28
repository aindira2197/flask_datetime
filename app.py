from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'


db = SQLAlchemy(app)


class Xodimlar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ism = db.Column(db.String(20))
    familiya = db.Column(db.String(20))
    tugilgan_sana = db.Column(db.DateTime, default=datetime.now)
    lavozim = db.Column(db.String(20))
    bolim = db.Column(db.String(20))
    telefon = db.Column(db.String(13) , unique=True)
    email = db.Column(db.String(40), unique=True)
    ish_haqi = db.Column(db.Integer)



class Mahsulotlar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mahsulot_nomi = db.Column(db.String(20))
    kategoriya = db.Column(db.String(20))
    ishlab_chiqaruvchi = db.Column(db.String(20))
    narx = db.Column(db.Integer)
    miqdor = db.Column(db.Integer)
    rang = db.column(db.String(20))
    ogirlik = db.Column(db.Float)
    kafolat_oy = db.Column(db.Integer)
    kelgan_sana = db.Column(db.DateTime, default=datetime.now)


class Buyurtmalar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mijoz_ismi = db.Column(db.String(20))
    mijoz_telefon = db.Column(db.String(13), unique=True)
    mahsulot_nomi = db.Column(db.String(20))
    miqdor = db.Column(db.Integer)
    narx = db.Column(db.Integer)
    jami_summa = db.Column(db.Integer)
    tolov_turi = db.Column(db.String(20))
    buyurtma_sana = db.Column(db.String(20))
    yetkazilgan = db.Column(db.String(5))



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
