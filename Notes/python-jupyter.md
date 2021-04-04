%matplotlib

%config InlineBackend.figure_format = 'svg'


%time
%%time

%timeit
%%timeit


# 该变默认主目录
jupyter notebook --generate-config

根据显示的路径，打开配置文件jupyter_notebook_config.py，全文搜索【notebook_dir】，找到后填入自己的工作路径并保存。（注意：工作路径不能出现中文，否则无法打开Jupyter Notebook）