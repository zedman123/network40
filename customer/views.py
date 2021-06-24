from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from .models import Snippet, Category, Customer
from django.views.generic import ListView, DetailView
from .filters import CustomerFilter
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import CustomerForm
from django.contrib.auth.models import User, auth
from .forms import SplitterForm
from .models import Splitter


def index(request):
    categories = Category.objects.filter(status='false')

    return render(request, 'index.html', {'category': categories})


def customer(request):
    return render(request, "customer.html", {'customer': Customer.objects.all()})


def home(request):
    return render(request, 'home.html')


def gpon(request):
    all_nodes = Category.objects.filter(status='splitter32')
    splitter_2 = Category.objects.filter(status='splitter2')
    return render(request, 'gpon.html', {'cat': all_nodes,
                                         'cats': splitter_2
                                         })


def organic(request):
    return render(request, 'organic.html')


def customer_list(request):
    all_customers = Customer.objects.all()

    return render(request, 'customer_list.html', {'customers': all_customers,

                                                  })


class CustomerListView(ListView):
    model = Customer
    template_name = 'customer_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = CustomerFilter(self.request.GET, queryset=self.get_queryset())


class CatListView(ListView):
    template_name = 'gpon.html'
    context_object_name = 'catlist'

    def get_queryset(self):
        content = {
            'cat': self.kwargs['category'],
            'customers': Customer.objects.filter(category__name=self.kwargs['category']).filter(
                status='True')
        }
        return content


class CustomerDetailView(DetailView):
    model = Customer
    fields = ['name', 'address', 'phone']


class CategoryDetailView(DetailView):
    model = Category
    fields = ['name', 'location']


def details(request, id):
    context = {}
    category = Category.objects.get(id=id)
    return render(request, 'details.html', {'category': category})


def customers_on_splitter(request, id):
    context = {}
    splitter_customers = Customer.objects.filter(id=id)
    return render(request, 'customers_on_splitter.html', {'customers': splitter_customers
                                                          })


def login1(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.info(request, 'You have succesfully logged in')
            return redirect("{% url 'welcome' %}")

        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')

    return render(request, 'login1.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password == '':
            messages.info(request, 'please enter a password')
        elif password2 == '':
            messages.info(request, 'you did not confirm the password')
        elif username == '':
            messages.info(request, 'you did not enter a username')
        elif password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email already exists')
            else:
                user = User.objects.create_user(username=username, password=password, email=email,
                                                first_name=first_name,
                                                last_name=last_name)
                user.save()
                messages.info(request, 'user created')
                return redirect('login')
        else:
            messages.info(request, 'password not matching')
        return redirect('register')

    else:
        return render(request, 'login1.html')


def show_customers(request):
    all_customers = Customer.objects.all()
    split_customers = Customer.objects.all()
    return render(request, "show_customers.html",
                  {'customer': all_customers,
                   'customers': split_customers,
                   })


def welcome(request):
    return render(request, "welcome.html")


def add_customer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST or None)
        if form.is_valid():
            form.save()
        else:
            splitter32 = request.POST['splitter32']
            name = request.POST['name']
            address = request.POST['address']
            phone = request.POST['phone']
            gps = request.POST['gps']

            ont = request.POST['ont']
            service_id = request.POST['service_id']
            parent = request.POST['parent']
            status = request.POST['status']

            messages.success(request, 'There is an error in the form')
            # return redirect('join')
            return render(request, 'customers/add_customer.html', {'splitter32': splitter32,
                                                                   'name': name,
                                                                   'address': address,
                                                                   'phone': phone,
                                                                   'gps': gps,
                                                                   'ont': ont,
                                                                   'service_id': service_id,
                                                                   'parent': parent,
                                                                   'status': status,
                                                                   })

        messages.success(request, 'The new customer has been successfully added')
        return redirect('home')
    else:
        return render(request, 'add_customer.html', {})


def add_splitter(request):
    if request.method == "POST":
        form = SplitterForm(request.POST or None)
        if form.is_valid():
            form.save()
        else:
            sid = request.POST['sid']
            location = request.POST['location']
            landmark = request.POST['landmark']
            gps = request.POST['gps']
            olt = request.POST['olt']
            port = request.POST['port']
            customers = request.POST['customers']
            noc = request.POST['noc']
            usage = request.POST['usage']
            disttoolt = request.POST['disttoolt']
            opl = request.POST['opl']
            notes = request.POST['notes']

            messages.success(request, 'There is an error in the form')
            # return redirect('join')
            return render(request, 'add_splitter.html', {'sid': sid,
                                                         'location': location,
                                                         'landmark': landmark,
                                                         'gps': gps,
                                                         'olt': olt,
                                                         'port': port,
                                                         'customers': customers,
                                                         'noc': noc,
                                                         'usage': usage,
                                                         'disttoolt': disttoolt,
                                                         'opl': opl,
                                                         'notes': notes,
                                                         })

        messages.success(request, 'The new splitter has been successfully added')
        return redirect('home')
    else:
        return render(request, 'add_splitter.html', {})


def customer_details(request, id):
    context = {}
    customers_full_details = Customer.objects.get(id=id)
    return render(request, 'customer_details.html', {'customer': customers_full_details})
