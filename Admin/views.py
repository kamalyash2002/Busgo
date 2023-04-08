from django.shortcuts import render
import mysql.connector as m
# Create your views here.
def bus(request):
    conn=m.connect(host="localhost",user="root",password="Yash@2002",database="bms")
    z=conn.cursor()
    z.execute("create table if not exists buses(busid int primary key,type varchar(6),route varchar(150),no_of_seats int,fare int,emergerncy_no varchar(15),time varchar(10))")
    conn.commit()
    return render(request,"bus.html")
def bank(request):
    conn=m.connect(host="localhost",user="root",password="Yash@2002",database="bms")
    z=conn.cursor()
    z.execute("create table if not exists bank(accno varchar(15) primary key,amt int,password varchar(20))")
    return render(request,"bank.html")
def aprofile(request):
    n="admin"
    return render(request,"adminprofile.html",{"name":n})
def addbus(request):
    info={"Route":"route","Number of seats":"ns","Fare":"fare","Emergency Number":"eno","Time":"time"}
    info=info.items()
    return render(request,"bus.html",{"info1":info})
def add(request):
    conn=m.connect(host="localhost",user="root",password="Yash@2002",database="bms")
    z=conn.cursor()
    a=AID()
    b=request.GET.get("type")
    c=request.GET.get("route")
    d=request.GET.get("ns")
    e=request.GET.get("fare")
    f=request.GET.get("eno")
    g=request.GET.get("time")
    z.execute("insert into buses values({},'{}','{}',{},{},{},'{}')".format(a,b,c,d,e,f,g))
    conn.commit()
    return render(request,"bus.html")
def editbus(request):
    conn=m.connect(host="localhost",user="root",password="Yash@2002",database="bms")
    z=conn.cursor()
    a=request.GET.get("bid")
    b=request.GET.get("type")
    c=request.GET.get("route")
    d=request.GET.get("ns")
    e=request.GET.get("fare")
    f=request.GET.get("eno")
    g=request.GET.get("time")
    z.execute("update buses set type='{}',route='{}',no_of_seats='{}',fare='{}',emergerncy_no='{}',time='{}' where busid={}".format(b,c,d,e,f,g,a))
    conn.commit()
    return render(request,"bus.html")
def edit(request):
    conn=m.connect(host="localhost",user="root",password="Yash@2002",database="bms")
    bid=request.GET.get("bno")
    z=conn.cursor()
    z.execute("select * from buses where busid={}".format(bid))
    f=z.fetchone()
    conn.commit()
    return render(request,"bus.html",{"b":f})
def editacc(request):
    conn=m.connect(host="localhost",user="root",password="Yash@2002",database="bms")
    acc=request.GET.get("ano")
    z=conn.cursor()
    z.execute("select * from bank where accno={}".format(acc))
    f=z.fetchone()
    conn.commit()
    return render(request,"bank.html",{"d":f})
def editaccount(request):
    conn=m.connect(host="localhost",user="root",password="Yash@2002",database="bms")
    z=conn.cursor()
    a=request.POST.get("accno")
    b=request.POST.get("amt")
    c=request.POST.get("p")
    z.execute("update bank set amt='{}',password='{}' where accno={}".format(b,c,a))
    conn.commit()
    return render(request,"bank.html")
def delbus(request):
    conn=m.connect(host="localhost",user="root",password="Yash@2002",database="bms")
    z=conn.cursor()
    z.execute("select * from buses")
    f=z.fetchall()
    conn.commit()
    if f!=[]:
        return render(request,"bus.html",{"info2":f})
    else:
        nb="No buses available"
        return render(request,"bus.html",{"nb":nb})
def delete(request):
    bno=request.GET.get("bno")
    bno=int(bno)
    conn=m.connect(host="localhost",user="root",password="Yash@2002",database="bms")
    z=conn.cursor()
    z.execute("delete from buses where busid={}".format(bno))
    conn.commit()
    return render(request,"bus.html")
def addacc(request):
    info="Information"
    return render(request,"bank.html",{"info3":info})
def addaccount(request):
    conn=m.connect(host="localhost",user="root",password="Yash@2002",database="bms")
    z=conn.cursor()
    a=request.POST.get("accno")
    b=request.POST.get("amt")
    c=request.POST.get("p")
    z.execute("insert into bank values({},{},'{}')".format(a,b,c))
    conn.commit()
    return render(request,"bank.html")
def delacc(request):
    conn=m.connect(host="localhost",user="root",password="Yash@2002",database="bms")
    z=conn.cursor()
    z.execute("select accno,amt from bank")
    f=z.fetchall()
    conn.commit()
    if f!=[]:
        return render(request,"bank.html",{"info4":f})
    else:
        nb="No bank accounts available"
        return render(request,"bank.html",{"nb":nb})
def deleteacc(request):
    conn=m.connect(host="localhost",user="root",password="Yash@2002",database="bms")
    z=conn.cursor()
    a=request.GET.get("ano")
    z.execute("delete from bank where accno={}".format(a))
    conn.commit()
    return render(request,"bank.html")
def about_us(request):
    return render(request,"about_us.html")
def AID():
    conn=m.connect(host="localhost",user="root",password="Yash@2002",database="bms")
    c=conn.cursor()
    c.execute("select * from buses")
    a=c.fetchall()
    conn.commit()
    if a==[]:
        return 1
    else:
        return a[len(a)-1][0]+1
