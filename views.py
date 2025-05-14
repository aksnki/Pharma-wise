from datetime import datetime

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from myapp.models import *


def login(request):
    return render(request,"index.html")
def login_post(request):
    username=request.POST['textfield']
    password=request.POST['textfield2']
    lobj=Login.objects.filter(username=username,password=password)
    if lobj.exists():
        lobj1=Login.objects.get(username=username,password=password)
        request.session['lid']=lobj1.id
        if lobj1.type=='admin':
            request.session['lid'] = lobj1.id
            return HttpResponse('<script>alert("Success");window.location="/myapp/admin_home/"</script>')
        elif lobj1.type=='customer':
            return HttpResponse('<script>alert("Success");window.location="/myapp/customer_home/"</script>')
        # elif lobj1.type=='pending':
        #     return HttpResponse('<script>alert("Not Verified");window.location="/myapp/login/"</script>')

        elif  lobj1.type=='pharma':
                return HttpResponse('<script>alert("Success");window.location="/myapp/pharma_home/"</script>')
        else:
            return HttpResponse('''<script>alert('invalid user');window.location='/myapp/login/'</script>''')

    else:
        return HttpResponse('''<script>alert('wrong username or password');window.location='/myapp/login/'</script>''')


def admin_home(request):
    if request.session['lid']=="":
        return HttpResponse('''<script>alert('Please login...');window.location='/myapp/login/'</script>''')
    else:
        return render(request,"admin/index.html")

def admin_view_pharma_accept(request):
    if request.session['lid']=="":
        return HttpResponse('''<script>alert('Please login...');window.location='/myapp/login/'</script>''')
    else:
        obj = pharmacy.objects.filter(status='pending')
        return render (request,'admin/view pharma& verify.html',{'data':obj})

def acceptpharma_post(request,id):
    if request.session['lid']=="":
        return HttpResponse('''<script>alert('Please login...');window.location='/myapp/login/'</script>''')
    else:
        data=pharmacy.objects.filter(LOGIN_id=id).update(status='approved')
        res=Login.objects.filter(id=id).update(type='pharma')
        return HttpResponse("<script>alert('Pharmacy Approved');window.location='/myapp/admin_view_pharma_approved/#services'</script>")

def rejectpharma_post(request,id):
    data=pharmacy.objects.filter(LOGIN_id=id).update(status='rejected')
    res=Login.objects.filter(id=id).update(type='rejected')


    return HttpResponse("<script>alert('Request Rejected');window.location='/myapp/admin_view_pharma_accept/#services'</script>")




def admin_view_pharma_accept_post(request):
    search=request.POST['textfield']
    obj = pharmacy.objects.filter(shop_name__icontains=search)
    return render(request, "admin/view pharma& verify.html", {"data": obj})

    #return HttpResponse('#')



def admin_view_pharma_approved(request):
    obj = pharmacy.objects.filter(status='approved')
    return render (request,'admin/approved pharma.html',{'data':obj})


def admin_view_pharma_approved_post(request):
    search = request.POST['textfield']
    obj = pharmacy.objects.filter(status='approved',shop_name__icontains=search)
    return render (request,'admin/approved pharma.html',{'data':obj})




def admin_view_pharma_rejected(request):
    obj = pharmacy.objects.filter(status='rejected')
    return render (request,'admin/rejected pharma.html',{'data':obj})


def admin_view_pharma_rejected_post(request):
    search = request.POST['textfield']
    obj = pharmacy.objects.filter(shop_name__contains=search)
    return render (request,'admin/rejected pharma.html',{'data':obj})






def admin_view_registered_pharma(request):
    obj = pharmacy.objects.all()
    return render (request,"admin/approved pharma.html")

def admin_view_customer(request):
    obj = customer.objects.all()
    return render(request,"admin/view customer.html",{"data":obj})
def admin_view_customer_post(request):
    search = request.POST['textfield']
    obj = customer.objects.filter(name__icontains=search)
    return render(request, "admin/view customer.html", {"data":obj})


def admin_view_review(request):
    obj = review.objects.all()
    return render (request,"admin/View review.html",{"data":obj})
def admin_view_review_post(request):
    fromdate=request.POST['textfield']
    todate=request.POST['textfield2']
    obj = review.objects.filter(date__range=[fromdate,todate])
    return render(request,"admin/View review.html",{"data":obj})

