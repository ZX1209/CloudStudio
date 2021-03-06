> http://zetcode.com/python/peewee/

## order_by
Person.select().order_by(Person.birthday.desc())


## join_from & BaseQuery.dicts 
```py

list(
    Name.select(Name, FilePath, CoverPath)
    .join_from(Name, FilePath)
    .join_from(Name, CoverPath)
    .where((Name.id >= start) & (Name.id <= end))
    .dicts()
)
```
## many to many field 
```py
class Student(BaseModel):
    name = CharField()

class Course(BaseModel):
    name = CharField()
    students = ManyToManyField(Student, backref='courses')

StudentCourse = Course.students.get_through_model() # star 

db.create_tables([
    Student,
    Course,
    StudentCourse])

# Get all classes that "huey" is enrolled in:
huey = Student.get(Student.name == 'Huey')
for course in huey.courses.order_by(Course.name):
    print(course.name)

# Get all students in "English 101":
engl_101 = Course.get(Course.name == 'English 101')
for student in engl_101.students:
    print(student.name)

# When adding objects to a many-to-many relationship, we can pass
# in either a single model instance, a list of models, or even a
# query of models:
huey.courses.add(Course.select().where(Course.name.contains('English')))

engl_101.students.add(Student.get(Student.name == 'Mickey'))
engl_101.students.add([
    Student.get(Student.name == 'Charlie'),
    Student.get(Student.name == 'Zaizee')])

# The same rules apply for removing items from a many-to-many:
huey.courses.remove(Course.select().where(Course.name.startswith('CS')))

engl_101.students.remove(huey)

# Calling .clear() will remove all associated objects:
cs_150.students.clear()
```



## foreign assign
When a model has a foreign key, you can directly assign a model instance to the foreign key field when creating a new record.

>>> tweet = Tweet.create(user=huey, message='Hello!')
You can also use the value of the related object’s primary key:

>>> tweet = Tweet.create(user=2, message='Hello again!')


Query operators
The following types of comparisons are supported by peewee:

## Comparison	Meaning
==	x equals y
<	x is less than y
<=	x is less than or equal to y
>	x is greater than y
>=	x is greater than or equal to y
!=	x is not equal to y
<<	x IN y, where y is a list or query
>>	x IS y, where y is None/NULL
%	x LIKE y where y may contain wildcards(title % '*'+k+'*')
**	x ILIKE y where y may contain wildcards
^	x XOR y
~	Unary negation (e.g., NOT x)


# Peewee mapping
A Model maps to the database table,
a Field to the table column,
and instance to the table row.

Peewee uses MySQLDatabase for MySQL,
PostgresqlDatabase for PostgreSQL,
and SqliteDatabase for SQLite.
In this tutorial, we work with SQLite database.

# Peewee field types
Field types in a Peewee model define the storage type of the model. They are translated to the corresponding database column types.
| Field  Type     | SQLite   | PostgreSQL | MySQL                      |
| --------------- | -------- | ---------- | -------------------------- |
| CharField       | varchar  | varchar    | varchar                    |
| TextField       | text     | text       | longtext                   |
| DateTimeField   | datetime | timestamp  | datetime                   |
| IntegerField    | integer  | integer    | integer                    |
| BooleanField    | smallint | boolean    | bool                       |
| FloatField      | real     | real       | real                       |
| DoubleField     | real     | double     | precision	double precision |
| BigIntegerField | integer  | bigint     | bigint                     |
| DecimalField    | decimal  | numeric    | numeric                    |
| PrimaryKeyField | integer  | serial     | integer                    |
| ForeignKeyField | integer  | integer    | integer                    |
| DateField       | date     | date       | date                       |
| TimeField       | time     | time       | time                       |
This table lists the Peewee field types and the corresponding SQLite, PostgreSQL and MySQL column types.

## Peewee model definition

In the first example, we create a simple database table.

model_definition.py

```
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

The example creates a `notes` database table in SQLite.

```
db = peewee.SqliteDatabase('test.db')
```

We initiate a `test.db` SQLite database. This creates a `test.db` file on the filesystem.

```
class Note(peewee.Model):
...
```

We define a database model called `Note`. Peewee models inherit from `peewee.Model`.

```
text = peewee.CharField()
created = peewee.DateField(default=datetime.date.today)
```

We specify the model fields. We have a `CharField` and a `DateField`. `CharField` is a field class for storing strings. `DateField` is a field class for storing dates. It takes a default value if not specified.

```
class Meta:
    database = db
    db_table = 'notes'
```

In the `Meta` class, we define the reference to the database and the database table name.

```
Note.create_table()
```

The table is created from a model with `create_table()`.

```
note1 = Note.create(text='Went to the cinema')
note1.save()
```

We create and save a new instance.

```
sqlite> select * from notes;
1|Went to the cinema|2018-11-01
2|Exercised in the morning|2018-10-20
3|Worked in the garden|2018-10-22
4|Listened to music|2018-11-01
```

We verify the data.

## Peewee drop table

The table is dropped with the `drop_table()` model method.

drop_table.py

```
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


