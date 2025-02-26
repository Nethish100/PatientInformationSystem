import mysql.connector
import random
from clrprint import *
import finalcsvconversion


cnx=mysql.connector.connect(user="root",passwd="",host="localhost")
cursor=cnx.cursor()

database="Patient"
sql="create database if not exists Patient"
cursor.execute(sql)

sql="use Patient"
cursor.execute(sql)

sql="create table if not exists Ids (Id varchar(50),Password varchar(50))"
cursor.execute(sql)

def register():
    y=str(clrinput(" Enter your username :",clr="magenta"))
    sql="select Id from Ids where Id like '{0}'".format(y)
    cursor.execute(sql)
    if cursor.fetchall():
        print("Id already exist try with other id")
        exit()
    else:
        z=clrinput(" Enter password :",clr="magenta")
        sql="insert into IDs (Id,Password) values ('{0}','{1}')".format(y,z)
        cursor.execute(sql)
        cnx.commit()
     

def login():
    i=str(clrinput(" Enter Id :- ",clr="yellow"))
    o=clrinput(" Enter password :- ",clr="yellow")
    print("\n")
    sql="select Id and Password from Ids where Id = '{0}' and Password = '{1}'".format(i,o)
    cursor.execute(sql)
    if cursor.fetchall():
        pass
    else:
        print("Please Try Again ! Wrong password or username")
        exit()

def Menu():
    clrprint('''---------------------------------//Menu//--------------------------------------''',clr="magenta")
    clrprint(" 1.Login\n","2.Register\n","3.Exit\n",clr=["red","green","yellow"])
    t=clrinput(" Enter your choice :- ",clr="green")
    if t=='1' or t=="Login" or t=="login":
        login()
    elif t=='2' or t=="Register" or t=="register":
        register()
    else:
        exit()
Menu()

sql='''create table if not exists Patients (PID varchar(500) not null Primary Key, F_Name varchar(50), S_Name varchar(150),
Mobile bigint, Dob date,Disease_History varchar(150), Gender char(11), Address varchar(200), City char(50), date_of_admission date, E_Age varchar(10),
B_Group varchar(20), Email varchar(50), Bed_number varchar(500))'''
cursor.execute(sql)

sql='''create table if not exists Doctors(Id varchar(50) not null Primary Key, F_Name varchar(50), S_Name varchar(50), Mobile bigint, Gender varchar(50), Address varchar(50), Dob date, Speciality varchar(50))'''
cursor.execute(sql)

sql='''create table if not exists Bill (Bed_number varchar(50), Patient_Id varchar(50), Name varchar(50), Date_of_Discharge date,
Total_Cost float(7), Cond_ition varchar(15), Vent_ilation varchar(5))'''
cursor.execute(sql)
cnx.commit()

def doctors():

    print("--------------------------------//Doctor Details//------------------------------")
    print("\n")

    Id=input("Assign an Id for the Doctor : - ")
    F=input("Enter First Name of the Doctor : - ")
    S=input("Enter Last name of the Doctor : - ")
    M=input("Enter Phone Number of the Doctor : - ")
    G=input("Enter Gender : - ")
    A=input("Enter Address : - ")
    d=input("Enter date of birth (YYYY-MM-DD) : - ")
    S=input("Enter Speciality : - ")

    if len(str(M))>10 or len(str(M))<10:
        print("PLEASE ENTER CORRECT MOBILE NUMBER/ 10 DIGIT PHONE NUMBER")

    else:
    
        sql='''insert into doctors(id,F_name,S_name,Mobile,Gender,Address,dob,Speciality) values ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}')'''.format(Id,F,S,M,G,A,d,S)
        cursor.execute(sql)
        cnx.commit()

        print("\nSUCCESSFULLY SAVED\n")
    
