# 判断表是否存在
SELECT count(*) FROM sqlite_master WHERE type='table' AND name='要查询的表名';

# 获取随机项
> http://www.bernzilla.com/2008/05/13/selecting-a-random-row-from-an-sqlite-table/
> http://docs.peewee-orm.com/en/latest/peewee/querying.html?highlight=fn.random#getting-random-records
When I originally presented my version of selecting a random row from a MySQL table, a commenter named Elvard set me straight:

SELECT * FROM table ORDER BY RAND () LIMIT 1;

Tonight, out of pure curiosity, I learned that selecting a random row from an SQLite table isn't much different:

SELECT * FROM table ORDER BY RANDOM() LIMIT 1;

The only key difference being that MySQL supports the RAND() function, whereas SQLite's is called RANDOM().

# 获取自动id
print conn.insert_id()

# 创建表
CREATE TABLE database_name.table_name(
   column1 datatype  PRIMARY KEY(one or more columns),
   column2 datatype,
   column3 datatype,
   .....
   columnN datatype,
);

# 自增主键
ID INTEGER PRIMARY KEY NOT NULL

## 自增插入
insert into QUOTES(QUOTE) values(?)


# 插入
INSERT INTO TABLE_NAME [(column1, column2, column3,...columnN)]
VALUES (value1, value2, value3,...valueN);

# 修改
update todos set state='done' where titie='this is a test'

# 删除
delete from table where ...

# 选择
select * from todos where ...

# 不重复选择
select distinct.. from .. ...

# 查看表列信息
# 比如 表 douban_move
PRAGMA table_info(douban_move)

# 排序语法
SELECT column-list
FROM table_name
[WHERE condition]
[ORDER BY column1, column2, .. columnN] [ASC | DESC];
## ASC 升序 从小到大
## DESC 降序 从大到小


# 外键 not tested
create table test(
    id intergate primer key not null,
    fkey int,
    foreign key(fkey) reference table(col),
);

# like 字符串匹配
% 任意个字符
_ 一个字符

escape '\'