def admin_change_password(request):
    return render (request,"admin/change pass.html")

def admin_change_password_post(request):
    old_password=request.POST['textfield']
    new_password=request.POST['textfield2']
    confrim_password=request.POST['textfield3']
    id = request.session['lid']


    obj=Login.objects.get(id=id)
    if obj.password == old_password:
        if confrim_password == new_password:
            Login.objects.filter(id=id).update(password=confrim_password)
            return HttpResponse("<script>alert('change password successfully');window.location='/myapp/login/'</script>")
        else:
            return HttpResponse("<script>alert('not found');window.location='/myapp/login/'</script>")
    else:
        return HttpResponse("<script>alert('not found');window.location='/myapp/login/'</script>")



def admin_view_complaint(request):
    c = complaint.objects.all()
    return render(request,'admin/view complaint.html',{"data":c})

def admin_view_complaint_post(request):
    fd = request.POST['fd']
    td = request.POST['td']
    c = complaint.objects.filter(date__range=[fd,td])
    return render(request,'admin/view complaint.html',{"data":c})





def pharma_home(request):
    return render(request,"pharma/index.html")
def pharma_signup(request):
    return render (request,"pharma/temsign.html")

def pharma_signup_post(request):
    username=request.POST['textfield']
    email=request.POST['textfield2']
    Owner_name=request.POST['textfield5']
    owner_phone=request.POST['textfield4']
    place=request.POST['textfield3']
    post=request.POST['textfield8']
    pin=request.POST['textfield9']
    district=request.POST['textfield10']
    document=request.FILES['fileField']
    photo=request.FILES['fileField2']
    password=request.POST['textfield6']
    confrim_password=request.POST['textfield7']


    log = Login.objects.filter(username=email)
    if log.exists():
        return HttpResponse('''<script>alert('User name already taken');window.location='/myapp/login/'</script>''')

    log = pharmacy.objects.filter(owner_phone=owner_phone)
    if log.exists():
        return HttpResponse('''<script>alert('Phone number  already exists');window.location='/myapp/login/'</script>''')



    if password==confrim_password:

        l = Login()
        l.username = email
        l.password = password
        l.type = "pending"
        l.save()

        obj=pharmacy()
        fs = FileSystemStorage()
        date = datetime.now().strftime('%Y%m%d-%H%M%S') +".jpg"
        fn = fs.save(date,photo)
        path = fs.url(date)

        fs1 = FileSystemStorage()
        date1 = datetime.now().strftime('%Y%m%d-%H%M%S') +"-1.jpg"
        fn1 = fs1.save(date1,document)
        path1 = fs1.url(date1)
        obj.photo=path
        obj.shop_name=username
        obj.email=email
        obj.owner_name=Owner_name
        obj.owner_phone=owner_phone
        obj.document=path1
        obj.place=place
        obj.post=post
        obj.pin=pin
        obj.district=district
        obj.photo=path
        obj.status='pending'
        obj.LOGIN = l
        obj.save()

        return HttpResponse('''<script>alert('pharmacy registered');window.location='/myapp/login/'</script>''')
    return HttpResponse('''<script>alert('invalid');window.location='/myapp/pharma_signup/'</script>''')


def pharma_view_order_update_status(request):
    fo = order_main.objects.filter(Shop__LOGIN_id=request.session['lid'])
    gh = payment.objects.filter(Order_main__Shop__LOGIN__id=request.session['lid'])
    return render(request,"pharma/view odr&update.html",{'data':fo, 'data1':gh})
def pharma_view_order_update_status_post(request):
    fo = request.POST['textfield']
    to = request.POST['textfield2']
    obj = order_main.objects.filter(date__range=[fo,to])
    return render(request,'pharma/view odr&update.html',{"data":obj})

def pharma_order_status(request,id):
    return render(request,"pharma/order staus.html",{"data":id})

def pharma_order_status_post(request):
    status=request.POST['status']
    oid=request.POST['oid']
    order_main.objects.filter(id=oid).update(status=status)

    b = order_main.objects.get(id=oid).User.id

    obj = Notification()
    obj.pharmacy = pharmacy.objects.get(LOGIN_id=request.session['lid'])
    obj.customer_id = b
    obj.date = datetime.now()
    obj.notification = status
    obj.save()
    return HttpResponse('''<script>alert('Status Updated..!');window.location='/myapp/pharma_view_order_update_status/#about'</script>''')

