from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from bibliotecaapp import forms
from bibliotecaapp import models
from bibliotecaapp.models import autores
from django.db.models import Q
from django.urls import reverse
from django.core.serializers import serialize
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from user.models import User
from django.contrib.auth.forms import UserCreationForm
from functools import wraps

from django.views.generic import (
View,
TemplateView,
ListView,
DetailView
)





#revisar el valor que retorna en los modelos 

#prueba Reserva No borrar o modificar >:C
def detalles_libro(request):
    libro_id = request.GET.get('id')

    try:
        libro = get_object_or_404(models.libros, IDlibro=libro_id)
        detalles = {
            'portada': libro.portada,
            'descripcion': libro.descripcion,
            'titulo': libro.titulo,
            # Otros campos que desees incluir
        }
        return JsonResponse(detalles)
    except models.libros.DoesNotExist:
        return JsonResponse({'error': 'Libro no encontrado'}, status=404)
    except Exception as e:
        print('Error en detalles_libro:', e)  # Imprimir en la consola de Django
        return JsonResponse({'error': str(e)}, status=500)
    


  
def detalles_autor(request):
    autor_id = request.GET.get('id')

    try:
        autor = get_object_or_404(models.autores, IDautor=autor_id)
        detalles = {
            'nombre': autor.nombre,
           
        }
        return JsonResponse(detalles)
    except models.autores.DoesNotExist:
        return JsonResponse({'error': 'Autor no encontrado'}, status=404)
    except Exception as e:
        print('Error en detalles_autor:', e)
        return JsonResponse({'error': str(e)}, status=500)    
    
def detalles_reserva(request):
    reservas_id = request.GET.get('id')

    try:
        reservas = get_object_or_404(models.Reservas, IDreserva=reservas_id)
        detalles = {
            'IDreserva': reservas.IDreserva,
            # Otros campos que desees incluir
        }
        return JsonResponse(detalles)
    except models.Reservas.DoesNotExist:
        return JsonResponse({'error': 'Reserva no encontrada'}, status=404)
    except Exception as e:
        print('Error en detalles_reservas:', e)  # Imprimir en la consola de Django
        return JsonResponse({'error': str(e)}, status=500)  
#General

#Login
#def login(request): 
    return render(request, 'registration/login.html')

def exit(request):
    logout(request)
    return redirect('indexUsuario')

def register(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)
        if user_creation_form.is_valid():
            user_creation_form.save()
            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            return redirect(indexUsuario)
        else:
            
            data['form'] = user_creation_form

    return render(request, 'registration/register.html', data)
    

def is_superuser_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_superuser:
            return redirect('/indexEmpleado')
        return view_func(request, *args, **kwargs)
    return _wrapped_view

@is_superuser_required
def indexUsuario(request):
    return render(request, 'usuario/index.html')

@user_passes_test(lambda u: u.is_superuser, login_url='/404')
def indexEmpleado(request):
    return render(request, 'empleado/index.html')

@is_superuser_required
def mostrarSobreNosotros(request):
    return render(request,'usuario/about.html')

def nada(request):
    return render(request,'usuario/nada.html')

def enviarCorreo(correo, nombreCompleto):
    context = {'correo': correo, 'nombreCompleto' : nombreCompleto}
    template = get_template('correo.html')
    content = template.render(context)
    correo = EmailMultiAlternatives(
        'Mensaje de contacto recibido - BiblioTech',
        'BiblioTech',
        settings.EMAIL_HOST_USER,
        [correo]
    )
    correo.attach_alternative(content, 'text/html')
    correo.send()

@is_superuser_required
def mostrarPreguntas(request):
    return render(request, 'usuario/faq.html') 

