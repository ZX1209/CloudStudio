#\e[ 参数 m
       ECMA-48 Set Graphics Rendition

       The  ECMA-48  SGR  sequence ESC [ parameters m sets display attributes.  Several attributes
       can be set in the same sequence, separated by  semicolons.   An  empty  parameter  (between
       semicolons or string initiator or terminator) is interpreted as a zero.

       param   result
       0       reset all attributes to their defaults
       1       set bold
       2       set half-bright (simulated with color on a color display)
       4       set  underscore (simulated with color on a color display)
               (the colors used to simulate dim  or  underline  are  set
               using ESC ] ...)
       5       set blink
       7       set reverse video
       10      reset  selected mapping, display control flag, and toggle
               meta flag (ECMA-48 says "primary font").
       11      select null mapping, set display control flag, reset tog‐
               gle meta flag (ECMA-48 says "first alternate font").
       12      select null mapping, set display control flag, set toggle
               meta flag (ECMA-48 says "second  alternate  font").   The
               toggle meta flag causes the high bit of a byte to be tog‐
               gled before the mapping table translation is done.
       21      set normal intensity (ECMA-48 says "doubly underlined")
       22      set normal intensity

       24      underline off
       25      blink off
       27      reverse video off
       30      set black foreground
       31      set red foreground
       32      set green foreground
       33      set brown foreground
       34      set blue foreground
       35      set magenta foreground
       36      set cyan foreground
       37      set white foreground
       38      set underscore on, set default foreground color
       39      set underscore off, set default foreground color
       40      set black background
       41      set red background
       42      set green background
       43      set brown background
       44      set blue background
       45      set magenta background
       46      set cyan background
       47      set white background
       49      set default background color


