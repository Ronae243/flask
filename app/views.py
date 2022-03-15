"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""
import os
from app import app, db
from flask import render_template, request, redirect, url_for, flash, send_from_directory
from .forms import ContactForm
from werkzeug.utils import secure_filename
from .models import HouseProperties


@app.route('/photos/<filename>')
def get_images(filename):
    spec_img = send_from_directory(os.path.join(os.getcwd(),
    app.config['UPLOAD_FOLDER']), filename)
    return spec_img

@app.template_filter()
def numberFormat(value):
    return format(int(value), ',d')

# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Ronae Johnson")


@app.route('/properties/create', methods = ['GET','POST'])
def properties_c():
    form = ContactForm()

    if request.method == 'POST':
        if form.validate_on_submit() == True:
            title = request.form['title']
            num_of_rooms = request.form['num_rooms']
            num_of_bathrooms = request.form['num_bathrooms']
            price = request.form['price']
            property_type = request.form['property_type']
            location = request.form['location']
            description = request.form['description']
            file = request.files['up_image']

            #saves photos to uplaods folder
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))


            #passes data to collected from from to database
            entry = HouseProperties(title, description, num_of_rooms, num_of_bathrooms, price, property_type, location, filename)
            db.session.add(entry)
            db.session.commit()

            flash('Message sent to server')
            return redirect(url_for('properties_s'))
        else:
            flash('Message was not sent')
            return render_template('add.html', form=form)
    elif request.method == 'GET':
        return render_template('add.html', form=form)



@app.route('/properties', methods = ['GET', 'POST'])
def properties_s():
    form = ContactForm()
    column_data = HouseProperties.query.all()
    return render_template('properties.html', image_gal = column_data, view_btn = form)

"""

@app.route('/properties/<propertyid>')
def property():
"""

###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
