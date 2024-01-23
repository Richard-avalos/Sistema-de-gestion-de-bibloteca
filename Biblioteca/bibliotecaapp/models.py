from django.db import models
from user.models import User

# Create your models here.


class autores(models.Model):
    IDautor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=70)
    sexo = models.CharField(max_length=1)
    fechaNacimiento = models.DateField()
    alias = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    

class usuarios(models.Model):
    IDusuario = models.AutoField(primary_key=True)
    nombre  = models.CharField(max_length=100)
    direccion = models.CharField(max_length=300)
    telefono = models.CharField(max_length=12)
    documentoIdentidad = models.CharField(max_length=30)
    correo = models.EmailField(max_length=255, unique=True)
    fechaRegistro = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre
    
    
class editoriales(models.Model):
    IDeditorial = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=300)
    telefono= models.CharField(max_length=15)
    correo = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre 
    
class generos(models.Model):
    IDgenero = models.AutoField(primary_key=True)
    nombreGenero = models.CharField(max_length=70)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombreGenero

    
class recursosTecnologicos(models.Model):
    IDrecurso = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=150)
    ubicacion = models.CharField(max_length=200)
    estadoEquipo = models.CharField(max_length=200)
    estado = models.SmallIntegerField()
    marca = models.CharField(max_length=300)

    def __str__(self):
        return self.tipo


class libros(models.Model):
    IDlibro = models.IntegerField(primary_key=True)
    ISBN = models.IntegerField()
    titulo = models.CharField(max_length=255)
    portada = models.URLField(null=True)
    IDautor = models.ForeignKey(autores, on_delete=models.CASCADE)
    IDgenero = models.ForeignKey(generos, on_delete=models.CASCADE)
    descripcion = models.TextField(null=True)
    fechaPublicacion = models.IntegerField()
    edicion = models.CharField(max_length=50, null=True)
    IDeditorial = models.ForeignKey(editoriales, on_delete=models.CASCADE)
    existencias = models.IntegerField()
    sinopsis = models.TextField(null=True)
    paginas = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.titulo

 
class cargos(models.Model):
    IDcargo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    
    def __str__(self):
        return self.nombre


class empleados(models.Model):
    IDempleado = models.AutoField(primary_key=True)
    IDcargo = models.ForeignKey(cargos, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=300)
    documentoIdentidad = models.CharField(max_length=30)
    telefono = models.CharField(max_length=20)
    fechaContratacion = models.DateField(auto_now_add=True)
    estado = models.SmallIntegerField()
    
    def __str__(self):
        return self.nombre 

class prestamos(models.Model):
    IDprestamo = models.AutoField(primary_key=True)
    id = models.ForeignKey(User, on_delete=models.CASCADE)
    IDlibro = models.ForeignKey(libros, on_delete=models.CASCADE)
    IDempleado = models.ForeignKey(empleados, on_delete=models.CASCADE, null=True, blank=True)
    fechaSalida = models.DateTimeField(auto_now_add=True)
    fechaEntrada = models.DateTimeField()

    def __str__(self):
        return str(self.IDprestamo)

    def to_json(self):
        return {
            'libro': str(self.IDlibro),
            'usuario': str(self.id),
            'fechaSalida': str(self.fechaSalida),
            'fechaEntrada': str(self.fechaEntrada),
            # Add more fields as needed
        }
    
class reservas(models.Model):
    IDreserva = models.AutoField(primary_key=True)
    id = models.ForeignKey(User, on_delete=models.CASCADE)
    IDlibro = models.ForeignKey(libros, on_delete=models.CASCADE)
    fechaReserva = models.DateTimeField(auto_now_add=True)
    fechaRetiro = models.DateTimeField()
    estado = models.SmallIntegerField()
    
    def __str__(self):
        return self.IDreserva
    
class reservasUsuarios(models.Model):
    IDreservaUsuario = models.AutoField(primary_key=True)
    id = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=150, null=True)
    IDlibro = models.ForeignKey(libros, on_delete=models.CASCADE)
    fechaReserva = models.DateTimeField(auto_now_add=True)
    fechaRetiro = models.DateTimeField()
    
    def __str__(self):
        return self.IDreservaUsuario
    

class reseñas (models.Model):
    IDreseña = models.AutoField(primary_key=True)
    IDprestamo = models.ForeignKey(prestamos,on_delete=models.CASCADE)
    comentario = models.TextField()
    puntuacion = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return self.IDreseña

class tipoPenalizaciones(models.Model):
    IDtipoPenalizacion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class penalizaciones(models.Model):
    IDpenalizacion = models.AutoField(primary_key=True)
    IDprestamo = models.ForeignKey(prestamos, on_delete=models.CASCADE)
    IDtipoPenalizacion = models.ForeignKey(tipoPenalizaciones, on_delete=models.CASCADE)
    estadoPenalizacion = models.SmallIntegerField()
    detalle = models.TextField()

    def __str__(self):
        return self.IDpenalizacion


class prestamoRecursos(models.Model):
    IDprestamoRecurso = models.AutoField(primary_key=True)
    IDrecurso = models.ForeignKey(recursosTecnologicos, on_delete=models.CASCADE)
    id = models.ForeignKey(User, on_delete=models.CASCADE)
    IDempleado = models.ForeignKey(empleados,on_delete=models.CASCADE)
    inicio = models.DateTimeField(auto_now_add=True)
    salida = models.DateTimeField()
    detalle = models.TextField()

    def __str__(self): 
        return self.IDprestamoRecurso

class historialVisitas(models.Model):
    IDvisita = models.AutoField(primary_key=True)
    id = models.ForeignKey(User, on_delete=models.CASCADE)
    salida = models.TimeField(null=True)
    entrada = models.DateTimeField(auto_now_add=True)
    presencial = models.SmallIntegerField(null=True, editable=True)

    def __str__(self):
        return self.IDvisita

class comentarios(models.Model):
    IDcomentario = models.AutoField(primary_key=True)
    libro = models.ForeignKey('Libros', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    comentario = models.TextField()

class contacto(models.Model):
    IDcontacto = models.AutoField(primary_key=True)
    nombreCompleto = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    telefono = models.CharField(max_length=25)
    mensaje = models.TextField()

    def __str__(self):
        return self.IDcontacto


    