def pharma_oder_sub(request,id):
    vd=order_sub.objects.filter(Order_main_id=id)
    return render(request,"pharma/odr sub.html",{'data':vd})


def pharma_manage_medicine_view(request):
    obj=medicine.objects.filter(Pharmacy__LOGIN_id=request.session['lid'])
    return render (request,"pharma/mange med dlt medicine.html",{"data":obj})

def pharma_manage_medicine_view_post(request):
    search=request.POST['textfield']
    obj = medicine.objects.filter(Pharmacy__LOGIN_id=request.session['lid'],name__icontains=search)
    return render (request,"pharma/mange med dlt medicine.html",{"data":obj})




def pharma_manage_medicine_edit(request,id):
    obj=medicine.objects.get(id=id)
    return render (request,"pharma/edit medicine.html",{"data":obj})
def pharma_manage_medicine_edit_post(request):
    medicine_name=request.POST['textfield']
    ingredients=request.POST['textfield2']
    quantity=request.POST['textfield3']
    warning=request.POST['textfield4']
    manuf_date=request.POST['textfield5']
    exp_date=request.POST['textfield6']
    category=request.POST['select']
    price=request.POST['textfield7']
    id=request.POST['id']


    obj = medicine.objects.get(id=id)
    if 'fileField' in request.FILES:
        Image = request.FILES['fileField']
        if Image !="":
            fs = FileSystemStorage()
            date = datetime.now().strftime('%Y%m%d-%H%M%S') + ".jpg"
            fn = fs.save(date, Image)
            path = fs.url(date)
            obj.image = path

    obj.name=medicine_name
    obj.ingredients=ingredients
    obj.quantity=quantity
    obj.warning=warning
    obj.manuf_date=manuf_date
    obj.exp_date=exp_date
    obj.category=category
    obj.price=price
    obj.save()

    return HttpResponse('''<script>alert('Updated Sucessfully');window.location="/myapp/pharma_manage_medicine_view/"</script>''')

def pharma_delete_medicine(request,id):
    obj = medicine.objects.filter(id=id).delete()
    return redirect("/myapp/pharma_manage_medicine_view/")
#
# def pharma_manage_medicine_delete(request):
#     obj = medicine.objects.get(id=id)
#     return redirect (request,"pharma/mange med dlt medicine.html")
def pharma_manage_medicine_delete_post(request):
    search=request.POST['textfield']
    return redirect('''<script>alert('Delete Successfull');window.location="/myapp/pharma_manage_medicine_view/"</script>''')


def pharma_manage_medicine_add(request):
    return  render (request,"pharma/mange med add medicine.html")
def pharma_manage_medicine_add_post(request):
    medicine_name = request.POST['textfield']
    ingredients = request.POST['textfield2']
    quantity = request.POST['textfield3']
    warning = request.POST['textfield4']
    manuf_date = request.POST['textfield5']
    exp_date = request.POST['textfield6']
    category = request.POST['select']
    Image=request.FILES['fileField']
    price = request.POST['textfield8']

    # obj = medicine()
    fs = FileSystemStorage()
    date = datetime.now().strftime('%Y%m%d-%H%M%S') + ".jpg"
    fn = fs.save(date, Image)
    path = fs.url(date)

    obj = medicine()
    obj.name = medicine_name
    obj.ingredients = ingredients
    obj.quantity = quantity
    obj.warning = warning
    obj.manuf_date = manuf_date
    obj.exp_date = exp_date
    obj.category = category
    obj.price = price
    obj.image = path
    obj.Pharmacy = pharmacy.objects.get(LOGIN_id=request.session['lid'])
    obj.save()

    return HttpResponse('''<script>alert('Added Sucessfilly');window.location="/myapp/pharma_manage_medicine_add/#about"</script>''')

def pharma_manage_stock_view(request):
    obj = stock.objects.all()
    return render(request,"pharma/view stock.html",{"data":obj})
def pharma_manage_stock_view_post(request):
    search = request.POST['textfield']
    obj = stock.objects.filter(Medicine__name__icontains=search)
    return render(request,"pharma/view stock.html",{"data":obj})

