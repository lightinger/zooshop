from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from django.contrib.auth import authenticate, login
from django.views import View
from django.views.generic import FormView
from django.contrib import messages
from users.models import User
from utils.send_email import send_email
from .forms import ContactForm
from . models import Category, Product, Basket, Brand, Contact, Subscribe
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    products = Product.objects.all()[:12]
    categories = Category.objects.all()[:6]
    context = {
        'products': products,
        'catalog': categories,
    }
    return render(request, 'index.html', context=context)


def catalog(request, **kwargs):
    category = get_object_or_404(Category, slug=kwargs.get('slug'))
    sort_option = request.GET.get('sort')

    products = Product.objects.filter(categories=category)

    if sort_option == 'price_low_to_high':
        products = products.order_by('price')
    elif sort_option == 'price_high_to_low':
        products = products.order_by('-price')

    paginator = Paginator(products, 12)
    page = request.GET.get('page')

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    max_page_display = 7
    current_page = products.number

    if paginator.num_pages <= max_page_display:
        page_range = range(1, paginator.num_pages + 1)
    elif current_page <= max_page_display // 2:
        page_range = range(1, max_page_display + 1)
    elif current_page >= paginator.num_pages - max_page_display // 2:
        page_range = range(paginator.num_pages - max_page_display + 1, paginator.num_pages + 1)
    else:
        page_range = range(current_page - max_page_display // 2, current_page + max_page_display // 2 + 1)

    context = {
        'products': products,
        'selected_category': category,
        'sort_option': sort_option,
        'page_range': page_range,
    }
    return render(request, 'shop-left-sidebar.html', context=context)


def about(request):
    brands = Brand.objects.all()
    context = {
        'brands': brands,
    }
    return render(request, 'about.html', context)


class ContactUsView(FormView):
    template_name = 'contact.html'
    model = Contact
    success_url = '/contact-us/'
    form_class = ContactForm

    def form_valid(self, form):
        contact, _ = Contact.objects.get_or_create(
            email=form.cleaned_data['email'],
            defaults={
                'name': form.cleaned_data['name'],
                'message': form.cleaned_data['message']
            }
        )
        send_email(
            subject='Thank you for your message!',
            to_email=[contact.email],
            message=f'Thank you for your message! {contact.name.title()}'
        )
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'message: ' f"Thank you {form.cleaned_data.get('name').upper()} for your massage"
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        messages.add_message(
            self.request,
            messages.WARNING,
            form.errors
        )
        return super().form_invalid(form)

    def form_invalid(self, form):
        messages.add_message(
            self.request,
            messages.WARNING,
            'message: ' f"Please send correct data"
        )
        return super().form_invalid(form)


def faq(request):
    context = {}
    return render(request, 'faq.html', context=context)


def product(request, **kwargs):
    single_product = get_object_or_404(Product, slug=kwargs.get('slug'))
    context = {
        'product': single_product,
    }
    return render(request, 'product-details.html', context=context)


def blog(request):
    context = {}
    return render(request, 'blog.html', context=context)


def blog_details(request):
    context = {}
    return render(request, 'blog-details.html', context=context)


def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def basket_remove(request, product_id):
    basket_item = get_object_or_404(Basket, user=request.user, product_id=product_id)
    if basket_item.quantity > 1:
        basket_item.quantity -= 1
        basket_item.save()
    else:
        basket_item.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def basket_view(request):
    basket_items = Basket.objects.filter(user=request.user)
    total_quantity = sum(item.quantity for item in basket_items)
    for item in basket_items:
        item.subtotal = item.product.price * item.quantity
    total_amount = sum(item.subtotal for item in basket_items)
    context = {
        'basket_items': basket_items,
        'total_quantity': total_quantity,
        'total_amount': total_amount
    }
    return render(request, 'basket.html', context)


class LoginRegisterView(View):
    template_name = 'login-register.html'
    register_success_template_name = 'register_success.html'
    login_success_template_name = 'login_success.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        if request.POST.get('submit_button') == 'Register':
            return self.register_user(request)
        elif request.POST.get('submit_button') == 'Login':
            return self.login_user(request)

        return render(request, self.template_name, {'error_message': 'Invalid form submission'})

    def register_user(self, request):
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            return render(request, self.template_name, {'error_message': 'Passwords do not match'})
        user = User.objects.create_user(email=email, password=password1)

        return render(request, self.register_success_template_name)

    def login_user(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(email=email, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, self.login_success_template_name)
            else:
                return render(request, self.template_name, {'error_message': 'Account is not active'})
        else:
            return render(request, self.template_name, {'error_message': 'Invalid login credentials'})


def checkout(request):
    context = {}
    return render(request, 'checkout.html', context=context)


def search_product(request):
    query = request.GET.get('s')
    sort_option = request.GET.get('sort')

    products = Product.objects.filter(title__icontains=query)

    if sort_option == 'price_low_to_high':
        products = products.order_by('price')
    elif sort_option == 'price_high_to_low':
        products = products.order_by('-price')

    paginator = Paginator(products, 12)
    page = request.GET.get('page')

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)


    max_page_display = 7
    current_page = products.number

    if paginator.num_pages <= max_page_display:
        page_range = range(1, paginator.num_pages + 1)
    elif current_page <= max_page_display // 2:
        page_range = range(1, max_page_display + 1)
    elif current_page >= paginator.num_pages - max_page_display // 2:
        page_range = range(paginator.num_pages - max_page_display + 1, paginator.num_pages + 1)
    else:
        page_range = range(current_page - max_page_display // 2, current_page + max_page_display // 2 + 1)

    context = {
        'products': products,
        'query': query,
        'sort_option': sort_option,
        'page_range': page_range,
    }
    return render(request, 'search_results.html', context=context)