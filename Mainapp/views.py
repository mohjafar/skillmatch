from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.conf import settings
from django.core.mail import send_mail
from random import randrange
from .models import Worker, Category, Buyer, Servicebook, Contact, Feedback


def HomePage(Request):
    data = Worker.objects.filter(status="True")
    return render(Request, "index.html", {"data": data})


# def feedback_view(Request):
#     user = User.objects.get(username=Request.user)
#     buyer=Buyer.objects.get(username = user.username)
#     if Request.method == "POST":

       
#         name = Request.POST.get("name")
#         email = Request.POST.get("email")
#         message = Request.POST.get("message")
#         service = Servicebook.objects.filter(username=user.username)
#         print(service,'\n\n\n')
#         feed=Feedback.objects.get_or_create(name=name, email=email, message=message)
#         if feed:
       

#             for ser in service:
#                 ser.cancell = 2
#                 ser.save()
#             return redirect("/booking/")
        

#     messages.success(Request, "Your Feedback Has Been Successfully Submit")

#     return render(Request, "feedback_form.html")


@login_required(login_url="/login/")
def WorkerJob(Request):
    try:
        user = User.objects.get(username=Request.user)
        worker = Worker.objects.get(username=user.username)
        buyers = worker.buyeruser.all()
        services = Servicebook.objects.filter(
            Q(username__in=[buyer.username for buyer in buyers])
            & Q(workerusername=user.username)
        )

        # services = Servicebook.objects.filter(username__in=[buyer.username for buyer in buyers])

    except:
        user = User.objects.get(username=Request.user)
        buyer = Buyer.objects.get(username=user.username)

        return redirect("/booking/")

    return render(Request, "workerjob.html", {"worker": worker, "services": services})


def CompleteWork(Request):
    user = User.objects.get(username = Request.user)
    buyer = Buyer.objects.get(username=user.username)
    #buyers = worker.buyeruser.all()
   
    #services = Servicebook.objects.filter(Q (username__in =[buyer.username for buyer in buyers])& Q(service__in=[buyer.service for buyer in buyers]))
    #print(services,'\n\n\n\n')
    services = Servicebook.objects.filter(Q(workerusername=user.username) |Q(username=user.username))#&Q(service__in=[buyer.username for buyer in buyer.username]))
    print(services,'\n\n\n')
    for ser in services:
        ser.cancell=1
        ser.save()
    return redirect('/booking/')


@login_required(login_url="/login/")
def BookPage(Request):

    try:
        user = User.objects.get(username=Request.user)
        service = Servicebook.objects.filter(username=user.username).order_by('-id')
        buyer = Buyer.objects.get(username=user.username)
        for ser in service:
            if ser.cancell == 1:
                pass
                #return redirect('/feedback_form/')
            elif ser.cancell ==2:
                return redirect('/booking/')

    except:
        try:
            

            user = User.objects.get(username=Request.user)
            worker = Worker.objects.get(username=user.username)
        except:
            pass

    return render(Request, "booking.html", {"service": service})


@login_required(login_url="/login/")
def PlumberPage(Request):
    data = Worker.objects.filter(category_w__name="Plumber")
    return render(Request, "plumber.html", {"data": data})


@login_required(login_url="/login/")
def ElectricianPage(Request):
    data = Worker.objects.filter(category_w__name="Electrician")
    return render(Request, "electrician.html", {"data": data})


@login_required(login_url="/login/")
def CarpenterPage(Request):
    data = Worker.objects.filter(category_w__name="Carpenter")
    return render(Request, "carpenter.html", {"data": data})


@login_required(login_url="/login/")
def PainterPage(Request):
    data = Worker.objects.filter(category_w__name="Painter")
    return render(Request, "carpenter.html", {"data": data})


@login_required(login_url="/login/")
def MachenicPage(Request):
    data = Worker.objects.filter(category_w__name="Mechanic")
    return render(Request, "carpenter.html", {"data": data})


@login_required(login_url="/login/")
def ProfilePage(Request, id):
    profi = Worker.objects.get(id=id)
    return render(Request, "EmployeeData.html", {"pro": profi})


def account(Request):
    return render(Request, "account.html")


def SignupSection(Request):
    if Request.method == "POST":
        p = Request.POST.get("password")
        cp = Request.POST.get("cpassword")
        if p == cp:
            b = Buyer()
            b.name = Request.POST.get("name")
            b.username = Request.POST.get("username")
            b.email = Request.POST.get("email")
            b.phone = Request.POST.get("phone")
            b.pic = Request.FILES.get("pic")
            user = User(username=b.username, email=b.email)
            try:
                if user is not None:
                    user.set_password(p)
                    b.save()
                    user.save()
                    subject = "Thanks For Create Customer Account."
                    message = (f"Hi {b.name},\n, Thanks for creating a new customer account.\n Our Worker Contact You Soon.")
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list = [b.email]
                    send_mail(subject, message, email_from, recipient_list)

                    return redirect("/login/")
            except:
                messages.success(Request, "Username Already Used By Someone")

        else:
            messages.success(
                Request, "Password And Confirm Password Does't Matched !!!!!"
            )

    return render(Request, "signup.html")


