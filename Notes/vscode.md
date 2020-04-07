Name: One Dark Flatland Monokai
Id: reblws.one-dark-flatland-monokai
Description: Flatland Monokai syntax colors with a One Dark editor shell
Version: 0.1.0
Publisher: Enrico Baculinao
VS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=reblws.one-dark-flatland-monokai

# syntax hightlight
https://code.visualstudio.com/api/language-extensions/syntax-highlight-guide#scope-inspector
inspect scope
```json
"editor.tokenColorCustomizations": {
        "textMateRules": [
            {
                "scope": "keyword.declaration.dart",
                "settings": {
                    "foreground": "#fa6f39"
                }
            }
        ]
    }
}
```

# theme-color
https://code.visualstudio.com/api/references/theme-color

# env workspace specific
"terminal.integrated.env.linux": {
    "PATH": "${env:PATH}:/tmp/sslocal.log"
}



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

## VS Code Snippet Generator



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
## task can also do that
see vscode-tasks.md

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


# Predefined variables examples
Supposing that you have the following requirements:

A file located at /home/your-username/your-project/folder/file.ext opened in your editor;
The directory /home/your-username/your-project opened as your root workspace.
So you will have the following values for each variable:

${workspaceFolder} - /home/your-username/your-project
${workspaceFolderBasename} - your-project
${file} - /home/your-username/your-project/folder/file.ext
${relativeFile} - folder/file.ext
${fileBasename} - file.ext
${fileBasenameNoExtension} - file
${fileDirname} - /home/your-username/your-project/folder
${fileExtname} - .ext
${lineNumber} - line number of the cursor
${selectedText} - text selected in your code editor
${execPath} - location of Code.exe


# task.json schema 全参数 模板
https://code.visualstudio.com/docs/editor/tasks-appendix
ps 触发参数提醒
# launch.json schema 全参数 模板
by invoking IntelliSense inside the launch.json string attributes.
