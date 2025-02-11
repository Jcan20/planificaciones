from django.shortcuts import render
from .models import Constructora,Cliente,Vivienda,Actividad
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
# VIASTA DEL INICIO 
def inicio(request):
    return render(request, 'inicio.html')

#/VISTAS CONTRUCTORA/
#/                  /

# Listado de Constructoras
def listadoConstructoras(request):
    constructoras = Constructora.objects.all()
    return render(request, "Constructora/listadoConstructoras.html", {'constructoras': constructoras})

# Formulario de Nueva Constructora
def nuevaConstructora(request):
    return render(request, 'Constructora/nuevaConstructora.html')

# Guardar Constructora
def guardarConstructora(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '').strip()
        direccion = request.POST.get('direccion', '').strip()
        telefono = request.POST.get('telefono', '').strip()
        email = request.POST.get('email', '').strip()

        errors = {}
        if not nombre:
            errors['nombre'] = "El nombre es obligatorio."
        if not direccion:
            errors['direccion'] = "La dirección es obligatoria."
        if not telefono:
            errors['telefono'] = "El teléfono es obligatorio."
        if not email:
            errors['email'] = "El correo es obligatorio."
        
        if errors:
            for field, error_msg in errors.items():
                messages.error(request, error_msg)
            return redirect('nuevaConstructora')

        Constructora.objects.create(nombre=nombre, direccion=direccion, telefono=telefono, email=email)
        messages.success(request, "Constructora registrada exitosamente.")
        return redirect('listadoConstructoras')

    else:
        messages.error(request, "Método no permitido.")
        return redirect('nuevaConstructora')

# Editar Constructora
def editarConstructora(request, id):
    constructora = get_object_or_404(Constructora, id=id)
    return render(request, 'Constructora/editarConstructora.html', {'constructora': constructora})

# Actualizar Constructora
def actualizarConstructora(request):
    if request.method == 'POST':
        id = request.POST.get('id')  # Obtener el id de la constructora
        constructora = get_object_or_404(Constructora, id=id)

        nombre = request.POST.get('nombre', '').strip()
        direccion = request.POST.get('direccion', '').strip()
        telefono = request.POST.get('telefono', '').strip()
        email = request.POST.get('email', '').strip()

        # Validaciones
        if not nombre or not direccion or not telefono or not email:
            messages.error(request, "Todos los campos son obligatorios.")
            return redirect('editarConstructora', id=id)  # Redirigir de nuevo al formulario de edición

        # Actualizar los campos de la constructora
        constructora.nombre = nombre
        constructora.direccion = direccion
        constructora.telefono = telefono
        constructora.email = email
        constructora.save()

        messages.success(request, "Constructora actualizada correctamente.")
        return redirect('listadoConstructoras')

    else:
        messages.error(request, "Método no permitido.")
        return redirect('listadoConstructoras')

# Eliminar Constructora
def eliminarConstructora(request, id):
    constructoraEliminar = get_object_or_404(Constructora, id=id)
    constructoraEliminar.delete()
    messages.success(request, "Constructora eliminada exitosamente.")
    return redirect('listadoConstructoras')


#|METODOS DE CLIENTE|
# Listado de Clientes
def listadoClientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'Cliente/listadoClientes.html', {'clientes': clientes})

# Formulario de Nuevo Cliente
def nuevoCliente(request):
    return render(request, 'Cliente/nuevoCliente.html')

# Guardar Cliente
def guardarCliente(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '').strip()
        direccion = request.POST.get('direccion', '').strip()
        telefono = request.POST.get('telefono', '').strip()
        email = request.POST.get('email', '').strip()

        errors = {}
        if not nombre:
            errors['nombre'] = "El nombre es obligatorio."
        if not direccion:
            errors['direccion'] = "La dirección es obligatoria."
        if not telefono:
            errors['telefono'] = "El teléfono es obligatorio."
        if not email:
            errors['email'] = "El correo es obligatorio."
        
        if errors:
            for field, error_msg in errors.items():
                messages.error(request, error_msg)
            return redirect('nuevoCliente')

        Cliente.objects.create(nombre=nombre, direccion=direccion, telefono=telefono, email=email)
        messages.success(request, "Cliente registrado exitosamente.")
        return redirect('listadoClientes')

    else:
        messages.error(request, "Método no permitido.")
        return redirect('nuevoCliente')

# Editar Cliente
def editarCliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    return render(request, 'Cliente/editarCliente.html', {'cliente': cliente})

# Vista para actualizar el cliente
def actualizarCliente(request, id):  # Añadido el parámetro id
    if request.method == 'POST':
        cliente = get_object_or_404(Cliente, id=id)
        
        nombre = request.POST.get('nombre', '').strip()
        direccion = request.POST.get('direccion', '').strip()
        telefono = request.POST.get('telefono', '').strip()
        email = request.POST.get('email', '').strip()
        
        # Validaciones
        if not nombre or not direccion or not telefono or not email:
            messages.error(request, "Todos los campos son obligatorios.")
            return redirect('editarCliente', id=id)
        
        # Actualizar los campos del cliente
        cliente.nombre = nombre
        cliente.direccion = direccion
        cliente.telefono = telefono
        cliente.email = email
        cliente.save()
        
        messages.success(request, "Cliente actualizado correctamente.")
        return redirect('listadoClientes')
    
    else:
        messages.error(request, "Método no permitido.")
        return redirect('listadoClientes')

