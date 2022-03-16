from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired



class ContactForm(FlaskForm):
    title = StringField('Property Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    num_rooms = IntegerField('No. of Rooms', validators=[DataRequired()], render_kw={'placeholder': '3'})
    num_bathrooms = IntegerField('No. of Bathrooms', validators=[DataRequired()], render_kw={'placeholder': '2'})
    price = IntegerField('Price', validators=[DataRequired()], render_kw={'placeholder': '15,000,000'})
    property_type = SelectField('Property Type', choices=[('House'),('Apartment')], validators=[InputRequired()])
    location = StringField('Location', validators=[DataRequired()], render_kw={'placeholder': '10 Waterloo Rd'})
    up_image = FileField('Photos', validators=[FileRequired(), FileAllowed(['jpg','png'])])
    submit = SubmitField('Add Property')