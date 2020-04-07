# Subclass relationships:
timedelta
tzinfo
    timezone
time
date
    datetime


import datetime
import pytz    # for time zone

datetime.datetime.now(tz=pytz.timezone('UTC'))



datetime.datetime.date(year,month,day)

datetime.datetime.time(hour,minute,second,microseconds)

dateime.datetime.datetime(....)

# 获取现在的日期时间
datetime.now().isoformat()


## 时间间隔 类型

datetime.timedelta(days=7)



## time to string

datetime.datetime.strftime()



## string to datetime

datetime.datetime.strptime()



## reference



| Directive | Meaning                                                      | Example                                                      | Notes    |
| --------- | ------------------------------------------------------------ | ------------------------------------------------------------ | -------- |
| `%a`      | Weekday as locale’s abbreviated name.                        | Sun, Mon, …, Sat (en_US);So, Mo, …, Sa (de_DE)               | (1)      |
| `%A`      | Weekday as locale’s full name.                               | Sunday, Monday, …, Saturday (en_US);Sonntag, Montag, …, Samstag (de_DE) | (1)      |
| `%w`      | Weekday as a decimal number, where 0 is Sunday and 6 is Saturday. | 0, 1, …, 6                                                   |          |
| `%d`      | Day of the month as a zero-padded decimal number.            | 01, 02, …, 31                                                |          |
| `%b`      | Month as locale’s abbreviated name.                          | Jan, Feb, …, Dec (en_US);Jan, Feb, …, Dez (de_DE)            | (1)      |
| `%B`      | Month as locale’s full name.                                 | January, February, …, December (en_US);Januar, Februar, …, Dezember (de_DE) | (1)      |
| `%m`      | Month as a zero-padded decimal number.                       | 01, 02, …, 12                                                |          |
| `%y`      | Year without century as a zero-padded decimal number.        | 00, 01, …, 99                                                |          |
| `%Y`      | Year with century as a decimal number.                       | 0001, 0002, …, 2013, 2014, …, 9998, 9999                     | (2)      |
| `%H`      | Hour (24-hour clock) as a zero-padded decimal number.        | 00, 01, …, 23                                                |          |
| `%I`      | Hour (12-hour clock) as a zero-padded decimal number.        | 01, 02, …, 12                                                |          |
| `%p`      | Locale’s equivalent of either AM or PM.                      | AM, PM (en_US);am, pm (de_DE)                                | (1), (3) |
| `%M`      | Minute as a zero-padded decimal number.                      | 00, 01, …, 59                                                |          |
| `%S`      | Second as a zero-padded decimal number.                      | 00, 01, …, 59                                                | (4)      |
| `%f`      | Microsecond as a decimal number, zero-padded on the left.    | 000000, 000001, …, 999999                                    | (5)      |
| `%z`      | UTC offset in the form ±HHMM[SS] (empty string if the object is naive). | (empty), +0000, -0400, +1030                                 | (6)      |
| `%Z`      | Time zone name (empty string if the object is naive).        | (empty), UTC, EST, CST                                       |          |
| `%j`      | Day of the year as a zero-padded decimal number.             | 001, 002, …, 366                                             |          |
| `%U`      | Week number of the year (Sunday as the first day of the week) as a zero padded decimal number. All days in a new year preceding the first Sunday are considered to be in week 0. | 00, 01, …, 53                                                | (7)      |
| `%W`      | Week number of the year (Monday as the first day of the week) as a decimal number. All days in a new year preceding the first Monday are considered to be in week 0. | 00, 01, …, 53                                                | (7)      |
| `%c`      | Locale’s appropriate date and time representation.           | Tue Aug 16 21:30:00 1988 (en_US);Di 16 Aug 21:30:00 1988 (de_DE) | (1)      |
| `%x`      | Locale’s appropriate date representation.                    | 08/16/88 (None);08/16/1988 (en_US);16.08.1988 (de_DE)        | (1)      |
| `%X`      | Locale’s appropriate time representation.                    | 21:30:00 (en_US);21:30:00 (de_DE)                            | (1)      |
| `%%`      | A literal `'%'` character.                                   | %                                                            |          |



Several additional directives not required by the C89 standard are included for convenience. These parameters all correspond to ISO 8601 date values. These may not be available on all platforms when used with the `strftime()` method. The ISO 8601 year and ISO 8601 week directives are not interchangeable with the year and week number directives above. Calling `strptime()` with incomplete or ambiguous ISO 8601 directives will raise a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError).

| Directive | Meaning                                                      | Example                                  | Notes |
| --------- | ------------------------------------------------------------ | ---------------------------------------- | ----- |
| `%G`      | ISO 8601 year with century representing the year that contains the greater part of the ISO week (`%V`). | 0001, 0002, …, 2013, 2014, …, 9998, 9999 | (8)   |
| `%u`      | ISO 8601 weekday as a decimal number where 1 is Monday.      | 1, 2, …, 7                               |       |
| `%V`      | ISO 8601 week as a decimal number with Monday as the first day of the week. Week 01 is the week containing Jan 4. | 01, 02, …, 53                            | (8)   |
