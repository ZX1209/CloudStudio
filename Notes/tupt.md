# 6.5. Colours and Cursor Movement With **tput**

As with so many things in Unix, there is more than one way to achieve the same ends. A utility called **tput** can also be used to move the cursor around the screen, get back information about the status of the terminal, or set colours. **man tput** doesn't go into much detail about the available commands, but Emilio Lopes e-mailed me to point out that **man terminfo** will give you a *huge* list of capabilities, many of which are device independent, and therefore better than the escape sequences previously mentioned. He suggested that I rewrite all the examples using **tput** for this reason. He is correct that I should, but I've had some trouble controlling it and getting it to do everything I want it to. However, I did rewrite one prompt which you can see as an example:[Section 12.8](https://www.tldp.org/HOWTO/Bash-Prompt-HOWTO/clockt.html). 

Here is a list of tput capabilities that I have found useful:

**tput Colour Capabilities**

- **tput setab [1-7]**

  Set a background colour using ANSI escape

- **tput setb [1-7]**

  Set a background colour

- **tput setaf [1-7]**

  Set a foreground colour using ANSI escape

- **tput setf [1-7]**

  Set a foreground colour

**tput Text Mode Capabilities**

- **tput bold**

  Set bold mode

- **tput dim**

  turn on half-bright mode

- **tput smul**

  begin underline mode

- **tput rmul**

  exit underline mode

- **tput rev**

  Turn on reverse mode

- **tput smso**

  Enter standout mode (bold on rxvt)

- **tput rmso**

  Exit standout mode

- **tput sgr0**

  Turn off all attributes (doesn't work quite as expected)

**tput Cursor Movement Capabilities**

- **tput cup Y X**

  Move cursor to screen location X,Y (top left is 0,0)

- **tput sc**

  Save the cursor position

- **tput rc**

  Restore the cursor position

- **tput lines**

  Output the number of lines of the terminal

- **tput cols**

  Output the number of columns of the terminal

- **tput cub N**

  Move N characters left

- **tput cuf N**

  Move N characters right

- **tput cub1**

  move left one space

- **tput cuf1**

  non-destructive space (move right one space)

- **tput ll**

  last line, first column (if no cup)

- **tput cuu1**

  up one line

**tput Clear and Insert Capabilities**

- **tput ech N**

  Erase N characters

- **tput clear**

  clear screen and home cursor

- **tput el1**

  Clear to beginning of line

- **tput el**

  clear to end of line

- **tput ed**

  clear to end of screen

- **tput ich N**

  insert N characters (moves rest of line forward!)

- **tput il N**

  insert N lines

This is by no means a complete list of what **terminfo** and **tput** allow, in fact it's only the beginning. **man tput** and **man terminfo** if you want to know more.