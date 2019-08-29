import tkinter,time,random,tkinter.messagebox
from tkinter import *
from PIL import Image, ImageTk
from s20190803.August_reply.tk_mysql_bank import mysql111,json111


js = json111.bank_json()
mys = mysql111.Bank_peoples()
mys.__init__()
mys.creattable1()
mys.creattable1_freeze()


class tk3:


    def Root_closing(self):
        root_closing = tkinter.Toplevel()
        root_closing.title('中华Python银行')
        root_closing.geometry('300x200')
        label1 = tkinter.Label(root_closing, text='卡号')
        label1.place(x=20, y=30)
        label2 = tkinter.Label(root_closing, text='密码')
        label2.place(x=20, y=60)

        entry1 = tkinter.Entry(root_closing)
        entry1.place(x=120, y=30)
        entry2 = tkinter.Entry(root_closing)
        entry2.place(x=120, y=60)

        def root_closing_get():
            res9 = mys.select_table_c_p()
            p = (int(entry1.get()), str(entry2.get()))
            if p in res9:
                res1 = mys.select_table_freeze()
                res2 = mys.select_table_bank_people()
                list1 = []
                list2 = []
                for e in res1:
                    list1.append(e[0])
                for i in res2:
                    list2.append(i[0])
                if int(entry1.get()) in list1:
                        tkinter.messagebox.showinfo('提示', '此账号已被冻结,请先解冻')
                elif int(entry1.get()) in list2:
                    mys.delete_table_clossing_account(entry1.get(), entry2.get())
                    tkinter.messagebox.showinfo('提示', '销户成功')
                    root_closing.destroy()
                else:
                    tkinter.messagebox.showinfo('提示', '没此账号')
            else:
                tkinter.messagebox.showinfo('提示', '登陆失败')

        button1 = tkinter.Button(root_closing, text='销   户', command=root_closing_get)
        button1.place(x=160, y=100)
        root_closing.mainloop()



    def Root_unfreeze(self):
        root_unfreeze = tkinter.Toplevel()
        root_unfreeze.title('中华Python银行')
        root_unfreeze.geometry('300x200')
        label1 = tkinter.Label(root_unfreeze, text='卡号')
        label1.place(x=20, y=30)
        label2 = tkinter.Label(root_unfreeze, text='密码')
        label2.place(x=20, y=60)

        entry1 = tkinter.Entry(root_unfreeze)
        entry1.place(x=120, y=30)
        entry2 = tkinter.Entry(root_unfreeze)
        entry2.place(x=120, y=60)

        def root_unfreeze_get():
            res9 = mys.select_table_c_p()
            p = (int(entry1.get()), str(entry2.get()))
            if p in res9:
                res1 = mys.select_table_freeze()
                list1 = []
                for e in res1:
                    list1.append(e[0])
                if int(entry1.get()) in list1:
                    mys.delete_table_freeze(entry1.get(), entry2.get())
                    tkinter.messagebox.showinfo('提示', '解冻账户成功')
                    root_unfreeze.destroy()
                else:
                    tkinter.messagebox.showinfo('提示', '没此账号')
            else:
                tkinter.messagebox.showinfo('提示', '登陆失败')

        button1 = tkinter.Button(root_unfreeze, text='解   结', command=root_unfreeze_get)
        button1.place(x=160, y=100)
        root_unfreeze.mainloop()


    def Root_freeze(self):
        root_freeze = tkinter.Toplevel()
        root_freeze.title('中华Python银行')
        root_freeze.geometry('300x200')
        label1 = tkinter.Label(root_freeze, text='卡号')
        label1.place(x=20, y=30)
        label2 = tkinter.Label(root_freeze, text='密码')
        label2.place(x=20, y=60)

        entry1 = tkinter.Entry(root_freeze)
        entry1.place(x=120, y=30)
        entry2 = tkinter.Entry(root_freeze)
        entry2.place(x=120, y=60)

        def root_freeze_get():
            res9 = mys.select_table_c_p()
            p = (int(entry1.get()), str(entry2.get()))
            if p in res9:
                res1 = mys.select_table_bank_people()
                list1 = []
                for e in res1:
                    list1.append(e[0])
                if int(entry1.get()) in list1:
                    mys.insert_table1_freeze(entry1.get(), entry2.get())
                    tkinter.messagebox.showinfo('提示', '冻结账户成功')
                    root_freeze.destroy()
                else:
                    tkinter.messagebox.showinfo('提示', '没此账号')
            else:
                tkinter.messagebox.showinfo('提示', '登陆失败')

        button1 = tkinter.Button(root_freeze, text='冻   结', command=root_freeze_get)
        button1.place(x=160, y=100)
        root_freeze.mainloop()


    def Root_transfer(self):
        root_transfer = tkinter.Toplevel()
        root_transfer.title('中华Python银行')
        root_transfer.geometry('300x200')
        label1 = tkinter.Label(root_transfer, text='卡号')
        label1.place(x=20, y=30)
        label2 = tkinter.Label(root_transfer, text='密码')
        label2.place(x=20, y=60)
        label3 = tkinter.Label(root_transfer, text='请输入转款金额')
        label3.place(x=20, y=90)
        label4 = tkinter.Label(root_transfer, text='请输入对方卡号')
        label4.place(x=20, y=120)

        entry1 = tkinter.Entry(root_transfer)
        entry1.place(x=120, y=30)
        entry2 = tkinter.Entry(root_transfer)
        entry2.place(x=120, y=60)
        entry3 = tkinter.Entry(root_transfer)
        entry3.place(x=120, y=90)
        entry4 = tkinter.Entry(root_transfer)
        entry4.place(x=120, y=120)

        def transfer_entry3_get():
            res = mys.select_view_balan(entry1.get(), entry2.get())
            if int(entry3.get()) > 0 and int(entry3.get()) % 100 == 0 and int(entry3.get()) <= int(res[0][0]):
                bal2 = int(res[0][0]) - int(entry3.get())
                mys.update_deposit(bal2, entry1.get(), entry2.get())

                res1 = mys.select_view_balan_single(entry4.get())
                bal3 = int(res1[0][0]) + int(entry3.get())
                mys.update_transfer(bal3, entry4.get())
                tkinter.messagebox.showinfo('提示', '转账成功')
                root_transfer.destroy()
            elif int(entry3.get()) >= int(res[0][0]):
                for k in res:
                    k1 = int(k[0])
                tkinter.messagebox.showinfo('提示', '余额不足,余额为{}'.format(str(k1)))
            else:
                tkinter.messagebox.showinfo('提示', '请输入100倍的正整数')

        def root_transfer_get():
            res9 = mys.select_table_c_p()
            p = (int(entry1.get()), str(entry2.get()))
            if p in res9:
                res1 = mys.select_table_freeze()
                res2 = mys.select_table_bank_people()
                list1 = []
                list2 = []
                for e in res1:
                    list1.append(e[0])
                for i in res2:
                    list2.append(i[0])
                if int(entry1.get()) in list2 and int(entry4.get()) in list2 and int(entry4.get()) != int(entry1.get()):
                    transfer_entry3_get()
                elif int(entry1.get()) in list1:
                    tkinter.messagebox.showinfo('提示', '你的账号已被冻结,无法转账')
                elif int(entry4.get()) in list1:
                    tkinter.messagebox.showinfo('提示', '对方账号已被冻结,无法转账')
                else:
                    tkinter.messagebox.showinfo('提示', '转账失败')
            else:
                tkinter.messagebox.showinfo('提示', '登陆失败')

        button1 = tkinter.Button(root_transfer, text='确   定', command=root_transfer_get)
        button1.place(x=160, y=150)
        root_transfer.mainloop()

    def Root_withdrawal(self):
        root_withdrawal = tkinter.Toplevel()
        root_withdrawal.title('中华Python银行')
        root_withdrawal.geometry('300x200')
        label1 = tkinter.Label(root_withdrawal, text='卡号')
        label1.place(x=20, y=30)
        label2 = tkinter.Label(root_withdrawal, text='密码')
        label2.place(x=20, y=60)
        label3 = tkinter.Label(root_withdrawal, text='请输入取款金额')
        label3.place(x=20, y=90)

        entry1 = tkinter.Entry(root_withdrawal)
        entry1.place(x=120, y=30)
        entry2 = tkinter.Entry(root_withdrawal)
        entry2.place(x=120, y=60)
        entry3 = tkinter.Entry(root_withdrawal)
        entry3.place(x=120, y=90)

        def withdrawal_entry3_get():
            res = mys.select_view_balan(entry1.get(), entry2.get())
            if int(entry3.get()) > 0 and int(entry3.get()) % 100 == 0 and int(entry3.get()) <= int(res[0][0]):
                bal2 = int(res[0][0]) - int(entry3.get())
                mys.update_deposit(bal2, entry1.get(), entry2.get())
                tkinter.messagebox.showinfo('提示', '取款成功')
                root_withdrawal.destroy()
            elif int(entry3.get()) >= int(res[0][0]):
                for k in res:
                    k1 = int(k[0])
                tkinter.messagebox.showinfo('提示', '余额不足,余额为{}'.format(str(k1)))
            else:
                tkinter.messagebox.showinfo('提示', '请输入100倍的正整数')

        def withdrawal1():
            res2 = mys.select_table_bank_people()
            list1 = []
            for i in res2:
                list1.append(i[0])
            if int(entry1.get()) in list1:
                withdrawal_entry3_get()
            else:
                tkinter.messagebox.showinfo('提示', '无此账号')

        def withdrawal2():
            res1 = mys.select_table_freeze()
            res2 = mys.select_table_bank_people()
            list1 = []
            list2 = []
            for e in res1:
                list1.append(e[0])
            for i in res2:
                list2.append(i[0])
            if int(entry1.get()) in list2 and int(entry1.get()) not in list1:
                withdrawal_entry3_get()
            elif int(entry1.get()) in list2 and int(entry1.get()) in list1:
                tkinter.messagebox.showinfo('提示', '此为冻结账号,请先解冻')
            else:
                tkinter.messagebox.showinfo('提示', '无此账号')

        def withdrawal_get():
            res9 = mys.select_table_c_p()
            p = (int(entry1.get()), str(entry2.get()))
            if p in res9:
                res1 = mys.select_table_freeze()
                if len(res1) == 0:
                    withdrawal1()
                else:
                    withdrawal2()
            else:
                tkinter.messagebox.showinfo('提示', '登陆失败')

        button1 = tkinter.Button(root_withdrawal, text='确   定', command=withdrawal_get)
        button1.place(x=160, y=130)
        root_withdrawal.mainloop()


    def Root_deposit(self):
        root_deposit = tkinter.Toplevel()
        root_deposit.title('中华Python银行')
        root_deposit.geometry('300x200')
        label1 = tkinter.Label(root_deposit, text='卡号')
        label1.place(x=20, y=30)
        label2 = tkinter.Label(root_deposit, text='密码')
        label2.place(x=20, y=60)
        label3 = tkinter.Label(root_deposit, text='请输入存款金额')
        label3.place(x=20, y=90)

        entry1 = tkinter.Entry(root_deposit)
        entry1.place(x=120, y=30)
        entry2 = tkinter.Entry(root_deposit)
        entry2.place(x=120, y=60)
        entry3 = tkinter.Entry(root_deposit)
        entry3.place(x=120, y=90)

        def deposit_entry3_get():
            res = mys.select_view_balan(entry1.get(), entry2.get())
            if int(entry3.get()) > 0 and int(entry3.get()) % 100 == 0:
                bal2 = int(entry3.get()) + int(res[0][0])
                mys.update_deposit(bal2, entry1.get(), entry2.get())
                tkinter.messagebox.showinfo('提示', '存款成功')
                root_deposit.destroy()
            else:
                tkinter.messagebox.showinfo('提示', '请输入100倍的正整数')

        def deposit1():
            res2 = mys.select_table_bank_people()
            list1 = []
            for i in res2:
                list1.append(i[0])
            if int(entry1.get()) in list1:
                deposit_entry3_get()
            else:
                tkinter.messagebox.showinfo('提示', '无此账号')

        def deposit2():
            res1 = mys.select_table_freeze()
            res2 = mys.select_table_bank_people()
            list1 = []
            list2 = []
            for e in res1:
                list1.append(e[0])
            for i in res2:
                list2.append(i[0])
            if int(entry1.get()) in list2 and int(entry1.get()) not in list1:
                deposit_entry3_get()
            elif int(entry1.get()) in list2 and int(entry1.get()) in list1:
                tkinter.messagebox.showinfo('提示', '此为冻结账号,请先解冻')
            else:
                tkinter.messagebox.showinfo('提示', '无此账号')

        def deposit_get():
            res9 = mys.select_table_c_p()
            p = (int(entry1.get()), str(entry2.get()))
            if p in res9:
                res1 = mys.select_table_freeze()
                if len(res1) == 0:
                    deposit1()
                else:
                    deposit2()
            else:
                tkinter.messagebox.showinfo('提示', '登陆失败')

        button1 = tkinter.Button(root_deposit, text='确   定', command=deposit_get)
        button1.place(x=160, y=130)
        root_deposit.mainloop()


    def Root_balan(self):
        root_balan = tkinter.Toplevel()
        root_balan.title('中华Python银行')
        root_balan.geometry('300x200')
        label1 = tkinter.Label(master=root_balan, text='账户名', bg='blue')
        label1.place(x=30, y=50)
        label2 = tkinter.Label(master=root_balan, text='密   码', bg='blue')
        label2.place(x=30, y=80)
        entry1 = tkinter.Entry(root_balan, bg='blue')
        entry1.place(x=80, y=50)
        entry2 = tkinter.Entry(root_balan, bg='blue')
        entry2.place(x=80, y=80)

        def view_balan():
            res9 = mys.select_table_c_p()
            p = (int(entry1.get()), str(entry2.get()))
            if p in res9:
                res1 = mys.select_table_freeze()
                res2 = mys.select_table_bank_people()
                list1 = []
                list2 = []
                for i in res1:
                    list1.append(i[0])
                for e in res2:
                    list2.append(e[0])
                if int(entry1.get()) in list1:
                    res = mys.select_view_balan(entry1.get(), entry2.get())
                    for k in res:
                        k1 = int(k[0])
                    tkinter.messagebox.showinfo('提示', '此为冻结账号,冻结金额为:{}'.format(str(k1)))
                    root_balan.destroy()
                elif int(entry1.get()) in list2:
                    res = mys.select_view_balan(entry1.get(), entry2.get())
                    for d in res:
                        d1 = int(d[0])
                    tkinter.messagebox.showinfo('提示', '账户余额为:{}'.format(str(d1)))
                    root_balan.destroy()
                else:
                    tkinter.messagebox.showinfo('提示', '无此账号')
            else:
                tkinter.messagebox.showinfo('提示', '登陆失败')

        button = tkinter.Button(root_balan, text='确定', bg='pink', command=view_balan)
        button.place(x=120, y=110)
        root_balan.mainloop()

    def main_interface(self):
        root3 = tkinter.Toplevel()
        root3.title('中华Python银行')
        root3.geometry('800x600')
        path3 = Image.open(r'E:\python23\logo3.jpg')
        photo3 = ImageTk.PhotoImage(path3)
        label = tkinter.Label(root3, image=photo3, height=0, width=0, compound='left')
        label.place(relx=0, rely=0)
        ft = ('', 18)
        button1 = tkinter.Button(root3, text='查询余额', font=ft, bg='blue', command=self.Root_balan)
        button1.place(x=100, y=20)
        button2 = tkinter.Button(root3, text='存    款', font=ft, bg='blue', command=self.Root_deposit)
        button2.place(x=100, y=100)
        button3 = tkinter.Button(root3, text='取    款', font=ft, bg='blue', command=self.Root_withdrawal)
        button3.place(x=100, y=180)
        button4 = tkinter.Button(root3, text='转    账', font=ft, bg='blue',command=self.Root_transfer)
        button4.place(x=580, y=20)
        button5 = tkinter.Button(root3, text='冻    结', font=ft, bg='blue',command=self.Root_freeze)
        button5.place(x=580, y=100)
        button6 = tkinter.Button(root3, text='解    冻', font=ft, bg='blue',command=self.Root_unfreeze)
        button6.place(x=580, y=180)
        button7 = tkinter.Button(root3, text='销    户', font=ft, bg='blue',command=self.Root_closing)
        button7.place(x=580, y=260)
        root3.mainloop()

    def interface_register(self):
        # root1.destroy()
        root2 = tkinter.Toplevel()
        root2.title('中华Python银行')
        root2.geometry('800x600')
        path2 = Image.open(r'E:\python23\logo2.jpg')
        photo2 = ImageTk.PhotoImage(path2)
        label = tkinter.Label(root2, image=photo2, height=0, width=0, compound='left')
        label.place(relx=0, rely=0)

        def tick():
            time2 = time.strftime('%H:%M:%S\n''%Y-%m-%d\n')
            clock.config(text=time2)
            clock.after(200, tick)

        clock = tkinter.Label(root2, font=('times', 8, 'bold'), bg='green')
        clock.grid(row=0, column=0)
        tick()
        ft1 = ('', 12)
        label1 = tkinter.Label(master=root2, text='账户名', bg='blue', font=ft1)
        label1.place(x=200, y=50)
        label2 = tkinter.Label(master=root2, text='密  码', bg='blue', font=ft1)
        label2.place(x=200, y=80)
        label3 = tkinter.Label(master=root2, text='密  码', bg='blue', font=ft1)
        label3.place(x=200, y=110)

        label4 = tkinter.Label(root2, text='姓  名', bg='blue', font=ft1)
        label4.place(x=200, y=140)
        label5 = tkinter.Label(root2, text='身份证', bg='blue', font=ft1)
        label5.place(x=200, y=170)
        label6 = tkinter.Label(root2, text='年  龄', bg='blue', font=ft1)
        label6.place(x=200, y=200)
        label7 = tkinter.Label(root2, text='性  别', bg='blue', font=ft1)
        label7.place(x=200, y=230)
        label8 = tkinter.Label(root2, text='手机号', bg='blue', font=ft1)
        label8.place(x=200, y=260)
        label9 = tkinter.Label(root2, text='地  址', bg='blue', font=ft1)
        label9.place(x=200, y=290)

        def suijihaoma():
            str1 = '1234567890'
            str2 = ''
            for i in range(1, 6):
                str2 += random.choice(str1)
            if str2[0] == '0':
                a = list(str2)
                str3 = '1'
                for i in range(1, len(a)):
                    str3 += str(a[i])
                return str3
            else:
                return str2

        e = StringVar()
        entry1 = tkinter.Entry(master=root2, bg='green', textvariable=e)
        e.set(suijihaoma())
        entry1.place(x=270, y=50)
        entry1['state'] = 'readonly'
        entry2 = tkinter.Entry(master=root2, bg='green')
        entry2.place(x=270, y=80)
        entry2['show'] = '*'
        entry3 = tkinter.Entry(master=root2, bg='green')
        entry3.place(x=270, y=110)
        entry3['show'] = '*'

        entry4 = tkinter.Entry(root2, bg='green')
        entry4.place(x=270, y=140)
        entry5 = tkinter.Entry(root2, bg='green')
        entry5.place(x=270, y=170)
        entry6 = tkinter.Entry(root2, bg='green')
        entry6.place(x=270, y=200)
        entry7 = tkinter.Entry(root2, bg='green')
        entry7.place(x=270, y=230)
        entry8 = tkinter.Entry(root2, bg='green')
        entry8.place(x=270, y=260)
        entry9 = tkinter.Entry(root2, bg='green')
        entry9.place(x=270, y=290)

        def mima():
            if entry2.get() == entry3.get():
                val = '密码一致'
                label10 = tkinter.Label(root2, textvariable=val)
                label10.place(x=450, y=110)
            else:
                val = '密码不一致'
                label10 = tkinter.Label(root2, textvariable=val)
                label10.place(x=450, y=110)
                entry2.delete(0, len(entry2.get()))
                entry3.delete(0, len(entry3.get()))

        def get_msg():
            card_id1 = entry1.get()
            password1 = entry2.get()
            name1 = entry4.get()
            id1 = entry5.get()
            age1 = entry6.get()
            sex1 = entry7.get()
            phone1 = entry8.get()
            adress1 = entry9.get()
            mys.insert_table1(card_id1, password1, name1, id1, age1, sex1, phone1, adress1)

        def bind_button1():
            mima()
            if entry2.get() == '' and entry3.get() == '':
                tkinter.messagebox.showinfo('提示', '注册失败')
            else:
                get_msg()
                tkinter.messagebox.showinfo('提示', '注册成功')
                js.json_write(entry1.get(), entry2.get())
                root2.destroy()
                self.main_interface()

        button1 = tkinter.Button(root2, text='注  册', bg='yellow', command=bind_button1)
        button1.place(x=260, y=330)

        button2 = tkinter.Button(root2, text='退  出', bg='yellow', command=root2.destroy)
        button2.place(x=360, y=330)
        root2.mainloop()

    def interface_login(self):
        root1 = tkinter.Tk()
        root1.title('中华Python银行')
        root1.geometry('800x600')
        # image_path = r'E:\python23\logo.gif'
        # pic = PhotoImage(file=image_path)
        path1 = Image.open(r'E:\python23\logo1.jpg')
        photo1 = ImageTk.PhotoImage(path1)
        label = tkinter.Label(root1, image=photo1, height=0, width=0, compound='left')
        label.place(relx=0, rely=0)

        def tick():
            time2 = time.strftime('%H:%M:%S\n''%Y-%m-%d\n')
            clock.config(text=time2)
            clock.after(200, tick)

        clock = tkinter.Label(root1, font=('times', 8, 'bold'), bg='green')
        clock.grid(row=0, column=0)
        tick()

        label1 = tkinter.Label(master=root1, text='卡   号:', bg='blue')
        label1.place(x=200, y=50)
        label2 = tkinter.Label(master=root1, text='密   码:', bg='blue')
        label2.place(x=200, y=80)

        entry1 = tkinter.Entry(master=root1, bg='green', bd=2)
        entry1.place(x=260, y=50)
        entry2 = tkinter.Entry(master=root1, bg='green', bd=2)
        entry2.place(x=260, y=80)
        entry2['show'] = '*'

        def get_login():
            res1 = mys.select_table_bank_people()
            if len(res1) == 0:
                tkinter.messagebox.showinfo('提示', '请先开户')
                entry1.delete(0, len(entry1.get()))
                entry2.delete(0, len(entry2.get()))
            else:
                res9 = mys.select_table_c_p()
                p = (int(entry1.get()), str(entry2.get()))
                if p in res9:
                    tkinter.messagebox.showinfo('提示', '登陆成功')
                    entry1.delete(0, len(entry1.get()))
                    entry2.delete(0, len(entry2.get()))
                    self.main_interface()
                else:
                    tkinter.messagebox.showinfo('提示', '登陆失败')
                    entry1.delete(0, len(entry1.get()))
                    entry2.delete(0, len(entry2.get()))

        button1 = tkinter.Button(root1, text='开  户', bg='yellow', command=self.interface_register)
        button1.place(x=260, y=150)
        button2 = tkinter.Button(root1, text='登  录', bg='yellow', command=get_login)
        button2.place(x=310, y=150)
        button3 = tkinter.Button(root1, text='退  出', bg='yellow', command=root1.destroy)
        button3.place(x=360, y=150)
        root1.mainloop()


f = tk3()
f.interface_login()
