import pymysql
class mysqlstudent():


    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='xingpeixun',db='pythonclass')
        print(self.conn)


    def creattable(self):
        cursor = self.conn.cursor()
        self.conn.begin()
        cursor.execute('drop table if exists mysql_student')
        cursor.execute('create table mysql_student (id int primary key auto_increment,name varchar(10) not null,age varchar(4),sex varchar(2),education text not null,phone varchar(12) not null,class_ varchar(10),introducer varchar(10),address text)')
        self.conn.commit()
        row = cursor.fetchall()
        return row
        # cursor.close()
        # self.conn.close()


    def insert_table(self,name1,age1,sex1,education1,phone1,class_1,introducer1,address1):
            cursor = self.conn.cursor()
            self.conn.begin()
            a1='insert into mysql_student(name,age,sex,education,phone,class_,introducer,address) values (%s,%s,%s,%s,%s,%s,%s,%s)'
            a2=(name1,age1,sex1,education1,phone1,class_1,introducer1,address1)
            cursor.execute(a1,a2)
            self.conn.commit()
            row = cursor.fetchall()
            return row
            # cursor.close()
            # self.conn.close()

    def delete_table(self,phone1):
        cursor = self.conn.cursor()
        self.conn.begin()
        b1="delete from mysql_student where phone=%s"
        b2 = phone1
        cursor.execute(b1,b2)
        self.conn.commit()
        row = cursor.fetchall()
        return row
        # cursor.close()
        # self.conn.close()


    def update_table(self,name1,age1,sex1,education1,phone1,class_1,introducer1,address1,name,phone):
        cursor = self.conn.cursor()
        self.conn.begin()
        c1 = 'update mysql_student set name=%s,age=%s,sex=%s,education=%s,phone=%s,class_=%s,introducer=%s,address=%s where name = %s and phone = %s;'
        c2 = (name1,age1,sex1,education1,phone1,class_1,introducer1,address1,name,phone)
        cursor.execute(c1,c2)
        self.conn.commit()
        row = cursor.fetchall()
        return row
        # cursor.close()
        # self.conn.close()


    def select_table(self,phone1):
        cursor = self.conn.cursor()
        self.conn.begin()
        d1= 'select * from mysql_student where phone=%s'
        d2 = phone1
        cursor.execute(d1,d2)
        self.conn.commit()
        row = cursor.fetchall()
        return row
        # cursor.close()
        # self.conn.close()


    def select_all(self):
        cursor = self.conn.cursor()
        self.conn.begin()
        cursor.execute('select * from mysql_student')
        self.conn.commit()
        row = cursor.fetchall()
        return row
        # cursor.close()
        # self.conn.close()


    def select_all1(self):
        cursor = self.conn.cursor()
        self.conn.begin()
        cursor.execute('select name from mysql_student')
        self.conn.commit()
        row = cursor.fetchall()
        return row
        # cursor.close()
        # self.conn.close()


ms = mysqlstudent()
while 1:

    code = input('请输入你的选择:')
    if code == '1':
        ms.creattable()
    elif code == '2':
        name = input('名字:')
        age = input('岁数:')
        sex = input('性别:')
        education = input('学历:')
        phone = input('电话:')
        class_ = input('班级:')
        introducer = input('介绍人:')
        address = input('地址:')
        ms.insert_table(name1=name,age1=age,sex1=sex,education1=education,phone1=phone,class_1=class_,introducer1=introducer,address1=address)

    elif code == '3':
        phone = input('请输入电话:')
        ms.delete_table(phone)

    elif code == '4':
        name3 = input('原名字:')
        phone3 = input('原电话:')
        name2 = input('名字:')
        age2 = input('岁数:')
        sex2 = input('性别:')
        education2 = input('学历:')
        phone2 = input('电话:')
        class_2 = input('班级:')
        introducer2 = input('介绍人:')
        address2 = input('地址:')
        ms.update_table(name1=name2,age1=age2,sex1=sex2,education1=education2,phone1=phone2,class_1=class_2,introducer1=introducer2,address1=address2,name=name3,phone=phone3)

    elif code == '5':
        phone = input('电话:')
        res = ms.select_table(phone)
        print(res)
    elif code == '6':
        res = ms.select_all()
        print(res)
    elif code == '7':
        res = ms.select_all1()
        print(res)
    else:
        cursor.close()
        self.conn.close()


# conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='xingpeixun',db='pythonclass')
# cursor = conn.cursor()
# cursor.execute('drop database student_system')
# cursor.execute('show databases')
# row = cursor.fetchall()
# print(row)
#
# cursor.close()
# conn.close()