from django.shortcuts import render
from Home import views as inf
import mysql.connector as m
f=""
t=""
d=""
mains={}
n=""
list1=""
tf=""
ti=""
account=""
amt=""
busid=""
seats=""
maxseat=""
y=[]
def logout(request):
    return render(request,"Home.html")
def ticbook(request):
    return render(request,"bookticket.html")
def ctic(request):
    conn=m.connect(host="localhost",user="root",password="Yash@2002",database="bms")
    c=conn.cursor()
    a=inf.details()
    id=a[0][1]
    c.execute("select * from transactions where email='{}' ".format(id))
    k=c.fetchall()
    l=[]
    for i in k:
        l.append((i[0],i[1],i[4],i[5],i[6],i[7],i[10]))
    conn.close()
    if l!=[]:
        return render(request,"cancelticket.html",{"info":l})
    else:
        no="No Tickets Booked"
        return render(request,"cancelticket.html",{"no":no})
def cancel(request):
    conn=m.connect(host="localhost",user="root",password="Yash@2002",database="bms")
    c=conn.cursor()
    tid=request.GET.get("tid")
    c.execute("select tfare,accno from transactions where tid={}".format(int(tid)))
    k=c.fetchall()
    conn.commit()
    accno=k[0][1]
    tfare=k[0][0]
    c.execute("select * from bank where accno='{}'".format(accno))
    amt=c.fetchall()
    conn.commit()
    amount=amt[0][1]
    addamt=int(amount)+0.75*int(tfare)
    c.execute("update bank set amt={} where accno='{}'".format(addamt,accno))
    conn.commit()
    c.execute("delete from transactions where tid={}".format(tid))
    conn.commit()
    a=inf.details()
    id=a[0][1]
    c.execute("select * from transactions where email='{}' ".format(id))
    g=c.fetchall()
    conn.commit()
    l=[]
    for i in g:
        l.append((i[0],i[1],i[4],i[5],i[6],i[7],i[10]))
    conn.close()
    if g!=[]:
        return render(request,"cancelticket.html",{"info":l})
    else:
        no="No ticket"
        return render(request,"cancelticket.html",{"no":no})
def profile(request):
    a=inf.details()
    n=a[0][0]
    return render(request,"Profile.html",{"name":n})
def search(request):
    global f,t,d,list1
    f=request.GET.get("f")
    t=request.GET.get("t")
    d=request.GET.get("date")
    l=(f,t,d)
    conn=m.connect(host="localhost",user="root",password="Yash@2002",database="bms")
    c=conn.cursor()
    c.execute("select * from buses")
    k=c.fetchall()
    list1=[]
    for i in k:
        j=i[2].split(":")
        if f in j and t in j:
            list1.append((i[0],i[1],i[3],i[4],i[6]))
    conn.close()
    if list1!=[]:
        return render(request,"bookticket.html",{"info":list1,"l":l})
    else:
        na="No buses available for this route"
        return render(request,"bookticket.html",{"na":na,"l":l})
def cav(request):
    global d,list1,f,t,d,busid,seats,maxseat,y
    l=(f,t,d)
    conn=m.connect(host="localhost",user="root",password="Yash@2002",database="bms")
    c=conn.cursor()
    busid=request.GET.get("bid")
    c.execute("select seat_no from transactions where busid={} and date='{}' ".format(busid,d))
    k=c.fetchall()
    conn.commit()
    c.execute("select no_of_seats from buses where busid={}".format(busid))
    s=c.fetchone()
    conn.commit()
    maxseat=s[0]
    seats=[]
    for i in k:
        for j in i:
            j=j.split(",")
            for k in j:
                seats.append(int(k))
    v=[]
    for i in range(1,maxseat):
        v.append(i)
    y=[]
    for i in v:
        if i not in seats:
            y.append(i)
    c=0
    show="show"
    for i in seats:
        c+=1
    if seats==[]:
        yo="No Seats booked"
        return render(request,"bookticket.html",{"info":list1,"yo":yo,"s":maxseat,"l":l,"show":show})
    elif c==int(maxseat):
        yo="All Seats Booked for this date"
        return render(request,"bookticket.html",{"info":list1,"yo":yo,"l":l,"show":show})
    return render(request,"bookticket.html",{"info":list1,"seats":seats,"s":maxseat,"l":l,"show":show})
