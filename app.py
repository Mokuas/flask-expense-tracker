from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_scss import Scss

app = Flask(__name__)
Scss(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database_v2.db'
db = SQLAlchemy(app)

class MyExpenses(db.Model):
    __tablename__ = "expenses"
    id = db.Column(db.Integer, primary_key=True)
    catagoryid = db.Column(db.Integer, db.ForeignKey('categories.id', ondelete="RESTRICT"))
    description = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    amount = db.Column(db.Integer, nullable=False)
    category = db.relationship('MyCategories', backref='expenses')

class MyCategories(db.Model):
    __tablename__ = "categories"
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50), unique=True, nullable=False)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        form_type = request.form.get("form_type")
        if form_type == "category":
            category_name = (request.form.get('content') or "").strip()
            if not category_name:
                return "Category name required", 400
            new_cat = MyCategories(category=category_name)
            db.session.add(new_cat)
            db.session.commit()
            return redirect(url_for('index'))

        elif form_type == "expense":
            cat_id = request.form.get('category_id', type=int)
            desc = (request.form.get('expense_input_description') or "").strip()
            amount = request.form.get('expense_input_amount', type=int)

            if not (cat_id and desc and amount is not None):
                return "Category, description and amount are required.", 400

            new_exp = MyExpenses(
                catagoryid=cat_id,
                description=desc,
                amount=amount
            )
            db.session.add(new_exp)
            db.session.commit()
            return redirect(url_for('index'))

        # GET
    expenses = MyExpenses.query.order_by(MyExpenses.date.desc()).all()
    catagories = MyCategories.query.order_by(MyCategories.category.asc()).all()
    return render_template("index.html", catagories=catagories, expenses=expenses)

@app.route("/editCategory/<int:id>", methods=['GET', 'POST'])
def editCategory(id):
    category = MyCategories.query.get_or_404(id)
    if request.method == "POST":
        category.category  = request.form['category']
        try:
            db.session.commit()
            return redirect("/")
        except Exception as e:
            print(f"Error: {e}")
            return f"Error: {e}"
    else:
        return render_template('editCategory.html', category=category)

@app.route("/deleteCategory/<int:id>", methods=['GET', 'POST'])
def deleteCategory(id):
    category = MyCategories.query.get_or_404(id)
    try:
        db.session.delete(category)
        db.session.commit()
        return redirect("/")
    except Exception as e:
        print(f"Error: {e}")
        return f"Error: {e}"



if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)