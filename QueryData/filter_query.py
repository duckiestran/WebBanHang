from flask import Flask
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:duckytran-166@localhost:5432/sale"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


def main():
    items = Items.query.filter_by(MSac="Black")
    for item in items:
        print(f'Mã MH: {item.MaMH} - {item.TenMH} - {item.MSac} - {item.DLuong} - {item.KThuoc_inchs} - {item.DonGia_dong}')
        
        
if __name__ == "__main__":
    with app.app_context():
        main()