from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, IntegerField, SelectField, DateField, URLField
from wtforms.validators import DataRequired, Email, Length, NumberRange, Optional, ValidationError
from datetime import date


class RegistrationForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(max=50)])
    surname = StringField('Surname', validators=[DataRequired(), Length(max=50)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=120)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    contact_number = StringField('Contact Number', validators=[DataRequired(), Length(max=20)])
    street_address = StringField('Street Address', validators=[DataRequired(), Length(max=200)])


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])


class EventForm(FlaskForm):
    title = StringField('Event Title', validators=[DataRequired(), Length(max=200)])
    description = TextAreaField('Description', validators=[DataRequired()])
    category = SelectField('Category', choices=[
        ('Street Food', 'Street Food'),
        ('Fine Dining', 'Fine Dining'),
        ('Desserts & Baking', 'Desserts & Baking'),
        ('Vegan / Plant-Based', 'Vegan / Plant-Based')
    ], validators=[DataRequired()])
    date = DateField('Event Date', validators=[DataRequired()])
    start_time = StringField('Start Time', validators=[DataRequired(), Length(max=10)])
    end_time = StringField('End Time', validators=[DataRequired(), Length(max=10)])
    venue = StringField('Venue', validators=[DataRequired(), Length(max=200)])
    capacity = IntegerField('Ticket Capacity', validators=[DataRequired(), NumberRange(min=1)])
    image_url = URLField('Event Image URL', validators=[Optional(), Length(max=500)])

    def validate_date(self, field):
        if field.data and field.data < date.today():
            raise ValidationError('Event date cannot be in the past. Please select a future date.')


class BookingForm(FlaskForm):
    quantity = IntegerField('Number of Tickets', validators=[DataRequired(), NumberRange(min=1, max=10)])


class CommentForm(FlaskForm):
    content = TextAreaField('Your Comment', validators=[DataRequired(), Length(min=1, max=500)])