def book(request):
    global y,maxseat
    global busid
    conn=m.connect(host="localhost",user="root",password="Yash@2002",database="bms")
    c=conn.cursor()
    global f,t,d,main
    global n
    global list1
    global tf,ti
    l=(f,t,d)
    ti=AID()
    c.execute("select * from buses where busid={}".format(busid))
    k=c.fetchall()
    conn.commit()
    b=inf.details()
    n=b[0][0]
    id=b[0][1]
    frm=f
    to=t
    d=d
    pho=k[0][5]
    time=k[0][6]
    sno=request.GET.get("seats")
    snos=sno.split(",")
    totalseats=len(snos)
    tf=int(int(k[0][4])*totalseats)
    c.execute("select * from transactions where date='{}' and busid={}".format(d,busid))
    x=c.fetchall()
    conn.commit()
    h=0
    for i in snos:
        if int(i) not in y:
            h=1
            break
    if x==[] or h==0:
        status="Not Paid"
        accno="None"
        c.execute("insert into transactions values({},{},'{}','{}','{}','{}','{}','{}','{}','{}',{},'{}','{}')".format(ti,busid,n,id,f,t,d,time,sno,pho,tf,status,accno))
        conn.commit()
        conn.close()
        main={"Ticket Id":ti,"Bus Number":busid,"Name":n,"Email Id":id,"From":f,"To":t,"Date":d,"Time":time,"Seat Numbers":sno,"Emergency Number":pho,"Total Fare":tf}
        mains=main.items()
        return render(request,"payment.html",{"mains":mains})
    elif h==1:
        sab="Invalid Seats or Seats already book for this date"
        return render(request,"bookticket.html",{'info':list1,'w':sab,"seats":seats,"s":maxseat,"l":l,"show":"show"})
def pay(request):
    global main,tf,ti,account,amt
    accno=request.POST.get("Accno")
    account=accno
    pas=request.POST.get("Pass")
    conn=m.connect(host="localhost",user="root",password="Yash@2002",database="bms")
    c=conn.cursor()
    c.execute("select * from bank where accno={}".format(accno))
    i=c.fetchall()
    conn.commit()
    if i!=[]:
        pa=i[0][2]
        amt=i[0][1]
        amtleft=amt-int(tf)
    else:
        pa=""
    if pa==pas and i!=[]:
        if int(amtleft)>=0:
            p="Paid"
            c.execute("update transactions set status='{}',accno='{}' where tid={}".format(p,accno,ti))
            conn.commit()
            c.execute("update bank set amt={} where accno='{}' ".format(int(amtleft),accno))
            conn.commit()
            conn.close()
            tic=main.values()
            l=[tic]
            return render(request,"ticket.html",{"tic":l})
        else:
            note1="Not Sufficient balance to book ticket"
            note2="Cannot book tickets"
            mains=main.items()
            return render(request,"payment.html",{"mains":mains,"note1":note1,"note2":note2})
    else:
        note="Incorrect Id or Password"
        mains=main.items()
        return render(request,"payment.html",{"mains":mains,"note1":note})
def cancelticket(request):
    global account,amt,ti
    conn=m.connect(host="localhost",user="root",password="Yash@2002",database="bms")
    c=conn.cursor()
    c.execute("delete from transactions where tid={}".format(ti))
    conn.commit()
    c.execute("update bank set amt={} where accno={}".format(amt,account))
    conn.commit()
    a=inf.details()
    name=a[0][0]
    return render(request,"Profile.html",{"name":name})
def tb(request):
    return render(request,"bookticket.html")
def AID():
    conn=m.connect(host="localhost",user="root",password="Yash@2002",database="bms")
    c=conn.cursor()
    c.execute("select * from transactions")
    a=c.fetchall()
    conn.commit()
    if a==[]:
        return 101
    else:
        return a[len(a)-1][0]+1
