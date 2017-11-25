from django.shortcuts import render


# Create your views here.
#from mysite.forms import ContactForm,ListForm,UserForm
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render,redirect
from TaxApp.forms import ProductForm
from TaxApp.models import Product,Code,Result,Taxation
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


'''

if request.user.is_authenticated():
        currentuser = request.user
        name=currentuser.first_name
        items = Borrower.objects.filter(borrower__icontains=name)
'''




#if request.user.is_authenticated():
@login_required
def bill(request):

    if request.user.is_authenticated():
        currentuser = request.user
        identity=currentuser.first_name
        bill= Result.objects.filter(identity__icontains=identity)
        print(bill)
        return render(request, 'bill.html',
                          {'bill': bill})







@login_required
def map(request):
    return render(request,'maps.html')

@login_required
def index(request):
    print("hi")
    return render(request,'index.html')


def about(request):
    return render(request,'about.html')

def gst_logout(request):
    if request.user.is_authenticated():
        logout(request)
        return render(request,'logout.html')  
    else:
        return HttpResponseRedirect('/login')


def gst_register(request):
    if request.method == 'POST':
        state = request.POST.get('state')
        username = request.POST.get('email')
        password = request.POST.get('password')
        name = request.POST.get('name')
        user = User.objects.create(
            first_name = name,
            last_name = state,
            username = username,
            )
        user.set_password(password)
        user.save()

        user = authenticate(username = username, password = password)
        login(request, user)
        return redirect('/inventory/')
    else:
        return render(request,'loginwithcss.html')   

def gst_login(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user :
            if user.is_active:
                login(request,user)
                return redirect('/inventory/')
            else:
                return HttpResponse('Disabled Account')
        else:
            return HttpResponse("Invalid Login details.Are you trying to Sign up?")
    else:
        return render(request,'loginwithcss.html')





@login_required
def index2(request):
    print("hello")
    print(request.user.is_authenticated())

    
    errors = []
    if 'q' and 'states' and 'count' in request.GET:

        q = request.GET['q']
        states=request.GET['states']
        count=request.GET['count']
        print(states)
        if not q:
            errors.append('Enter a valid barcode')
            print("helllo")
        
        else:
         
            if request.user.is_authenticated():
                currentuser = request.user
                print(currentuser)
                identity=currentuser.first_name
                email=currentuser.username
                state=currentuser.last_name
                #print (q)
                #print (email)
                text = q.split()
                scan=text[1]
                #print(scan)
                items = Product.objects.filter(email__icontains=email, product_name__icontains=scan)
                #print (items)
                #print(len(items))
                
                item=items[0]

              
                cp=item.cost_price
                sp=item.selling_price
                quantity=item.quantity
                hsn=item.category


                taxlist = Taxation.objects.filter(code__icontains=hsn)
                taxes=taxlist[0]
                cgst=taxes.cgst
                igst=taxes.igst
                sgst=taxes.sgst
                #print(cgst,igst,sgst)
                profit=sp-cp
                if state==states:
                    value=1
                else:
                    value=0

                tax1=(cgst*sp)/100

                if value:
                    tax3=0
                    tax2=(sgst*sp)/100
                else:
                    tax2=0
                    tax3=(igst*sp)/100





                print("Before result")

                Result.objects.create(identity=identity,product_name=scan,quantity=count,cost_price=cp,selling_price=sp,profit=profit,hsn=hsn,tax1=tax1,tax2=tax2,tax3=tax3)

                return render(request, 'index2.html')
        
    return render(request, 'index2.html',
              {'errors': errors})





@login_required
def  inventory(request):
    if request.method == 'POST':
        form = ProductForm(request.POST ,request.FILES or None )
        if form.is_valid():
            cd = form.cleaned_data
            if request.user.is_authenticated():
                currentuser = request.user
                email=currentuser.username


                Product.objects.create(product_name=cd['product_name'],quantity=cd['quantity'],cost_price=cd['cost_price'],selling_price=cd['selling_price'],email=email,category=cd['category'])
        		
            
        form = ProductForm()    
        return render(request,'inventorywithcss.html',{'form': form})               
    else:
        form = ProductForm()
    return render(request, 'inventorywithcss.html', {'form': form})    

