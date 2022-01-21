from django.http.response import HttpResponseRedirect
from app1.templates.forms import proform
from app1.models import *
from .forms import *
from django.shortcuts import render ,redirect,get_object_or_404
from django.http import HttpResponse, request
# from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db.models import Q
import random
import qrcode
import os
import razorpay

from firstproj.settings import BASE_DIR
from email.message import EmailMessage
import smtplib
from django.views.decorators.csrf import csrf_exempt


# from .models import products,login
# Create your views here.
def hello(self):
    return HttpResponse("Successfully Logged -in !")
def home(self):
    return render(self,'index3.html')

def gallery(request):
        return render(request,'gallery.html')

def clean(request):
    return render(request,'index1.html')

def page(self):
    obj = products.objects.all()
    return render(self,'index3.html',{'xyz':obj})

def page1(self): 
    obj1 = products.objects.filter(name='Gas')
    return render(self,'index3.html',{'abc':obj1})

def page2(self): 
    obj2 = products.objects.filter(pk=1)
    return render(self,'index3.html',{'pqr':obj2})

def regist1(request):
    if request.POST:

        name = request.POST['email1']
        passa = request.POST['pass1']

        try:
            check = signup.objects.get(Email=name)

            if check.Password == passa:
                w = login()
                w.Email = name
                w.Password = passa
                w.save()
                request.session['Email']=check.Email
                return redirect('home')
                
            else:
                msg = 'Input Right value'
                return render(request , 'index5.html',{'msg':msg}) 
        except:
            # msg = 'Wrong Username'
            return render(request,'index5.html', {'msg':msg})
    return render(request,'index5.html')   


def regist(request):
    if request.POST:
        name2 = request.POST['name1']
        e_mail = request.POST['email1']
        passd = request.POST['pass1']
        passe = request.POST['pass2']
        changi = request.POST['pass3']

        try:
            if passe == passd:
                v = signup()
                v.Username = name2
                v.Email = e_mail
                v.Password = passd
                v.Password1 = passe
                v.forgot_ans = changi
                v.save()
                return redirect('regi1')
            else:
                msg1 = 'Enter Same Password'
                return render(request , 'index4.html',{'msg1':msg1}) 
        finally:
            return redirect('regi1')   

    return render(request,'index4.html')
    # return render(self,'reg.html',{'data':a,"v":b})

def Confirm(request):
    if request.POST:
        data = request.POST['conf1']
        try:
            valid = signup.objects.get(forgot_ans=data)
            if valid:
                request.session['Email'] = valid.Email
                return redirect('forgot')
            else:
                return HttpResponse('that is it')    
        except:
            return HttpResponse('Wrong Answer')
    return render(request,'conf_pass.html')

def forgot(request):
    if 'Email' in request.session:
        if request.POST:
            pass1 = request.POST['pass11']
            pass2 = request.POST['pass22']
            print(pass1,pass2)
            
            if pass1 == pass2:
                obj = signup.objects.get(Email=request.session['Email'])
                obj.Password = pass2
                obj.save()
                del request.session['user']
                return redirect('regi1')
            else:
                messages.add_message(request, messages.ERROR, 'Not Same')
            
        return render(request,'pass_changer.html')
    return redirect('regi1')












def index(request):
    if 'Email' in request.session.keys():
        per = signup.objects.get(Email = request.session['Email'])
        return render(request,'index.html',{'USER':per})
    else:
        return redirect('regi1')

def items1(request):
    obj3 = items.objects.all()
    s = request.GET.get('search')
    if s:
        e=items.objects.filter(Q(Title__icontains=s) | Q(Description__icontains=s | Q(Description__icontains=s))).distinct()
    else: 
        e = items.objects.all()
    return render(request,'index1.html',{'itm':obj3,'r':e})

# def book_list(request):
#     book = items.objects.all()

#     return render(request, 'index1.html', {'object_list':book})

def book_view(request, pk):
    book= get_object_or_404(items, pk=pk)    
    return render(request,'review.html', {'object':book})

