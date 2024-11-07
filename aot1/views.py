from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.shortcuts import render, get_object_or_404

# Create your views here.

def fun1(request):
    return HttpResponse("Hii")

def fun2(request):
    return HttpResponse("Hello world!!")

def fun3(request):
    return render(request,"dumm.html")

def fun4(request):
    return render(request,"dumm.html",{'name':'Siya'})

def fun5(request):
    context={
        'fruits':['banana','apple','orange'],           #last comma is imp otherwise there is a chance of error
    }
    return render(request,"fruit.html",context)

def fun6(request):
    items=[
        {'name':'Phone','price':5000,'quantity':5},
        {'name':'TV','price':15000,'quantity':6},
        {'name':'Washing machine','price':7000,'quantity':10},
    ]
    return render(request,"item.html",{'item':items})

def task1(request):
    products=[
        {'name':'Laptop','Price':30000,'availability':'In Stock'},
        {'name':'Smartphone','Price':40000,'availability':'Out of Stock'},
        {'name':'Tablet','Price':20000,'availability':'In Stock'},
        {'name':'Headphones','Price':5000,'availability':'In Stock'},
    ]
    return render(request,"product.html",{'item':products})

def fun7(request):
    data=user.objects.all()                                     #retrieving the data that was added in the admin page..so import the models first
    return render(request,"all.html",{'data1':data})

# def fun8(request):
#     if request.method == 'POST':
#         id=request.POST.get('id')
#         name=request.POST.get('name')
#         age=request.POST.get('age')                             #get and post
#         date=request.POST.get('date')
#         user_obj=user()
#         user_obj.user_id=id
#         user_obj.user_name=name
#         user_obj.user_age=age
#         user_obj.date=date
#         user_obj.save()
#     return render(request,"addus.html")
def fun9(request):
    if request.method == 'POST':
        id=request.POST.get('id')
        name=request.POST.get('name')
        age=request.POST.get('age')                             #get and post
        date=request.POST.get('date')
        user.objects.create(user_id=id,user_name=name,user_age=age,date=date)
        return redirect('hi')
    return render(request,"addus.html")   




def task2a(request):
    if request.method == 'POST':
        id=request.POST.get('id')
        title=request.POST.get('title')
        author=request.POST.get('author')
        date=request.POST.get('date')
        isbn=request.POST.get('isbn')

        book_obj=Book()
        book_obj.book_id=id
        book_obj.title=title
        book_obj.author=author
        book_obj.published_date=date
        book_obj.isbn=isbn
        book_obj.save()
    return render(request,"bookfm.html")

def task2b(request):
    data=Book.objects.all()
    return render(request,"bookdp.html",{'data1':data})


def emp(request):
    if request.method == 'POST':
        id=request.POST.get('id')
        name=request.POST.get('name')
        age=request.POST.get('age')
        phno=request.POST.get('ph')

        emp_obj=Employee()
        emp_obj.emp_id=id
        emp_obj.emp_name=name
        emp_obj.emp_age=age
        emp_obj.emp_phno=phno
        emp_obj.save()
        return redirect('re')
    return render(request,"empfm.html")

def emp2(request):
    data=Employee.objects.all()
    return render(request,"emdp.html",{'data1':data})