def pharma_view_complaint_replay(request):
    obj = complaint.objects.all()
    return render(request,"pharma/compalint & replay.html",{'data':obj})

def pharma_view_complaint_replay_post(request):
    fromdate=request.POST['textfield']
    todate=request.POST['textfield']
    obj = complaint.objects.filter(date__range=[fromdate,todate])
    return render(request, "pharma/compalint & replay.html", {"data": obj})

def pahrma_send_replay(request,id):
    return render (request, "pharma/send replay.html", {'id':id})

def pharma_send_replay_post(request):
    Sid= request.POST['Sid']
    replay=request.POST['textarea']
    obj=complaint.objects.filter(id=Sid).update(stauts='replaied',replay=replay)
    return HttpResponse('<script>alert("Success");window.location="/myapp/pharma_view_complaint_replay/#about"</script>')


def pharma_manage_stock_update(request):
    rs=medicine.objects.all()
    return render(request,"pharma/mange stock add.html",{'data':rs})
def pharma_manage_stock_update_post(request):
    medicine=request.POST['select']
    qty=request.POST['textfield2']
    ss=stock.objects.filter(Medicine_id=medicine)
    if ss.exists():
        qq=0
        q=stock.objects.get(Medicine_id=medicine).quantity
        c=int(q)+int(qty)
        qq+=c
        stock.objects.filter(Medicine_id=medicine).update(quantity=qq)
        return HttpResponse(
            '''<script>alert('Updated Successfull');window.location="/myapp/pharma_manage_stock_view/#about"</script>''')

    else:
        s = stock()
        s.Medicine_id = medicine
        s.quantity = qty
        s.save()
        return HttpResponse('''<script>alert('Updated Successfull');window.location="/myapp/pharma_manage_stock_view/"</script>''')

def pharma_manage_stock_delete(request,id):
    obj = stock.objects.filter(id=id).delete()
    return redirect("/myapp/pharma_manage_stock_view/")
#def pharma_manage_stock_delete_post(request):
    #search = request.POST['textfield']
    # return redirect('''<script>alert('Delete Successfull');window.location="/myapp/pharma_manage_stock_view/"</script>''')


def pharma_view_order_payment(request):
    obj = order_sub.objects.filter(Order_main__Shop__LOGIN_id=request.session['lid'])
    return render (request,"pharma/view order.html",{'data':obj})


def pharma_view_prescription(request):
    res = priscription.objects.filter(Pharmacy__LOGIN__id=request.session['lid'])
    return render(request,"pharma/view priscription.html",{'data':res})
def pharma_view_prescription_post(request):
    search = request.POST['textfield']
    obj = priscription.objects.filter(User__name__icontains=search)
    return render(request,'pharma/view priscription.html',{"data":obj})

def pharma_bill_entry(request,id):
    obj = stock.objects.filter(Medicine__Pharmacy__LOGIN_id=request.session['lid'])
    return render (request,"pharma/bill entry.html",{"data":obj,'id':id})


def pharma_bill_entry_post(request):
    med = request.POST['item']
    print(med)
    quantity = request.POST['qty']
    price = float(request.POST['price'])
    pid = request.POST['pid']
    print(pid)
    total_amount = float(quantity) * price

    res = Billentry()
    res.date = datetime.now()
    res.PRESCRIPTION_id = pid
    res.status = 'pending'
    res.quantity = quantity
    res.total_amount = total_amount
    res.Stock_id = stock.objects.get(Medicine_id=med).id
    res.paystatus='pending'
    res.save()
    return HttpResponse('<script>alert("Bill entry added successfully");window.location="/myapp/pharma_view_prescription/#about"</script>')



def pharma_view_bill_entry(request,id):
    res = Billentry.objects.filter(PRESCRIPTION_id=id)
    return render(request,"pharma/view bills.html",{'data':res})
def pharma_view_bill_entry_post(request):
    fo = request.POST['textfield']
    to = request.POST['textfield2']
    obj = Billentry.objects.filter(date__range=[fo,to])
    return render(request,'pharma/view bills.html',{"data":obj})

def pharma_bill_history(request):
    res = order_sub.objects.filter(Order_main__Shop__LOGIN_id=request.session['lid'])
    return render(request,"pharma/bill history.html",{'data':res})
