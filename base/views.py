from django.shortcuts import redirect, render
from . models import ProductsModel,Category,CartModel
from django.db.models import Q

def home(request):
    trend=False
    offer=False

    if 'q' in request.GET:
        q=request.GET['q']
        try:
            category=Category.objects.get(category_name__icontains=q)
            all_products=ProductsModel.objects.filter(products_category=category)
        except:
            all_products=ProductsModel.objects.filter(
            Q(product_name__icontains=q)| 
            Q(product_desc__icontains=q)|
            Q(product_price__icontains=q))

    elif 'category_nav' in request.GET:
        category_nav=request.GET['category_nav']
        cat=Category.objects.get(category_name=category_nav)
        all_products=ProductsModel.objects.filter(product_category=cat)

    elif 'trending' in request.GET:
        all_products=ProductsModel.objects.filter(trending=True)
        trend=True
    
    elif 'offer' in request.GET:
        all_products=ProductsModel.objects.filter(offer=True)
        offer=True

    else:
        all_products=ProductsModel.objects.all()
    
    all_categories=Category.objects.all()
    context={'all_products':all_products,'all_categories':all_categories,'trend': trend,'offer':offer}
    return render(request, 'home.html',context)


def add_products(request):
    if request.method=='POST':
        product_category=request.POST['category']
        product_name=request.POST.get('product_name')
        product_desc=request.POST['product_desc']
        product_price=request.POST['product_price']
        product_image=request.FILES.get('product_image','Default.jpg')
        print(product_image,product_category,product_name,product_desc,product_price)
        Category_instance=Category.objects.get(category_name=product_category)

        ProductsModel.objects.create(
            product_category=Category_instance,
            product_name=product_name,
            product_desc=product_desc,
            product_price=product_price,
            product_image=product_image)
        return redirect('home')
    all_categories=Category.objects.all()
    return render(request, 'add_products.html',{'all_categories':all_categories,'add_products':True})


def product_detail(request, pk):
    pro = ProductsModel.objects.get(id=pk)
    return render(request, 'product_detail.html', {'product': pro})


def cart(request):
    cartproducts=CartModel.objects.filter(host=request.user)
    totalamount=0
    for i in cartproducts:
        totalamount+=i.totalprice
    return render(request,'cart.html',{'cartproducts':cartproducts,'ta':totalamount,'cart':True,'cart_count':cart_count(request)})



def addtocart(request,pk):
    pro=ProductsModel.objects.get(id=pk)
    try:
        c=CartModel.objects.get(Q(products_name=pro.product_name)&Q(host=request.user))
        c.quantity+=1
        c.totalprice+=pro.product_price
        c.save()
        return redirect('cart')
    except:
        CartModel.objects.create(
            products_name=pro.product_name,
            products_desc=pro.product_desc,
            products_price=pro.product_price,
            product_category=pro.product_category,
            quantity=1,
            totalprice=pro.product_price,
            host=request.user
    )
    return redirect('cart')

def cart_count(request):
    return CartModel.objects.filter(host=request.user).count()


def support(request):
    return render(request, 'support.html',{'support':True})

def knowus(request):
    return render(request, 'knowus.html',{'knowus':True})




def update_cart(request,pk,op):
    cart_item=CartModel.objects.get(id=pk)
    pro=ProductsModel.objects.get(product_name=cart_item.products_name)
    if op == '+':
        cart_item.quantity+=1
        cart_item.totalprice+=pro.product_price
        cart_item.save()
    else:
        cart_item.quantity-=1
        cart_item.totalprice-=pro.product_price
        cart_item.save()
        if cart_item.quantity==0:
            cart_item.delete()
    return redirect('cart')

def remove_from_cart(request,pk):
    cart_item=CartModel.objects.get(id=pk)
    cart_item.delete()
    return redirect('cart')
