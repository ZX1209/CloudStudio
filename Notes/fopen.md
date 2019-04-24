DESCRIPTION
       The  fopen()  function opens the file whose name is the string pointed to by path and asso‐
       ciates a stream with it.

       The argument mode points to a string beginning with one of the following sequences  (possi‐
       bly followed by additional characters, as described below):

       r      Open text file for reading.  The stream is positioned at the beginning of the file.

       r+     Open  for  reading  and  writing.   The stream is positioned at the beginning of the
              file.

       w      Truncate file to zero length or create text file for writing.  The stream  is  posi‐
              tioned at the beginning of the file.

       w+     Open  for  reading and writing.  The file is created if it does not exist, otherwise
              it is truncated.  The stream is positioned at the beginning of the file.

       a      Open for appending (writing at end of file).  The file is created  if  it  does  not
              exist.  The stream is positioned at the end of the file.

       a+     Open  for reading and appending (writing at end of file).  The file is created if it
              does not exist.  The initial file position for reading is at the  beginning  of  the
              file, but output is always appended to the end of the file.

#r
打开文件,进行读

#r+
打开文件,进行读写

#w
将存在的文件清空或创造新文件来写

#w+
打开文件进行读写,不存则创建,否则将清空来写

#a
打开文件来追加(文件指针在文件尾),如不存在则创建

#a+
打开文件来读写,如不存在则创建
初始文件指针在文件开头,但输出总加载文件末尾

