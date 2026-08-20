"""


Ejercicio 2

El modelo Producto tiene el campo codigo con unique=True, eso significa
que la base de datos no  permite codigos repetidos para NINGUN usuario,
ni siquiera para un admin. Como no puedo modificar el modelo, no hay
forma de que un admin registre un codigo duplicado , porque la base de
datos lo va a rechazar de todas formas.
Entonces hay una contradiccion: piden que el admin si pueda duplicar
codigos pero el modelo lo impide con unique=True.
Como se resolveria: le preguntaria al que armo el requerimiento si en
verdad se necesita permitir codigos duplicados para admins. Si es asi
hay que modificar el modelo como quitar el unique o ponerlo condicional.
Si el modelo no se puede tocar, entonces ese requisito no se puede
cumplir tal cual esta escrito, y solo puedo validar las demas reglas.
Las otras validaciones del nombre obligatorio, precio mayor a 0, stock
no negativo si las hago en el formulario sin tocar el modelo.


"""

from django import forms
from django.core.exceptions import ValidationError
from .models import Producto


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ["nombre", "codigo", "precio", "stock", "activo"]

    def __init__(self, *args, **kwargs):
        self.usuario = kwargs.pop("usuario", None)
        super().__init__(*args, **kwargs)

    def clean_nombre(self):
        nombre = self.cleaned_data.get("nombre")
        if not nombre or nombre.strip() == "":
            raise ValidationError("El  nombre es obligatorio")
        return nombre

    def clean_precio(self):
        precio = self.cleaned_data.get("precio")
        if precio is None or precio <= 0:
            raise ValidationError("El precio tiene que ser mayor a cero")
        return precio

    def clean_stock(self):
        stock = self.cleaned_data.get("stock")
        if stock is not None and stock < 0:
            raise ValidationError("El stock no puede ser negativo")
        return stock

    def clean_codigo(self):
        codigo = self.cleaned_data.get("codigo")

        productos = Producto.objects.filter(codigo=codigo)
        if self.instance.pk:
            productos = productos.exclude(pk=self.instance.pk)

        if productos.exists():
            # aca es donde deberia poder dejar pasar al admin, pero
            # como el modelo tiene unique=True, la base de datos igual
            # va a tirar error aunque yo no valide nada aca
            if self.usuario and self.usuario.is_staff:
                raise ValidationError(
                    "Este codigo ya existe. No se puede duplicar porque "
                    "el modelo tiene unique=True aunque seas admin, "
                    "habria que modificar el modelo para permitirlo"
                )
            raise ValidationError("Este codigo ya esta en uso")

        return codigo