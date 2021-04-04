
语法:tar [主选项+辅选项] 文件或目录

主选项
1、c 创建新的档案文件。如果用户想备份一个目录或是一些文件，就要选择这个选项。相当于打包
2、x 从档案文件中释放文件。相当于拆包。
3、t 列出档案文件的内容，查看已经备份了哪些文件

辅选项
1、-z ：是否同时具有 gzip 的属性？亦即是否需要用 gzip 压缩或解压？ 一般格式为xx.tar.gz或xx. tgz
2、-j ：是否同时具有 bzip2 的属性？亦即是否需要用 bzip2 压缩或解压？一般格式为xx.tar.bz2 
3、-v ：压缩的过程中显示文件！这个常用
4、-f ：使用档名，请留意，在 f 之后要立即接档名喔！不要再加其他参数！
5、-p ：使用原文件的原来属性（属性不会依据使用者而变）
6、--exclude FILE：在压缩的过程中，不要将 FILE 打包！

# 加密 解密
没有内置的加密解密.
可以与 openssl 或?

# 源路径问题
zip 与 tar 最好在 同级目录下运行,否则会有冗余路径在压缩文件上.
也不要用../之类的父目录语法.


# tar.gz unpackage
tar -zxvf xxxx.tar.gz

# To extract an uncompressed archive:
tar -xvf /path/to/foo.tar

# To create an uncompressed archive:
tar -cvf /path/to/foo.tar /path/to/foo/

# To extract a .gz archive:
tar -xzvf /path/to/foo.tgz

# To create a .gz archive:
tar -czvf /path/to/foo.tgz /path/to/foo/

# To list the content of an .gz archive:
tar -ztvf /path/to/foo.tgz

# To extract a .bz2 archive:
tar -xjvf /path/to/foo.tgz

# To create a .bz2 archive:
tar -cjvf /path/to/foo.tgz /path/to/foo/

# To extract a .tar in specified Directory:
tar -xvf /path/to/foo.tar -C /path/to/destination/

# To list the content of an .bz2 archive:
tar -jtvf /path/to/foo.tgz

# To create a .gz archive and exclude all jpg,gif,... from the tgz
tar czvf /path/to/foo.tgz --exclude=\*.{jpg,gif,png,wmv,flv,tar.gz,zip} /path/to/foo/

# To use parallel (multi-threaded) implementation of compression algorithms:
tar -z ... -> tar -Ipigz ...
tar -j ... -> tar -Ipbzip2 ...
tar -J ... -> tar -Ipixz ...
