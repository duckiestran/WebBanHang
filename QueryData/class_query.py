from flask import Flask
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:duckytran-166@localhost:5432/sale"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


def main():
    items = Item.query.all()
    for item in items:
        print(f'Mã MH: {item.MaH} - {item.TenH} - {item.Gia} - {item.Made_in} - {item.Note}')
        
        
if __name__ == "__main__":
    with app.app_context():
        main()