@is_superuser_required
def librosUsuarios(request):
    if request.method == 'GET':
        # Obtener parámetro de búsqueda desde la URL
        query = request.GET.get('q', '')

        # Imprimir para depuración
        print(f"Query: {query}")

        # Filtrar libros según el parámetro de búsqueda
        libros_filtrados = models.libros.objects.filter(
            Q(IDautor__nombre__icontains=query) |
            Q(titulo__icontains=query) |
            Q(IDgenero__nombreGenero__icontains=query)
        )

        # Imprimir para depuración
        print("Libros filtrados:", libros_filtrados)

        # Renderizar la página con los resultados filtrados y la query
        return render(request, 'usuario/libros.html', {'libros': libros_filtrados, 'query': query})

    # Renderizar la página sin filtros si no es una solicitud GET
    return render(request, 'usuario/libros.html', {})

@is_superuser_required
def libro(request):
    if request.method == 'GET':
        # Obtener parámetros de búsqueda desde la URL
        autor = request.GET.get('autor', '')
        titulo = request.GET.get('titulo', '')
        categoria = request.GET.get('categoria', '')

        # Filtrar libros según los parámetros de búsqueda
        libros_filtrados = models.Libros.objects.filter(
            Q(IDautor__nombre__icontains=autor) |
            Q(titulo__icontains=titulo) |
            Q(IDgenero__nombreGenero__icontains=categoria)
        )

        # Renderizar la página con los resultados filtrados
        return render(request, 'nombre_de_tu_template.html', {'libros': libros_filtrados})

    # Renderizar la página sin filtros si no es una solicitud GET
    return render(request, 'nombre_de_tu_template.html', {})

