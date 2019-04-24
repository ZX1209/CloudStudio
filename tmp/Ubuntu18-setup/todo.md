# 更新源

sudo cp /etc/apt/sources.list /etc/apt/sources.list.bak

echo "
#清华
# 默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-updates main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-updates main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-backports main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-backports main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-security main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-security main restricted universe multiverse

# 预发布软件源，不建议启用
# deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-proposed main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-proposed main restricted universe multiverse


#ustc
deb https://mirrors.ustc.edu.cn/ubuntu/ bionic main restricted universe multiverse
deb-src https://mirrors.ustc.edu.cn/ubuntu/ bionic main restricted universe multiverse

deb https://mirrors.ustc.edu.cn/ubuntu/ bionic-security main restricted universe multiverse
deb-src https://mirrors.ustc.edu.cn/ubuntu/ bionic-security main restricted universe multiverse

deb https://mirrors.ustc.edu.cn/ubuntu/ bionic-updates main restricted universe multiverse
deb-src https://mirrors.ustc.edu.cn/ubuntu/ bionic-updates main restricted universe multiverse

deb https://mirrors.ustc.edu.cn/ubuntu/ bionic-backports main restricted universe multiverse
deb-src https://mirrors.ustc.edu.cn/ubuntu/ bionic-backports main restricted universe multiverse

## Not recommended
# deb https://mirrors.ustc.edu.cn/ubuntu/ bionic-proposed main restricted universe multiverse
# deb-src https://mirrors.ustc.edu.cn/ubuntu/ bionic-proposed main restricted universe multiverse

#阿里云源
deb http://mirrors.aliyun.com/ubuntu/ bionic main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ bionic-security main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ bionic-updates main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ bionic-proposed main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ bionic-backports main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-security main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-updates main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-proposed main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-backports main restricted universe multiverse

#163源
deb http://mirrors.163.com/ubuntu/ bionic main restricted universe multiverse
deb http://mirrors.163.com/ubuntu/ bionic-security main restricted universe multiverse
deb http://mirrors.163.com/ubuntu/ bionic-updates main restricted universe multiverse
deb http://mirrors.163.com/ubuntu/ bionic-proposed main restricted universe multiverse
deb http://mirrors.163.com/ubuntu/ bionic-backports main restricted universe multiverse
deb-src http://mirrors.163.com/ubuntu/ bionic main restricted universe multiverse
deb-src http://mirrors.163.com/ubuntu/ bionic-security main restricted universe multiverse
deb-src http://mirrors.163.com/ubuntu/ bionic-updates main restricted universe multiverse
deb-src http://mirrors.163.com/ubuntu/ bionic-proposed main restricted universe multiverse
deb-src http://mirrors.163.com/ubuntu/ bionic-backports main restricted universe multiverse
" > /etc/apt/sources.list

sudo apt update
sudo apt upgrade

# 美化
sudo apt-get install gnome-tweak-tool


# 更该系统语言
language support


# sublime setting
{
    "bold_folder_labels": true,
    "color_scheme": "Packages/Color Scheme - Default/Monokai.sublime-color-scheme",
    "default_encoding": "UTF-8",
    "default_line_ending": "LF",
    "expand_tabs_on_save": true,
    "font_options":
    [
        "gdi"
    ],
    "font_size": 16,
    "ignored_packages":
    [
        "AppleScript",
        "Colorcoder",
        "Emmet",
        "GitGutter",
        "IMESupport",
        "JavaScript",
        "MarkdownEditing",
        "Material Theme",
        "Material Theme - Appbar",
        "SmartMarkdown",
        "Status Bar Time",
        "Statusbar Path",
        "Vintage",
        "Zeal"
    ],
    "indent_guide_options":
    [
        "draw_normal",
        "draw_active"
    ],
    "line_padding_bottom": 3,
    "line_padding_top": 3,
    "original_color_scheme": "Packages/Boxy Theme/schemes/Boxy Tomorrow.tmTheme",
    "overlay_scroll_bars": "enabled",
    "show_encoding": true,
    "tab_size": 4,
    "theme": "Boxy Tomorrow.sublime-theme",
    "theme_accent_tangerine": true,
    "theme_font_md": true,
    "theme_icons_materialized": true,
    "theme_scrollbar_rounded": true,
    "theme_sidebar_close_always_visible": true,
    "theme_sidebar_disclosure": true,
    "theme_sidebar_font_xl": true,
    "theme_sidebar_indent_top_level_disabled": true,
    "theme_sidebar_indent_xl": true,
    "theme_sidebar_size_md": true,
    "theme_size_xs": true,
    "theme_tab_font_xl": true,
    "theme_tab_selected_label_bold": true,
    "theme_tab_selected_underlined": true,
    "theme_unified": true,
    "translate_tabs_to_spaces": true
}


# 主题
# 安装一个叫gnome-tweak-tool gnome桌面(ubuntu18.04的桌面系统-优化-工具)
sudo apt install gnome-tweak-tool
# 在应用界面打开它，名字就要tweak，你可以设置字体大小了