def pharma_bill_history_post(request):
    fo = request.POST['textfield']
    to = request.POST['textfield2']
    res = order_sub.objects.filter(Order_main__Shop__LOGIN_id=request.session['lid'],date__range=[fo,to])
    return render(request, "pharma/bill history.html", {'data': res})

def pharma_bill_history2(request):
    res = Billentry.objects.filter(PRESCRIPTION__Pharmacy__LOGIN_id=request.session['lid'])
    return render(request,"pharma/HISTORY 2.html",{'data':res})
def pharma_bill_history2_post(request):
    fo = request.POST['textfield']
    to = request.POST['textfield2']
    res = Billentry.objects.filter(PRESCRIPTION__Pharmacy__LOGIN_id=request.session['lid'],date__range=[fo,to])
    return render(request, "pharma/HISTORY 2.html", {'data': res})


def pharma_view_profile(request):
    res = pharmacy.objects.get(LOGIN__id=request.session['lid'])
    return render (request,"pharma/view profile.html",{'data':res})

def pharma_edit_profile(request):
    res = pharmacy.objects.get(LOGIN_id=request.session['lid'])
    return render(request, "pharma/edit profile.html", {'data': res})
def  pharma_edit_profile_post(request):
    username = request.POST['textfield']
    email = request.POST['textfield2']
    Owner_name = request.POST['textfield5']
    owner_phone = request.POST['textfield4']
    place = request.POST['textfield3']
    post = request.POST['textfield8']
    pin = request.POST['textfield9']
    district = request.POST['textfield10']
    document = request.FILES['fileField']
    photo = request.FILES['fileField2']

    l = Login.objects.get(id=request.session['lid'])
    l.username = email
    l.save()

    obj = pharmacy.objects.get(LOGIN_id=request.session['lid'])
    obj.email = email
    obj.owner_name = Owner_name
    obj.owner_phone = owner_phone
    obj.document = document
    obj.place = place
    obj.post = post
    obj.pin = pin
    obj.district = district
    obj.photo = photo
    # obj.status = status
    obj.save()

    return HttpResponse('''<script>alert('Profile updated Sucessfully');window.location="/myapp/pharma_view_profile/#about"</script>''')


def logout(request):
    request.session['lid']=""
    return redirect('/myapp/login/')

def pharma_view_review(request):
    obj = review.objects.all()
    return render(request, "pharma/View review.html", {"data": obj})
def pharma_view_review_post(request):
    fromdate=request.POST['textfield']
    todate=request.POST['textfield2']
    obj = review.objects.filter(date__range=[fromdate,todate])
    return render(request,"pharma/View review.html",{"data":obj})

def pharma_change_password(request):
    return render(request,"pharma/pharma_pass.html")
def pharma_change_password_post(request):
    old_password = request.POST['textfield']
    new_password = request.POST['textfield2']
    confrim_password = request.POST['textfield3']
    id = request.session['lid']

    obj = Login.objects.get(id=id)
    if obj.password == old_password:
        if confrim_password == new_password:
            Login.objects.filter(id=id).update(password=confrim_password)
            return HttpResponse(
                "<script>alert('change password successfully');window.location='/myapp/login/'</script>")
        else:
            return HttpResponse("<script>alert('not found');window.location='/myapp/login/'</script>")

def pharma_notification(request):
    return render(request,"pharma/notification.html")
def pharma_notification_post(request):
    return


def customer_home(request):
    return render(request,"Customer/uindex.html")

def customer_signup(request):
    return render(request,"first.html")
def customer_signup_post(request):
    username=request.POST['textfield']
    email=request.POST['textfield2']
    phone=request.POST['textfield5']
    gender=request.POST['RadioGroup1']
    password=request.POST['textfield3']
    confrim_password=request.POST['textfield4']

    if password==confrim_password:
        l = Login()
        l.username = email
        l.password = password
        l.type = "customer"
        l.save()

        obj = customer()
        obj.name=username
        obj.email=email
        obj.phone=phone
        obj.gender=gender
        obj.LOGIN=l
        obj.save()


        return HttpResponse("'''<script>alert('Customer registered');window.location='/myapp/login/'</script>'''")
    return HttpResponse('''<script>alert('invalid');window.location='/myapp/customer_signup/'</script>''')

