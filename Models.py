from django.db import models

# Create your models here.


class Login(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    type=models.CharField(max_length=100)

class pharmacy(models.Model):
    shop_name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    owner_name=models.CharField(max_length=100)
    owner_phone=models.CharField(max_length=100)
    document=models.CharField(max_length=200)
    place=models.CharField(max_length=100)
    post=models.CharField(max_length=100)
    pin=models.CharField(max_length=100)
    district=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    photo=models.CharField(max_length=200)
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)


class customer(models.Model):
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)

class order_main(models.Model):
    User = models.ForeignKey(customer, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.CharField(max_length=100,default='')
    status = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    Shop = models.ForeignKey(pharmacy, on_delete=models.CASCADE)
    online = models.CharField(max_length=100)
    shop_bills = models.CharField(max_length=100)

class payment(models.Model):
    date=models.CharField(max_length=100)
    Order_main=models.ForeignKey(order_main,on_delete=models.CASCADE)
    amount=models.CharField(max_length=100)
    status=models.CharField(max_length=100)


class medicine(models.Model):
    name=models.CharField(max_length=100)
    ingredients=models.CharField(max_length=100)
    quantity=models.CharField(max_length=100)
    warning=models.CharField(max_length=100)
    exp_date=models.CharField(max_length=100)
    manuf_date=models.CharField(max_length=100)
    image=models.CharField(max_length=300,default="")
    price=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    Pharmacy=models.ForeignKey(pharmacy,on_delete=models.CASCADE)

class stock(models.Model):
    Medicine=models.ForeignKey(medicine,on_delete=models.CASCADE)
    quantity=models.IntegerField(max_length=100)

class order_sub(models.Model):
    Stock=models.ForeignKey(stock,on_delete=models.CASCADE)
    Order_main=models.ForeignKey(order_main,on_delete=models.CASCADE)
    quantity=models.CharField(max_length=100)
    amount=models.CharField(max_length=100)

class cart(models.Model):
    User=models.ForeignKey(customer,on_delete=models.CASCADE)
    Medicine=models.ForeignKey(medicine,on_delete=models.CASCADE,default=1)
    quantity=models.CharField(max_length=100)

class complaint(models.Model):
    User=models.ForeignKey(customer,on_delete=models.CASCADE)
    pharmacy=models.ForeignKey(pharmacy,on_delete=models.CASCADE,default=1)
    date=models.CharField(max_length=100)
    complaint=models.CharField(max_length=200)
    replay=models.CharField(max_length=200)
    stauts=models.CharField(max_length=100)

class priscription(models.Model):
    User=models.ForeignKey(customer,on_delete=models.CASCADE)
    file=models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    Pharmacy = models.ForeignKey(pharmacy, on_delete=models.CASCADE)


class review(models.Model):
    User=models.ForeignKey(customer,on_delete=models.CASCADE)
    date=models.DateField()
    review=models.CharField(max_length=100)



class Billentry(models.Model):
    date=models.DateField()
    PRESCRIPTION = models.ForeignKey(priscription, on_delete=models.CASCADE)
    total_amount=models.BigIntegerField()
    status=models.CharField(max_length=100)
    quantity=models.CharField(max_length=100)
    paystatus=models.CharField(max_length=100)
    Stock=models.ForeignKey(stock,on_delete=models.CASCADE)

class Prescriptionpayment(models.Model):
    date=models.CharField(max_length=100)
    BILLENTRY=models.ForeignKey(Billentry,on_delete=models.CASCADE)
    amount=models.CharField(max_length=100)
    status=models.CharField(max_length=100)

class Notification(models.Model):
    customer=models.ForeignKey(customer, on_delete=models.CASCADE)
    pharmacy=models.ForeignKey(pharmacy, on_delete=models.CASCADE)
    date=models.DateField()
    notification=models.CharField(max_length=100)
