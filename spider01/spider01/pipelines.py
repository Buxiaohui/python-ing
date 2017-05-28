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
import sys

sys.path.append('.')
from . import moko_sqlite


class Spider01Pipeline(object):
    def __init__(self, sqlite_file, sqlite_table):
        self.sqlite_file = sqlite_file
        self.sqlite_table = sqlite_table

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            sqlite_file=crawler.settings.get('SQLITE_FILE'),  # 从 settings.py 提取
            sqlite_table=crawler.settings.get('SQLITE_TABLE', 'mokoItem')  # 从 settings.py 提取
        )

    def open_spider(self, spider):
        print('----open_spider')

        self.init(self.sqlite_table, self.sqlite_table, 'mokoItemChild')

    def close_spider(self, spider):
        conn = moko_sqlite.get_conn(DB_FILE_PATH)
        cu = moko_sqlite.get_cursor(conn)
        moko_sqlite.close_all(conn, cu)

    '''sql 语句不是很熟悉'''

    def process_item(self, item, spider):
        # insert into (author, carrer, childUrlTail, hitNum, url) values (?, ?, ?, ?, ?)
        # key顺序a-z
        insert_sql1 = "insert into {0}({1}) values ({2})".format(self.sqlite_table,
                                                                 ', '.join(item.fields.keys()),
                                                                 ', '.join(['?'] * len(item.fields.keys())))
        insert_main_sql = "insert into mokoItem(childUrlCode ,url, author, hitNum, carrer, childUrlTail) values (?, ?, ?, ?, ?, ?)"
        insert_child_sql = "insert into mokoItemChild(childUrlCode , author,imgUrl) values (? ,? ,?)"

        try:
            print('sql is %s' % insert_main_sql)
            print('sql is %s' % insert_child_sql)
            print('---process_item ---')
            print(item)
            # print(item.fields)
            # item_data = item
            # print(item_data)
            # print('---process_item ---item.values()')
            # print(item.values())
            # print('---item.keys---')
            # print(item.keys())
            # print('---item.fields.items---')
            # print(item.fields.items())
            # print('---item.items---')
            # print(item.items())
            # print('---item.fields---')
            # print(item.fields)
            # print('---item.fields.values()---')
            # print(item.fields.values())
        except Exception as e:
            print("!!!print error %s" % str(e))
        conn = moko_sqlite.get_conn(DB_FILE_PATH)
        cu = moko_sqlite.get_cursor(conn)
        # cu.execute(insert_sql, item.fields.values())
        try:
            cu.execute(insert_main_sql, (
                item['childUrlCode'], item['url'], item['author'], item['hitNum'], item['carrer'],
                item['childUrlTail']))
            # 这种格式，批量插入
            # param = ((username1, salt1, pwd1), (username2, salt2, pwd2), (username3, salt3, pwd3))
            param = []
            for i in (item['imgs']):
                # 第一列childUrlCode，第二列author，第三列imgUrl
                # param.append([table.cell(i, 0).value, table.cell(i, 1).value, table.cell(i, 2).value])
                print("-----item['imgs'](i)----")
                print((i))
                param.append([item['childUrlCode'], item['author'], (i)])
                # cu.execute(insert_child_sql, (item['childUrlCode'], item['author'],"ahhahaha"))
                print("----------param--------")
                print(param)
            cu.executemany(insert_child_sql, param)
            conn.commit()
        except Exception as e:
            print("----------Exception--------")
            print(e)
        return item

    def init(self, db_name, table_name, table_name_child):
        print('----init')
        '''初始化方法'''
        # 数据库文件绝句路径
        global DB_FILE_PATH
        DB_FILE_PATH = '/Users/bxh/Downloads/111/{0}.db'.format(db_name)
        # 数据库表名称
        global TABLE_NAME
        global TABLE_NAME_CHILD
        TABLE_NAME = table_name
        TABLE_NAME_CHILD = table_name_child
        print('---table_name_child name is %s ' % table_name_child)
        global SHOW_SQL
        SHOW_SQL = True
        # 如果存在数据库表，则删除表
        self.drop_table_test()
        # 创建数据库表student
        self.create_table_test()

    def drop_table_test(self):
        '''删除数据库表测试'''
        print('删除数据库表测试...')
        conn = moko_sqlite.get_conn(DB_FILE_PATH)
        moko_sqlite.drop_table(conn, TABLE_NAME)
        moko_sqlite.drop_table(conn, TABLE_NAME_CHILD)

    def create_table_test(self):
        '''创建数据库表测试'''
        print('创建数据库表测试...')
        create_main_table_sql = '''CREATE TABLE `mokoItem` (
                              `id` Integer,
                              `childUrlCode` varchar(20) NOT NULL,
                              `url` varchar(20) NOT NULL,
                              `author` varchar(4) DEFAULT NULL,
                              `hitNum` int(11) DEFAULT NULL,
                              `carrer` varchar(200) DEFAULT NULL,
                              `childUrlTail` varchar(200) DEFAULT NULL,
                               PRIMARY KEY (`id`)
                            )'''
        create_child_table_sql = '''CREATE TABLE `mokoItemChild` (
                                      `id` Integer,
                                      `childUrlCode` varchar(20) NOT NULL,
                                      `author` varchar(4) DEFAULT NULL,
                                      `imgUrl` varchar(200) DEFAULT NULL,
                                       PRIMARY KEY (`id`)
                                    )'''
        moko_sqlite.create_table(moko_sqlite.get_conn(DB_FILE_PATH), create_main_table_sql)
        moko_sqlite.create_table(moko_sqlite.get_conn(DB_FILE_PATH), create_child_table_sql)