def patient():

    print("-------------------------------//Patient Details//----------------------------")

    y=int(input("Enter how many customer's detail you want to add : - "))
    print("\n")

    for i in range(y):
        pid=input("Enter Patient Id of Patient {0} :- ".format(i+1))
        f=input("Enter First Name of Patient {0} :- ".format(i+1))
        s=input("Enter Second Name of Patient {0} :- ".format(i+1))
        m=int(input("Enter Mobile number of Patient {0} :- ".format(i+1)))
        dob=input("Enter Date of Birth of Patient {0} :- ".format(i+1))
        dh=input("Enter Disease history of Patient {0} if had any :- ".format(i+1))
        g=input("Enter Gender of Patient {0} :- ".format(i+1))
        ha=input("Enter Home Address of Patient {0} :- ".format(i+1))
        ci=input("Enter City :- ".format(i+1))
        doa=input("Enter date of admission : - ")
        age=input("Enter Age of Patient {0} :- ".format(i+1))
        blood=input("Enter Blood Group of Patient {0} :- ".format(i+1))
        email=input("Enter Email Id of Patient {0} :- ".format(i+1))
        Doctor=input("Enter First name of Doctor who is going to treat : - ")

        sql="select * from Doctors where F_Name = '{0}'".format(Doctor)
        cursor.execute(sql)

        if cursor.fetchone():
            break
        else:
            print("\nDoctor Not Found ! Please Enter Doctor's Record First\n")
            doctors()
            
        if len(str(m))>10 or len(str(m))<10:
            print("PLEASE ENTER CORRECT MOBILE NUMBER/ 10 DIGIT PHONE NUMBER")
            break
        elif email.count('@')==0 and email.count(".")==0:
            print("PLEASE ENTER CORRECT EMAIL")
            break
        else:
            bed = pid + f[0:1] + s[0:1]

            con=input("Condition of patient i) Mild ii) Severe iii) Critical - ")
            vent=input("Any need of Ventilation i) Yes ii) No - ")
            dod=input("Enter period of admission (days) - ")
            if con=="i)" or con=="i" or con=="Mild" or con=="mild":
                cost1=100
            else:
                cost1=0
                
            if con=="ii)" or con=="ii" or con=="Severe" or con=="severe":
                cost2=500
            else:
                cost2=0
                
            if con=="iii)" or con=="iii" or con=="Critical" or con=="critical":
                cost3=600
            else:
                cost3=0

            if vent=="Yes" or vent=="yes" or vent=="i)" or vent=="i":
                cost4=1000
            else:
                cost4=0
                
            if vent=="No" or vent=="no" or vent=="ii)" or vent=="ii":
                cost5=500
            else:
                cost5=0

            totalvent=(int(cost4)+int(cost5))*int(dod)
            totalcri=(int(cost1)+int(cost2)+int(cost3))*int(dod)
            total=totalvent+totalcri
            gst=total*9/100
            totalc=total+gst
            print("\nTOTAL - ",total)
            print("GST - ",gst)
            print("TOTAL COST - ",totalc,"\n")
            
            ini=input("Save Record ? - ")
            
            if ini=="Yes" or ini=="yes":
                sql='''insert into bill(Bed_number,Patient_Id,Name,Date_of_Discharge,Total_Cost,Cond_ition,Vent_ilation) values('{0}','{1}','{2}','{3}','{4}','{5}','{6}')'''.format(bed,pid,f,dod,total,con,vent)
                cursor.execute(sql)
                cnx.commit()
                
                sql='''insert into Patients (PID,F_Name,S_Name,Mobile,Dob,Disease_History,Gender,Address,City,date_of_admission,E_Age,B_Group,Email,Bed_number)
                values ('{0}','{1}','{2}',{3},'{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}','{13}')'''.format(pid,f,s,m,dob,dh,g,ha,ci,doa,age,blood,email,bed)
                cursor.execute(sql)
                cnx.commit()
        
                print("\nRECORD ADDED SUCCESSFULLY\n")

            else:
                pass
                
    print("\n") 

