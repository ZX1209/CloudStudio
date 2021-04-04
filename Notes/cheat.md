
#Personal cheatsheets are saved in the ~/.cheat directory by default
#but you can specify a different default
#by exporting a DEFAULT_CHEAT_DIR environment variable:
export DEFAULT_CHEAT_DIR='/path/to/my/cheatdir'

#You can additionally instruct cheat to look for cheatsheets in other directories
#by exporting a CHEATPATH environment variable:
export CHEATPATH='/path/to/my/cheats'
export CHEATPATH="$CHEATPATH:/path/to/more/cheats"

#cheat can optionally apply syntax highlighting to your cheatsheets.
#To enable syntax highlighting, export a CHEATCOLORS environment variable:
export CHEATCOLORS=true

export Notes='~/CloudStudio/Notes'
export DEFAULT_CHEAT_DIR=$Notes

export OtherNotes='~/CloudStudio/Notes/notes-others'
export CHEATPATH=$OtherNotes

export CHEATCOLORS=true
export CHEAT_EDITOR=vim
