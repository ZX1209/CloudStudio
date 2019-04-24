# head metadata

# frameset 
`col="25.*"`

# 单选 多选 下拉框 
# name 算是,索引字段..
```html
<form action="target.file" method="post" onsubmit="return checkForm(this);">
    
    <!-- 单选 -->
    <input type="radio" name="sex"value="male"> something behand..seems no limit
    <input type="radio" name="sex" value="female"> something behand..seems no limit

    <!-- 下拉框 -->
    <select name="carer">
        <option value="学生">学生</option>
        <option value="教师">教师</option>
        <option value="other">other</option>
    </select>

    <!-- 多选 -->
    <input type="checkbox" name="hobies" value="电脑网站">电脑网站 &nbsp
    <input type="checkbox" name="hobies" value="影音娱乐">影音娱乐 &nbsp
    <input type="checkbox" name="hobies" value="棋牌娱乐">棋牌娱乐 &nbsp
    <input type="checkbox" name="hobies" value="读书读报">读书读报 &nbsp
    <input type="checkbox" name="hobies" value="美酒佳肴">美酒佳肴 &nbsp
    <input type="checkbox" name="hobies" value="绘画书法">绘画书法 &nbsp

    <!-- 多行文本 -->
    <textarea rows="4" cols="20" name="self_introduce">
    输入你的个人说明
    </textarea>

    <td>
        <input type="submit" value="提交">
    </td>
    <td>
        <input type="reset" value="清楚">
    </td>
</form>
```

# 强行空格
&nbsp;或全角空格符

# 水平线
<hr />

# 列表
ol
type = 1/a/A/i/I

ul
dir
meau

# 封装
div
span 
display:inline,block,inline-block


# 换行
<br />

# 表格
table
caption: 标题
tr: 行
th: 表头
td: 单元格

rowspan
colspan

# placeholder 
# 输入框提示信息
<input type="text" placeholder="要显示的文字">

#
onclick
onkeypress

#换行
<br />

# 超链接
<a href=""></a>

# 图片
<img src="path/to/file or http://" alt="nothing">

# 视频
<video width="320" height="240" controls>
  <source src="movie.mp4" type="video/mp4">
  <source src="movie.ogg" type="video/ogg">
  <source src="movie.webm" type="video/webm">
  <object data="movie.mp4" width="320" height="240">
    <embed src="movie.swf" width="320" height="240">
  </object> 
</video>

