from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from bibliotecaapp import models
from django.contrib.auth.forms import UserCreationForm
from user.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User 
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            'telefono',
            'documentoIdentidad',
        ]
        labels= {'documentoIdentidad': 'Documento de identidad '}
        


class crearAutores(forms.ModelForm):
    
    SEXO_CHOICES = (
        ('M', 'Mujer'),
        ('H', 'Hombre'),
        ('N', 'No definido'), 
    )
    
    sexo = forms.ChoiceField(choices=SEXO_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    
    class Meta:
        model = models.autores
        fields = [
            'nombre',
            'nacionalidad',
            'sexo',
            'fechaNacimiento',
            'alias',
        ]
        
        labels = {
           'nombre': 'Nombre',
           'nacionalidad': 'Nacionalidad',
           'sexo':  'Sexo',
           'fechaNacimiento':  'Fecha de Nacimiento',
           'alias':  'Alias',

        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'nacionalidad': forms.TextInput(attrs={'class': 'form-control'}),
            'fechaNacimiento': forms.SelectDateWidget(years=range(1950, 2050), attrs={'class': 'form-control'}),
            'alias': forms.TextInput(attrs={'class': 'form-control'}),
        }
 
class crearUsuarios(forms.ModelForm):
    class Meta: 
        model = models.usuarios
        fields = [
            'nombre',
            'direccion',
            'telefono',
            'documentoIdentidad',
            'correo',
        ]
        labels = {
            'nombre' : 'Nombre',
            'direccion' : 'Dirección',
            'telefono' : 'Teléfono',
            'documentoIdentidad' : 'Documento de Identidad',
            'correo' : 'Correo',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono' : forms.TextInput(attrs={'class': 'form-control' }),
            'documentoIdentidad' : forms.TextInput(attrs={'class': 'form-control' }),
            'correo': forms.TextInput(attrs={'class': 'form-control'}),   
            
            
        }

class crearEditoriales(forms.ModelForm):
    class Meta: 
        model = models.editoriales
        fields = [
            'nombre',
            'direccion',
            'telefono',
            'correo',
        ]
        labels = {
            'nombre' : 'Nombre',
            'direccion' : 'Dirección',
            'telefono' : 'Teléfono',
            'correo': 'Correo',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono' : forms.TextInput(attrs={'class': 'form-control' }),
            'correo': forms.TextInput(attrs={'class': 'form-control'}),     
        }

class crearGeneros(forms.ModelForm):
    class Meta:
        model = models.generos
        fields = [
            'nombreGenero',
            'descripcion',
        ]
        
        labels = {
           'nombreGenero': 'Nombre',
           'descripcion': 'Descripcion'
        }
        widgets = {
            'nombreGenero': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
        }

class crearRecursosTecnologicos(forms.ModelForm):
    ESTADO_CHOICES = (
        (1, 'Disponible'),
        (0, 'No disponible'),
    )
    
    estado = forms.ChoiceField(choices=ESTADO_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}), initial=1)

    class Meta:
        model = models.recursosTecnologicos
        fields = [
            'tipo',
            'ubicacion',
            'estadoEquipo',
            'estado',
            'marca',
        ]
        labels = {
            'tipo': 'Tipo de recurso',
            'ubicacion': 'Ubicacion del recurso',
            'estadoEquipo': 'Estado del recurso',
            'estado':'Estado del recurso',
            'marca': 'Marca del recurso',
        }
        widgets = {
            'tipo':forms.TextInput(attrs={'class': 'form-control'}),
            'ubicacion':forms.TextInput(attrs={'class': 'form-control'}),
            'estadoEquipo':forms.TextInput(attrs={'class': 'form-control'}),
            'marca':forms.TextInput(attrs={'class': 'form-control'}),
        }