def customer_search_medicine(request,id):
    request.session['mid']=id
    obj = stock.objects.filter(Medicine__Pharmacy_id=id)
    return render (request,"Customer/search medicine.html",{"data":obj})

def customer_search_medicine_post(request):
    med=request.POST['textfield']
    obj = stock.objects.filter(Medicine__Pharmacy_id=request.session['mid'],Medicine__name__icontains=med)
    return render (request,"Customer/search medicine.html",{"data":obj})

def customer_addtocart(request,id):
    data=medicine.objects.get(id=id)
    return render(request,"Customer/add to cart.html",{"data":data})
def customer_addtocart_post(request):
    quantity = request.POST['quantity']
    obj = request.POST['pid']

    if int(quantity) > int(stock.objects.get(Medicine_id=obj).quantity):
        print(stock.objects.get(Medicine_id=obj).quantity)
        return HttpResponse('<script>alert("out of stock");window.location="/myapp/customer_view_cart/#services"</script>')
    elif int(quantity) <= int(stock.objects.get(Medicine_id=obj).quantity):
        re = cart.objects.filter(Medicine_id=obj)

        if re.exists():
            e = cart.objects.get(Medicine_id=obj).quantity
            qu = int(e) + int(quantity)
            cart.objects.filter(Medicine_id=obj).update(quantity=qu)
            return HttpResponse(
                '<script>alert("added to cart successfully");window.location="/myapp/customer_view_cart/#services"</script>')
        else:
            data = cart()
            data.User = customer.objects.get(LOGIN_id=request.session['lid'])
            data.Medicine_id = obj
            data.quantity = quantity
            data.save()
            return HttpResponse(
                '<script>alert("added to cart successfully");window.location="/myapp/customer_view_cart/#services"</script>')
    else:
        return HttpResponse('<script>alert("please add valid data");window.location="/myapp/customer_view_cart/#services"</script>')


def customer_view_cart(request):
    obj = cart.objects.filter(User__LOGIN_id=request.session['lid'])
    l=[]
    ttl = 0
    k=""
    for i in obj:
        s=""
        if stock.objects.filter(Medicine_id=i.Medicine.id).exists():
            d=stock.objects.get(Medicine_id=i.Medicine.id)
            if int(i.quantity)>int(d.quantity):
                s="out"


        p=medicine.objects.get(id=i.Medicine.id).price
        m=int(i.quantity)*int(p)
        ttl+=m
        l.append({
            'id':i.id,
            'name':i.Medicine.name,
            'image':i.Medicine.image,
            'price':i.Medicine.price,
            'quantity':i.quantity,
            'total':m,
            's':s

        })
        if s=="out":
            k="no"
        print(l)
        print(k)
    return render(request, "Customer/view cart.html", {'data': l,'ttl':str(ttl),'p':k})


def customer_remove_cart(request,id):
    obj= cart.objects.filter(id=id).delete()
    return redirect("/myapp/customer_view_cart/")

def customer_uploads(request,id):
    return render(request,"Customer/upload.html",{'id':id})
def customer_uploads_post(request):
    pr=request.FILES['fileField2']
    id=request.POST['id']

    fs = FileSystemStorage()
    date = 'prescription/'+datetime.now().strftime('%Y%m%d-%H%M%S') + ".jpg"
    fs.save(date, pr)
    path = fs.url(date)

    obj=priscription()
    obj.file=path
    obj.User=customer.objects.get(LOGIN_id=request.session['lid'])
    obj.Pharmacy_id=id
    obj.date=datetime.now().strftime('%Y-%m-%d')
    obj.save()
    return HttpResponse('<script>alert("Uploaded successfully");window.location="/myapp/customer_view_uploads/"</script>')

def customer_view_uploads(request):
    obj=priscription.objects.filter(User__LOGIN_id=request.session['lid'])
    return render(request,"Customer/view uploads.html",{'data':obj})


def customer_view_bill_payment(request):
    res=Billentry.objects.filter(PRESCRIPTION__User__LOGIN_id=request.session['lid'])
    return render(request,"Customer/view bill.html",{'data':res})


