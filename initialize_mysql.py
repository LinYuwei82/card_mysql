import pymysql


# import os
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def create_db(database):
    db = pymysql.connect(
        host="localhost",  # localhost
        port=3306,
        user="root",
        password="ABcd654321"
    )
    cursor = db.cursor()
    cursor.execute(f"create database if not exists {database}")
    cursor.close()
    db.close()
    return database


def open_db(database):
    db = pymysql.connect(
        host="localhost",  # localhost
        port=3306,
        user="root",
        password="ABcd654321",
        database=database
    )
    return db


def exec_db(database, sql, *values):
    db = open_db(database)
    cursor = db.cursor()
    try:
        cursor.execute(sql, values)  # 执行增删改的SQL语句
        db.commit()
        return 1  # 执行成功
    except:
        db.rollback()  # 发生错误时回滚
        return 0
    finally:
        cursor.close()  # 关闭游标
        db.close()  # 关闭数据库连接


db1 = create_db("devicedb")
open_db(db1)
sql1 = "create table if not exists tb_device (dev_id int primary key auto_increment, dev_name varchar(20), " \
       "location varchar(20), control_range varchar(20), phone varchar(20))"
sql2 = "create table if not exists tb_user (userName varchar(20) primary key , userPwd varchar(20))"
exec_db(db1, sql1)
exec_db(db1, sql2)