class crearLibros(forms.ModelForm): 

    class Meta: 
        model = models.libros
        fields = [
            'ISBN',
            'titulo',
            'portada',
            'IDautor',
            'IDgenero',
            'IDeditorial',
            'descripcion',
            'fechaPublicacion',
            'edicion',
            'existencias',
            'sinopsis',
            'paginas',
        ]
        labels = {
            'ISBN' : 'ISBN',
            'titulo' : 'Título',
            'portada':'Portada',
            'IDautor': 'Autor',
            'IDgenero' : 'Género',
            'IDeditorial' : 'Editorial',
            'descripcion' : 'Descripción',
            'fechaPublicacion' : 'Fecha de publicación',
            'edicion' : 'Edición',
            'existencias' : 'Existencias',
            'sinopsis' : 'Sinopsis',
            'paginas' : 'Páginas',
        }
        widgets = {
            
            'ISBN' : forms.NumberInput(attrs={'class': 'form-control'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'portada': forms.URLInput(attrs={'class': 'form-control'}),
            'IDautor': forms.Select(attrs={'class': 'form-control'}),
            'IDgenero': forms.Select(attrs={'class': 'form-control'}),
            'IDeditorial': forms.Select(attrs={'class': 'form-control'}),
            'descripcion':  forms.Textarea(attrs={'class': 'form-control'}),
            'fechaPublicacion': forms.NumberInput(attrs={'class': 'form-control'}),
            'edicion': forms.TextInput(attrs={'class': 'form-control'}),
            'existencias': forms.TextInput(attrs={'class': 'form-control'}),
            'sinopsis':forms.Textarea(attrs={'class': 'form-control'}),
            'paginas' : forms.NumberInput(attrs={'class': 'form-control'}),
        } 
             
class crearCargos(forms.ModelForm):
    class Meta:
        model = models.cargos
        fields = [
            'nombre',
            'descripcion',
        ]
        
        labels = {
           'nombre': 'Nombre',
           'descripcion': 'Descripcion'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
        }

class crearEmpleados(forms.ModelForm):
    ESTADO_CHOICES = (
        (1, 'Activo'),
        (0, 'Inactivo'),
    )
    
    estado = forms.ChoiceField(choices=ESTADO_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}), initial=1)
    
    class Meta:
        model = models.empleados
        fields = [
            'nombre',
            'direccion',
            'documentoIdentidad',
            'telefono',
            'IDcargo',
            'estado',
        ]

        labels = {
            'IDcargo': 'Cargo',
            'nombre': 'Nombre',
            'direccion': 'Dirección',
            'documentoIdentidad': 'Documento de identidad',
            'telefono': 'Teléfono',
            'estado': 'Estado',
        }

        widgets = {
            'IDcargo': forms.Select(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'documentoIdentidad': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
        }

class crearPrestamos(forms.ModelForm):
    
    class Meta:
        model = models.prestamos
        fields = [
            'id',
            'IDlibro',
            'IDempleado',
            'fechaEntrada',
        ]

        labels = {
            'id': "Nombre del usuario",
            'IDlibro': "Libro",
            'IDempleado': "Nombre del empleado",
            'fechaEntrada': "Fecha de entrega",
        }

        widgets = {
            'id': forms.Select(attrs={'class': 'form-control'}),
            'IDlibro': forms.Select(attrs={'class': 'form-control'}),
            'IDempleado': forms.Select(attrs={'class': 'form-control'}),
            'fechaEntrada': forms.DateInput(attrs={'class': 'form-control'}),
        }
class crearReservaUsuario(forms.ModelForm):
   
    class Meta:
        model = models.reservasUsuarios
        fields = [
            #'id',
            'IDlibro',
            'fechaRetiro',

        ]

        labels = {
           # 'id':'Nombre del usuario',
            'IDlibro': 'Libro',
            'fechaRetiro': 'Fecha de retiro del libro',

        }
        
        widgets = {
           # 'id': forms.Select(attrs={'class': 'form-control'}),
            'IDlibro': forms.Select(attrs={'class': 'form-control'}),
            'fechaRetiro': forms.DateInput(attrs={'class': 'form-control'}),

        }
class crearReservas(forms.ModelForm):
    ESTADO_CHOICES = (
        (1, 'Hecha'),
        (0, 'No hecha'),
    )
    
    estado = forms.ChoiceField(choices=ESTADO_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}), initial=0)
    
    class Meta:
        model = models.reservas
        fields = [
            'id',
            'IDlibro',
            'fechaRetiro',
            'estado',

        ]

        labels = {
            'id':'Nombre del usuario',
            'IDlibro': 'Libro',
            'fechaRetiro': 'Fecha de retiro del libro',
            'estado': 'Estado de la reserva',

        }
        
        widgets = {
            'id': forms.Select(attrs={'class': 'form-control'}),
            'IDlibro': forms.Select(attrs={'class': 'form-control'}),
            'fechaRetiro': forms.DateInput(attrs={'class': 'form-control'}),

        }

