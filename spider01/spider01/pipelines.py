# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

'''class Spider01Pipeline(object):
    def process_item(self, item, spider):
        print('---process_item---')
        print(item)
        return item
'''
import os
import sqlite3


class Spider01Pipeline(object):
    def __init__(self, sqlite_file, sqlite_table):
        self.sqlite_file = sqlite_file
        self.sqlite_table = sqlite_table

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            sqlite_file=crawler.settings.get('SQLITE_FILE'),  # 从 settings.py 提取
            sqlite_table=crawler.settings.get('SQLITE_TABLE', 'items')  # 从 settings.py 提取
        )

    def open_spider(self, spider):
        print('----open_spider')
        self.init(self.sqlite_table, self.sqlite_table)

    def close_spider(self, spider):
        conn = self.get_conn(DB_FILE_PATH)
        cu = self.get_cursor(conn)
        self.close_all(conn, cu)

    '''sql 语句不是很熟悉'''

    def process_item(self, item, spider):
        # insert into (author, carrer, chaildUrlTail, hitNum, url) values (?, ?, ?, ?, ?) key顺序a-z
        insert_sql1 = "insert into {0}({1}) values ({2})".format(self.sqlite_table,
                                                                ', '.join(item.fields.keys()),
                                                                ', '.join(['?'] * len(item.fields.keys())))
        insert_sql = "insert into mokoItem(url, author, hitNum, carrer, chaildUrlTail) values (?, ?, ?, ?, ?)"

        try:
            print('---process_item ---')
            print('sql is %s' % insert_sql)
            print('sql1 is %s' % insert_sql1)
            print(item)
            print(item.fields)
            item_data = item
            print(item_data)
            print('---process_item ---item.values()')
            print(item.values())
            print('---item.keys---')
            print(item.keys())
            print('---item.fields.items---')
            print(item.fields.items())
            print('---item.items---')
            print(item.items())
            print('---item.fields---')
            print(item.fields)
            print('---item.fields.values()---')
            print(item.fields.values())
        except Exception as e:
            print("!!!print error %s" % e)
        conn = self.get_conn(DB_FILE_PATH)
        cu = self.get_cursor(conn)
        # cu.execute(insert_sql, item.fields.values())
        cu.execute(insert_sql, (item['url'], item['author'], item['hitNum'], item['carrer'], item['chaildUrlTail']))
        conn.commit()

        return item

    def init(self, db_name, table_name):
        print('----init')
        '''初始化方法'''
        # 数据库文件绝句路径
        global DB_FILE_PATH
        DB_FILE_PATH = '/Users/bxh/Downloads/111/{0}.db'.format(db_name)
        # 数据库表名称
        global TABLE_NAME
        TABLE_NAME = table_name
        global SHOW_SQL
        SHOW_SQL = True
        # 如果存在数据库表，则删除表
        self.drop_table_test()
        # 创建数据库表student
        self.create_table_test()

    def drop_table(self, conn, table):
        '''如果表存在,则删除表，如果表中存在数据的时候，使用该
        方法的时候要慎用！'''
        sql = 'DROP TABLE IF EXISTS ' + table
        if table is not None and table != '':
            if SHOW_SQL:
                print('执行sql:[{}]'.format(sql))
            cu = self.get_cursor(conn)
            cu.execute(sql)
            conn.commit()
            print('删除数据库表[{}]成功!'.format(table))
            self.close_all(conn, cu)
        else:
            print('the [{}] is empty or equal None!'.format(sql))

    def drop_table_test(self):
        '''删除数据库表测试'''
        print('删除数据库表测试...')
        conn = self.get_conn(DB_FILE_PATH)
        self.drop_table(conn, TABLE_NAME)

    def create_table_test(self):
        '''创建数据库表测试'''
        print('创建数据库表测试...')
        create_table_sql = '''CREATE TABLE `mokoItem` (
                              `id` Integer,
                              `url` varchar(20) NOT NULL,
                              `author` varchar(4) DEFAULT NULL,
                              `hitNum` int(11) DEFAULT NULL,
                              `carrer` varchar(200) DEFAULT NULL,
                              `chaildUrlTail` varchar(200) DEFAULT NULL,
                               PRIMARY KEY (`id`)
                            )'''

        self.create_table(self.get_conn(DB_FILE_PATH), create_table_sql)

    def create_table(self, conn, sql):
        '''创建数据库表：student'''
        if sql is not None and sql != '':
            cu = self.get_cursor(conn)
            print('执行sql:[{}]'.format(sql))
            cu.execute(sql)
            conn.commit()
            print('创建数据库表[%s]成功!' % TABLE_NAME)
            self.close_all(conn, cu)
        else:
            print('the [{}] is empty or equal None!'.format(sql))

    def close_all(self, conn, cu):
        '''关闭数据库游标对象和数据库连接对象'''
        try:
            if cu is not None:
                cu.close()
        finally:
            if cu is not None:
                cu.close()

    '''该方法是获取数据库的游标对象，参数为数据库的连接对象
        如果数据库的连接对象不为None，则返回数据库连接对象所创
        建的游标对象；否则返回一个游标对象，该对象是内存中数据
        库连接对象所创建的游标对象'''

    def get_cursor(self, conn):
        if conn is not None:
            return conn.cursor()
        else:
            return self.get_conn('').cursor()

    '''获取到数据库的连接对象，参数为数据库文件的绝对路径
        如果传递的参数是存在，并且是文件，那么就返回硬盘上面改
        路径下的数据库文件的连接对象；否则，返回内存中的数据接
        连接对象'''

    def get_conn(self, path):
        conn = sqlite3.connect(path)
        if os.path.exists(path) and os.path.isfile(path):
            print('硬盘上面:[{}]'.format(path))
            return conn
        else:
            conn = None
            print('内存上面:[:memory:]')
            return sqlite3.connect(':memory:')