def WorkerSignup(Request):
    if Request.method == "POST":
        p = Request.POST.get("password")
        cp = Request.POST.get("cpassword")
        category_id = Request.POST.get("category")

        if p == cp:
            category_instance = Category.objects.get(pk=category_id)

            name = Request.POST.get("name")
            username = Request.POST.get("username")
            description = Request.POST.get("description")
            phone = Request.POST.get("phone")
            email = Request.POST.get("email")
            location = Request.POST.get("location")
            exprience = Request.POST.get("exprience")
            if Request.FILES.get("pic1"):
                pic1 = Request.FILES.get("pic1")
            try:

                w = Worker.objects.create(
                    name=name,
                    pic1=pic1,
                    username=username,
                    email=email,
                    description=description,
                    phone=phone,
                    location=location,
                    exprience=exprience,
                    category_w=category_instance,
                )
                w.save()
                user = User(username=w.username,email=w.email)
                try:
                    if user is not None:
                        user.set_password(p)
                        w.save()
                        user.save()
                        subject = "Thanks for creating a new worker account."
                        message = (f"Hi {w.name},\nPlease fill your skills on your profile page and wait for the client.\nThey will contact you soon. \nThank you")
                        email_from = settings.EMAIL_HOST_USER
                        recipient_list = [w.email]
                        send_mail(subject, message, email_from, recipient_list)
                        return redirect("/login/")
                except:
                    pass
            except:
                messages.error(Request, "Username or email Already Used By Someone")
        else:

            messages.success(
                Request, "Password And Confirm Password Does't Matched !!!!!"
            )
    categories = Category.objects.all()

    return render(Request, "worker.html", {"categories": categories})


def LoginPage(Request):

    if Request.method == "POST":
        username = Request.POST.get("username")
        password = Request.POST.get("password")
        user = authenticate(username=username, password=password)
        # user1 = User.objects.get(username=username,password=password)
        try:
            if user.is_superuser:
                return redirect("/admin/")
            else:
                login(Request, user)
                return redirect("/")
        except:

            messages.error(
                Request, "Username Or Password Is Incurrect Please Try  Again !!!!!"
            )
    return render(Request, "login.html")


def LogOut(Request):
    logout(Request)
    return redirect("/")


def SearchPage(Request):
    search = Request.POST.get("search")
    # search1 = Request.POST.get('search1')
    try:
        data = Worker.objects.filter(Q(category_w__name__icontains=search))

    # location=Worker.objects.filter(Q(location__icontains=search1))

    except:
        pass

    return render(Request, "index.html", {"data": data})


def SearchLocation(Request):

    search = Request.POST.get("search1")
    data = Worker.objects.filter(Q(location__icontains=search))
    # print(data,'\n\n\n\n')
    return render(Request, "index.html", {"data": data})


@login_required(login_url="/login/")
def UpdateEmp(Request, id):
    data = Worker.objects.get(id=id)
    try:
        if Request.method == "POST":
            data.name = Request.POST.get("name")
            category_name = Request.POST.get("category")
            category_instance = Category.objects.get(name=category_name)
            data.category_w = (
                category_instance  # Set category_w with the Category instance
            )
            data.phone = Request.POST.get("phone")
            data.location = Request.POST.get("location")
            data.exprience = Request.POST.get("exprience")
            data.description = Request.POST.get("description")
            data.save()
            return redirect("/")
    except:
        messages.error(
            Request,
            "Please Enter Value Between (Carpainter | Painter | Mechanic | Plumber | Or Electrician) Only",
        )
    # categories=Category.objects.all()
    return render(Request, "updateEmp.html", {"data": data})


def UpdateProfile(Request):
    user = User.objects.get(username=Request.user)
    if user.is_superuser:
        return redirect("/admin/")
    else:
        buyer = Buyer.objects.get(username=user.username)
        if Request.method == "POST":
            buyer.name = Request.POST.get("name")
            buyer.phone = Request.POST.get("phone")
            buyer.email = Request.POST.get("email")
            buyer.pic = Request.FILES.get("pic")
            buyer.save()
            return redirect("/profile/")
    return render(Request, "Updateprofile.html", {"buyer": buyer})


@login_required(login_url="/login/")
def AddToCart(Request, id):
    cart = Request.session.get("cart", None)
    p = Worker.objects.get(id=id)
    if cart is None:
        cart = {
            str(p.id): {
                "pid": p.id,
                "pic": p.pic1.url,
                "pid": p.id,
                "name": p.name,
                "category_w": p.category_w.name,
                "phone": p.phone,
                "description": p.description,
                "location": p.location,
                "exprience": p.exprience,
            }
        }
        # Request.session['cart'] = cart

    else:
        # if str(p.id) in cart:
        #     item = cart[str(p.id)]
        cart.setdefault(
            str(p.id),
            {
                "pid": p.id,
                "pic": p.pic1.url,
                "pid": p.id,
                "name": p.name,
                "category_w": p.category_w.name,
                "phone": p.phone,
                "description": p.description,
                "location": p.location,
                "exprience": p.exprience,
            },
        )
    Request.session["cart"] = cart

    Request.session.set_expiry(60 * 60 * 24 * 45)
    return redirect("/cart/")


