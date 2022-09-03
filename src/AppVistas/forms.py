from django.forms import Form, IntegerField, CharField, BooleanField, DateField

class ProductoFormulario(Form):

    modelo = CharField()
    articulo = IntegerField()
    stock = BooleanField()

class MarcaFormulario(Form):

    nombre = CharField()
    nacionalidad = CharField()
    Inicio_Actividad = DateField()