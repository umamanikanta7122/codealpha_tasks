from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from .models import Product, Cart, Review, Order, OrderItem
import google.generativeai as genai
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


genai.configure(
    api_key="YOUR_API_KEY"

)

model = genai.GenerativeModel("gemini-2.0-flash-lite")


def login_user(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('/')

        else:
            return render(request, 'login.html', {
                'error': 'Invalid username or password'
            })

    return render(request, 'login.html')

@login_required(login_url='/login/')
def home(request):

    query = request.GET.get('q')
    category = request.GET.get('category')
    selected_category = request.GET.get('category')

    products = Product.objects.all()

    if query:
        products = products.filter(name__icontains=query)

    if category:
        products = products.filter(category=category)

    cart_items = Cart.objects.filter(user=request.user)

    cart_count = sum(item.quantity for item in cart_items)

    categories = Product.objects.values_list(
        'category',
        flat=True
    ).distinct()

    return render(request, 'home.html', {
        'products': products,
        'cart_count': cart_count,
        'product_count': products.count(),
        'categories': categories,
        'selected_category': selected_category,
    })


def product_detail(request, product_id):

    product = Product.objects.get(id=product_id)

    reviews = Review.objects.filter(
        product=product
    ).order_by('-created_at')

    return render(request, 'product_detail.html', {
        'product': product,
        'reviews': reviews
    })


@login_required(login_url='/login/')
def cart(request):

    cart_items = Cart.objects.filter(user=request.user)

    total = sum(item.product.price * item.quantity for item in cart_items)

    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total': total
    })


def remove_from_cart(request, cart_id):

    item = Cart.objects.get(id=cart_id, user=request.user)

    item.delete()

    return redirect('/cart/')

@login_required(login_url='/login/')
def add_to_cart(request, product_id):

    product = Product.objects.get(id=product_id)

    cart_item, created = Cart.objects.get_or_create(
        user=request.user,
        product=product
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('/')


def register(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            print("FORM VALID")

            user = form.save()

            login(request, user)

            print("USER LOGGED IN:", request.user.is_authenticated)

            return redirect('home')

        else:
            print(form.errors)

    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})


def logout_user(request):

    logout(request)

    return redirect('/login/')



@login_required(login_url='/login/')
def checkout(request):
    return render(request, 'checkout.html')



def increase_quantity(request, cart_id):

     item = Cart.objects.get(id=cart_id, user=request.user)

     item.quantity += 1

     item.save()

     return redirect('/cart/')
@login_required(login_url='/login/')
def order_success(request):

    if request.method == "POST":

        name = request.POST.get("name")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        payment = request.POST.get("payment")

        cart_items = Cart.objects.filter(user=request.user)

        total = sum(
            item.product.price * item.quantity
            for item in cart_items
        )

        order = Order.objects.create(
            user=request.user,
            customer_name=name,
            phone=phone,
            address=address,
            total_amount=total
        )

        for item in cart_items:

            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )

        cart_items.delete()

    return render(request, 'order_success.html')
    


def decrease_quantity(request, cart_id):

    item = Cart.objects.get(id=cart_id, user=request.user)

    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()

    return redirect('/cart/')

@login_required(login_url='/login/')
def add_review(request, product_id):

    if request.method == "POST":

        product = Product.objects.get(id=product_id)

        rating = request.POST.get('rating')

        comment = request.POST.get('comment')

        Review.objects.create(
            product=product,
            user=request.user,
            rating=rating,
            comment=comment
        )

    return redirect('product_detail', product_id=product_id)

@login_required(login_url='/login/')
def my_orders(request):

    orders = Order.objects.filter(
        user=request.user
    ).order_by('-created_at')

    return render(
        request,
        'my_orders.html',
        {
            'orders': orders
        }
    )


from django.http import JsonResponse

from django.http import JsonResponse

def chatbot(request):

    message = request.GET.get("message", "").lower()

    if "phone" in message:
        reply = "Check our Smartphones category."

    elif "laptop" in message:
        reply = "Check our Laptops category."

    elif "watch" in message:
        reply = "Check our Watches category."

    elif "order" in message:
        reply = "You can track orders from My Orders."

    else:
        reply = "Welcome to TechVerse! How can I help you today?"

    return JsonResponse({
        "reply": reply
    })