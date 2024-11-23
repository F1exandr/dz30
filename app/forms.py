from wtforms import Form, IntegerField, validators
class NumberForm(Form):
    number = IntegerField('Number', [validators.DataRequired(), validators.NumberRange(min=1, max=100)])