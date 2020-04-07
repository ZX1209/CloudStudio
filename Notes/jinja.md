# assignments ,variables
{% set unkonwFileIconName = 'unknown.svg' %}

# Macros & Call
## Macros
Macros are comparable with functions in regular programming languages. They are useful to put often used idioms into reusable functions to not repeat yourself (“DRY”).

Here’s a small example of a macro that renders a form element:

{% macro input(name, value='', type='text', size=20) -%}
    <input type="{{ type }}" name="{{ name }}" value="{{
        value|e }}" size="{{ size }}">
{%- endmacro %}
The macro can then be called like a function in the namespace:

<p>{{ input('username') }}</p>
<p>{{ input('password', type='password') }}</p>
If the macro was defined in a different template, you have to import it first.

## Call
In some cases it can be useful to pass a macro to another macro. For this purpose, you can use the special call block. The following example shows a macro that takes advantage of the call functionality and how it can be used:

{% macro render_dialog(title, class='dialog') -%}
    <div class="{{ class }}">
        <h2>{{ title }}</h2>
        <div class="contents">
            {{ caller() }}
        </div>
    </div>
{%- endmacro %}

{% call render_dialog('Hello World') %}
    This is a simple dialog rendered by using a macro and
    a call block.
{% endcall %}
It’s also possible to pass arguments back to the call block. This makes it useful as a replacement for loops. Generally speaking, a call block works exactly like a macro without a name.

Here’s an example of how a call block can be used with arguments:

{% macro dump_users(users) -%}
    <ul>
    {%- for user in users %}
        <li><p>{{ user.username|e }}</p>{{ caller(user) }}</li>
    {%- endfor %}
    </ul>
{%- endmacro %}

{% call(user) dump_users(list_of_user) %}
    <dl>
        <dl>Realname</dl>
        <dd>{{ user.realname|e }}</dd>
        <dl>Description</dl>
        <dd>{{ user.description }}</dd>
    </dl>
{% endcall %}



# python 对象..当然喽

# 控制命令
{% %} 

# 打印变量
{{ }}

# 过滤
{{ name|capitalize }}
safe,capitalize,lower,upper,title,trim,striptags

# 注释
{# #}