def update():
    print("--------------------------------//Update Record//------------------------------")

    ei=input("Enter ID of patient :-")

    sql="select * from patients where pid = '{0}'".format(ei)
    cursor.execute(sql)

    rec=cursor.fetchone()

    if rec:
        print("DATA FOUND SUCCESSFULLY\n")

        print("*PATIENT ID CANNOT BE CHANGED*\n")
        
        print("PATIENT ID - %s"%rec[0])
        print("FIRST NAME - %s"%rec[1])
        print("SECOND NAME - %s"%rec[2])
        print("MOBILE NUMBER - %d"%rec[3])
        print("DATE OF BIRTH - %s"%rec[4])
        print("DISEASE HISTORY - %s"%rec[5])
        print("GENDER - %s"%rec[6])
        print("ADDRESS - %s"%rec[7])
        print("CITY - %s"%rec[8])
        print("DATE OF ADMISSION - %s"%rec[9])
        print("AGE - %s"%rec[10])
        print("BLOOD GROUP - %s"%rec[11])
        print("EMAIL - %s"%rec[12])
        print("Bed - %s"%rec[13])

        print("\nPLEASE ENTER EVERY INFORMATION WITH UPDATION\n")

        f=input("Enter First Name of Patient :- ")
        s=input("Enter Second Name of Patient :- ")
        m=int(input("Enter Mobile number of Patient :- "))
        dob=input("Enter Date of Birth of Patient :- ")
        dh=input("Enter Disease history of Patient if had any :- ")
        g=input("Enter Gender of Patient :- ")
        ha=input("Enter Home Address of Patient :- ")
        ci=input("Enter City :- ")
        doa=input("Enter Date of admission :- ")
        age=input("Enter Age of Patient :- ")
        blood=input("Enter Blood Group of Patient :- ")
        email=input("Enter Email Id of Patient :- ")

       
        sql='''update patients set f_name = '{0}', s_name = '{1}', Mobile = {2}, Dob = '{3}', Disease_History = '{4}', Gender = '{5}',
        Address = '{6}',E_Age = '{7}',B_Group = '{8}',Email = "{9}", City = "{10}", date_of_admission = "{11}" '''.format(f,s,m,dob,dh,g,ha,age,blood,email,ci,doa)
        cursor.execute(sql)
        cnx.commit()

        print("\nSUCCESSFULLY UPDATED DATA\n")

    else:
        print("RECORD NOT FOUND ! PLEASE CHECK AGAIN")
    print("\n")

def Search():
    print("--------------------------------//Search Record//------------------------------")

    y=input("Enter patient id : - ")

    sql="select * from patients where pid = '{0}'".format(y)
    cursor.execute(sql)

    rec=cursor.fetchone()

    if rec:
        print("\nDATA FOUND\n")

        print("PATIENT ID - %s"%rec[0])
        print("BED NUMBER - %s"%rec[13])
        print("FIRST NAME - %s"%rec[1])
        print("SECOND NAME - %s"%rec[2])
        print("MOBILE NUMBER - %d"%rec[3])
        print("DATE OF BIRTH - %s"%rec[4])
        print("DISEASE HISTORY - %s"%rec[5])
        print("GENDER - %s"%rec[6])
        print("ADDRESS - %s"%rec[7])
        print("CITY - %s"%rec[8])
        print("DATE OF ADMISSION - %s"%rec[9])
        print("AGE - %s"%rec[10])
        print("BLOOD GROUP - %s"%rec[11])
        print("EMAIL - %s"%rec[12])
        
        print("\n")

    else:
        print("\nRECORD NOT FOUND\n")
    
def Delete():
    print("--------------------------------//Delete Record//------------------------------")

    eu=input("Enter patient id to delete : - ")

    sql="delete from patients where pid = '{0}'".format(eu)
    cursor.execute(sql)
    cnx.commit()

    rec=cursor.fetchone()

    if rec:
        sql="delete from bill where pid = '{0}'".format(eu)
        cursor.execute(sql)
        cnx.commit()

        print("DATA DELETED SUCCESSFULLY")

    else:
        print("\nRECORD NOT FOUND\n")

