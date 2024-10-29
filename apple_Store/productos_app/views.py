from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Pedido
from django.contrib.auth.decorators import login_required


def producto_list(request):
    productos = Producto.objects.all()
    return render(request, 'productos_app/producto_list.html', {'productos': productos})


def producto_detalle(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        cantidad = int(request.POST.get('cantidad', 1))
        subtotal = cantidad * producto.precio
        request.session['producto_id'] = producto.id
        request.session['cantidad'] = cantidad
        request.session['subtotal'] = float(subtotal)
        return redirect('realizar_compra')
    return render(request, 'productos_app/producto_detalle.html', {'producto': producto})


def realizar_compra(request):
    subtotal = request.session.get('subtotal', 0)
    producto_id = request.session.get('producto_id')
    cantidad = request.session.get('cantidad')
    producto = get_object_or_404(Producto, pk=producto_id)

    if request.method == 'POST':
        nombre_cliente = request.POST['nombre']
        direccion = request.POST['direccion']
        telefono = request.POST['telefono']
        email = request.POST['email']

        Pedido.objects.create(
            producto=producto,
            cantidad=cantidad,
            subtotal=subtotal,
            nombre_cliente=nombre_cliente,
            direccion=direccion,
            telefono=telefono,
            email=email
        )
        return redirect('confirmar_compra')
    return render(request, 'productos_app/realizar_compra.html', {'producto': producto, 'subtotal': subtotal})


def confirmar_compra(request):
    return render(request, 'productos_app/confirmar_compra.html')

def ubicacion(request):
    return render(request, 'productos_app/ubicacion.html')


@login_required
def ver_pedidos(request):
    pedidos = Pedido.objects.all()  
    return render(request, 'productos_app/ver_pedidos.html', {'pedidos': pedidos})