# Eliminar Cliente
def eliminarCliente(request, id):
    clienteEliminar = get_object_or_404(Cliente, id=id)
    clienteEliminar.delete()
    messages.success(request, "Cliente eliminado exitosamente.")
    return redirect('listadoClientes')

#|||vivienda from django.shortcuts import render, get_object_or_404, redirect

# Listado de Viviendas
def listadoViviendas(request):
    viviendas = Vivienda.objects.all()
    return render(request, 'Vivienda/listadoViviendas.html', {'viviendas': viviendas})

# Formulario de Nueva Vivienda
def nuevaVivienda(request):
    clientes = Cliente.objects.all()
    constructoras = Constructora.objects.all()
    return render(request, 'Vivienda/nuevoVivienda.html', {'clientes': clientes, 'constructoras': constructoras})

# Guardar Vivienda
def guardarVivienda(request):
    if request.method == 'POST':
        direccion = request.POST.get('direccion', '').strip()
        tipo = request.POST.get('tipo', '').strip()
        metros_cuadrados = request.POST.get('metros_cuadrados', '').strip()
        precio = request.POST.get('precio', '').strip()
        cliente_id = request.POST.get('cliente')
        constructora_id = request.POST.get('constructora')
        estado = request.POST.get('estado')

        # Validaciones
        errors = {}
        if not direccion:
            errors['direccion'] = "La dirección es obligatoria."
        if not tipo:
            errors['tipo'] = "El tipo es obligatorio."
        if not metros_cuadrados:
            errors['metros_cuadrados'] = "Los metros cuadrados son obligatorios."
        if not precio:
            errors['precio'] = "El precio es obligatorio."
        if not cliente_id:
            errors['cliente'] = "Debe seleccionar un cliente."
        if not constructora_id:
            errors['constructora'] = "Debe seleccionar una constructora."
        
        if errors:
            for field, error_msg in errors.items():
                messages.error(request, error_msg)
            return redirect('nuevaVivienda')

        cliente = get_object_or_404(Cliente, id=cliente_id)
        constructora = get_object_or_404(Constructora, id=constructora_id)

        Vivienda.objects.create(
            direccion=direccion,
            tipo=tipo,
            metros_cuadrados=metros_cuadrados,
            precio=precio,
            cliente=cliente,
            constructora=constructora,
            estado=estado
        )

        messages.success(request, "Vivienda registrada exitosamente.")
        return redirect('listadoViviendas')

    else:
        messages.error(request, "Método no permitido.")
        return redirect('nuevaVivienda')

# Editar Vivienda
def editarVivienda(request, id):
    vivienda = get_object_or_404(Vivienda, id=id)
    clientes = Cliente.objects.all()
    constructoras = Constructora.objects.all()
    return render(request, 'Vivienda/editarVivienda.html', {'vivienda': vivienda, 'clientes': clientes, 'constructoras': constructoras})

# Actualizar Vivienda
def actualizarVivienda(request, id):
    if request.method == 'POST':
        vivienda = get_object_or_404(Vivienda, id=id)

        direccion = request.POST.get('direccion', '').strip()
        tipo = request.POST.get('tipo', '').strip()
        metros_cuadrados = request.POST.get('metros_cuadrados', '').strip()
        precio = request.POST.get('precio', '').strip()
        cliente_id = request.POST.get('cliente')
        constructora_id = request.POST.get('constructora')
        estado = request.POST.get('estado')

        # Validaciones
        if not direccion or not tipo or not metros_cuadrados or not precio or not cliente_id or not constructora_id:
            messages.error(request, "Todos los campos son obligatorios.")
            return redirect('editarVivienda', id=id)

        cliente = get_object_or_404(Cliente, id=cliente_id)
        constructora = get_object_or_404(Constructora, id=constructora_id)

        vivienda.direccion = direccion
        vivienda.tipo = tipo
        vivienda.metros_cuadrados = metros_cuadrados
        vivienda.precio = precio
        vivienda.cliente = cliente
        vivienda.constructora = constructora
        vivienda.estado = estado
        vivienda.save()

        messages.success(request, "Vivienda actualizada correctamente.")
        return redirect('listadoViviendas')

    else:
        messages.error(request, "Método no permitido.")
        return redirect('editarVivienda', id=id)

# Eliminar Vivienda
def eliminarVivienda(request, id):
    vivienda = get_object_or_404(Vivienda, id=id)

    # Eliminar la vivienda seleccionada
    vivienda.delete()

    messages.success(request, "Vivienda eliminada correctamente.")
    return redirect('listadoViviendas')





#|--------actividad----|
def nuevaActividad(request):
    """Vista para mostrar el formulario de nueva actividad"""
    viviendas = Vivienda.objects.all()
    return render(request, 'Actividad/nuevaActividad.html', {
        'viviendas': viviendas
    })

