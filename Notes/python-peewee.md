# delete
Deleting records
To delete a single model instance, you can use the Model.delete_instance() shortcut. delete_instance() will delete the given model instance and can optionally delete any dependent objects recursively (by specifying recursive=True).

>>> user = User.get(User.id == 1)
>>> user.delete_instance()  # Returns the number of rows deleted.
1

>>> User.get(User.id == 1)
UserDoesNotExist: instance matching query does not exist:
SQL: SELECT t1."id", t1."username" FROM "user" AS t1 WHERE t1."id" = ?
PARAMS: [1]
To delete an arbitrary set of rows, you can issue a DELETE query. The following will delete all Tweet objects that are over one year old:

>>> query = Tweet.delete().where(Tweet.creation_date < one_year_ago)
>>> query.execute()  # Returns the number of rows deleted.
7
For more information, see the documentation on:

Model.delete_instance()
Model.delete()
DeleteQuery

# attention
backref 调用后要用get来获取,,不不不,get只是获取一个,backref可以迭代?

## namedtuple



select
where
join

get



## select
```py
query = (Note
         .select(Note.content, Note.timestamp, Person.first, Person.last)
         .join(Person, on=(Note.person_id == Person.id))
         .where(Note.timestamp >= datetime.date(2018, 1, 1))
         .order_by(Note.timestamp)
         .namedtuples())

for row in query:
    print(row.timestamp, '-', row.content, '-', row.first, row.last)

tmpi = Item.select().where((Item.iid == iid) & (Item.title == title)).get()
```

> http://docs.peewee-orm.com/en/latest/peewee/query_operators.html

## 总结
类(继承 peewee.Model) 对应 一个表
变量(无需类对象) 对应列 类型由peewee.filed 控制
类的instance (用 create() 创建) 为 一行(一条记录)
自动有个 id 好像..
里面的Mate class 是自定义,数据库与表名的吧
Note.create_table() 初始化
Note.drop_table() 删除表

总的操作分两类
query 和 execution
要么直接执行,要么生成一个query来执行

query 有
Note.insert_many([{'colName':'value',...}])
Note.delete().where(Note.id>3)
Note.update(created=dateime.date(2018,10,27)).where(Note.id==1)

execution 有
select(),where(),get(),limit(),count(),sql(),offset()
 这些都有不同的职能,注意
 不要 Item.select(Item.due>today())
 要 Item.select(Item.due,Item.title).where(Item.due>today())
 跟sql语句差不多,毕竟是生成的

order_by(),Note.created.desc()
delete_by_id()

加入一列
bob = Note(name='Bob')
bob.save()
When you call save(), the number of rows modified is returned.

or 
bob = Note.create(name='Bob')
bob.name = "nothign"
bob.save()

## fn()
Peewee provides a magical helper fn(), which can be used to call any SQL function. In the above example, fn.COUNT(Pet.id).alias('pet_count') would be translated into COUNT(pet.id) AS pet_count.

fn.random?

## Working with existing databases
If you already have a database, you can autogenerate peewee models using pwiz, a model generator. For instance, if I have a postgresql database named charles_blog, I might run:

python -m pwiz -e postgresql charles_blog > blog_models.py

## Peewee mapping
A Model maps to the database table,
a Field to the table column,
and instance to the table row.

Peewee uses MySQLDatabase for MySQL,
PostgresqlDatabase for PostgreSQL,
and SqliteDatabase for SQLite.
In this tutorial, we work with SQLite database.

