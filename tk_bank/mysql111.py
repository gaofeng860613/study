import pymysql
class Bank_peoples():


    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='xingpeixun',db='pythonclass')
        print(self.conn)


    def creattable1(self):
        cursor = self.conn.cursor()
        self.conn.begin()
        cursor.execute('drop table if exists Bank_people')
        cursor.execute('create table Bank_people (card_id int primary key auto_increment not null,password varchar(20),balan varchar(20) default 0,name varchar(10),id varchar(20),age varchar(4),sex varchar(2),phone varchar(12),address text)')
        self.conn.commit()
        row = cursor.fetchall()
        return row


    def creattable1_freeze(self):
        cursor = self.conn.cursor()
        self.conn.begin()
        cursor.execute('drop table if exists Bank_people_freeze')
        cursor.execute('create table Bank_people_freeze (card_id int primary key auto_increment not null,password varchar(20))')
        self.conn.commit()
        row = cursor.fetchall()
        return row


    def insert_table1(self,card_id1,password1,name1,id1,age1,sex1,phone1,address1):
            cursor = self.conn.cursor()
            self.conn.begin()
            a1='insert into Bank_people(card_id,password,name,id,age,sex,phone,address) values (%s,%s,%s,%s,%s,%s,%s,%s)'
            a2=(card_id1,password1,name1,id1,age1,sex1,phone1,address1)
            cursor.execute(a1,a2)
            self.conn.commit()
            row = cursor.fetchall()
            return row

    def insert_table1_freeze(self, card_id1, password1):
        cursor = self.conn.cursor()
        self.conn.begin()
        a1 = 'insert into Bank_people_freeze(card_id,password) values (%s,%s)'
        a2 = (card_id1, password1)
        cursor.execute(a1, a2)
        self.conn.commit()
        row = cursor.fetchall()
        return row


    def delete_table_freeze(self,card_id1,password1):
        cursor = self.conn.cursor()
        self.conn.begin()
        b1="delete from Bank_people_freeze where card_id=%s and password=%s"
        b2 = (card_id1,password1)
        cursor.execute(b1,b2)
        self.conn.commit()
        row = cursor.fetchall()
        return row


    def delete_table_clossing_account(self,card_id1,password1):
        cursor = self.conn.cursor()
        self.conn.begin()
        b1="delete from Bank_people where card_id=%s and password=%s"
        b2 = (card_id1,password1)
        cursor.execute(b1,b2)
        self.conn.commit()
        row = cursor.fetchall()
        return row


    def update_deposit(self,balan1,card_id1,password1):
        cursor = self.conn.cursor()
        self.conn.begin()
        c1 = 'update Bank_people set balan=%s where card_id = %s and password = %s;'
        c2 = (balan1,card_id1,password1)
        cursor.execute(c1,c2)
        self.conn.commit()
        row = cursor.fetchall()
        return row


    def update_withdrawal(self,balan1,card_id1,password1):
        cursor = self.conn.cursor()
        self.conn.begin()
        c1 = 'update Bank_people set balan=%s where card_id = %s and password = %s;'
        c2 = (balan1,card_id1,password1)
        cursor.execute(c1,c2)
        self.conn.commit()
        row = cursor.fetchall()
        return row


    def update_transfer(self,balan1,card_id1):
        cursor = self.conn.cursor()
        self.conn.begin()
        c1 = 'update Bank_people set balan=%s where card_id = %s;'
        c2 = (balan1,card_id1)
        cursor.execute(c1,c2)
        self.conn.commit()
        row = cursor.fetchall()
        return row


    def select_table(self,card_id1,password1):
        cursor = self.conn.cursor()
        self.conn.begin()
        d1 = 'select card_id, password from Bank_people where card_id=%s and password=%s'
        d2 = (card_id1, password1)
        cursor.execute(d1,d2)
        self.conn.commit()
        row = cursor.fetchall()
        return row


    def select_view_balan(self,card_id1,password1):
        cursor = self.conn.cursor()
        self.conn.begin()
        d1 = 'select balan from Bank_people where card_id=%s and password=%s'
        d2 = (card_id1,password1)
        cursor.execute(d1,d2)
        self.conn.commit()
        row = cursor.fetchall()
        return row


    def select_view_balan_single(self,card_id1):
        cursor = self.conn.cursor()
        self.conn.begin()
        d1 = 'select balan from Bank_people where card_id=%s'
        d2 = card_id1
        cursor.execute(d1,d2)
        self.conn.commit()
        row = cursor.fetchall()
        return row


    def select_table_freeze(self):
        cursor = self.conn.cursor()
        self.conn.begin()
        cursor.execute('select card_id from Bank_people_freeze')
        self.conn.commit()
        row = cursor.fetchall()
        return row


    def select_table_bank_people(self):
        cursor = self.conn.cursor()
        self.conn.begin()
        cursor.execute('select card_id from Bank_people')
        self.conn.commit()
        row = cursor.fetchall()
        return row

    def select_table_c_p(self):
        cursor = self.conn.cursor()
        self.conn.begin()
        cursor.execute('select card_id, password from Bank_people')
        self.conn.commit()
        row = cursor.fetchall()
        return row


    def select_all(self):
        cursor = self.conn.cursor()
        self.conn.begin()
        cursor.execute('select * from Bank_people')
        self.conn.commit()
        row = cursor.fetchall()
        return row
