import csv
from flask import Flask
from create_table import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:duckytran-166@localhost:5432/sale"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


def main():
    items = Items(MaMH="8", TenMH="Màn hình LG", MSac="Black", DLuong="None", KThuoc_inchs="27", DonGia_dong=8000000)
    db.session.add(items)
    db.session.commit()


if __name__ == "__main__":
    with app.app_context():  # allow developer interact with flask via command line
        main()