## Peewee field types
Field types in a Peewee model define the storage type of the model. They are translated to the corresponding database column types.
| Field  Type     | SQLite   | PostgreSQL | MySQL                     |
|-----------------|----------|------------|---------------------------|
| CharField       | varchar  | varchar    | varchar                   |
| TextField       | text     | text       | longtext                  |
| DateTimeField   | datetime | timestamp  | datetime                  |
| IntegerField    | integer  | integer    | integer                   |
| BooleanField    | smallint | boolean    | bool                      |
| FloatField      | real     | real       | real                      |
| DoubleField     | real     | double     | precision	double precision |
| BigIntegerField | integer  | bigint     | bigint                    |
| DecimalField    | decimal  | numeric    | numeric                   |
| PrimaryKeyField | integer  | serial     | integer                   |
| ForeignKeyField | integer  | integer    | integer                   |
| DateField       | date     | date       | date                      |
| TimeField       | time     | time       | time                      |
This table lists the Peewee field types and the corresponding SQLite, PostgreSQL and MySQL column types.

## Peewee model definition
```py
#!/usr/bin/env python3

import peewee
import datetime

db = peewee.SqliteDatabase('test.db')

class Note(peewee.Model):

    text = peewee.CharField()
    created = peewee.DateField(default=datetime.date.today)

    class Meta:

        database = db
        db_table = 'notes'


Note.create_table()

note1 = Note.create(text='Went to the cinema')
note1.save()

note2 = Note.create(text='Exercised in the morning',
        created=datetime.date(2018, 10, 20))
note2.save()

note3 = Note.create(text='Worked in the garden',
        created=datetime.date(2018, 10, 22))
note3.save()

note4 = Note.create(text='Listened to music')
note4.save()
```

We verify the data.

## Peewee drop table

The table is dropped with the `drop_table()` model method.
Note.drop_table()

## Peewee insert_many

The `insert_many()` method allows to do bulk creates.

```py
data = [
    { 'text': 'Tai chi in the morning', 'created': datetime.date(2018, 10, 20) },
    { 'text': 'Visited friend', 'created': datetime.date(2018, 10, 12) },
    { 'text': 'Went to cinema', 'created': datetime.date(2018, 10, 5) },
    { 'text': 'Listened to music', 'created': datetime.date(2018, 10, 28) },
    { 'text': 'Watched TV all day', 'created': datetime.date(2018, 10, 14) },
    { 'text': 'Worked in the garden', 'created': datetime.date(2018, 10, 22) },
    { 'text': 'Walked for a hour', 'created': datetime.date(2018, 10, 28) }
]


# We define the data in a list of dictionaries.
with db.atomic():

    query = Note.insert_many(data)
    query.execute()

```
We execute the bulk operation. The `atomic()` method puts the bulk operation in a transaction.

## Peewee select all instances

The `select()` method is used to retrieve instances of the defined models..


The example fetches and displayes all `Note` instances.

```
notes = Note.select()

```

The `select()` method creates a SELECT query. If no fields are explicitly provided, the query will by default select all the fields defined on the model.

## Peewee filter with where

The `where()` method can filter data based on a given condition.


The example retrieves all rows with Id greater than three.

```py
notes = Note.select().where(Note.id > 3)

```

The `where()` methods applies a filtering condition on the query.

## Peewee multiple where expressions

We can combine multiple where expressions.


```py
notes = Note.select().where((Note.id > 2) & (Note.id < 6))

```

We use two where expressions combined with the & operator.

## Peewee retrieve single instance

There are two ways to select a single instance; each of them uses a `get()` method.

The example shows how to retrieve a single instance in two ways.

```py
note1 = Note.select().where(Note.text == 'Went to cinema').get()

note2 = Note.get(Note.text == 'Listened to music')

```
We can use the chain of Note.select().where().get() methods.

There is also a `Note.get()` shortcut method, which does the same.



## Peewee selecting specific columns

Inside the `select()` method, we can specify the names of the columns to be included in the query.

columns.py

```py
notes = Note.select(Note.text, Note.created).limit(2)

output = [e for e in notes.tuples()]
print(output)

```

The example includes two columns: text and created. The Id is skipped. We limit the query to two instances.


## Peewee count instances

To calculate the number of model instances in the table, we can use the `count()` method.

