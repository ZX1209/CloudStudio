Highlighting
Highlighting tags is configurable. Use defaultHighlight to set up highlights for all tags. If you need to configure individual tags differently, use customHighlight. If settings are not specified in customHighlight, the value from defaultHighlight is used. If a setting is not specified in defaultHighlight then the older, deprecated icon, iconColour and iconColours settings are used.

Both defaultHighlight and customHighlight allow for the following settings:

foreground - used to set the foreground colour of the highlight in the editor and the marker in the ruler.

background - used to set the background colour of the highlight in the editor.

opacity - percentage value used with the background colour. 100% will produce an opaque background which will obscure selection and other decorations.

Foreground and background colours can be one of "red", "green", "blue", "yellow", "magenta", "cyan", "grey", "white" or "black". RGB values can also be used (e.g. "#80FF00").

icon - used to set a different icon in the tree view. Must be a valid octicon (see https://octicons.github.com/). Defaults to a tick if it's not valid.

iconColour - used to set the colour of the icon in the tree. If not specified, it will try to use the foreground colour, the background colour and then the older settings, in that order.

rulerColour - used to set the colour of the marker in the overview ruler. If not specified, it will to use the foreground colour.

rulerLane - used to set the lane for the marker in the overview ruler. If not specified, it will default to the right hand lane. Use one of "left", "center", "right", or "full".

type - used to control how much is highlighted in the editor. Valid values are:

tag - highlights just the tag
text - highlights the tag and any text after the tag
line - highlights the entire line containing the tag
hideFromTree - used to hide tags from the tree, but still highlight in files

Example:

"todo-tree.defaultHighlight": {
    "icon": "alert",
    "type": "text",
    "foreground": "red",
    "background": "white",
    "opacity": 50,
    "iconColour": "blue"
},
"todo-tree.customHighlight": {
    "TODO": {
        "icon": "check",
        "type": "line"
    },
    "FIXME": {
        "foreground": "black",
        "iconColour": "yellow"
    }
}
Note: The highlight configuration is separate from the settings for the search. Adding settings in customHighlight does not automatically add the tags into todo-tree.tags.

Installing