def customer_raz_pay(request,amount):
    import razorpay
    razorpay_api_key = "rzp_test_MJOAVy77oMVaYv"
    razorpay_secret_key = "MvUZ03MPzLq3lkvMneYECQsk"

    razorpay_client = razorpay.Client(auth=(razorpay_api_key, razorpay_secret_key))

    # amount = 200
    amounts= float(amount)*100

    # Create a Razorpay order (you need to implement this based on your logic)
    order_data = {
        'amount': amounts,
        'currency': 'INR',
        'receipt': 'order_rcptid_11',
        'payment_capture': '1',  # Auto-capture payment
    }

    # Create an order
    order = razorpay_client.order.create(data=order_data)


    context = {
        'razorpay_api_key': razorpay_api_key,
        'amount': order_data['amount'],
        'currency': order_data['currency'],
        'order_id': order['id'],
    }




    c=cart.objects.filter(User__LOGIN_id= request.session['lid']).values_list('Medicine__Pharmacy_id').distinct()

    for i in c:
        c2 = cart.objects.filter(User__LOGIN_id=request.session['lid'],Medicine__Pharmacy_id=i[0])
        pay = order_main()
        pay.User = customer.objects.get(LOGIN_id=request.session['lid'])
        pay.date = datetime.now().today()
        pay.amount = 0
        pay.status = 'Successfull'
        pay.Shop_id =i[0]
        pay.type='self'
        pay.online='pending'
        pay.save()
        mytotal=0
        for j in c2:
            if stock.objects.filter(Medicine_id=j.Medicine.id).exists():
                s=stock.objects.get(Medicine_id=j.Medicine.id)
                pay2=order_sub()
                pay2.Order_main_id=pay.id
                pay2.Stock_id=s.id
                pay2.amount = amount
                pay2.quantity=j.quantity
                pay2.save()
                print(j.quantity)
                mytotal+=float(j.Medicine.price)*float(j.quantity)
                if stock.objects.filter(Medicine_id=j.Medicine.id).exists():
                    print("1")
                    print("mid",j.Medicine.id)

                    s=stock.objects.get(Medicine_id=j.Medicine.id)
                    print("stock", s.quantity,"cart",j.quantity)
                    stock.objects.filter(Medicine_id=j.Medicine.id).update(quantity=int(s.quantity)-int(j.quantity))
        print("ghgh",mytotal)
        obj = payment()
        obj.User=customer.objects.get(LOGIN_id=request.session['lid'])
        obj.Order_main=pay
        obj.date = datetime.now().strftime('%Y%m%d')
        obj.amount = amount
        obj.status='paid'
        obj.save()
        order_main.objects.filter(id=pay.id).update(amount=mytotal)
        cart.objects.filter(User__LOGIN_id=request.session['lid']).delete()
    return render(request, 'customer/payment.html',{ 'razorpay_api_key': razorpay_api_key,
        'amount': order_data['amount'],
        'currency': order_data['currency'],
        'order_id': order['id'],"id":id})



def customer_view_cart_payment(request):
    return render(request,"Customer/view cart.html")

def customer_send_complaint_replay(request):
    ph=pharmacy.objects.filter(status="approved")
    return render(request,"Customer/send complaint.html",{'data':ph})
def customer_send_complaint_replay_post(request):
    complaints=request.POST['textarea']
    ph=request.POST['pid']
    obj=complaint()
    obj.date=datetime.now().strftime('%Y-%m-%d')
    obj.complaint=complaints
    obj.replay='pending'
    obj.stauts='pending'
    obj.User=customer.objects.get(LOGIN=request.session['lid'])
    obj.pharmacy=pharmacy.objects.get(id=ph)
    obj.save()
    return HttpResponse('''<script>alert('Complaint sent Sucessfully.kindly check Replies'); window.location="/myapp/customer_view_replay/#services"</script>''')

def customer_view_replay(request):
    obj=complaint.objects.filter(User__LOGIN_id=request.session['lid'])
    return render(request,"Customer/view replay.html",{'data':obj})
def customer_view_replay_post(request):
    fromdate=request.POST['textfield']
    todate=request.POST['textfield2']
    obj = complaint.objects.filter(User__LOGIN_id=request.session['lid'],date__range=[fromdate,todate])
    return render(request, "Customer/view replay.html", {'data': obj})
def customer_send_review(request):
    return render (request,"Customer/send review.html")
