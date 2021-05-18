from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import *
import pymysql



#   정보 수정하기

def clear_box():
    resultbox.delete(0,END)
    messagebox.showinfo('완료','조회창을 초기화했습니다')


def insert_window():
    ins_window = Tk()
    ins_window.title("데이터를 입력합니다")
    ins_window.geometry("300x200")
    ins_window.resizable(width=FALSE, height=FALSE)
    
    nlabel0 = Label(ins_window, text = "추가할 데이터를 입력하세오", font =(15))
    nlabel0.place(x=10,y=10)

   #정보 삽입

    def insert():

        fid = ins_fid.get()
        fname = ins_fname.get()
        flo = ins_flo.get()
        fad = ins_fad.get()
        fch = ins_fch.get()
        fs = ins_fs.get()

        conn=pymysql.connect(host='127.0.0.1',user='Park',password='4415',\
        db='mini_pro',charset='utf8')
        cur=conn.cursor()

        cur.execute("use mini_pro")

        sql = "insert into smart_fac values('"+fid+"','"+fname+"','"+flo+"','"+fad+"','"+fch+"','"+fs+"')"

        try:
            cur.execute(sql)
        except:
            messagebox.showerror('오류','잘못된 입력입니다')
            return
        
        conn.commit()
        cur.close()
        conn.close()
        messagebox.showinfo('성공','입력되었습니다.')

        ins_window.quit()
        ins_window.destroy()

    #입력부

    button_ins = Button(ins_window, text = "입력",command = insert)
    button_ins.place(x=230,y=150)

    inlabel1 = Label(ins_window, text = "공장번호")
    inlabel1.place(x=5,y=55)
    ins_fid = Entry(ins_window, width = 10, bg = 'white')
    ins_fid.place(x=60,y=55)

    inlabel2 = Label(ins_window, text = "공장이름")
    inlabel2.place(x=5,y=85)
    ins_fname = Entry(ins_window, width = 10, bg = 'white')
    ins_fname.place(x=60,y=85)

    inlabel3 = Label(ins_window, text = "공장위치")
    inlabel3.place(x=5,y=115)
    ins_flo = Entry(ins_window, width = 10, bg = 'white')
    ins_flo.place(x=60,y=115)

    inlabel4 = Label(ins_window, text = "관리자")
    inlabel4.place(x=144,y=55)
    ins_fad = Entry(ins_window, width = 10, bg = 'white')
    ins_fad.place(x=190,y=55)
    
    inlabel5 = Label(ins_window, text = "점검일")
    inlabel5.place(x=144,y=85)
    ins_fch = Entry(ins_window, width = 10, bg = 'white')
    ins_fch.place(x=190,y=85)

    inlabel6 = Label(ins_window, text = "재고 수")
    inlabel6.place(x=142,y=115)
    ins_fs = Entry(ins_window, width = 10, bg = 'white')
    ins_fs.place(x=190,y=115)

 
    ins_window.mainloop()
    

#### 데이터 제거

def delete_window():
    del_window = Tk()
    del_window.title("데이터를 제거합니다")
    del_window.geometry("220x100")
    del_window.resizable(width=FALSE, height=FALSE)

    dlabel0 = Label(del_window, text = "삭제할 공장데이터의 ID를 입력하세요.")
    dlabel0.place(x=5,y=10)

    dlabel1 = Label(del_window, text = "공장ID")
    dlabel1.place(x=10,y=45)

    #정보 제거
          
    def delete():
            
        del_id = delete_Id.get()
            
        conn=pymysql.connect(host='127.0.0.1',user='Park',password='4415',\
                     db='mini_pro',charset='utf8')
            
        cur=conn.cursor()
        cur.execute("use mini_pro")

        sql = "delete from smart_fac where f_id = '"+del_id+"'"

        try:
            cur.execute(sql)
        except:
            messagebox.showerror('오류','잘못된 입력입니다')
            return
            
        conn.commit()
        conn.close()
        messagebox.showinfo('삭제완료','입력된 정보가 삭제되었습니다.')

        del_window.quit()
        del_window.destroy()


    delete_Id = Entry(del_window, width = 12, bg = 'white')
    delete_Id.place(x=60,y=48)

    button_del = Button(del_window, text = "삭제",command = delete)
    button_del.place(x=160,y=45)

    del_window.mainloop()

