# xdotool

## mouse move left
xdotool mousemove_relative -- -15 0

## mouse click
xdotool click 4

> Command line automation for X11.

- Retrieve the X-Windows window ID of the running Firefox window(s):

`xdotool search --onlyvisible --name {{firefox}}`

- Click the right mouse button:

`xdotool click {{3}}`