```py
n2 = Note.select().where(Note.created >= datetime.date(2018, 10, 20)).count()
print(n2)

```

## Peewee show SQL statements

The generated SQL statements can be shown with the `sql()`method.

```py
note3 = Note.select().where(Note.id == 3)
print(note3.sql())

```

The example displays the SQL to which the ORM query is translated.

```
$ ./show_sql.py
('SELECT "t1"."id", "t1"."text", "t1"."created" FROM "notes" AS "t1"
    WHERE ("t1"."id" = ?)', [3])

```

This is the output.

## Peewee offset, limit

With the `offset` and `limit` attributes we can define the initial skip of instances and number of instances to be included in the `select()`.

```py
# offset???
notes = Note.select().offset(2).limit(3)

for note in notes:
    print(note.id, note.text, note.created)

```

The example returns three instances, starting from the second instance.

## Peewee ordering

The retrieved instances can be ordered with `order_by()`.

The code example orders the instances by the date of creation.

```py
notes = Note.select(Note.text, Note.created).order_by(Note.created)

# This line returns the note instances ordered by creation date in ascending order.

notes = Note.select(Note.text, Note.created).order_by(Note.created.desc())

# To retrieve the notes in ascending order, we append the `desc()`method on the field.

```
## Peewee delete instance

The `delete_by_id()` method deletes an instance identified by its Id. It returns the number of deleted instances.

```py
n2 = Note.delete_by_id(1)
print(n2)

```
The example deletes a `Note` instance with Id 1.

## Peewee delete multiple instances

To delete more instances, we call the `delete()` method. It returns the number of successfully deleted instances.

```
query = Note.delete().where(Note.id > 3)
n = query.execute()

print('{} instances deleted'.format(n))

```

In the example, we delete all instances with Id greater than three.

```
$ ./delete_instances.py
4 instances deleted

```

In our case, we have deleted four `Note` instances.

## Peewee update instance

The `update()` method updates an instance. It returns the number of successfully updated instances.

```py
query = Note.update(created=datetime.date(2018, 10, 27)).where(Note.id == 1)
n = query.execute()

print('# of rows updated: {}'.format(n))

```

The example modifies the creation date of the note with Id 1.

## Peewee one-to-many relationship

In the following example, we are going to map models to existing tables. Relationships between models are created with `ForeignKeyField`.

This SQL creates two table: `customers` and `reservations`. There is a one-to-many relationship between the two tables: one customer can have many reservations.

one2many.py

```py
#!/usr/bin/env python3

import peewee
import datetime

db = peewee.SqliteDatabase('test.db')

class Customer(peewee.Model):

    name = peewee.TextField()

    class Meta:

        database = db
        db_table = 'customers'

class Reservation(peewee.Model):

    customer = peewee.ForeignKeyField(Customer, backref='reservations')
    created = peewee.DateField(default=datetime.date.today)

    class Meta:

        database = db
        db_table = 'reservations'

customer = Customer.select().where(Customer.name == 'Paul Novak').get()

for reservation in customer.reservations:

    print(reservation.id)
    print(reservation.created)

```

In the example we define two models that map to the tables. Then we select a customer and show his reservations.

```
customer = peewee.ForeignKeyField(Customer, backref='reservations')
```

A relationship between `Customer` and `Reservation` models is created with `ForeignKeyField`. The `backref` attribute sets how we can refer to reservations from a customer.

```
for reservation in customer.reservations:
```

The customer instance has a property `reservations`, which contains the corresponding reservations.


# tmp
[(i.iid, i.title) for i in self.curList.todoitems]

> http://zetcode.com/python/peewee/
# ref
> http://docs.peewee-orm.com/en/latest/peewee/interactive.html
> https://geek-docs.com/python/python-tutorial/python-peewee.html#Peewee_where-2
> https://mozillazg.com/2015/03/peewee-quickstart-zh-cn.html#hidid5