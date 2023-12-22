from operator import or_
from flask import Flask
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:duckytran-166@localhost:5432/sale"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


def main():
    items = Items.query.filter(or_(Items.TenMH == "iPhone 12 ProMax", Items.DonGia_dong > 25000000))
    for item in items:
        print(f'Mã MH: {item.MaMH} - {item.TenMH} - {item.MSac} - {item.DLuong} - {item.KThuoc_inchs} - {item.DonGia_dong}')
        
        
if __name__ == "__main__":
    with app.app_context():
        main()