#############################
#        데이터 수정
#############################

#수정 1번 : 공장이름 수정

def up_fname():
    up_window = Tk()
    up_window.title("데이터를 수정합니다")
    up_window.geometry("240x150")
    up_window.resizable(width=FALSE, height=FALSE)

    uplabel0 = Label(up_window, text = "수정할 공장의 ID와 이름을 입력하세요.")
    uplabel0.place(x=10,y=10)
    uplabel1 = Label(up_window, text = "공장ID")
    uplabel1.place(x=5,y=50)
    uplabel2 = Label(up_window, text = "공장이름")
    uplabel2.place(x=5,y=100)

    def update():
        
        up_id = update_id.get()
        up_name = update_name.get()
        
        conn=pymysql.connect(host='127.0.0.1',user='Park',password='4415',\
                     db='mini_pro',charset='utf8')
            
        cur=conn.cursor()
        cur.execute("use mini_pro")

        sql = "update smart_fac set f_name = '"+up_name+"' where f_id = '"+up_id+"'"

        try:
            cur.execute(sql)
        except:
            messagebox.showerror('오류','잘못된 입력입니다')
            return
            
        conn.commit()
        conn.close()
        messagebox.showinfo('수정완료','입력된 정보가 수정되었습니다.')

        up_window.quit()
        up_window.destroy()

    update_id = Entry(up_window, width = 12, bg = 'white')
    update_id.place(x=80, y=55)
    update_name = Entry(up_window, width = 12, bg = 'white')
    update_name.place(x=80, y=105)

    button_up = Button(up_window, text = "수정", command = update)
    button_up.place(x=180,y=100)

    up_window.mainloop()

#수정 2번 : 공장위치 수정

def up_flo():
    up_window = Tk()
    up_window.title("데이터를 수정합니다")
    up_window.geometry("240x150")
    up_window.resizable(width=FALSE, height=FALSE)

    uplabel0 = Label(up_window, text = "수정할 공장의 ID와 위치를 입력하세요.")
    uplabel0.place(x=10,y=10)
    uplabel1 = Label(up_window, text = "공장ID")
    uplabel1.place(x=5,y=50)
    uplabel2 = Label(up_window, text = "공장위치")
    uplabel2.place(x=5,y=100)

    def update():
        
        up_id = update_id.get()
        up_lo = update_lo.get()
        
        conn=pymysql.connect(host='127.0.0.1',user='Park',password='4415',\
                     db='mini_pro',charset='utf8')
            
        cur=conn.cursor()
        cur.execute("use mini_pro")

        sql = "update smart_fac set f_location = '"+up_lo+"' where f_id = '"+up_id+"'"

        try:
            cur.execute(sql)
        except:
            messagebox.showerror('오류','잘못된 입력입니다')
            return
            
        conn.commit()
        conn.close()
        messagebox.showinfo('수정완료','입력된 정보가 수정되었습니다.')
        
        up_window.quit()
        up_window.destroy()

    update_id = Entry(up_window, width = 12, bg = 'white')
    update_id.place(x=80, y=55)
    update_lo = Entry(up_window, width = 12, bg = 'white')
    update_lo.place(x=80, y=105)

    button_up = Button(up_window, text = "수정", command = update)
    button_up.place(x=180,y=100)

    up_window.mainloop()

#수정 3번 : 관리자 수정