@is_superuser_required
def detalle_libro(request, IDlibro):
    libro = get_object_or_404(models.libros, IDlibro=IDlibro)

    if request.method == 'POST':
        form = forms.crearComentario(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.libro = libro
            comentario.save()
            return redirect('detalle_libro', IDlibro=IDlibro)
    else:
        form = forms.crearComentario()

    comentarios_libro = models.comentarios.objects.filter(libro=libro)

    return render(request, 'usuario/infoLibro.html', {'libro': libro, 'comentarios': comentarios_libro, 'form': form})

#Views de los formularios
@login_required
def vistaUsuarios(request):
    if request.method == 'POST':
        form = forms.crearUsuarios(request.POST)
        if form.is_valid():
            form.save()
            return redirect(mostrarUsuarios)
    else:
        form = forms.crearUsuarios()
    
    return render(request, 'empleado/formularios/crearUsuario.html', {'form': form})

def view404(request):
    return render(request,'404.html')


@login_required
def vistaAutores(request):
    if request.method == 'POST':
        form = forms.crearAutores(request.POST)
        if form.is_valid():
            form.save()
            return redirect(mostrarAutores)  
    else:
        form = forms.crearAutores()
    
    return render(request, 'empleado/formularios/crearAutor.html', {'form': form})


@login_required
def vistaEditoriales(request):
    if request.method == 'POST':
        form = forms.crearEditoriales(request.POST)
        if  form.is_valid():
                form.save()
                return redirect (mostrarEditoriales)
    else:
        form = forms.crearEditoriales()
    
    return render(request, 'empleado/formularios/crearEditorial.html', {'form': form})

@login_required
def vistaGeneros(request):
    if request.method == 'POST':
        form = forms.crearGeneros(request.POST)
        if  form.is_valid():
            form.save()
            return redirect (mostrarGeneros) 
    else:
        form = forms.crearGeneros()
    
    return render(request, 'empleado/formularios/crearGenero.html', {'form': form})

@login_required
def vistaRecursosTecnologicos(request):
    if request.method == 'POST':
        form = forms.crearRecursosTecnologicos(request.POST)
        if  form.is_valid():
                form.save()
                return redirect (mostrarRecursosTecnologicos)
    else:
        form = forms.crearRecursosTecnologicos()
        
    return render(request, 'empleado/formularios/crearRecursosTecnologicos.html', {'form': form})
@login_required
def vistaLibros(request):
    if request.method == 'POST':
        form = forms.crearLibros(request.POST)
        if form.is_valid():
            form.save() 
            return redirect (mostrarLibros)  
    else:
        form = forms.crearLibros()
    
    return render(request, 'empleado/formularios/crearLibros.html', {'form': form})

@login_required
def vistaCargos(request):
    if request.method == 'POST':
        form = forms.crearCargos(request.POST)
        if form.is_valid():
            form.save()
            return redirect(mostrarCargos)  
    else:
        form = forms.crearCargos()
        
    return render(request, 'empleado/formularios/crearCargo.html', {'form': form})

@login_required
def vistaEmpleado(request):
    if request.method == 'POST':
        form = forms.crearEmpleados(request.POST)
        if form.is_valid():
            form.save()
            return redirect(mostrarEmpleados)  
    else:
        form = forms.crearEmpleados()
    
    return render(request, 'empleado/formularios/crearEmpleado.html', {'form': form})

@login_required
def vistaPrestamos(request):
    if request.method == 'POST':
        form = forms.crearPrestamos(request.POST)
        if form.is_valid():
            prestamo = form.save(commit=False) 
            libro_prestado = prestamo.IDlibro
            libro_prestado.existencias -= 1
            libro_prestado.save()
            prestamo.save()  
            return redirect(mostrarPrestamos)
    else:
        form = forms.crearPrestamos()

    return render(request, 'empleado/formularios/crearPrestamos.html', {'form': form})

@is_superuser_required
@login_required
def vistaPrestamosUsuario(request):
    if request.method == 'POST':
        form = forms.crearPrestamos(request.POST)
        if form.is_valid():
            prestamo = form.save(commit=False) 
            libro_prestado = prestamo.IDlibro
            libro_prestado.existencias -= 1
            libro_prestado.save()
            prestamo.save()  
            return redirect(librosUsuarios)
    else:
        form = forms.crearPrestamos()

    return render(request, 'empleado/formularios/crearPrestamos.html', {'form': form})

@is_superuser_required
@login_required
def vistaReservasUsuario(request):
    if request.method == 'POST':
        form = forms.crearReservaUsuario(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.id = request.user
            reserva.username = request.user.username
            reserva.save()
            print("Reserva guardada exitosamente.")
            return redirect(librosUsuarios)
        else:
            print("Formulario no válido. Errores:", form.errors)
    else:
        form = forms.crearReservaUsuario()

    return render(request, 'usuario/crearReservaUsuario.html', {'form': form})



@login_required
def vistaReservas(request):
    if request.method == 'POST':
        form = forms.crearReservas(request.POST)
        if form.is_valid():
            form.save()
            return redirect()
    else:
        form = forms.crearReservas()

    return render(request, 'empleado/formularios/crearReservas.html', {'form': form})

@is_superuser_required
@login_required
def vistaReseñas(request):
    if request.method == 'POST':
        
        form = forms.crearReseñas(request.POST)
        if form.is_valid():
            codigo_prestamo = form.cleaned_data['codigo_prestamo']
            
            try:
                prestamo = models.prestamos.objects.get(IDprestamo=codigo_prestamo)
                form.instance.IDprestamo = prestamo
                form.save()
                return redirect(vistaReseñas)
            except models.prestamos.DoesNotExist:
                form.add_error('codigo_prestamo', 'El código de préstamo no es válido')
    else:
        form = forms.crearReseñas()

    return render(request, 'usuario/crearReseñas.html', {'form': form})


def get_loan_info(request, codigo_prestamo):
    try:
        prestamo = models.prestamos.objects.get(IDprestamo=codigo_prestamo)
        loan_info = prestamo.to_json()
        return JsonResponse(loan_info)
    except models.prestamos.DoesNotExist:
        return JsonResponse({'error': 'El código de préstamo no es válido.'})

@login_required
def vistaTipoPenalizacion(request):
    if request.method == 'POST':
        form = forms.crearTipoPenalizaciones(request.POST)
        if form.is_valid():
            form.save()
            return redirect(mostrarTipoPenalizacion)  
    else:
        form = forms.crearTipoPenalizaciones()
    
    return render(request, 'empleado/formularios/crearTipoPenalizaciones.html', {'form': form})

@login_required
def vistaPenalizaciones(request):
    if request.method == 'POST':
        form = forms.crearPenalizaciones(request.POST)
        if form.is_valid():
            form.save()
            return redirect(mostrarPenalizaciones)
    else:
        form = forms.crearPenalizaciones()

    return render(request, 'empleado/formularios/crearPenalizaciones.html', {'form': form})

@login_required
def vistaPrestamoRecursos(request):
    if request.method == 'POST':
        form = forms.crearPrestamoRecursos(request.POST)
        if form.is_valid():
            form.save()
            return redirect(mostrarPrestamosRecursos)
    else:
        form = forms.crearPrestamoRecursos()

    return render(request, 'empleado/formularios/crearPrestamoRecursos.html', {'form': form})

@login_required
def vistaHistorialVisitas(request):
    if request.method == 'POST':
        form = forms.crearHistorialVisitas(request.POST)
        if form.is_valid():
            if not form.cleaned_data['salida']:
                form.cleaned_data['salida'] = None
            form.save()
            return redirect(mostrarHistorialVisitas)  
    else:
        form = forms.crearHistorialVisitas()
    
    return render(request, 'empleado/formularios/crearHistorialVisitas.html', {'form': form})

@is_superuser_required
def vistaContacto(request):
    if request.method == 'POST':
        form = forms.crearContacto(request.POST)
        correo = request.POST.get('correo')
        nombre = request.POST.get('nombreCompleto')
        enviarCorreo(correo, nombre)
        if form.is_valid():
            form.save()
            return redirect('/indexContact/?ok') 
    else:
        form = forms.crearContacto()
    
    return render(request, 'usuario/contact.html', {'form': form})


#Views de las tablas 
@login_required
def mostrarUsers(request):
    listUsers = User.objects.all()
    return render(request, 'empleado/tablas/tablaUsersDjango.html', {'listUsers': listUsers})

@login_required
def mostrarAutores(request):
    listAutores = autores.objects.all()
    return render(request, 'empleado/tablas/tablaAutor.html', {'listAutores': listAutores})

@login_required
def mostrarUsuarios(request):
    listUsuarios = models.usuarios.objects.all()
    return render(request, 'empleado/tablas/tablaUsuarios.html', {'listUsuarios': listUsuarios})

@login_required
def mostrarGeneros(request):
    listGeneros = models.generos.objects.all()
    return render(request, 'empleado/tablas/tablaGeneros.html', {'listGeneros': listGeneros} )

@login_required
def mostrarEditoriales(request):
    listEditoriales = models.editoriales.objects.all()
    return render(request, 'empleado/tablas/tablaEditoriales.html', {'listEditoriales': listEditoriales} )

@login_required
def mostrarRecursosTecnologicos(request):
    listRecursosTecnologicos = models.recursosTecnologicos.objects.all()
    return render(request, 'empleado/tablas/tablaRecursosTecnologicos.html', {'listRecursosTecnologicos': listRecursosTecnologicos} )

@login_required
def mostrarLibros(request):
    listLibros = models.libros.objects.all()
    return render(request, 'empleado/tablas/tablaLibros.html', {'listLibros': listLibros} )

@login_required
def mostrarCargos(request):
    listCargos = models.cargos.objects.all()
    return render(request, 'empleado/tablas/tablaCargos.html', {'listCargos': listCargos} )

@login_required
def mostrarEmpleados(request):
   listEmpleados = models.empleados.objects.all()
   return render(request, 'empleado/tablas/tablaEmpleados.html', {'listEmpleados': listEmpleados})

@login_required
def mostrarPrestamos(request):
    listPrestamos = models.prestamos.objects.all()
    return render(request, 'empleado/tablas/tablaPrestamos.html', {'listPrestamos': listPrestamos} )

@login_required
def mostrarReservas(request):
    listReservas = models.reservasUsuarios.objects.all()
    return render(request, 'empleado/tablas/tablaReservas.html', {'listReservas': listReservas} )

@login_required
def mostrarReservasUsuarios(request):
    listReservasUsuarios = models.reservasUsuarios.objects.all()
    return render(request, 'empleado/tablas/tablaReservaUsuarios.html', {'listReservasUsuarios': listReservasUsuarios} )

@login_required
def mostrarReseñas(request):
    listReseñas = models.reseñas.objects.all()
    return render(request, 'empleado/tablas/tablaReseñas.html', {'listReseñas': listReseñas} )

@login_required
def mostrarPenalizaciones(request):
    listPenalizaciones = models.penalizaciones.objects.all()
    return render(request, 'empleado/tablas/tablaPenalizaciones.html', {'listPenalizaciones': listPenalizaciones} )

@login_required
def mostrarTipoPenalizacion(request):
    listTipoPenalizacion = models.tipoPenalizaciones.objects.all()
    return render(request, 'empleado/tablas/tablaTipoPenalizaciones.html', {'listTipoPenalizacion': listTipoPenalizacion} )

@login_required
def mostrarPrestamosRecursos(request):
    listPrestamosRecursos = models.prestamoRecursos.objects.all()
    return render(request, 'empleado/tablas/tablaPrestamoRecurso.html', {'listPrestamosRecursos': listPrestamosRecursos} )

@login_required
def mostrarContactosTabla(request):
    listContactos = models.contacto.objects.all()
    return render(request, 'empleado/tablas/tablaContactos.html', {'listContactos': listContactos} )

@login_required
def mostrarHistorialVisitas(request):
    listHistorialVisitas = models.historialVisitas.objects.all()
    return render(request, 'empleado/tablas/tablaHistorialVisitas.html', {'listHistorialVisitas': listHistorialVisitas} )

#Funciones para eliminar
def eliminarAutor(request, IDautor):
    autor = models.autores.objects.get(IDautor=IDautor)
    autor.delete()
    return redirect(mostrarAutores)

def eliminarUsuario(request, IDusuario):
    usuario = models.usuarios.objects.get(IDusuario=IDusuario)
    usuario.delete()
    return redirect(mostrarUsuarios)

def eliminarEditorial(request, IDeditorial):
    editorial = models.editoriales.objects.get(IDeditorial=IDeditorial)
    editorial.delete()
    return redirect(mostrarEditoriales)

def eliminarGenero(request, IDgenero):
    genero = models.generos.objects.get(IDgenero=IDgenero)
    genero.delete()
    return redirect(mostrarGeneros)

def eliminarCargo(request, IDcargo):
    cargo = models.cargos.objects.get(IDcargo=IDcargo)
    cargo.delete()
    return redirect(mostrarCargos)



def eliminarEmpleado(request, IDempleado):
    empleado = models.empleados.objects.get(IDempleado=IDempleado)
    empleado.delete()
    return redirect(mostrarEmpleados)

def eliminarLibro(request, IDlibro):
    libro = models.libros.objects.get(IDlibro=IDlibro)
    libro.delete()
    return redirect(mostrarLibros)

def eliminarPrestamo(request, IDprestamo):
    prestamo = models.prestamos.objects.get(IDprestamo=IDprestamo)
    prestamo.delete()
    return redirect(mostrarPrestamos)

def eliminarRecursoTecnologico(request, IDrecurso):
    recurso = models.recursosTecnologicos.objects.get(IDrecurso=IDrecurso)
    recurso.delete()
    return redirect(mostrarRecursosTecnologicos)

def eliminarPenalizacion(request, IDpenalizacion):
    penalizacion = models.penalizaciones.objects.get(IDpenalizacion=IDpenalizacion)
    penalizacion.delete()
    return redirect(mostrarPenalizaciones)

def eliminarReserva(request, IDreserva):
    reserva = models.reservas.objects.get(IDreserva=IDreserva)
    reserva.delete()
    return redirect(mostrarReservas)

def eliminarTipoPenalizacion(request, IDtipoPenalizacion):
    tipoPenalizacion = models.tipoPenalizaciones.objects.get(IDtipoPenalizacion=IDtipoPenalizacion)
    tipoPenalizacion.delete()
    return redirect(mostrarTipoPenalizacion)

def eliminarHistorialVisita(request, IDvisita):
    HistorialVisita = models.historialVisitas.objects.get(IDvisita=IDvisita)
    HistorialVisita.delete()
    return redirect(mostrarHistorialVisitas)

def eliminarPrestamoRecurso(request, IDprestamoRecurso):
    prestamoRecurso = models.prestamoRecursos.objects.get(IDprestamoRecurso=IDprestamoRecurso)
    prestamoRecurso.delete()
    return redirect(mostrarPrestamosRecursos)

def eliminarContacto(request, IDcontacto):
    contactos = models.contacto.objects.get(IDcontacto=IDcontacto)
    contactos.delete()
    return redirect(mostrarContactosTabla)



#Funciones para editar
def editarAutor(request, IDautor):
    autor = models.autores.objects.get(IDautor=IDautor)

    if request.method == 'POST':
        form = forms.crearAutores(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            return redirect(mostrarAutores)  
    else:
        form = forms.crearAutores(instance=autor)

    return render(request, "empleado/formularios/crearAutor.html", {'form': form, 'autor': autor})

def editarUsuario(request, IDusuario):
    usuario = models.usuarios.objects.get(IDusuario=IDusuario)

    if request.method == 'POST':
        form = forms.crearUsuarios(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect(mostrarUsuarios)  
    else:
        form = forms.crearUsuarios(instance=usuario)

    return render(request, "empleado/formularios/crearUsuario.html", {'form': form, 'usuario': usuario})

def editarEditorial(request, IDeditorial):
    editorial = models.editoriales.objects.get(IDeditorial=IDeditorial)

    if request.method == 'POST':
        form = forms.crearEditoriales(request.POST, instance=editorial)
        if form.is_valid():
            form.save()
            return redirect(mostrarEditoriales)   
    else:
        form = forms.crearEditoriales(instance=editorial)

    return render(request, "empleado/formularios/crearEditorial.html", {'form': form, 'editorial': editorial})

def editarCargo(request, IDcargo):
    cargo = models.cargos.objects.get(IDcargo=IDcargo)

    if request.method == 'POST':
        form = forms.crearCargos(request.POST, instance=cargo)
        if form.is_valid():
            form.save()
            return redirect(mostrarCargos)   
    else:
        form = forms.crearCargos(instance=cargo)

    return render(request, "empleado/formularios/crearCargo.html", {'form': form, 'cargo': cargo})

def editarGenero(request, IDgenero):
    genero = models.generos.objects.get(IDgenero=IDgenero)

    if request.method == 'POST':
        form = forms.crearGeneros(request.POST, instance=genero)
        if form.is_valid():
            form.save()
            return redirect(mostrarGeneros)   
    else:
        form = forms.crearGeneros(instance=genero)

    return render(request, "empleado/formularios/crearGenero.html", {'form': form, 'genero': genero})

def editarEmpleado(request, IDempleado):
    empleado = get_object_or_404(models.empleados, IDempleado=IDempleado)

    if request.method == 'POST':
        form = forms.crearEmpleados(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            # Puedes agregar un mensaje de éxito aquí si lo deseas
            return redirect('index_empleado')  # Redirige a la página de empleados
    else:
        form = forms.crearEmpleados(instance=empleado)

    return render(request, 'empleado/formularios/crearEmpleado.html', {'form': form, 'empleado': empleado})

        
    
def editarLibro(request, IDlibro):
    libro = models.libros.objects.get(IDlibro=IDlibro)

    if request.method == 'POST':
        form = forms.crearLibros(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect(mostrarLibros)   
    else:
        form = forms.crearLibros(instance=libro)

    return render(request, "empleado/formularios/crearLibros.html", {'form': form, 'libro': libro})

def editarPrestamo(request, IDprestamo):
    prestamo = models.prestamos.objects.get(IDprestamo=IDprestamo)

    if request.method == 'POST':
        form = forms.crearPrestamos(request.POST, instance=prestamo)
        if form.is_valid():
            form.save()
            return redirect(mostrarPrestamos)   
    else:
        form = forms.crearPrestamos(instance=prestamo)

    return render(request, "empleado/formularios/crearPrestamos.html", {'form': form, 'prestamo': prestamo})

def editarRecursoTecnologico(request, IDrecurso):
    recurso = models.recursosTecnologicos.objects.get(IDrecurso=IDrecurso)

    if request.method == 'POST':
        form = forms.crearRecursosTecnologicos(request.POST, instance=recurso)
        if form.is_valid():
            form.save()
            return redirect(mostrarRecursosTecnologicos)   
    else:
        form = forms.crearRecursosTecnologicos(instance=recurso)

    return render(request, "empleado/formularios/crearRecursosTecnologicos.html", {'form': form, 'recurso': recurso})

def editarPenalizacion(request, IDpenalizacion):
    penalizacion = models.penalizaciones.objects.get(IDpenalizacion=IDpenalizacion)

    if request.method == 'POST':
        form = forms.crearPenalizaciones(request.POST, instance=penalizacion)
        if form.is_valid():
            form.save()
            return redirect(mostrarPenalizaciones)   
    else:
        form = forms.crearPenalizaciones(instance=penalizacion)

    return render(request, "empleado/formularios/crearPenalizaciones.html", {'form': form, 'penalizacion': penalizacion})

def editarReserva(request, IDreserva):
    reserva = models.reservas.objects.get(IDreserva=IDreserva)

    if request.method == 'POST':
        form = forms.crearReservas(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return redirect(mostrarReservas)   
    else:
        form = forms.crearReservas(instance=reserva)

    return render(request, "empleado/formularios/crearReservas.html", {'form': form, 'reserva': reserva})

def editarTipoPenalizacion(request, IDtipoPenalizacion):
    tipoPenalizacion = models.tipoPenalizaciones.objects.get(IDtipoPenalizacion=IDtipoPenalizacion)

    if request.method == 'POST':
        form = forms.crearTipoPenalizaciones(request.POST, instance=tipoPenalizacion)
        if form.is_valid():
            form.save()
            return redirect(mostrarTipoPenalizacion)   
    else:
        form = forms.crearTipoPenalizaciones(instance=tipoPenalizacion)

    return render(request, "empleado/formularios/crearTipoPenalizaciones.html", {'form': form, 'tipoPenalizacion': tipoPenalizacion})

def editarHistorialVisitas(request, IDvisita):
    visita = models.historialVisitas.objects.get(IDvisita=IDvisita)

    if request.method == 'POST':
        form = forms.crearHistorialVisitas(request.POST, instance=visita) #cambiar form
        if form.is_valid():
            form.save()
            return redirect(mostrarHistorialVisitas)   
    else:
        form = forms.crearHistorialVisitas(instance=visita) #cambiar form

    return render(request, "empleado/formularios/crearHistorialVisitas.html", {'form': form, 'visita': visita})

def editarPrestamoRecurso(request, IDprestamoRecurso):
    prestamoRecurso = models.prestamoRecursos.objects.get(IDprestamoRecurso=IDprestamoRecurso)

    if request.method == 'POST':
        form = forms.crearPrestamoRecursos(request.POST, instance=prestamoRecurso) #cambiar form
        if form.is_valid():
            form.save()
            return redirect(mostrarPrestamosRecursos)   
    else:
        form = forms.crearPrestamoRecursos(instance=prestamoRecurso) #cambiar form

    return render(request, "empleado/formularios/crearPrestamoRecursos.html", {'form': form, 'prestamoRecurso': prestamoRecurso})


def prueba2(request):
    return render(request,'usuario/formulrioprueba(noborrar).html') 




class Error404View(TemplateView):
    template_name = "bibliotecaapp/error_404.html"


class Error505View(TemplateView):
    template_name = "error_500.html"

    @classmethod
    def as_error_view(cls):

        v = cls.as_view()
        def view(request):
            r = v(request)
            r.render()
            return r
        return view