Note.drop_table()

```

The example drops the `notes` table.

## Peewee insert_many

The `insert_many()` method allows to do bulk creates.

insert_many.py

```
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

data = [
    { 'text': 'Tai chi in the morning', 'created': datetime.date(2018, 10, 20) },
    { 'text': 'Visited friend', 'created': datetime.date(2018, 10, 12) },
    { 'text': 'Went to cinema', 'created': datetime.date(2018, 10, 5) },
    { 'text': 'Listened to music', 'created': datetime.date(2018, 10, 28) },
    { 'text': 'Watched TV all day', 'created': datetime.date(2018, 10, 14) },
    { 'text': 'Worked in the garden', 'created': datetime.date(2018, 10, 22) },
    { 'text': 'Walked for a hour', 'created': datetime.date(2018, 10, 28) }
]

with db.atomic():

    query = Note.insert_many(data)
    query.execute()

```

The code example recreates the `notes` table in one bulk create operation.

```
data = [
    { 'text': 'Tai chi in the morning', 'created': datetime.date(2018, 10, 20) },
    { 'text': 'Visited friend', 'created': datetime.date(2018, 10, 12) },
    { 'text': 'Went to cinema', 'created': datetime.date(2018, 10, 5) },
    { 'text': 'Listened to music', 'created': datetime.date(2018, 10, 28) },
    { 'text': 'Watched TV all day', 'created': datetime.date(2018, 10, 14) },
    { 'text': 'Worked in the garden', 'created': datetime.date(2018, 10, 22) },
    { 'text': 'Walked for a hour', 'created': datetime.date(2018, 10, 28) }
]

```

We define the data in a list of dictionaries.

```
with db.atomic():

    query = Note.insert_many(data)
    query.execute()

```

We execute the bulk operation. The `atomic()` method puts the bulk operation in a transaction.

## Peewee select all instances

The `select()` method is used to retrieve instances of the defined models..

fetch_all.py

```
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


notes = Note.select()

for note in notes:
    print('{} on {}'.format(note.text, note.created))

```

The example fetches and displayes all `Note` instances.

```
notes = Note.select()

```

The `select()` method creates a SELECT query. If no fields are explicitly provided, the query will by default select all the fields defined on the model.

```
$ ./fetch_all.py
Tai chi in the morning on 2018-10-20
Visited friend on 2018-10-12
Went to cinema on 2018-10-05
Listened to music on 2018-10-28
Watched TV all day on 2018-10-14
Worked in the garden on 2018-10-22
Walked for a hour on 2018-10-28

```

This is the output.

## Peewee filter with where

The `where()` method can filter data based on a given condition.

where_clause.py

```
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

notes = Note.select().where(Note.id > 3)

for note in notes:
    print('{} {} on {}'.format(note.id, note.text, note.created))

```

The example retrieves all rows with Id greater than three.

```
notes = Note.select().where(Note.id > 3)

```

The `where()` methods applies a filtering condition on the query.

```
$ ./where_clause.py
4 Listened to music on 2018-10-28
5 Watched TV all day on 2018-10-14
6 Worked in the garden on 2018-10-22
7 Walked for a hour on 2018-10-28

```

This is the output.

## Peewee multiple where expressions

We can combine multiple where expressions.

multiple_where_expr.py

```
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

notes = Note.select().where((Note.id > 2) & (Note.id < 6))

for note in notes:
    print('{} {} on {}'.format(note.id, note.text, note.created))

```

The example retrieves all rows whose id is greater than two and lower than six.

```
notes = Note.select().where((Note.id > 2) & (Note.id < 6))

```

We use two where expressions combined with the & operator.

```
$ ./multiple_where_expr.py
3 Went to cinema on 2018-10-05
4 Listened to music on 2018-10-28
5 Watched TV all day on 2018-10-14

```

This is the output.

## Peewee retrieve single instance

There are two ways to select a single instance; each of them uses a `get()` method.

single_instance.py

```
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


note1 = Note.select().where(Note.text == 'Went to cinema').get()

print(note1.id)
print(note1.text)
print(note1.created)

note2 = Note.get(Note.text == 'Listened to music')

print(note2.id)
print(note2.text)
print(note2.created)

```

The example shows how to retrieve a single instance in two ways.

```
note1 = Note.select().where(Note.text == 'Went to cinema').get()

```

We can use the chain of `Note.select().where().get()`methods.

```
note2 = Note.get(Note.text == 'Listened to music')

```

There is also a `Note.get()` shortcut method, which does the same.

```
$ ./single_instance.py
3
Went to cinema
2018-10-05
4
Listened to music
2018-10-28

```

This is the output.

## Peewee selecting specific columns

Inside the `select()` method, we can specify the names of the columns to be included in the query.

columns.py

```
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