def up_fadm():
    up_window = Tk()
    up_window.title("데이터를 수정합니다")
    up_window.geometry("240x150")
    up_window.resizable(width=FALSE, height=FALSE)

    uplabel0 = Label(up_window, text = "수정할 공장의 ID와 관리자를 입력하세요.")
    uplabel0.place(x=10,y=10)
    uplabel1 = Label(up_window, text = "공장ID")
    uplabel1.place(x=5,y=50)
    uplabel2 = Label(up_window, text = "관리자")
    uplabel2.place(x=5,y=100)

    def update():
        
        up_id = update_id.get()
        up_adm = update_adm.get()
        
        conn=pymysql.connect(host='127.0.0.1',user='Park',password='4415',\
                     db='mini_pro',charset='utf8')
            
        cur=conn.cursor()
        cur.execute("use mini_pro")

        sql = "update smart_fac set f_adm = '"+up_adm+"' where f_id = '"+up_id+"'"

        try:
            cur.execute(sql)
        except:
            messagebox.showerror('오류','잘못된 입력입니다')
            return
            
        conn.commit()
        conn.close()
        messagebox.showinfo('수정완료','입력된 정보가 수정되었습니다.')
        
        up_window.quit()
        up_window.destroy()

    update_id = Entry(up_window, width = 12, bg = 'white')
    update_id.place(x=80, y=55)
    update_adm = Entry(up_window, width = 12, bg = 'white')
    update_adm.place(x=80, y=105)

    button_up = Button(up_window, text = "수정", command = update)
    button_up.place(x=180,y=100)

    up_window.mainloop()

#수정 4번 : 점검일 수정

def up_fcheck():
    up_window = Tk()
    up_window.title("데이터를 수정합니다")
    up_window.geometry("240x150")
    up_window.resizable(width=FALSE, height=FALSE)

    uplabel0 = Label(up_window, text = "수정할 공장의 ID와 점검일을 입력하세요.")
    uplabel0.place(x=10,y=10)
    uplabel1 = Label(up_window, text = "공장ID")
    uplabel1.place(x=5,y=50)
    uplabel2 = Label(up_window, text = "점검날짜")
    uplabel2.place(x=5,y=100)

    def update():
        
        up_id = update_id.get()
        up_check = update_check.get()
        
        conn=pymysql.connect(host='127.0.0.1',user='Park',password='4415',\
                     db='mini_pro',charset='utf8')
            
        cur=conn.cursor()
        cur.execute("use mini_pro")

        sql = "update smart_fac set f_check = '"+up_check+"' where f_id = '"+up_id+"'"

        try:
            cur.execute(sql)
        except:
            messagebox.showerror('오류','잘못된 입력입니다')
            return
            
        conn.commit()
        conn.close()
        messagebox.showinfo('수정완료','입력된 정보가 수정되었습니다.')
        
        up_window.quit()
        up_window.destroy()

    update_id = Entry(up_window, width = 12, bg = 'white')
    update_id.place(x=80, y=55)
    update_check = Entry(up_window, width = 12, bg = 'white')
    update_check.place(x=80, y=105)

    button_up = Button(up_window, text = "수정", command = update)
    button_up.place(x=180,y=100)

    up_window.mainloop()

#수정 5번 : 재고량 수정

def up_fsen():
    up_window = Tk()
    up_window.title("데이터를 수정합니다")
    up_window.geometry("240x150")
    up_window.resizable(width=FALSE, height=FALSE)

    uplabel0 = Label(up_window, text = "수정할 공장의 ID와 재고량을 입력하세요.")
    uplabel0.place(x=10,y=10)
    uplabel1 = Label(up_window, text = "공장ID")
    uplabel1.place(x=5,y=50)
    uplabel2 = Label(up_window, text = "재고량")
    uplabel2.place(x=5,y=100)

    def update():
        
        up_id = update_id.get()
        up_sen = update_sen.get()
        
        conn=pymysql.connect(host='127.0.0.1',user='Park',password='4415',\
                     db='mini_pro',charset='utf8')
            
        cur=conn.cursor()
        cur.execute("use mini_pro")

        sql = "update smart_fac set f_stock_all = '"+up_sen+"' where f_id = '"+up_id+"'"

        try:
            cur.execute(sql)
        except:
            messagebox.showerror('오류','잘못된 입력입니다')
            return
            
        conn.commit()
        conn.close()
        messagebox.showinfo('수정완료','입력된 정보가 수정되었습니다.')
        
        up_window.quit()
        up_window.destroy()

    update_id = Entry(up_window, width = 12, bg = 'white')
    update_id.place(x=80, y=55)
    update_sen = Entry(up_window, width = 12, bg = 'white')
    update_sen.place(x=80, y=105)

    button_up = Button(up_window, text = "수정", command = update)
    button_up.place(x=180,y=100)

    up_window.mainloop()

