这些是Android Studio 1.0.2的默认位置，可以通过编辑 ..../android-studio/bin/idea.properties 来更改它们。

删除android-studio文件夹;
删除sdk文件夹（如果它不在android-studio目录中;
）
删除 ~/.AndroidStudio ，其中包含 config 和 system ;
删除 ~/.android ;
如果使用配置 - ＆gt;创建桌面条目创建了快捷方式，则删除 ~/.local/share/applications/jetbrains-android-studio.desktop 。
注意：添加到上面的第5步 - 有时图标启动器可以位于以下位置之一：

/usr/share/applications
/usr/local/share/applications
如果您的启动器文件位于前两个目录中的任何一个，则需要root权限才能将其删除。

的PPA 结果 从Linux发行版中完全删除Android Studio的更深层次步骤还包括删除与Android Studio相关的PPA。

在Ubuntu 16.04中，

转到软件和更新＆gt;其他软件
向下滚动列表，然后选择查找与Android-studio
相关的列表
点击删除并验证
这有助于停止更新和非常烦人的错误消息：
The package has not been installed. I can't find the archive for it.