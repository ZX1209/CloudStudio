
# settings
```js
    // todo tree settings
    "todo-tree.regex": "((//|#|<!--|;|/\\*|^)\\s*($TAGS):|^\\s*- \\[ \\])",
    "todo-tree.tags": [
        "TODO",
        "FIXME",
        "tag",
        "done"
    ],
    "todo-tree.regexCaseSensitive": false,
    "todo-tree.showInExplorer": true,
    "todo-tree.defaultHighlight": {
        "foreground": "white",
        "background": "yellow",
        "icon": "check",
        "rulerColour": "yellow",
        "type": "tag",
        "iconColour": "yellow"
    },
    "todo-tree.customHighlight": {
        "todo": {
            "background": "yellow",
            "rulerColour": "yellow"
        },
        "FIXME": {
            "background": "red",
            "icon": "beaker",
            "rulerColour": "red",
        },
        "tag": {
            "background": "blue",
            "icon": "tag",
            "rulerColour": "blue",
            "rulerLane": "full"
        },
        "done": {
            "background": "green",
            "icon": "issue-closed",
            "rulerColour": "green",
        }
    }
```