def task3a(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        description=request.POST.get('description')
        price=request.POST.get('price')
        quantity=request.POST.get('Stockqnty')
        product_obj=Product()
        product_obj.pro_name=name
        product_obj.pro_desc=description
        product_obj.pro_price=price
        product_obj.stock_qntuy=quantity
        product_obj.save()
        return redirect('res')
    return render(request,"productfm.html")

def task3b(request):
    data=Product.objects.all()
    return render(request,"productdp.html",{'data1':data})


def delete_user(request,id):
    u=user.objects.get(user_id=id)
    u.delete()
    return redirect('hi')

def task4a(request):
    if request.method == 'POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        phno=request.POST.get('phonenum')
        address=request.POST.get('address')
        dob=request.POST.get('dob')

        cust_obj=Customer()
        cust_obj.first_name=fname
        cust_obj.last_name=lname
        cust_obj.email=email
        cust_obj.phone_number=phno
        cust_obj.address=address
        cust_obj.date_of_birth=dob
        cust_obj.save()
        return redirect('ct')

    return render(request,"custfm.html")

def task4b(request):
    data=Customer.objects.all()
    return render(request,"custdp.html",{'data1':data})

def delete_cust(request,id):
    cust=Customer.objects.get(pk=id)
    cust.delete()
    return redirect('ct')



def task5a(request):
    if request.method == 'POST':
        title=request.POST.get('title')
        content=request.POST.get('content')
        author=request.POST.get('author')

        blog_obj=Blog()
        blog_obj.title=title
        blog_obj.content=content
        blog_obj.author=author
        blog_obj.save()
        return redirect('bg')

    return render(request,"blogfm.html")

def task5b(request):
    data=Blog.objects.all()
    return render(request,"blogdp.html",{'data1':data})

def delete_blog(request,id):
    blog=Blog.objects.get(id=id)
    blog.delete()
    return redirect('bg')

def update_blog(request,id):
    blog=Blog.objects.get(id=id)
    if request.method == 'POST':
        title=request.POST.get('title')
        content=request.POST.get('content')
        author=request.POST.get('author')
        blog.title=title
        blog.content=content
        blog.author=author
        blog.save()
        return redirect('bg')
    return render(request,"update_blog.html",{'data':blog})

def prod(request):
    data=productmodel.objects.all()
    return render(request,"prodp.html",{'data1':data})
def prodv(request):
    user1=user.objects.all()
    if request.method == 'POST':
        id=request.POST.get('id')
        pname=request.POST.get('proname')
        prod_obj=productmodel()
        prod_obj.pro_id=id
        prod_obj.pro_name=pname
        prod_obj.user1=user.objects.get(user_id=request.POST.get('users'))
        prod_obj.save()
        return redirect("dm")
    
    return render(request,"profm.html",{'user':user1})


def employget(request):
    emp=employ.objects.all()
    return render(request,'emp_get.html',{'data':emp})        

def employadd(request):
    data=category.objects.all()
    if request.method == "POST":
        id=request.POST.get('id')
        name=request.POST.get('name')
        emp_obj=employ()
        emp_obj.emp_id=id
        emp_obj.emp_name=name
        emp_obj.cata=category.objects.get(cat_id=request.POST.get('cat'))
        emp_obj.save()
    return render(request,'empadd_form.html',{'data2':data})

def delete_emp(request,id):
    emp=employ.objects.get(emp_id=id)
    emp.delete()
    return redirect('get')
def update_emp(request,id):
    data=category.objects.all()
    data1=employ.objects.get(emp_id=id)
    if request.method == 'POST':
        id=request.POST.get('id')
        name=request.POST.get('name')
        data1.emp_id=id
        data1.emp_name=name
        data1.cata=category.objects.get(cat_id=request.POST.get('cat'))
        data1.save()
        return redirect('get')
    return render(request,"update_emp.html",{'value':data,'value1':data1})



#Task
def bookget(request):
    book=Bookm.objects.all()
    return render(request,"book_get.html",{'data':book})

def bookadd(request):
    data=Publisher.objects.all()
    if request.method == 'POST':
        name=request.POST.get('title')
        date=request.POST.get('pdate')
        isbn=request.POST.get('isbn')
        book_obj=Bookm()
        book_obj.title=name
        book_obj.pub_date=date
        book_obj.isbn=isbn
        book_obj.publisher=Publisher.objects.get(id=request.POST.get('pub'))
        book_obj.save()
        return redirect('gt')
    return render(request,"book_add.html",{'data2':data})

def book_del(request,id):
    book=Bookm.objects.get(id=id)
    book.delete()
    return redirect('gt')

def book_update(request,id):
    data=Publisher.objects.all()
    book=Bookm.objects.get(id=id)
    if request.method == 'POST':
        name=request.POST.get('title')
        date=request.POST.get('pdate')
        isbn=request.POST.get('isbn')
        book.title=name
        book.pub_date=date
        book.isbn=isbn
        book.publisher=Publisher.objects.get(id=request.POST.get('pub'))
        book.save()
        return redirect('gt')

    return render(request,"update_book.html",{'data':data,'data2':book})

#task
def courseget(request):
    cs=Course.objects.all()
    return render(request,'courseget.html',{'data':cs})

def studentget(request):
    std=Student.objects.all()
    return render(request,"student_get.html",{'data':std})

def studentadd(request):
    data=Course.objects.all()
    if request.method == 'POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        phno=request.POST.get('phno')
        student_obj=Student()
        student_obj.first_name=fname
        student_obj.last_name=lname
        student_obj.email=email
        student_obj.phone_number=phno
        student_obj.course=Course.objects.get(id=request.POST.get('cse'))
        student_obj.save()
        return redirect('st')
    return render(request,"studentadd_form.html",{'data':data})

def student_del(request,id):
    std=Student.objects.get(id=id)
    std.delete()
    return redirect('st')

def student_update(request,id):
    cs=Course.objects.all()
    std=Student.objects.get(id=id)
    if request.method == 'POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        phno=request.POST.get('phno')
        std.first_name=fname
        std.last_name=lname
        std.email=email
        std.phone_number=phno
        std.course=Course.objects.get(id=request.POST.get('cse'))
        std.save()
        return redirect('st')
    return render(request,"update_student.html",{'data':std,'data2':cs})

def course_list(request):
    courses=Course.objects.all()
    return render(request,"course_list.html",{'data2':courses})

def course_details(request,id):
    course=Course.objects.get(id=id)
    students=Student.objects.filter(course=course)
    return render(request,"course_details.html",{'course':course,'students':students})

#task
from django.db.models import Q
def organizerget(request):
    oraganizer=Organizer.objects.all()
    return render(request,"organizer_get.html",{'data':oraganizer})

def organizeradd(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phno=request.POST.get('phno')
        organizer_obj=Organizer()
        organizer_obj.name=name
        organizer_obj.contact_email=email
        organizer_obj.phone_number=phno
        organizer_obj.save()
        return redirect('or')
    return render(request,"organizeradd.html")

def organizer_del(request,id):
    orgainzer=Organizer.objects.get(id=id)
    orgainzer.delete()
    return redirect('or')

def organizer_update(request,id):
    orgainzer=Organizer.objects.get(id=id)
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phno=request.POST.get('phno')
        orgainzer.name=name
        orgainzer.contact_email=email
        orgainzer.phone_number=phno
        orgainzer.save()
        return redirect('or')
    return render(request,"update_organizer.html",{'data':orgainzer})


def eventget(request):
    event=Event.objects.all()
    if request.method == 'POST':
        value=request.POST.get('search')
        srch=Event.objects.filter(Q(title__icontains=value))
        return render(request,"event_get.html",{'data':srch})
    return render(request,"event_get.html",{'data':event})

def eventadd(request):
    organizer=Organizer.objects.all()
    if request.method == 'POST':
        title=request.POST.get('title')
        date=request.POST.get('date')
        lcn=request.POST.get('location')
        event_obj=Event()
        event_obj.title=title
        event_obj.date=date
        event_obj.location=lcn
        event_obj.organizer=Organizer.objects.get(id=request.POST.get('org'))
        event_obj.save()
        return redirect('ev')
    return render(request,"eventadd.html",{'data':organizer})

def event_del(request,id):
    event=Event.objects.get(id=id)
    event.delete()
    return redirect('ev')

def event_update(request,id):
    organizer=Organizer.objects.all()
    event=Event.objects.get(id=id)
    if request.method == 'POST':
        title=request.POST.get('title')
        date=request.POST.get('date')
        lcn=request.POST.get('location')
        event.title=title
        event.date=date
        event.location=lcn
        event.organizer=Organizer.objects.get(id=request.POST.get('org'))
        event.save()
        return redirect('ev')
    return render(request,"update_event.html",{'data':event,'data2':organizer})

def index_view(request):
    return render(request,"index.html")

#task
def post_get(request):
    po=Post.objects.all()
    return render(request,"post_list.html",{'data':po})

def post_add(request):
    if request.method == 'POST':
        title=request.POST.get('title')
        content=request.POST.get('content')
        post_obj=Post()
        post_obj.title=title
        post_obj.content=content
        post_obj.save()
        return redirect('po')
    return render(request,"post_add.html")

from .forms import postform
def post_v(request):
    if request.method == 'POST':
        form=postform(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=postform()
    return render(request,"posth.html",{'form':form})

def post_update(request,id):
    po=Post.objects.get(id=id)
    if request.method == 'POST':
        title=request.POST.get('title')
        content=request.POST.get('content')
        po.title=title
        po.content=content
        po.save()
        return redirect('po')
    return render(request,"post_update.html",{'data':po})

from .forms import UserRegistrationForm
def userreg_v(request):
    if request.method == 'POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()  
    else:
        form=UserRegistrationForm()
    return render(request,"userh.html",{'form':form})


def userimg(request):
    users=Userimg.objects.all()
    return render(request,"userimg_get.html",{'users':users})

#task
def image_get(request):
    img=Image.objects.all()
    return render(request,"image_get.html",{'data':img})

def img_add(request):
    if request.method== 'POST':
        titile=request.POST.get('title')
        img=request.FILES.get('img')
        img_obj=Image()
        img_obj.title=titile
        img_obj.Image_up=img
        img_obj.save()
        return redirect('im')
    return render(request,'imgadd_form.html')  

def fun10(request):
    return render(request,"base.html")
def fun12(request):
    return render(request,"home.html")
def fun13(request):
    return render(request,"about.html")

#task
def base2(request):
    return render(request,"base2.html")

def product(request):
    return render(request,"products.html")





    



    






