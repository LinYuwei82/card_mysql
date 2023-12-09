import pymysql
from PyQt5.QtWidgets import QMessageBox

userName = ""
Ver = ' Ver 1.0.0'
copyrights = '深圳市安业物业管理有限公司'
record = ''


def open_db():
    db = pymysql.connect(
        host="localhost",  # localhost
        port=3306,
        user="root",
        password="ABcd654321",
        database="devicedb"
        # charset="utf-8",
        # autocommit=True
    )
    return db


def exec_remove_duplicate():
    db = open_db()
    cursor = db.cursor()
    try:
        sql1 = "DROP TEMPORARY TABLE IF EXISTS temp_table"
        sql2 = "CREATE TEMPORARY TABLE temp_table AS SELECT MIN(dev_id) AS dev_id, dev_name, location, " \
               "control_range, phone FROM tb_device GROUP BY dev_name, location, control_range, phone"
        sql3 = "DELETE FROM tb_device WHERE dev_id NOT IN (SELECT dev_id FROM temp_table)"
        cursor.execute(sql1)
        cursor.execute(sql2)
        cursor.execute(sql3)
        db.commit()
        return 1  # 执行成功
    except:
        db.rollback()  # 发生错误时回滚
        return 0
    finally:
        cursor.close()  # 关闭游标
        db.close()  # 关闭数据库连接


def exec_db(sql, values):
    db = open_db()
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


def query_count(sql, *keys):
    db = open_db()
    cursor = db.cursor()
    cursor.execute(sql, keys)
    result = cursor.fetchone()[0]
    cursor.close()
    db.close()
    return result


def exec_del(sql, *values):
    db = open_db()
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


def query_desc(sql, *keys):
    db = open_db()
    cursor = db.cursor()
    cursor.execute(sql, keys)
    result1 = cursor.fetchall()
    result2 = cursor.description
    cursor.close()
    db.close()
    return result1, result2


# 带参数的精确查询
def query_db(sql, *keys):
    db = open_db()
    cursor = db.cursor()
    cursor.execute(sql, keys)
    result = cursor.fetchall()
    cursor.close()
    db.close()
    return result


# 不带参数的模糊查询
def query_db2(sql):
    db = open_db()
    cursor = db.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    db.close()
    return result


def exit_info():
    select = QMessageBox.information(None, '退出系统', '确定退出系统？', QMessageBox.Yes | QMessageBox.No)
    return select


def delete_info():
    select = QMessageBox.warning(None, '删除数据', '确定删除除？', QMessageBox.Yes | QMessageBox.No)
    return select


def delete_all_info():
    select = QMessageBox.warning(None, '清空所有数据', '确定清空所有数据？', QMessageBox.Yes | QMessageBox.No)
    return select


def remove_duplicate_info():
    select = QMessageBox.information(None, '合并重复数据', '确定合并重复数据？', QMessageBox.Yes | QMessageBox.No)
    return select