def guardarActividad(request):
    """Vista para procesar y guardar una nueva actividad"""
    if request.method == 'POST':
        try:
            # Obtener datos del formulario
            vivienda_id = request.POST.get('vivienda')
            descripcion = request.POST.get('descripcion')
            fecha_inicio = request.POST.get('fecha_inicio')
            fecha_fin = request.POST.get('fecha_fin')
            estado = request.POST.get('estado')
            email = request.POST.get('email')
            foto = request.FILES.get('foto')

            # Validaciones
            if not vivienda_id or not descripcion or not fecha_inicio or not estado:
                messages.error(request, 'Por favor complete todos los campos obligatorios.')
                return redirect('nuevaActividad')

            # Validar email si se proporciona
            if email:
                try:
                    validate_email(email)
                except ValidationError:
                    messages.error(request, 'Por favor ingrese un correo electrónico válido.')
                    return redirect('nuevaActividad')

            # Crear nueva actividad
            actividad = Actividad(
                vivienda_id=vivienda_id,
                descripcion=descripcion,
                fecha_inicio=fecha_inicio,
                estado=estado,
                email=email
            )

            # Agregar campos opcionales si se proporcionan
            if fecha_fin:
                actividad.fecha_fin = fecha_fin
            if foto:
                actividad.foto = foto

            actividad.save()
            messages.success(request, 'Actividad registrada exitosamente.')
            return redirect('listadoActividades')

        except Exception as e:
            messages.error(request, f'Error al guardar la actividad: {str(e)}')
            return redirect('nuevaActividad')

    return redirect('nuevaActividad')

def listadoActividades(request):
    """Vista para mostrar el listado de actividades"""
    actividades = Actividad.objects.all().order_by('-fecha_inicio')
    return render(request, 'Actividad/listadoActividades.html', {
        'actividades': actividades
    })

def editarActividad(request, id):
    """Vista para mostrar el formulario de edición de actividad"""
    actividad = get_object_or_404(Actividad, id=id)
    viviendas = Vivienda.objects.all()
    return render(request, 'Actividad/editarActividad.html', {
        'actividad': actividad,
        'viviendas': viviendas
    })

def actualizarActividad(request, id):
    """Vista para procesar y actualizar una actividad existente"""
    if request.method == 'POST':
        try:
            actividad = get_object_or_404(Actividad, id=id)

            # Obtener datos del formulario
            vivienda_id = request.POST.get('vivienda')
            descripcion = request.POST.get('descripcion')
            fecha_inicio = request.POST.get('fecha_inicio')
            fecha_fin = request.POST.get('fecha_fin')
            estado = request.POST.get('estado')
            email = request.POST.get('email')
            foto = request.FILES.get('foto')

            # Validaciones
            if not vivienda_id or not descripcion or not fecha_inicio or not estado:
                messages.error(request, 'Por favor complete todos los campos obligatorios.')
                return redirect('editarActividad', id=id)

            # Validar email si se proporciona
            if email:
                try:
                    validate_email(email)
                except ValidationError:
                    messages.error(request, 'Por favor ingrese un correo electrónico válido.')
                    return redirect('editarActividad', id=id)

            # Actualizar actividad
            actividad.vivienda_id = vivienda_id
            actividad.descripcion = descripcion
            actividad.fecha_inicio = fecha_inicio
            actividad.estado = estado
            actividad.email = email

            # Actualizar campos opcionales si se proporcionan
            if fecha_fin:
                actividad.fecha_fin = fecha_fin
            if foto:
                actividad.foto = foto

            actividad.save()
            messages.success(request, 'Actividad actualizada exitosamente.')
            return redirect('listadoActividades')

        except Exception as e:
            messages.error(request, f'Error al actualizar la actividad: {str(e)}')
            return redirect('editarActividad', id=id)

    return redirect('listadoActividades')

def eliminarActividad(request, id):
    """Vista para eliminar una actividad"""
    try:
        actividad = get_object_or_404(Actividad, id=id)
        actividad.delete()
        messages.success(request, 'Actividad eliminada exitosamente.')
    except Exception as e:
        messages.error(request, f'Error al eliminar la actividad: {str(e)}')
    
    return redirect('listadoActividades')


from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def enviar_correo_actividad(request, id):
    try:
        actividad = get_object_or_404(Actividad, id=id)
        
        if not actividad.email:
            messages.error(request, 'Esta actividad no tiene un correo electrónico asociado.')
            return redirect('listadoActividades')
        
        # Preparar el contenido del correo
        context = {
            'actividad': actividad,
            'BASE_URL': request.build_absolute_uri('/')[:-1]
        }
        
        # Renderizar el template HTML
        html_message = render_to_string('email_template.html', context)
        plain_message = strip_tags(html_message)
        
        # Enviar el correo
        send_mail(
            subject='Detalles de la Actividad',
            message=plain_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[actividad.email],
            html_message=html_message,
            fail_silently=False,
        )
        
        messages.success(request, f'Correo enviado exitosamente a {actividad.email}')
    except Exception as e:
        messages.error(request, f'Error al enviar el correo: {str(e)}')
    
    return redirect('listadoActividades')
