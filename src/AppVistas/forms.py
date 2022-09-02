from django.forms import Form, IntegerField, CharField, EmailField, BooleanField, PasswordInput, ImageField

class ProductoFormulario(Form):

    modelo = CharField()
    articulo = IntegerField()
    stock = BooleanField()

class MarcaFormulario(Form):

    nombre = CharField()
    nacionalidad = CharField()