class crearReseñas(forms.ModelForm):
    codigo_prestamo = forms.CharField(label='Código de Préstamo', widget=forms.TextInput(attrs={'class': 'form-control'}))
    puntuacion = forms.IntegerField(widget=forms.HiddenInput())

    class Meta:
        model = models.reseñas
        fields = ['comentario', 'puntuacion']

        labels = {
            'comentario': 'Comentario de la reseña',
            'puntuacion': 'Puntuación',
        }

        widgets = {
            'comentario': forms.Textarea(attrs={'class': 'form-control'}),
            

        }

class crearTipoPenalizaciones(forms.ModelForm):

    class Meta:
        model = models.tipoPenalizaciones
        fields = [
            'nombre',
            'descripcion',
        ]
        
        labels = {
           'nombre': 'Nombre',
           'descripcion': 'Descripcion'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
        }

class crearPenalizaciones(forms.ModelForm):
    ESTADO_CHOICES = (
        (1, 'Activo'),
        (0, 'Inactivo'),
    )

    estadoPenalizacion = forms.ChoiceField(
        choices=ESTADO_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        initial=0,
        label='Tipo de penalizacion'  # Etiqueta personalizada
    )

    class Meta:
        model = models.penalizaciones
        fields = [
            'IDprestamo',
            'IDtipoPenalizacion',
            'estadoPenalizacion',
            'detalle',
        ]

        labels = {
            'IDprestamo': 'Prestamo', 
            'IDtipoPenalizacion': 'Tipo de penalizacion',
            'detalle': 'Detalles de la penalizacion',
        }

        widgets = {
            'IDprestamo': forms.Select(attrs={'class': 'form-control'}),
            'IDtipoPenalizacion': forms.Select(attrs={'class': 'form-control'}),
            'detalle': forms.Textarea(attrs={'class': 'form-control'}),
        }

class crearPrestamoRecursos(forms.ModelForm):
    

    class Meta:
        model = models.prestamoRecursos
        fields = [
            'IDrecurso',
            'id',
            'IDempleado',
            'salida',
            'detalle',
        ]

        labels = {
            'IDrecurso': 'Recurso',
            'id': 'Usuario',
            'IDempleado': 'Empleado',
            'salida': 'Fin del prestamo',
            'detalle': 'Detalle del prestamo',
        }

        widgets = {
            'IDrecurso': forms.Select(attrs={'class': 'form-control'}),
            'id': forms.Select(attrs={'class': 'form-control'}),
            'IDempleado': forms.Select(attrs={'class': 'form-control'}),
            'salida':  forms.SelectDateWidget(years=range(1950, ), attrs={'class': 'form-control'}),
            'detalle':forms.Textarea(attrs={'class': 'form-control'}),
        }

class crearHistorialVisitas(forms.ModelForm): 
    ESTADO_CHOICES = (
        (1, 'Presencial'),
    )
    
    presencial = forms.ChoiceField(choices=ESTADO_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}), initial=1)

    class Meta:
        model = models.historialVisitas
        fields = [
            'id',
            'salida',
            'presencial',
        ]

        labels = {
            'id': 'Usuario',
            'salida': 'Salida',
            'presencial': 'Presencial',
        }

        widgets = {
            'id': forms.Select(attrs={'class': 'form-control'}),
            'salida': forms.TimeInput(attrs={'class': 'form-control'}),
            'presencial': forms.HiddenInput(attrs={'value': 1}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['salida'].required = False

class crearComentario(forms.ModelForm):
   

    class Meta:
        model = models.comentarios
        fields = ['nombre', 'comentario']

        labels = {
            'nombre': 'Ingrese su nombre',
            'comentario': 'Comentario',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'comentario': forms.Textarea(attrs={'class': 'form-control'}),
        }

class crearContacto(forms.ModelForm):
    class Meta:
        model = models.contacto
        fields = ['nombreCompleto', 'correo', 'telefono', 'mensaje']
        labels = {
            'nombreCompleto': 'Nombre Completo',
            'correo': 'Correo',
            'telefono': 'Teléfono',
            'mensaje': 'Mensaje',
        }
        widgets = {
            'nombreCompleto': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'mensaje': forms.Textarea(attrs={'class': 'form-control'}),
        }