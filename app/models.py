from app import db
from flask_login import UserMixin
from datetime import date, timedelta


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=True)  # nullable for Yandex-only users
    city = db.Column(db.String(100), default='Уфа')
    yandex_id = db.Column(db.String(100), unique=True, nullable=True)

class SeasonalEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    month = db.Column(db.Integer, nullable=False)
    plant_name = db.Column(db.String(100), nullable=False)
    event_type = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text)
    emoji = db.Column(db.String(10), default='🌱')