def book_update(request, pk):
    book= get_object_or_404(items, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('item')
    return render(request, 'update.html', {'form':form})



def book_delete(request, pk):
    book= get_object_or_404(items, pk=pk)    
    # if request.method=='POST':
    book.delete()
    return redirect('item')
    # return render(request, 'delete.html', {'object':book})







def add_to_cart(request):
    if request.session.has_key('Email'):
        per = signup.objects.get(Email=request.session['Email'])
        citem = Mycart.objects.filter(person__id=per.id, status=False)
        obj = Mycart.objects.filter(person__id=per.id, status=False)
        num = Mycart.objects.filter(person__id=per.id, status=False).count()
        total = 0
        for q in citem:
            total += q.Item.Price
        total1 = total*100
        print(total)

        if request.method == 'POST':
            bid = request.POST['bid']
            print(bid)  
            p = items.objects.get(id=bid)
            citem = Mycart.objects.filter(person__id=per.id, status=False)

            if Mycart.objects.filter(Item__id=bid, person__id=per.id, status=False).exists():
                messages.warning(request, 'Item already in the cart')
                return redirect('item')
                return render(request, 'cart.html', {'p': p, 'per': per})
            else:
                # citem = Mycart.objects.filter(person__id=per.id, status=False)
                bk = get_object_or_404(items,id=bid)

                c = Mycart.objects.create(person=per, Item=bk)
                c.save()
                request.session['order_id']=c.id
                messages.warning(request, 'Item has beed added to cart')
                return redirect('item')
                return render(request, 'cart.html', {'p': p, 'obj':obj,'per': per,'ditem': citem})
        else:
            return render(request, 'cart.html', {'ditem': citem, 'num': num, 'per': per, 'total': total,'billing': total*100})
    else:
        messages.info(request, 'please login first to access the cart ')
        return redirect('regi1')




def remove_cart(request, id):
    if request.session.has_key('Email'):
        y = get_object_or_404(Mycart, id=id)
        y.delete()
        return redirect('Cart')


        
def place_order(request):
    if request.session.has_key('Email'):
        per = signup.objects.get(Email=request.session['Email'])
        citem = Mycart.objects.filter(person__id=per.id, status=False)
        total = 0
        books_incart = ''
        for q in citem:
            total += q.Item.Price
            books_incart = q.Item.Title +','+ books_incart
            print(total)
            print(books_incart)
        request.session['Total']=total

        if request.method == 'POST':
            full_name = 'Khanak'
            email = 'khanakrawal4112000@gmail.com'
            landmark = 'asdfghjk'
            city = 'asdefrghjk'

            # Malking Qrcode

            qrdata = f"""
            name = {full_name}
            email = {email}
            city = {city}
            landmark = {landmark}
            items name = {books_incart}
            amount = {total}
            """ 
            num = random.randint(1111,9999)
            obj = Orders(person=per)
            qr=qrcode.QRCode(version=1,box_size=10,border=5)
            qr.add_data(qrdata)
            qr.make(fit=True)
            img=qr.make_image(fill="black",back_color="white")
            img.save(os.path.join(BASE_DIR,"media/"+ str(num) +".jpeg"))
            y = f'{num}.jpeg'
            my_order = Orders.objects.create(person=per,Bitem=books_incart,order_amount=total,qrimage=y)
            my_order.save()
            print(my_order.order_id)

            # ----------- remove item from cart after placed the order ---------- #
            for i in citem:
                cart_obj = Mycart.objects.get(id=i.id)
                cart_obj.status = False
                cart_obj.save()

            # Sending Email to customer
            msg = EmailMessage()
            msg.set_content(f'''
            Thank you for your order.
            order details:

            Full name: {full_name}
            Email: {email}
            city: {city}
            Order Amount: {total}
            Order Id: {my_order.order_id}
            Items name: {books_incart}
            ''')

            msg['Subject'] = 'HOCC'
            msg['From'] = "khanakrawal4112000@gmail.com"
            msg['To'] = f"{email}"

            # Send the message via our own SMTP server.
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.login("khanakrawal4112000@gmail.com", "google92@")
            server.send_message(msg)
            server.quit()


            # Sending Mail    
            sender_email = 'khanakrawal4112000@gmail.com'
            password = 'google92@'
            message = f"""\
            Subject: Service Order
            To: {email}
            From: {sender_email}

            Thank you for your order, order details is  \n NAME:{full_name}\n EMAIL:{email}\n CITY:{city} \n Order Amount:{total}\n Items name:{books_incart}."""
            print(message)
            #address_type = request.POST['atype']
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, password)
            print('login success')
            server.sendmail(sender_email, email, message)
            print('email sent')
            server.quit()

            
            return redirect('myaccount')

    else:
        messages.info(request, 'please login first to access the cart ')
        return redirect('regi1')

def myaccount(request):
    if request.session.has_key('Email'):
        data = signup.objects.get(Email=request.session['Email'])
        my_order = Orders.objects.filter(person__id=data.id)
        return render(request, 'success.html', {'data': data,'my_order':my_order})

    else:
        return redirect('regi1')


def qrshow(request,order_id):
    q = get_object_or_404(Orders,order_id=order_id)
    return render(request,'qr.html',{'q':q})

def invoice(request,pk):
    x = get_object_or_404(Orders,pk=pk)
    f= open(f'media/invoice/{x.order_id}.txt','w')
    f.write('orderId:'+str(x.order_id))
    f.close()
    print('file done')
    f = f"invoice/{x.order_id}.txt"
    x.invoice = f
    x.save()
    return render(request,'invoice.html',{'x':x})











# ___________________________________Payment_________________________
def razor(request):
    if request.method == "POST":
        name = request.POST.get('name')
        amount = 50000

        client = razorpay.Client(
            auth=("rzp_test_lqsW2gWKFbM27g", "mdM6J2uG7TR5x06UFLWDnenU"))

        payment = client.order.create({'amount': amount, 'currency': 'INR',
                                       'payment_capture': '1'})
    return render(request, 'index.html')

@csrf_exempt
def success(request):
    return render(request, "success.html")


def checkout(request):
    return render(request , 'checkout.html')