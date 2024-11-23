from flask import Flask, request, render_template
from flask_wtf import FlaskForm
from wtforms import IntegerField, validators

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_secret_key'


class NumberForm(FlaskForm):
    number = IntegerField('Number', [validators.DataRequired(), validators.NumberRange(min=1, max=100)])


@app.route('/', methods=['GET', 'POST'])
def multiplier():
    form = NumberForm()
    if form.validate_on_submit():
        number = form.number.data
        result = number ** 2
        print(result)
        return 'Result: {}'.format(result)
    return render_template('base.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)