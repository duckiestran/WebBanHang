from flask import Flask, request, render_template
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:duckytran-166@localhost:5432/sale"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

@app.route('/')
def welcome():
    return render_template("index.html")


@app.route("/ShowItem")
def showItem():
    items = Item.query.all()
    return render_template("show all items.html", items=items)

@app.route("/addCustomer")
def addCustomer():
    return render_template("add-customers.html")


@app.route("/addCustomerSuccess")
def addCustomerSuccess():
    MaK = request.args.get("MaK")
    TenK = request.args.get("TenK")
    SDT = request.args.get("SDT")
    Date_of_birth = request.args.get("Date_of_birth")
    Address = request.args.get("Address")

    shop = Customer(MaK=MaK, TenK=TenK, SDT=SDT, Date_of_birth=Date_of_birth, Address=Address)
    db.session.add(shop)
    db.session.commit()
    return render_template("add-customers-success.html")


@app.route("/showCustomer")
def showCustomer():
    cus = Customer.query.all()
    return render_template("show all cus.html", customers=cus)


@app.route("/delCustomer")
def delCustomer():
    return render_template("del-customer.html")


@app.route("/delCustomerSuccess")
def delCustomerSuccess():
    MaK = request.args.get("MaK")
    exists = False
    exists = Customer.query.filter_by(MaK=MaK).scalar() is not None
    while exists:
        obj = Customer.query.filter_by(MaK=MaK).first()
        db.session.delete(obj)
        db.session.commit()
        return render_template("del-customer-success.html")
    else:
        return render_template('invalid_id.html')


@app.route("/updateCustomer")
def updateCustomer():
    return render_template("update-customer.html")


@app.route("/updateCustomerSuccess")
def updateCustomerSuccess():
    MaK = request.args.get("MaK")
    TenK = request.args.get("TenK")
    SDT = request.args.get("SDT")
    Date_of_birth = request.args.get("Date_of_birth")
    Address = request.args.get("Address")

    exists = Customer.query.filter_by(MaK=MaK).scalar()
    while exists:
        obj_change = Customer.query.filter_by(MaK=MaK).update(dict(TenK=TenK, SDT=SDT, Date_of_birth=Date_of_birth, Address=Address))
        db.session.commit()
        return render_template("update-customer-success.html")
    else:
        return render_template("invalid_id.html")


@app.route("/addItem")
def addItem():
    return render_template("add-items.html")


@app.route("/addItemSuccess")
def addItemSuccess():
    MaH = request.args.get("MaH")
    TenH = request.args.get("TenH")
    Gia = request.args.get("Gia")
    Made_in = request.args.get("Made_in")
    Note = request.args.get("Note")

    shop = Item(MaH=MaH, TenH=TenH, Gia=Gia, Made_in=Made_in, Note=Note)
    db.session.add(shop)
    db.session.commit()
    return render_template("add-items-success.html")


@app.route("/delItem")
def delItem():
    return render_template("del-item.html")


@app.route("/delItemSuccess")
def delItemSuccess():
    MaH = request.args.get("MaH")
    exists = False
    exists = Item.query.filter_by(MaH=MaH).scalar()
    while exists:
        obj_item = Item.query.filter_by(MaH=MaH).first()
        db.session.delete(obj_item)
        db.session.commit()
        return render_template("del-customer-success.html")
    else:
        return render_template('invalid_id.html')


@app.route("/updateItem")
def updateItem():
    return render_template("update-item.html")


@app.route("/updateItemSuccess")
def updateItemSuccess():
    MaH = request.args.get("MaH")
    TenH = request.args.get("TenH")
    Gia = request.args.get("Gia")
    Made_in = request.args.get("Made_in")
    Note = request.args.get("Note")

    exists = False
    exists = Item.query.filter_by(MaH=MaH).scalar()
    while exists:
        obj_item_change = Item.query.filter_by(MaH=MaH).update(dict(TenH=TenH, Gia=Gia, Made_in=Made_in, Note=Note))
        db.session.commit()
        return render_template("update-customer-success.html")
    else:
        return render_template("invalid_id.html")
    
    
@app.route("/showStaff")
def showStaff():
    staff = Staff.query.all()
    return render_template("show all staff.html", staff=staff)
    
    
@app.route("/addStaff")
def addStaff():
    return render_template("add staff.html")