def customer_send_review_post(request):
    reviews=request.POST['textarea']

    obj=review()
    obj.date = datetime.now().strftime('%Y-%m-%d')
    obj.review=reviews
    obj.User=customer.objects.get(LOGIN=request.session['lid'])
    obj.save()
    return HttpResponse('''<script>alert('Review sent Sucessfully');window.location="/myapp/customer_home/"</script>''')

def customer_view_profile(request):
    res=customer.objects.get(LOGIN_id=request.session['lid'])
    return render (request,"Customer/view profile.html",{'data':res})

def customer_edit_profile(request):
    res=customer.objects.get(LOGIN_id=request.session['lid'])
    return render (request,"Customer/view profile2.html",{'data':res})
def customer_edit_profile_post(request):
    name=request.POST['textfield']
    email=request.POST['textfield2']
    phone=request.POST['textfield3']
    gender=request.POST['RadioGroup1']

    l = Login.objects.get(id=request.session['lid'])
    l.username = email
    l.save()

    obj = customer.objects.get(LOGIN_id=request.session['lid'])
    obj.name = name
    obj.email = email
    obj.phone = phone
    obj.gender = gender
    obj.save()

    return HttpResponse('''<script>alert('Profile updated Sucessfully');window.location="/myapp/customer_view_profile/#services"</script>''')

def customer_change_password(request):
    return render (request,"Customer/change pass.html")
def customer_change_password_post(request):
    old_password=request.POST['textfield']
    new_password=request.POST['textfield2']
    confrim_password=request.POST['textfield3']
    id = request.session['lid']

    obj = Login.objects.get(id=id)
    if obj.password == old_password:
        if confrim_password == new_password:
            Login.objects.filter(id=id).update(password=confrim_password)
            return HttpResponse("<script>alert('change password successfully');window.location='/myapp/login/'</script>")
        else:
            return HttpResponse("<script>alert('not found');window.location='/myapp/customer_change_password/#services'</script>")
    else:
        return HttpResponse("<script>alert('invalid password');window.location='/myapp/customer_change_password/#services'</script>")

def customer_view_notification(request):
    obj =Notification.objects.filter(customer__LOGIN_id=request.session['lid'])
    return render(request,'Customer/view notification.html',{'data':obj})

def customer_view_notification_post(request):
    fd=request.POST['textfield']
    td=request.POST['textfield2']
    obj = Notification.objects.filter(customer__LOGIN_id=request.session['lid'],date__range=[fd,td])
    return render(request, 'Customer/view notification.html', {'data': obj})

def user_view_pharma_approved(request):
    obj = pharmacy.objects.filter(status='approved')
    return render (request,'Customer/approved pharma.html',{'data':obj})


def user_view_pharma_approved_post(request):
    search = request.POST['textfield']
    obj = pharmacy.objects.filter(shop_name__icontains=search,status='approved')
    return render (request,'Customer/approved pharma.html',{'data':obj})

def raz_pay2(request,amount,id):
    import razorpay
    razorpay_api_key = "rzp_test_MJOAVy77oMVaYv"
    razorpay_secret_key = "MvUZ03MPzLq3lkvMneYECQsk"

    razorpay_client = razorpay.Client(auth=(razorpay_api_key, razorpay_secret_key))

    # amount = 200
    amounts= float(amount)*100

    # Create a Razorpay order (you need to implement this based on your logic)
    order_data = {
        'amount': amounts,
        'currency': 'INR',
        'receipt': 'order_rcptid_11',
        'payment_capture': '1',  # Auto-capture payment
    }

    # Create an order
    order = razorpay_client.order.create(data=order_data)

    context = {
        'razorpay_api_key': razorpay_api_key,
        'amount': order_data['amount'],
        'currency': order_data['currency'],
        'order_id': order['id'],
    }

    obj = Prescriptionpayment()
    obj.BILLENTRY_id = id
    obj.date = datetime.now().strftime('%Y%m%d')
    obj.amount = float(amount)
    obj.status = 'paid'
    obj.save()


    Billentry.objects.filter(id=id).update(paystatus='paid')

    return render(request, 'Customer/payment.html',{ 'razorpay_api_key': razorpay_api_key,
        'amount': order_data['amount'],
        'currency': order_data['currency'],
        'order_id': order['id'],"id":id})
