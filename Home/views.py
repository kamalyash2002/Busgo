from django.shortcuts import render
import mysql.connector as m
# Create your views here.
f=""
def home(request):
    conn=m.connect(host="localhost",user="root",password="Yash@2002",database="bms")
    c=conn.cursor()
    c.execute("create table if not exists customers(name varchar(20),email varchar(100) primary key,password varchar(50),pho varchar(15),gender varchar(10))")
    conn.commit()
    c.execute("select * from customers")
    k=c.fetchall()
    if k==[]:
        c.execute("insert into customers values('{}','{}','{}',{},'{}')".format("admin","admin","password","NULL","NULL"))
        conn.commit()
        conn.close()
    return render(request,"home.html")
def signup(request):
    return render(request,"signup.html")
def Sign(request):
    conn=m.connect(host="localhost",user="root",password="Yash@2002",database="bms")
    c=conn.cursor()
    n=request.POST.get("name")
    i=request.POST.get("id")
    p=request.POST.get("Phno")
    g=request.POST.get("Gender")
    ps=request.POST.get("pass")
    c.execute("insert into customers values('{}','{}','{}',{},'{}')".format(n,i,ps,p,g))
    conn.commit()
    conn.close()
    return render(request,"Home.html")
def forpass(request):
    return render(request,"Forpass.html")
def Forpass(request):
    conn=m.connect(host="localhost",user="root",password="Yash@2002",database="bms")
    c=conn.cursor()
    n=request.POST.get("name")
    pn=request.POST.get("Phno")
    i=request.POST.get("id")
    p=request.POST.get("pass")
    cp=request.POST.get("cpass")
    c.execute("select * from customers where name='{}' and email='{}' and pho='{}' ".format(n,i,pn))
    info=c.fetchall()
    conn.commit()
    if p==cp and info!=[]:
        c.execute("update customers set password='{}' where name='{}' and email='{}' ".format(p,n,i))
        conn.commit()
        conn.close()
        return render(request,"Home.html")
    elif info==[]:
        ps="Invalid Details"
        return render(request,"Forpass.html",{"note":ps,})
    else:
        t=(n,pn,i)
        ps="Password Mismatched"
        return render(request,"Forpass.html",{"note":ps,"t":t})
def login(request):
    global f
    conn=m.connect(host="localhost",user="root",password="Yash@2002",database="bms")
    c=conn.cursor()
    i=request.POST.get("id")
    p=request.POST.get("pass")
    c.execute("select * from customers where email='{}' and password='{}' ".format(i,p))
    f=c.fetchall()
    if f!=[]:
        b=f[0][0]
        if b!='admin':
            c.execute("create table if not exists transactions(tid int primary key,busid int,name varchar(20),email varchar(30),startd varchar(20),endd varchar(20),date varchar(20),time varchar(20),seat_no varchar(100),emno varchar(20),tfare int,status varchar(30),accno varchar(30))")
            conn.commit()
            c.execute("delete from transactions where status='Not Paid'")
            conn.commit()
            return render(request,"Profile.html",{"name":b})
        else:
            return render(request,"adminprofile.html",{"name":b})
    else:
        a="Invalid Id or Password"
        return render(request,"Home.html",{"err":a})
def details():
    global f
    return f
