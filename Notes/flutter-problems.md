27 SEP 2019 • 1 MIN READ
修改项目下 build.gradle 和 flutter 安装目录flutter/packages/flutter_tools/gradle/flutter.gradle 两个文件中 buildscript 和allprojects 中的

google()
jcenter()
改为

maven { url 'https://maven.aliyun.com/repository/google' }
maven { url 'https://maven.aliyun.com/repository/jcenter' }
maven { url 'http://maven.aliyun.com/nexus/content/groups/public' }