@app.route("/addStaffSuccess")
def addStaffSuccess():
    MaNv = request.args.get("MaNv")
    TenNv = request.args.get("TenNv")
    Date_of_birth = request.args.get("Date_of_birth")
    Gender = request.args.get("Gender")
    SDT = request.args.get("SDT")

    add = Staff(MaNv=MaNv, TenNv=TenNv, Date_of_birth=Date_of_birth, Gender=Gender, SDT=SDT)
    db.session.add(add)
    db.session.commit()
    return render_template("add staff success.html")


@app.route("/delStaff")
def delStaff():
    return render_template("del-staff.html")


@app.route("/delStaffSuccess")
def delStaffSuccess():
    MaNv = request.args.get("MaNv")
    exists = True
    exists = Staff.query.filter_by(MaNv=MaNv).scalar()
    while exists:
        staff = Staff.query.filter_by(MaNv=MaNv).first()
        db.session.delete(staff)
        db.session.commit()
        return render_template("del-staff-success.html")
    else:
        return render_template('invalid_id.html')


@app.route("/updateStaff")
def updateStaff():
    return render_template("update-staff.html")


@app.route("/updateStaffSuccess")
def updateStaffSuccess():
    MaNv = request.args.get("MaNv")
    TenNv = request.args.get("TenNv")
    Date_of_birth = request.args.get("Date_of_birth")
    Gender = request.args.get("Gender")
    SDT = request.args.get("SDT")

    exists = True
    exists = Staff.query.filter_by(MaNv=MaNv).scalar() 
    while exists:
        staff_change = Staff.query.filter_by(MaNv=MaNv).update(dict(
            TenNv=TenNv, Date_of_birth=Date_of_birth, Gender=Gender, SDT=SDT))
        db.session.commit()
        return render_template("update-staff-success.html")
    else:
        return render_template("invalid_id.html")


@app.route("/addReport")
def addReport():
    return render_template("add report.html")


@app.route("/addReportSuccess")
def addReportSuccess():
    STT = request.args.get("STT")
    Pay = request.args.get("Pay")
    MaNv = request.args.get("MaNv")
    Working_house = request.args.get("Working_house")
    Shift = request.args.get("Shift")
    
    exist_MaNv = True
    exists_MaNv = Staff.query.filter_by(MaNv=MaNv).scalar()
    while exists_MaNv:
        report = Report(STT=STT, Pay=Pay, MaNv=MaNv, Working_house=Working_house, Shift=Shift)
        db.session.add(report)
        db.session.commit()
        return render_template("add report success.html")
    else:
        return render_template("invalid_id.html")


@app.route("/delReport")
def delReport():
    return render_template("del report.html")


@app.route("/delReportSuccess")
def delReportSuccess():
    STT = request.args.get("STT")
    exists = True
    exists = Report.query.filter_by(STT=STT).scalar()
    while exists:
        gg = Report.query.filter_by(STT=STT).first()
        db.session.delete(gg)
        db.session.commit()
        return render_template("del report success.html")
    else:
        return render_template('invalid_id.html')

@app.route("/updateReport")
def updateReport():
    return render_template("update report.html")


@app.route("/updateReportSuccess")
def updateReportSuccess():
    STT = request.args.get("STT")
    Pay = request.args.get("Pay")
    MaNv = request.args.get("MaNv")
    Working_house = request.args.get("Working_house")
    Shift = request.args.get("Shift")

    exists = True
    exists = Report.query.filter_by(STT=STT).scalar()
    while exists:
        report_change= Report.query.filter_by(STT=STT).update(dict(Pay=Pay, MaNv=MaNv, Working_house=Working_house, Shift=Shift))
        db.session.commit()
        return render_template("update report success.html")
    else:
        return render_template("invalid_id.html")


@app.route("/orderItem")
def orderItem():
    return render_template("order items.html")


@app.route("/orderItemSuccess")
def orderItemSuccess():
    So_HD = request.args.get("So_HD")
    Ngay_HD = request.args.get("Ngay_HD")
    MaK = request.args.get("MaK")
    MaH = request.args.get("MaH")
    Note = request.args.get("Note")

    exists_MaH = True
    exists_MaK = True
    exists_MaH = Item.query.filter_by(MaH=MaH).scalar() 
    exists_MaK = Customer.query.filter_by(MaK=MaK).scalar() 
    while exists_MaH and exists_MaK:

        bills = Bill(So_HD=So_HD, Ngay_HD=Ngay_HD, MaK=MaK, MaH=MaH, Note=Note)  
        db.session.add(bills)
        db.session.commit()
        return render_template("order items success.html")
    else:
        return render_template("invalid_id.html")


if __name__ =="__main__":
    app.run(debug=True)