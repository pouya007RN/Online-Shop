from django.shortcuts import render
from .models import OrderItem, Order
from .forms import OrderCreateForm
from .tasks import order_created
from cart.cart import Cart


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])


            cart.clear()

            order_created.delay(order.id)
            Order.paid = True
            return render(request, 'order/created.html', {'order': order})

    else:
        form = OrderCreateForm()
    return render(request, 'order/create.html', {'cart': cart,
                                                 'form': form})

def download(request):
    return render(request, 'order/created.html',{})