#########################################################################################
    
#정보 조회

def call_all():
   
    conn=pymysql.connect(host='127.0.0.1',user='Park',password='4415',\
                db='mini_pro',charset='utf8')
    
    cur=conn.cursor()
    cur.execute("use mini_pro")

    resultbox.delete(0,END)

    sql = "select * from smart_fac "

    try:
        cur.execute(sql)
        while True:
            row = cur.fetchone()
            if row== None:
                break
            f_id =row[0]
            f_name=row[1]
            f_location=row[2]
            f_adm=row[3]
            f_check=row[4]
            f_stock_all =row[5]
            txt = f_id+", " +f_name+ ", " +f_location+ ", " +f_adm+", "+str(f_check)+", "+str(f_stock_all)
            resultbox.insert(END,txt)
                
    except:
        messagebox.showerror('오류','잘못된 입력입니다')
        return
    
    cur.close()
    conn.close()
    messagebox.showinfo('성공','조회되었습니다.')
    
  
def call_id():
    
    fac_id = askstring("공장ID 조회","공장의 아이디를 입력하세요")
   
    conn=pymysql.connect(host='127.0.0.1',user='Park',password='4415',\
                db='mini_pro',charset='utf8')
    
    cur=conn.cursor()
    cur.execute("use mini_pro")

    resultbox.delete(0,END)

    sql = "select * from smart_fac where f_id = '"+fac_id+"'"

    try:
        cur.execute(sql)
        while True:
            row = cur.fetchone()
            if row== None:
                break
            f_id =row[0]
            f_name=row[1]
            f_location=row[2]
            f_adm=row[3]
            f_check=row[4]
            f_stock_all =row[5]
            txt = f_id+", " +f_name+ ", " +f_location+ ", " +f_adm+", "+str(f_check)+", "+str(f_stock_all)
            resultbox.insert(END,txt)
                
    except:
        messagebox.showerror('오류','잘못된 입력입니다')
        return
    
    cur.close()
    conn.close()
    messagebox.showinfo('성공','조회되었습니다.')
    
  
def call_name():
    
    fac_name = askstring("공장명 조회","공장명을 입력하세요")
   
    conn=pymysql.connect(host='127.0.0.1',user='Park',password='4415',\
                db='mini_pro',charset='utf8')
    
    cur=conn.cursor()
    cur.execute("use mini_pro")

    resultbox.delete(0,END)

    sql = "select * from smart_fac where f_name = '"+fac_name+"'"


    try:
        cur.execute(sql)
        while True:
            row = cur.fetchone()
            if row== None:
                break
            f_id =row[0]
            f_name=row[1]
            f_location=row[2]
            f_adm=row[3]
            f_check=row[4]
            f_stock_all =row[5]
            txt = f_id+", " +f_name+ ", " +f_location+ ", " +f_adm+", "+str(f_check)+", "+str(f_stock_all)
            resultbox.insert(END,txt)
                
    except:
        messagebox.showerror('오류','잘못된 입력입니다')
        return

    
    cur.close()
    conn.close()
    messagebox.showinfo('성공','조회되었습니다.')
    
    
