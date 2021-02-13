from app import app
from flask import render_template, redirect, url_for
from app.forms import PopulationForm
from app import cities

@app.route('/')
def hello():
    return '<h1>Form test</h1>'

@app.route('/population', methods=['GET', 'POST'])
def population():
    form = PopulationForm()
    if form.validate_on_submit():
        cities[form.city.data] = form.population.data
        form.city.data = ''
        form.population.data = ''
        return redirect(url_for('population'))
    return render_template('population.html', form=form)

@app.route('/view_all')
def view():
    return render_template('view_cities.html', cities=cities)