def Display():
    print("--------------------------------//Display Records//-----------------------------")

    sql="select * from patients"
    cursor.execute(sql)

    rec=cursor.fetchall()
    row=cursor.rowcount

    print("TOTAL {0} RECORDS FOUND".format(row))
    print("\n")

    for i in rec:
        print("PATIENT ID - "+i[0])
        print("FIRST NAME - "+i[1])
        print("SECOND NAME - "+i[2])
        print("MOBILE NUMBER - "+str(i[3]))
        print("DATE OF BIRTH - "+str(i[4]))
        print("DISEASE HISTORY - "+i[5])
        print("GENDER - "+i[6])
        print("ADDRESS - "+i[7])
        print("CITY - "+i[8])
        print("Date of Admission - "+str(i[9]))
        print("AGE - "+i[10])
        print("BLOOD GROUP - "+i[11])
        print("EMAIL - "+i[12])
        print("BED NUMBER - "+i[13])
        print("\n")

def Condition():
    print("-----------------------------//Condition of Patient//---------------------------")

    count=0
    count1=0
    count2=0
    
    sql="select count(cond_ition) from bill where Cond_ition = '{0}' or Cond_ition = '{1}' or Cond_ition = '{2}' or Cond_ition = '{3}'".format("Mild","mild","i","i)")
    cursor.execute(sql)

    rec=cursor.fetchall()
    for i in rec:
        count=i

    sql="select count(cond_ition) from bill where Cond_ition = '{0}' or Cond_ition = '{1}' or Cond_ition = '{2}' or Cond_ition = '{3}'".format("Severe","severe","ii","ii)")
    cursor.execute(sql)

    rec=cursor.fetchall()
    for i in rec:
        count1=i

    sql="select count(cond_ition) from bill where Cond_ition = '{0}' or Cond_ition = '{1}' or Cond_ition = '{2}' or Cond_ition = '{3}'".format("Critical","critical","iii","iii)")
    cursor.execute(sql)

    rec=cursor.fetchone()
    for i in rec:
        count2=i

    print("Number of patients with mild condition = ",count)
    print("Number of patients with severe condition = ",count1)
    print("Number of patients with critical condition = ",count2)
    print("\n")

def Display_D():
    print("--------------------------------//Display Records//-----------------------------")

    sql="select * from doctors"
    cursor.execute(sql)

    rec=cursor.fetchall()
    row=cursor.rowcount

    print("TOTAL {0} RECORDS FOUND".format(row))
    print("\n")

    for i in rec:
        print("ID - "+i[0])
        print("First Name - %s"%i[1])
        print("Last Name - %s"%i[2])
        print("Mobile - %s"%i[3])
        print("Gender - %s"%i[4])
        print("Address - %s"%i[5])
        print("Date of Birth - %s"%i[6])
        print("Speciality - %s"%i[7])
        
        print("\n")

def Delete_D():
    print("--------------------------------//Delete Record//------------------------------")

    eu=input("Enter id to delete : - ")

    sql="select * from doctors where id = '{0}'".format(eu)
    cursor.execute(sql)

    rec=cursor.fetchone()

    if rec:
        sql="delete from doctors where id = '{0}'".format(eu)
        cursor.execute(sql)
        cnx.commit()

        print("\n DATA DELETED SUCCESSFULLY")

    else:
        print("\n RECORD NOT FOUND\n")

