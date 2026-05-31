from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, IntegerField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Email, Length, Optional


class RegisterForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired(), Length(min=3, max=80)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField('Зарегистрироваться')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Войти')


class SeedForm(FlaskForm):
    catalog_id = SelectField('Выберите из справочника', coerce=int, validators=[Optional()])
    crop_name = StringField('Культура', validators=[DataRequired()])
    variety = StringField('Сорт')
    manufacturer = StringField('Производитель')
    purchase_date = DateField('Дата покупки', format='%Y-%m-%d', validators=[Optional()])
    expiry_date = DateField('Срок годности', format='%Y-%m-%d', validators=[Optional()])

    packets_count = IntegerField('Количество пакетиков', default=1)
    seeds_per_packet = IntegerField('Семян в одном пакетике', default=0)

    notes = TextAreaField('Заметки')
    submit = SubmitField('Добавить семена')


class PlantingForm(FlaskForm):
    seed_id = IntegerField('Выберите семена', validators=[DataRequired()])
    sowing_date = DateField('Дата посева', validators=[DataRequired()], format='%Y-%m-%d')
    quantity_sown = IntegerField('Сколько семян посеял', default=10)
    location = StringField('Место посадки')

    watering_interval = IntegerField('Поливать каждые (дней)', default=7)
    days_to_harvest = IntegerField('Дней до созревания урожая', default=60)

    notes = TextAreaField('Заметки')
    submit = SubmitField('Сохранить посадку')


class UserSettingsForm(FlaskForm):
    city = StringField('Ваш город', validators=[DataRequired()])
    submit = SubmitField('Сохранить город')
