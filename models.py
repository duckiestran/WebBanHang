from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Item(db.Model):
    __tablename__ = "items"
    MaH = db.Column(db.Integer, primary_key=True)
    TenH = db.Column(db.String, nullable=False)
    Gia = db.Column(db.String, nullable=False)
    Made_in = db.Column(db.String, nullable=False)
    Note = db.Column(db.String, nullable=False)


class Customer(db.Model):
    __tablename__ = "customers"
    MaK = db.Column(db.Integer, primary_key=True)
    TenK = db.Column(db.String, nullable=False)
    SDT =  db.Column(db.String, nullable=False)
    Date_of_birth = db.Column(db.String, nullable=False)
    Address = db.Column(db.String, nullable=False)

    
class Bill(db.Model):
    __tablename__ = "bills"
    So_HD = db.Column(db.Integer, primary_key=True)
    Ngay_HD = db.Column(db.String, nullable=False)
    MaK = db.Column(db.Integer, db.ForeignKey("customers.MaK"), nullable=False)
    MaH = db.Column(db.Integer, db.ForeignKey("items.MaH"), nullable=False)
    Note = db.Column(db.String, nullable=False)


class Staff(db.Model):
    __tablename__ = "staff"
    MaNv = db.Column(db.Integer, primary_key=True)
    TenNv = db.Column(db.String, nullable=True)
    Date_of_birth = db.Column(db.String, nullable=True)
    Gender = db.Column(db.String, nullable=False)
    SDT = db.Column(db.String, nullable=False)


class Report(db.Model):
    __tablename__ = "report"
    STT = db.Column(db.Integer, primary_key=True)
    Pay =  db.Column(db.String, nullable=True)
    MaNv = db.Column(db.Integer, db.ForeignKey("staff.MaNv"), nullable=False)
    Working_house = db.Column(db.String, nullable=False)
    Shift = db.Column(db.String, nullable=False)
