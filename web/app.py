from flask import Flask
import psycopg2
import os

app = Flask(__name__)


item_format = """<div><h2>{i}: {title}</h2><img src="{image_url}"></div>"""


@app.route("/")
def index():
    hostname = "db"
    username = os.environ["POSTGRES_USER"]
    password = os.environ["POSTGRES_PASSWORD"]
    database = os.environ["POSTGRES_DB"]

    # Create/Connect to database
    with psycopg2.connect(host=hostname, user=username, password=password, dbname=database) as connection:
        with connection.cursor() as cur:
            cur.execute("select title,image_url from sreality")
            items = "\n".join((item_format.format(
                title=title, image_url=image_url, i=i+1) for i, (title, image_url) in enumerate(cur.fetchall())))

    return items
