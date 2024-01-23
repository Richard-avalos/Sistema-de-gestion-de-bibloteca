"""
URL configuration for biblioteca project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from bibliotecaapp import views
from bibliotecaapp.views import  indexUsuario
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
# importacion para el error 404
from django.conf.urls import handler404, handler500
# se importa la view desde views usando la class y el template
from bibliotecaapp.views import Error404View, Error505View



urlpatterns = [
    path('admin/', admin.site.urls),

    #login
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', views.exit, name='exit'),
    path('login/', views.login),
    path('register/', views.register, name='register'),  

    path('', views.indexUsuario),
    

    
    path('indexUsuario/indexLibros/', views.librosUsuarios, name='librosUsuarios'),

    #No Borrar
    path('api/detalles_libro/', views.detalles_libro, name='detalles_libro'),
    
    path('api/detalles_autor/', views.detalles_autor, name='detalles_autor'),

    #General :)
     
    path('indexEmpleado/', views.indexEmpleado),
    path('indexUsuario/', views.indexUsuario, name='indexUsuario'),
    path('indexAbout/',views.mostrarSobreNosotros),
    path('indexContact/',views.vistaContacto),
    path('indexPreguntas/',views.mostrarPreguntas),


            
    path('indexUsuario/indexLibros/', views.librosUsuarios) ,


    path('crearReseña/', views.vistaReseñas, name='crear_resena'),
    path('api/get_loan_info/<int:codigo_prestamo>/', views.get_loan_info, name='get_loan_info'),

    path('crearReserva/', views.vistaReservasUsuario, name='crear_reserva'),
    
    
    path('indexUsuario/indexLibros/libros/<int:IDlibro>/', views.detalle_libro, name='detalle_libro'),
    path('indexUsuario/prestamos/crearPrestamosUsuarios/', views.vistaPrestamosUsuario),

    
   
    #formularios :)

    path('indexEmpleado/autores/crearAutor/', views.vistaAutores),
    path('indexEmpleado/usuarios/crearUsuario/', views.vistaUsuarios),
    path('indexEmpleado/editoriales/crearEditorial/', views.vistaEditoriales),
    path('indexEmpleado/generos/crearGenero/', views.vistaGeneros),
    path('indexEmpleado/recursosTecnologicos/crearRecursosTecnologicos/', views.vistaRecursosTecnologicos),
    path('indexEmpleado/libros/crearLibros/', views.vistaLibros),
    path('indexEmpleado/cargos/crearCargo/', views.vistaCargos),
    path('indexEmpleado/empleados/crearEmpleado/', views.vistaEmpleado),
    path('indexEmpleado/prestamos/crearPrestamos/', views.vistaPrestamos),
    path('indexEmpleado/tipoPenalizacion/crearTipoPenalizaciones/', views.vistaTipoPenalizacion),
    path('indexEmpleado/reservas/crearReservas/', views.vistaReservas),    
    path('indexEmpleado/penalizaciones/crearPenalizaciones/', views.vistaPenalizaciones),
    path('indexEmpleado/prestamoRecurso/crearPrestamoRecursos/', views.vistaPrestamoRecursos),
    path('indexEmpleado/historialVisitas/crearHistorialVisitas/', views.vistaHistorialVisitas),
    path('indexUsuario/reservas/crearReservas/', views.vistaReservasUsuario),
    

    
  

    #reseña del usuario
    path('crearReseña/', views.vistaReseñas),


    #tablas
    path('indexEmpleado/reservaUsuario/', views.mostrarReservasUsuarios),
    path('indexEmpleado/users/', views.mostrarUsers),
    path('indexEmpleado/autores/', views.mostrarAutores),
    path('indexEmpleado/usuarios/', views.mostrarUsuarios),
    path('indexEmpleado/editoriales/', views.mostrarEditoriales),
    path('indexEmpleado/generos/', views.mostrarGeneros),
    path('indexEmpleado/recursosTecnologicos/', views.mostrarRecursosTecnologicos),
    path('indexEmpleado/libros/', views.mostrarLibros),
    path('indexEmpleado/cargos/', views.mostrarCargos),
    path('indexEmpleado/empleados/', views.mostrarEmpleados),
    path('indexEmpleado/prestamos/', views.mostrarPrestamos),
    path('indexEmpleado/tipoPenalizacion/', views.mostrarTipoPenalizacion),
    path('indexEmpleado/prestamoRecurso/', views.mostrarPrestamosRecursos),
    path('indexEmpleado/historialVisitas/', views.mostrarHistorialVisitas),
    path('indexEmpleado/penalizaciones/', views.mostrarPenalizaciones),
    path('indexEmpleado/reservas/', views.mostrarReservas),
    path('indexEmpleado/contactos/', views.mostrarContactosTabla),
    path('indexEmpleado/reseñas/', views.mostrarReseñas),
    



    #Editar registros
    path('indexEmpleado/autores/editarAutor/<int:IDautor>/', views.editarAutor),
    path('indexEmpleado/usuarios/editarUsuario/<int:IDusuario>/', views.editarUsuario),
    path('indexEmpleado/editoriales/editarEditorial/<int:IDeditorial>/', views.editarEditorial),
    path('indexEmpleado/cargos/editarCargo/<int:IDcargo>/', views.editarCargo),
    path('indexEmpleado/generos/editarGenero/<int:IDgenero>/', views.editarGenero),
    path('indexEmpleado/empleados/editarEmpleado/<int:IDempleado>/', views.editarEmpleado, name='editar_empleado'),
    path('indexEmpleado/libros/editarLibro/<int:IDlibro>/', views.editarLibro),
    path('indexEmpleado/prestamos/editarPrestamo/<int:IDprestamo>/', views.editarPrestamo),
    path('indexEmpleado/recursosTecnologicos/editarRecursoTecnologico/<int:IDrecurso>/', views.editarRecursoTecnologico),
    path('indexEmpleado/penalizaciones/editarPenalizacion/<int:IDpenalizacion>/', views.editarPenalizacion),
    path('indexEmpleado/reservas/editarReserva/<int:IDreserva>/', views.editarReserva),
    path('indexEmpleado/tipoPenalizacion/editarTipoPenalizacion/<int:IDtipoPenalizacion>/', views.editarTipoPenalizacion),
    path('indexEmpleado/historialVisitas/editarHistorialVisita/<int:IDvisita>/',views.editarHistorialVisitas),
    path('indexEmpleado/prestamoRecurso/editarPrestamoRecurso/<int:IDprestamoRecurso>', views.editarPrestamoRecurso),


    #Eliminar registro
    path('indexEmpleado/autores/eliminarAutor/<IDautor>', views.eliminarAutor),
    path('indexEmpleado/usuarios/eliminarUsuario/<IDusuario>', views.eliminarUsuario),
    path('indexEmpleado/editoriales/eliminarEditorial/<IDeditorial>', views.eliminarEditorial),
    path('indexEmpleado/cargos/eliminarCargo/<IDcargo>', views.eliminarCargo),
    path('indexEmpleado/generos/eliminarGenero/<IDgenero>', views.eliminarGenero),
    path('indexEmpleado/empleados/eliminarEmpleado/<IDempleado>', views.eliminarEmpleado),
    path('indexEmpleado/libros/eliminarLibro/<IDlibro>', views.eliminarLibro),
    path('indexEmpleado/prestamos/eliminarPrestamo/<IDprestamo>', views.eliminarPrestamo),
    path('indexEmpleado/recursosTecnologicos/eliminarRecursoTecnologico/<IDrecurso>', views.eliminarRecursoTecnologico),
    path('indexEmpleado/penalizaciones/eliminarPenalizacion/<IDpenalizacion>',views.eliminarPenalizacion),
    path('indexEmpleado/reservas/eliminarReserva/<IDreserva>',views.eliminarReserva),
    path('indexEmpleado/tipoPenalizacion/eliminarTipoPenalizacion/<IDtipoPenalizacion>', views.eliminarTipoPenalizacion),
    path('indexEmpleado/prestamoRecurso/eliminarPrestamoRecurso/<IDprestamoRecurso>', views.eliminarPrestamoRecurso),
    path('indexEmpleado/historialVisitas/eliminarHistorialVisita/<IDvisita>', views.eliminarHistorialVisita),
    path('indexEmpleado/contactos/eliminarContacto/<IDcontacto>', views.eliminarContacto),




    #prueba
    
    path('formularioprueba',views.prueba2)




]  

handler404 = Error404View.as_view()

handler500 = Error505View.as_error_view()