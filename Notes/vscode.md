"python.jediEnabled": false

vscode note??? what for

$(wslpath '${file}')

# extentions
## todo-tree
really great
setting file see vscode-User

## Better Align
set key bind like this
{ "key": "ctrl+cmd+=",
"command": "wwm.aligncode",
"when": "editorTextFocus && !editorReadonly" }

and use it

## one dark pro

## Roboto Mono

## gi

## vscode icons

## Output Colorizer


yapf


## key binding command ***
yes it's what i want
 // python this file
    {
        "key": "ctrl+p",
        "command": "workbench.action.terminal.sendSequence",
        "args": {
            "text": "python $(wslpath '${file}')\n"
        }
    },


# short cut
ctrl+t go to symbol in workspace which is title or variable or function?
ctrl+u Undo cursor position
ctrl+k ctrl+x Trim trailing whitespace 消除行尾多余空格
ctrl+l select current line
ctrl+r 打开最近的文件
ctrl+g l workbench.action.gotoLine
ctrl+g j workbench.action.navigateToLastEditLocation

Shift+Alt + up/down
复制,移动

Ctrl+Shift+[    折叠（折叠）区域 Fold (collapse) region
Ctrl+Shift+]    展开（未折叠）区域 Unfold (uncollapse) region
Ctrl+K Ctrl+[   折叠（未折叠）所有子区域 Fold (collapse) all subregions
Ctrl+K Ctrl+]   展开（未折叠）所有子区域 Unfold (uncollapse) all subregions
Ctrl+K Ctrl+0   折叠（折叠）所有区域 Fold (collapse) all regions
Ctrl+K Ctrl+J   展开（未折叠）所有区域 Unfold (uncollapse) all regions


Shift + Alt + （拖动鼠标）    列（框）选择 Column (box) selection
Ctrl/Alt + (click)

Ctrl + F2   选择当前字的所有出现 Select all occurrences of current word

Alt +单击 插入光标 Insert cursor
Ctrl + Alt +↑/↓ 在上/下插入光标 Insert cursor above / below