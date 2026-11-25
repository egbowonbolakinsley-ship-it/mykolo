from django.shortcuts import render, redirect
from .models import Products, ProductSpec, Category
from .forms import ProductForm

# Create your views here.


# functions based view
# class based view

def homeView(request):
    username = "Kingsley"
    products = Products.objects.all()[:3]
    return render(
        request, 
        template_name="index.html",
        context={
            "username": username,
           "products": products
        }
        
        
    )


def aboutView(request):

    return render(request, template_name="about.html")



def productView(request):

    products = Products.objects.all()
    # products = Products.objects.filter(quantity__gte = 20)
    # products = Products.objects.filter(quantity__lte = 20)
    # products = Products.objects.filter(title__icontains = "Gucci")
    # products = Products.objects.filter(category__id = 1)
    # products = Products.objects.filter(category__name__icontains = "elec")
    print(products)

    # product = Products.objects.get(id = 1)
    # specs = ProductSpec.objects.filter(product = product)
    # print(specs)


    # print(product.specs.all())
    # print(product.descrption)


    return render(
            request, 
            template_name="product.html",
            context={
                "products": products
            }
        ) 

def singleProduct(request, id):
    product = Products.objects.get(id = id)
    
    return render(
        request,
        template_name="single.html",
        context= {
            "product": product
        }
    )

def addProductView(request):

    if request.method=="POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

        return redirect("products")

    else:

        form = ProductForm()
        return render(
            request,
            template_name="form.html",
            context={
                "form": form

            }


        )