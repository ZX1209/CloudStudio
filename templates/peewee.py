#!/usr/bin/env python3

import peewee
import datetime

db = peewee.SqliteDatabase("todo.db")


class TodoGroup(peewee.Model):
    group_name = peewee.CharField()
    ctime = peewee.DateField(default=datetime.date.today)

    class Meta:
        database = db
        db_table = "groups"  # file name to path,no repeat


class Detail(peewee.Model):
    detail = peewee.TextField()
    ctime = peewee.DateField(default=datetime.date.today)

    class Meta:
        database = db
        db_table = "details"  # file name to path,no repeat


class TodoItem(peewee.Model):
    f_group = peewee.ForeignKeyField(TodoGroup, backref="todos", default=None, null=True)
    f_detail = peewee.ForeignKeyField(Detail, backref="title", default=None, null=True)

    title = peewee.CharField()
    ctime = peewee.DateField(default=datetime.date.today)

    class Meta:
        database = db
        db_table = "items"  # file name to path,no repeat


def init_db():
    pass


def create_example():
    tmp_item = TodoItem(title="test1")
    tmp_item.save()

    tmp_detail = Detail(detail="some detail here")
    tmp_detail.save()

    tmp_item2 = TodoItem(title="test2 with detail", f_detail=tmp_detail.get_id())
    tmp_item2.save()

    tmp_group = TodoGroup(group_name="tmp group")
    tmp_group.save()

    tmp_item3 = TodoItem(title="test3 with detail", f_group=tmp_group.get_id())
    tmp_item3.save()

    # no continus create
    # 不能连续创建,,会有 write lock


def read_example():
    tmp_read_item = TodoItem.select().where(TodoItem.title == "test1").get()

    tmp_read_item2 = TodoItem.select().where(TodoItem.title == "test2 with detail").get()
    tmp_detail = tmp_read_item2.f_detail.get()
    tmp_detail.title.get()

    for todo in tmp_detail.title:
        print(todo.title)
    # can iter title

    # get all
    all_items = TodoItem.select()
    list(all_items)

    # like search
    all_items = TodoItem.select().where(TodoItem & "*test*")
    list(all_items)


def update_example():
    tmp_detail = Detail.select().where(Detail.detail == "some detail here").get()
    query = TodoItem.update(f_detail=tmp_detail).where(TodoItem.title == "test1")
    n = query.execute()

    # or
    tmp_item = TodoItem.select().where(TodoItem.title == "test1")
    tmp_item.f_detail = tmp_detail
    tmp_item.save()


def delete_example():
    tmp_item3 = TodoItem(title="delete test")
    tmp_item3.save()

    # tmp_item3.delete_instance()
    # tmp_item3.delete_by_id()

    # or,delete many
    query = TodoItem.delete().where(TodoItem.id > 3)
    n = query.execute()


# def exists_example():
#     Name.select().where(Name.name == '减肥十件事1').exists()
#     or count()

if __name__ == "__main__":
    TodoGroup.drop_table()
    TodoGroup.create_table()

    Detail.drop_table()
    Detail.create_table()

    TodoItem.drop_table()
    TodoItem.create_table()