@login_required(login_url="/login/")
def cartfrontpage(Request):
    cart = Request.session.get("cart", None)
    c = []

    if cart is not None:
        for value in cart.values():

            c.append(value)

    return render(Request, "cart.html", {"cart": c})


@login_required(login_url="/login/")
def ProfileSection(Request):
    try:
        user = User.objects.get(username=Request.user)
        buyer = Buyer.objects.get(username=user.username)
    except:
        user = User.objects.get(username=Request.user)
        buyer = Worker.objects.get(username=user.username)
        return redirect("/EmployeeData/")
    return render(Request, "profile.html", {"buyer": buyer})


@login_required(login_url="/login/")
def ProfilePage(Request):
    user = User.objects.get(username=Request.user)
    if user.is_superuser:
        return redirect("/admin/")
    else:
        try:
            worker = Worker.objects.get(username=Request.user)
        except:
            user = User.objects.get(username=Request.user)
            buyer = Buyer.objects.get(username=Request.user)
            return redirect("/profile/")

    return render(Request, "EmployeeData.html", {"pro": worker})


# Worker.objects.add(buyeruser=service.username)
@login_required(login_url="/login/")
def BookService(Request, id):
    try:
        user = User.objects.get(username=Request.user)
        buyer = Buyer.objects.get(username=user.username)

    except:
        messages.success(
            Request,
            "Your Account has a worker account so you not book the service,Create a customer a account and Book Your Service",
        )
        return redirect("/signup/")
    try:
        service = Worker.objects.get(id=id)
        service.buyeruser.add(buyer)
        if Request.method == "POST":
            date = Request.POST.get("date")
            time = Request.POST.get("time")
            Servicebook.objects.create(
                date=date,
                time=time,
                buyerphone=buyer.phone,
                username=buyer.username,
                service=service.category_w,
                workerusername=service.username,
            )
            # worker= Worker.objects.create()
            # worker.buyeruser.set([buyer.username])

            return redirect("/booking/")
    except:
        messages.success(Request, "Your Service Has Been Successfully Booked")

    return render(Request, "service.html")


def all_services(Request):
    return render(Request, "all_services.html")





@login_required(login_url="/login/")
def DeleteService(Request, id):
    user = User.objects.get(username=Request.user)
    buyer = Buyer.objects.get(username=user.username)
    service = Servicebook.objects.filter(id=id)

    messages.success(
        Request, f"Hii {buyer.name} Your Service Has  Successfully Cancelled"
    )

    service.delete()

    return redirect("/booking/")


def ContactUS(Request):
    if Request.method == "POST":
        co = Contact()
        co.name = Request.POST.get("name")
        co.email = Request.POST.get("email")
        co.phone = Request.POST.get("phone")
        co.subject = Request.POST.get("subject")
        co.message = Request.POST.get("message")
        co.save()

        messages.success(
            Request,
            "Thanks to Share Your Query With US!! Our Team Will Contact You Soon!!!!",
        )
    return render(Request, "contact.html")


def ForgetUsername(Request):
    if Request.method == "POST":
        try:
            username = Request.POST.get("username")
            user = User.objects.get(username=username)
            if user.is_superuser:
                return redirect("/admin/")

            else:
                buyer = Buyer.objects.get(username=username)
                otp = randrange(100000, 999999)
                buyer.otp = otp
                buyer.save()
                subject = "OTP for Password Reset : Team Eshop"
                message = (
                    " OTP for Password Reset  is  " + str(otp) + "\nTeam OnlineBazar"
                )
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [
                    buyer.email,
                ]
                send_mail(subject, message, email_from, recipient_list)
                Request.session["resetuser"] = username
                return redirect("/forget-otp/")
        except:
            messages.error(Request, "Invalid Username !!!!!")
    return render(Request, "forget-username.html")


def forgetOTP(Request):
    if Request.method == "POST":
        try:
            username = Request.session.get("resetuser", None)
            otp = Request.POST.get("otp")
            if username:
                buyer = Buyer.objects.get(username=username)
                if int(otp) == buyer.otp:
                    return redirect("/password/")
                else:
                    messages.error(Request, "Invalid OTP !!!")
            else:
                messages.error(Request, "Unauthorized ! ! ! ! ! Try Again")
        except:
            messages.error(Request, "Invalid Value, Please Enter a valid OTP Number")

    return render(Request, "forget-otp.html")


def password(Request):
    if Request.method == "POST":
        password = Request.POST.get("password")
        cpassword = Request.POST.get("cpassword")
        username = Request.session.get("resetuser", None)
        if username:
            if password == cpassword:
                user = User.objects.get(username=username)
                user.set_password(password)
                user.save()
                return redirect("/login/")
            else:
                messages.error(
                    Request, "Password and Confirm Password Doesn't Matched!!!!"
                )
        else:
            messages.error(Request, "Unauthorized  user ! ! ! ! ! try Again")

    return render(Request, "password.html")