def update_d():
    print("--------------------------------//Update Record//------------------------------")

    ei=input("Enter ID of Doctor :-")

    sql="select * from doctors where id = '{0}'".format(ei)
    cursor.execute(sql)

    rec=cursor.fetchone()

    if rec:
        print("DATA FOUND SUCCESSFULLY\n")

        print("*ID CANNOT BE CHANGED*\n")
        
        print("FIRST NAME - %s"%rec[1])
        print("SECOND NAME - %s"%rec[2])
        print("MOBILE NUMBER - %d"%rec[3])
        print("Gender - %s"%rec[4])
        print("Address - %s"%rec[5])
        print("Date of Birth - %s"%rec[6])
        print("Speciality - %s"%rec[7])

        print("\nPLEASE ENTER EVERY INFORMATION WITH UPDATION\n")

        f=input("Enter First Name :- ")
        s=input("Enter Second Name of :- ")
        m=int(input("Enter Mobile number of :- "))
        g=input("Enter Gender :- ")
        a=input("Enter Address :- ")
        d=input("Enter Date of Birth :- ")
        S=input("Enter speciality :- ")
        

        #(Id varchar(50) not null Primary Key, F_Name varchar(50), S_Name varchar(50), Mobile bigint, Gender varchar(50), Address varchar(50), Dob date, Speciality varchar(50))'''

       
        sql='''update doctors set f_name = '{0}', s_name = '{1}', Mobile = {2}, Dob = '{3}', Gender = '{4}', Address = '{5}',
        Dob = '{6}',Speciality = '{7}' where id = "{7}"'''.format(f,s,m,g,a,d,S,ei)
        cursor.execute(sql)
        cnx.commit()

        print("\nSUCCESSFULLY UPDATED DATA\n")

    else:
        print("RECORD NOT FOUND ! PLEASE CHECK AGAIN")
    print("\n")

    
def Search_D():
    print("--------------------------------//Search Record//------------------------------")

    y=input("Enter Doctor id : - ")

    sql="select * from doctors where id = '{0}'".format(y)
    cursor.execute(sql)

    rec=cursor.fetchone()

    if rec:
        print("\nDATA FOUND\n")

        print("ID - %s"%rec[0])
        print("First Name - %s"%rec[1])
        print("Last Name - %s"%rec[2])
        print("Mobile - %s"%rec[3])
        print("Gender - %s"%rec[4])
        print("Address - %s"%rec[5])
        print("Date of Birth - %s"%rec[6])
        print("Speciality - %s"%rec[7])
        
        print("\n")

    else:
        print("\nRECORD NOT FOUND\n")


def Main():
    while True:
        clrprint('''--------------------------//Patient Information System//------------------------''',clr="magenta")
        clrprint(" 1. Add Doctor's Record\n","2. Add Patient Record\n","3. Update Record\n","4. Update Doctor's Record\n","5. Search Patient\n",
        "6. Search Doctor's Record\n","7. Delete Record\n","8. Delete Doctor's Record\n","9. Display Records\n","10. Display Doctors Record\n","11. CSV Report Writing\n","12. Condition of Patient\n",
        "13. Exit\n",clr=["magenta","red","green","yellow","magenta","red","green","yellow","magenta","red","green","yellow","magenta"])

        e=int(clrinput(" Enter your choice :- ",clr="yellow"))
        if e==1:
            doctors()
        elif e==2:
            patient()
        elif e==3:
            update()
        elif e==4:
            update_d()
        elif e==5:
            Search()
        elif e==6:
            Search_D()
        elif e==7:
            Delete()
        elif e==8:
            Delete_D()
        elif e==9:
            Display()
        elif e==10:
            Display_D()
        elif e==11:
            tables=input("Enter 1 to select Patients Table\n2 for doctors table : - ")
            if tables=="1":
                table="Patients"
                database="Patient"
                finalcsvconversion.csvwrite_module(database,table)
            elif tables=="2":
                table="Doctors"
                database="Patient"
                finalcsvconversion.csvwrite_module(database,table)
        elif e==12:
            Condition()
        elif e==13:
            y=int(clrinput(" Enter 1 to exit or 2 to go back to menu : - ",clr="red"))
            if y==1:
                exit()
            else:
                Main()
Main()