notes = Note.select(Note.text, Note.created).limit(2)

output = [e for e in notes.tuples()]
print(output)

```

The example includes two columns: text and created. The Id is skipped. We limit the query to two instances.

```
$ ./columns.py
[('Tai chi in the morning', datetime.date(2018, 10, 20)),
    ('Visited friend', datetime.date(2018, 10, 12))]

```

This is the output.

## Peewee count instances

To calculate the number of model instances in the table, we can use the `count()` method.

count_instances.py

```
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

n = Note.select().count()
print(n)

n2 = Note.select().where(Note.created >= datetime.date(2018, 10, 20)).count()
print(n2)

```

The example counts the number of all instances and the number of instances where the date is equal or later than 2018/10/20.

```
$ ./count_instances.py
7
4

```

This is the output.

## Peewee show SQL statements

The generated SQL statements can be shown with the `sql()`method.

show_sql.py

```
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

offset_limit.py

```
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

notes = Note.select().offset(2).limit(3)

for note in notes:
    print(note.id, note.text, note.created)

```

The example returns three instances, starting from the second instance.

```
$ ./offset_limit.py
3 Went to cinema 2018-10-05
4 Listened to music 2018-10-28
5 Watched TV all day 2018-10-14

```

This is the output.

## Peewee ordering

The retrieved instances can be ordered with `order_by()`.

order_by.py

```
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


print('Ascending order')
print('*****************************')

notes = Note.select(Note.text, Note.created).order_by(Note.created)

for note in notes:
    print(note.text, note.created)

print()
print('Descending order')
print('*****************************')

notes = Note.select(Note.text, Note.created).order_by(Note.created.desc())

for note in notes:
    print(note.text, note.created)

```

The code example orders the instances by the date of creation.

```
notes = Note.select(Note.text, Note.created).order_by(Note.created)

```

This line returns the note instances ordered by creation date in ascending order.

```
notes = Note.select(Note.text, Note.created).order_by(Note.created.desc())

```

To retrieve the notes in ascending order, we append the `desc()`method on the field.

```
Ascending order
*****************************
Went to cinema 2018-10-05
Visited friend 2018-10-12
Watched TV all day 2018-10-14
Tai chi in the morning 2018-10-20
Worked in the garden 2018-10-22
Listened to music 2018-10-28
Walked for a hour 2018-10-28

Descending order
*****************************
Listened to music 2018-10-28
Walked for a hour 2018-10-28
Worked in the garden 2018-10-22
Tai chi in the morning 2018-10-20
Watched TV all day 2018-10-14
Visited friend 2018-10-12
Went to cinema 2018-10-05

```

This is the ordered list of note instances.

## Peewee delete instance

The `delete_by_id()` method deletes an instance identified by its Id. It returns the number of deleted instances.

delete_by_id.py

```
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

n2 = Note.delete_by_id(1)
print(n2)

```

The example deletes a `Note` instance with Id 1.

## Peewee delete multiple instances

To delete more instances, we call the `delete()` method. It returns the number of successfully deleted instances.

delete_instances.py

```
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

update_instance.py

```
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

query = Note.update(created=datetime.date(2018, 10, 27)).where(Note.id == 1)
n = query.execute()

print('# of rows updated: {}'.format(n))

```

The example modifies the creation date of the note with Id 1.

## Peewee one-to-many relationship

In the following example, we are going to map models to existing tables. Relationships between models are created with `ForeignKeyField`.

customers_reservations.sql

```
BEGIN TRANSACTION;
DROP TABLE IF EXISTS reservations;
DROP TABLE IF EXISTS customers;

CREATE TABLE IF NOT EXISTS customers(id INTEGER PRIMARY KEY, name TEXT);
INSERT INTO customers(Name) VALUES('Paul Novak');
INSERT INTO customers(Name) VALUES('Terry Neils');
INSERT INTO customers(Name) VALUES('Jack Fonda');
INSERT INTO customers(Name) VALUES('Tom Willis');

CREATE TABLE IF NOT EXISTS reservations(id INTEGER PRIMARY KEY, 
    customer_id INTEGER, created DATE, 
    FOREIGN KEY(customer_id) REFERENCES customers(id));
INSERT INTO reservations(customer_id, created) VALUES(1, '2018-22-11');
INSERT INTO reservations(customer_id, created) VALUES(2, '2018-28-11');
INSERT INTO reservations(customer_id, created) VALUES(2, '2018-29-11');
INSERT INTO reservations(customer_id, created) VALUES(1, '2018-29-11');
INSERT INTO reservations(customer_id, created) VALUES(3, '2018-02-12');
COMMIT;

```

This SQL creates two table: `customers` and `reservations`. There is a one-to-many relationship between the two tables: one customer can have many reservations.

```
sqlite> .read customers_reservations.sql 

```

We read the SQL file into the database.

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

```
$ ./one2many.py
1
2018-22-11
4
2018-29-11
```

This is the output.