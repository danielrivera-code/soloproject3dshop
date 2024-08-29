from flask import Flask
app = Flask(__name__)
app.secret_key = "dsdfhdfgjdfgjsfdhsdfghsdfg"

def format_date_found(date):
    return date.strftime("%B %d %Y")

app.add_template_filter(format_date_found)