def call_lo():
    
    fac_lo = askstring("위치 조회","공장 위치를 입력하세요")
   
    conn=pymysql.connect(host='127.0.0.1',user='Park',password='4415',\
                db='mini_pro',charset='utf8')
    
    cur=conn.cursor()
    cur.execute("use mini_pro")

    resultbox.delete(0,END)

    sql = "select * from smart_fac where f_location = '"+fac_lo+"'"


    try:
        cur.execute(sql)
        while True:
            row = cur.fetchone()
            if row== None:
                break
            f_id =row[0]
            f_name=row[1]
            f_location=row[2]
            f_adm=row[3]
            f_check=row[4]
            f_stock_all =row[5]
            txt = f_id+", " +f_name+ ", " +f_location+ ", " +f_adm+", "+str(f_check)+", "+str(f_stock_all)
            resultbox.insert(END,txt)
                
    except:
        messagebox.showerror('오류','잘못된 입력입니다')
        return
    cur.close()
    conn.close()
    messagebox.showinfo('성공','조회되었습니다.')
    

def call_adm():
    
    fac_adm = askstring("관리자 조회","관리자명을 입력하세요")
   
    conn=pymysql.connect(host='127.0.0.1',user='Park',password='4415',\
                db='mini_pro',charset='utf8')
    
    cur=conn.cursor()
    cur.execute("use mini_pro")

    resultbox.delete(0,END)

    sql = "select * from smart_fac where f_adm = '"+fac_adm+"'"


    try:
        cur.execute(sql)
        while True:
            row = cur.fetchone()
            if row== None:
                break
            f_id =row[0]
            f_name=row[1]
            f_location=row[2]
            f_adm=row[3]
            f_check=row[4]
            f_stock_all =row[5]
            txt = f_id+", " +f_name+ ", " +f_location+ ", " +f_adm+", "+str(f_check)+", "+str(f_stock_all)
            resultbox.insert(END,txt)
                
    except:
        messagebox.showerror('오류','잘못된 입력입니다')
        return

    
    cur.close()
    conn.close()
    messagebox.showinfo('성공','조회되었습니다.')


##############################################################
#                    처음 실행 창                            #
##############################################################

window = Tk()
window.title("공장 관리하기")
window.geometry("730x644")
window.resizable(width=FALSE, height=FALSE)

#상단 메뉴

all_menu = Menu(window)

ins_menu=Menu(all_menu , tearoff=0)
all_menu.add_cascade(label="정보 관리",menu=ins_menu)
ins_menu.add_command(label="추가하기", command = insert_window)
ins_menu.add_command(label="제거하기", command = delete_window)

new_menu=Menu(ins_menu)
ins_menu.add_cascade(label="수정하기",menu=new_menu)
new_menu.add_command(label="공장이름 수정",command = up_fname)
new_menu.add_command(label="공장위치 수정",command = up_flo)
new_menu.add_command(label="관리자 수정",command = up_fadm)
new_menu.add_command(label="점검일 수정",command = up_fcheck)
new_menu.add_command(label="재고량 수정",command = up_fsen)

see_menu=Menu(all_menu , tearoff=0)
all_menu.add_cascade(label="정보 조회",menu=see_menu)
see_menu.add_command(label="전체 조회", command = call_all)
see_menu.add_separator()
see_menu.add_command(label="ID로 조회", command = call_id)
see_menu.add_command(label="공장명으로 조회", command = call_name)
see_menu.add_command(label="공장 위치로 조회", command = call_lo)
see_menu.add_command(label="관리자 이름으로 조회", command = call_adm)


window.config(menu=all_menu)

#그림 삽입(gif 형식만 가능)

photo = PhotoImage(file='factory.gif')
photolabel=Label(window, image=photo)
photolabel.place(x=0,y=0)
#photolabel.pack(expand=1)

#텍스트 입

label0 = Label(window, text = "공장 관리 시스템에 오신 것을 환영합니다", font=("bold",20), bg = 'gray', fg='white')
label0.place(x=10,y=10)


#결과창

label1=Label(window, text = "조회 결과", font=("bold",15), bg='gray',fg='white')
label1.place(x=300, y=420)

resultbox = Listbox(window, bg='gray', fg='white', font=(10), width = 50, height = 10)
resultbox.place(x=300,y=450)

resultclear = Button(window, text = "결과 지우기", bg='gray', fg='white', command = clear_box)
resultclear.place(x=625, y=420)


window.mainloop()
