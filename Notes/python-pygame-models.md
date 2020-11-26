> https://www.pygame.org/docs/tut/PygameIntro.html

> To get the state of various input devices, you can forego the event queue and access the input devices directly with their appropriate modules: pygame.mousepygame module to work with the mouse, pygame.keypygame module to work with the keyboard, and pygame.joystickPygame module for interacting with joysticks, gamepads, and trackballs.. If you use this method, remember that pygame requires some form of communication with the system window manager and other parts of the platform. To keep pygame in sync with the system, you will need to call pygame.event.pump()internally process pygame event handlers to keep everything current. Usually, this should be called once per game loop. Note: Joysticks will not send any events until the device has been initialized.


## pygame.mouse
pygame module to work with the mouse
### pygame.mouse.get_pressed
get the state of the mouse buttons
### pygame.mouse.get_pos
get the mouse cursor position
### pygame.mouse.get_rel
get the amount of mouse movement
### pygame.mouse.set_pos
set the mouse cursor position
### pygame.mouse.set_visible
hide or show the mouse cursor
### pygame.mouse.get_visible
get the current visibility state of the mouse cursor
### pygame.mouse.get_focused
check if the display is receiving mouse input
### pygame.mouse.set_cursor
set the image for the mouse cursor
### pygame.mouse.set_system_cursor
set the mouse cursor to a system variant
### pygame.mouse.get_cursor
get the image of the mouse cursor

## pygame.sprite; Sprite ,Group
pygame module with basic game object classes
### pygame.sprite.Sprite
Simple base class for visible game objects.
Sprite(*groups) -> Sprite
The base class for visible game objects. Derived classes will want to override the Sprite.update() and assign a Sprite.image and Sprite.rect attributes. The initializer can accept any number of Group instances to be added to.
When subclassing the Sprite, be sure to call the base initializer before adding the Sprite to Groups. For example:
```py
class Block(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, color, width, height):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)

       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
       self.image = pygame.Surface([width, height])
       self.image.fill(color)

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       self.rect = self.image.get_rect()

```
#### pygame.sprite.Sprite.update
method to control sprite behavior
#### pygame.sprite.Sprite.add
add the sprite to groups
#### pygame.sprite.Sprite.remove
remove the sprite from groups
#### pygame.sprite.Sprite.kill
remove the Sprite from all Groups
#### pygame.sprite.Sprite.alive
does the sprite belong to any groups
#### pygame.sprite.Sprite.groups
list of Groups that contain this Sprite


### pygame.sprite.DirtySprite
A subclass of Sprite with more attributes and features.
### pygame.sprite.Group
A container class to hold and manage multiple Sprite objects.
Group(*sprites) -> Group
#### pygame.sprite.Group.sprites
list of the Sprites this Group contains
#### pygame.sprite.Group.copy
duplicate the Group
#### pygame.sprite.Group.add
add Sprites to this Group
#### pygame.sprite.Group.remove
remove Sprites from the Group
#### pygame.sprite.Group.has
test if a Group contains Sprites
#### pygame.sprite.Group.update
call the update method on contained Sprites

not allowed to pass args now


#### pygame.sprite.Group.draw
blit the Sprite images
#### pygame.sprite.Group.clear
draw a background over the Sprites


#### pygame.sprite.Group.empty
remove all Sprites
clear(Surface_dest, background) -> None
Erases the Sprites used in the last Group.draw() call. The destination Surface is cleared by filling the drawn Sprite positions with the background.

The background is usually a Surface image the same dimensions as the destination Surface. However, it can also be a callback function that takes two arguments; the destination Surface and an area to clear. The background callback function will be called several times each clear.

Here is an example callback that will clear the Sprites with solid red:

def clear_callback(surf, rect):
    color = 255, 0, 0
    surf.fill(color, rect)

### pygame.sprite.RenderPlain
Same as pygame.sprite.Group
### pygame.sprite.RenderClear
Same as pygame.sprite.Group
### pygame.sprite.RenderUpdates
Group sub-class that tracks dirty updates.
### pygame.sprite.OrderedUpdates
RenderUpdates sub-class that draws Sprites in order of addition.
### pygame.sprite.LayeredUpdates
LayeredUpdates is a sprite group that handles layers and draws like OrderedUpdates.
### pygame.sprite.LayeredDirty
LayeredDirty group is for DirtySprite objects. Subclasses LayeredUpdates.
### pygame.sprite.GroupSingle
Group container that holds a single sprite.
### pygame.sprite.spritecollide
Find sprites in a group that intersect another sprite.
### pygame.sprite.collide_rect
Collision detection between two sprites, using rects.
### pygame.sprite.collide_rect_ratio
Collision detection between two sprites, using rects scaled to a ratio.
### pygame.sprite.collide_circle
Collision detection between two sprites, using circles.
### pygame.sprite.collide_circle_ratio
Collision detection between two sprites, using circles scaled to a ratio.
### pygame.sprite.collide_mask
Collision detection between two sprites, using masks.
### pygame.sprite.groupcollide
Find all sprites that collide between two groups.
### pygame.sprite.spritecollideany
Simple test if a sprite intersects anything in a group.

## pygame.mixer
> https://www.pygame.org/docs/ref/mixer.html
pygame module for loading and playing sounds

### pygame.mixer.Sound
Create a new Sound object from a file or buffer object
Sound(filename) -> Sound
Sound(file=filename) -> Sound
Sound(buffer) -> Sound
Sound(buffer=buffer) -> Sound
Sound(object) -> Sound
Sound(file=object) -> Sound
Sound(array=object) -> Sound
#### pygame.mixer.Sound.play
begin sound playback
#### pygame.mixer.Sound.stop
stop sound playback
#### pygame.mixer.Sound.fadeout
stop sound playback after fading out
#### pygame.mixer.Sound.set_volume
set the playback volume for this Sound
#### pygame.mixer.Sound.get_volume
get the playback volume
#### pygame.mixer.Sound.get_num_channels
count how many times this Sound is playing
#### pygame.mixer.Sound.get_length
get the length of the Sound
#### pygame.mixer.Sound.get_raw
return a bytestring copy of the Sound samples.

### pygame.mixer.init
initialize the mixer module
### pygame.mixer.pre_init
preset the mixer init arguments
### pygame.mixer.quit
uninitialize the mixer
### pygame.mixer.get_init
test if the mixer is initialized
### pygame.mixer.stop
stop playback of all sound channels
### pygame.mixer.pause
temporarily stop playback of all sound channels
### pygame.mixer.unpause
resume paused playback of sound channels
### pygame.mixer.fadeout
fade out the volume on all sounds before stopping
### pygame.mixer.set_num_channels
set the total number of playback channels
### pygame.mixer.get_num_channels
get the total number of playback channels
### pygame.mixer.set_reserved
reserve channels from being automatically used
### pygame.mixer.find_channel
find an unused channel
### pygame.mixer.get_busy
test if any sound is being mixed
### pygame.mixer.get_sdl_mixer_version
get the mixer's SDL version

### pygame.mixer.Channel
Create a Channel object for controlling playback


## pygame.Rect
pygame object for storing rectangular coordinates
Rect(left, top, width, height) -> Rect
Rect((left, top), (width, height)) -> Rect
Rect(object) -> Rect

The Rect object has several virtual attributes which can be used to move and align the Rect:
:star:
x,y
top, left, bottom, right
topleft, bottomleft, topright, bottomright
midtop, midleft, midbottom, midright
center, centerx, centery
size, width, height
w,h

All of these attributes can be assigned to:

rect1.right = 10
rect2.center = (20,30)
Assigning to size, width or height changes the dimensions of the rectangle; all other assignments move the rectangle without resizing it. Notice that some attributes are integers and others are pairs of integers.

If a Rect has a nonzero width or height, it will return True for a nonzero test. Some methods return a Rect with 0 size to represent an invalid rectangle. A Rect with a 0 size will not collide when using collision detection methods (e.g. collidepoint(), colliderect(), etc.).

The coordinates for Rect objects are all integers. The size values can be programmed to have negative values, but these are considered illegal Rects for most operations.

There are several collision tests between other rectangles. Most python containers can be searched for collisions against a single Rect.

The area covered by a Rect does not include the right- and bottom-most edge of pixels. If one Rect's bottom border is another Rect's top border (i.e., rect1.bottom=rect2.top), the two meet exactly on the screen but do not overlap, and rect1.colliderect(rect2) returns false.

New in pygame 1.9.2: The Rect class can be subclassed. Methods such as copy() and move() will recognize this and return instances of the subclass. However, the subclass's __init__() method is not called, and __new__() is assumed to take no arguments. So these methods should be overridden if any extra attributes need to be copied.

### pygame.Rect.copy
copy the rectangle
### pygame.Rect.move
moves the rectangle
### pygame.Rect.move_ip
moves the rectangle, in place
### pygame.Rect.inflate
grow or shrink the rectangle size
### pygame.Rect.inflate_ip
grow or shrink the rectangle size, in place
### pygame.Rect.update
sets the position and size of the rectangle
### pygame.Rect.clamp
moves the rectangle inside another
### pygame.Rect.clamp_ip
moves the rectangle inside another, in place
### pygame.Rect.clip
crops a rectangle inside another
### pygame.Rect.clipline
crops a line inside a rectangle
### pygame.Rect.union
joins two rectangles into one
### pygame.Rect.union_ip
joins two rectangles into one, in place
### pygame.Rect.unionall
the union of many rectangles
### pygame.Rect.unionall_ip
the union of many rectangles, in place
### pygame.Rect.fit
resize and move a rectangle with aspect ratio
### pygame.Rect.normalize
correct negative sizes
### pygame.Rect.contains
test if one rectangle is inside another
### pygame.Rect.collidepoint
test if a point is inside a rectangle
### pygame.Rect.colliderect
test if two rectangles overlap
### pygame.Rect.collidelist
test if one rectangle in a list intersects
### pygame.Rect.collidelistall
test if all rectangles in a list intersect
### pygame.Rect.collidedict
test if one rectangle in a dictionary intersects
### pygame.Rect.collidedictall
test if all rectangles in a dictionary intersect








## pygame.time
pygame module for monitoring time
### pygame.time.get_ticks
get the time in milliseconds
### pygame.time.wait
pause the program for an amount of time
### pygame.time.delay
pause the program for an amount of time
### pygame.time.set_timer
repeatedly create an event on the event queue
### pygame.time.Clock
create an object to help track time
Clock() -> Clock
#### pygame.time.Clock.tick
update the clock


#### pygame.time.Clock.tick_busy_loop
update the clock
#### pygame.time.Clock.get_time
time used in the previous tick
#### pygame.time.Clock.get_rawtime
actual time used in the previous tick
#### pygame.time.Clock.get_fps
compute the clock framerate
Creates a new Clock object that can be used to track an amount of time. The clock also provides several functions to help control a game's framerate.


## pygame.draw
pygame module for drawing shapes
### pygame.draw.rect
draw a rectangle
### pygame.draw.polygon
draw a polygon
### pygame.draw.circle
draw a circle
### pygame.draw.ellipse
draw an ellipse
### pygame.draw.arc
draw an elliptical arc
### pygame.draw.line
draw a straight line

line(surface, color, start_pos, end_pos, width) -> Rect
line(surface, color, start_pos, end_pos, width=1) -> Rect
Draws a straight line on the given surface. There are no endcaps. For thick lines the ends are squared off.

Parameters:	
surface (Surface) -- surface to draw on
color (Color or int or tuple(int, int, int, [int])) -- color to draw with, the alpha value is optional if using a tuple (RGB[A])
start_pos (tuple(int or float, int or float) or list(int or float, int or float) or Vector2(int or float, int or float)) -- start position of the line, (x, y)
end_pos (tuple(int or float, int or float) or list(int or float, int or float) or Vector2(int or float, int or float)) -- end position of the line, (x, y)
width (int) --
(optional) used for line thickness

if width >= 1, used for line thickness (default is 1)
if width < 1, nothing will be drawn

Note When using width values > 1, lines will grow as follows.
For odd width values, the thickness of each line grows with the original line being in the center.

For even width values, the thickness of each line grows with the original line being offset from the center (as there is no exact center line drawn). As a result, lines with a slope < 1 (horizontal-ish) will have 1 more pixel of thickness below the original line (in the y direction). Lines with a slope >= 1 (vertical-ish) will have 1 more pixel of thickness to the right of the original line (in the x direction).

Returns:	
a rect bounding the changed pixels, if nothing is drawn the bounding rect's position will be the start_pos parameter value (float values will be truncated) and its width and height will be 0

Return type:	
Rect

Raises:	
TypeError -- if start_pos or end_pos is not a sequence of two numbers

### pygame.draw.lines
draw multiple contiguous straight line segments
### pygame.draw.aaline
draw a straight antialiased line
### pygame.draw.aalines
draw multiple contiguous straight antialiased line segments


## pygame
the top level pygame package
### pygame.init
initialize all imported pygame modules
### pygame.quit
uninitialize all pygame modules
### pygame.get_init
returns True if pygame is currently initialized
### pygame.error
standard pygame exception
### pygame.get_error
get the current error message
### pygame.set_error
set the current error message
### pygame.get_sdl_version
get the version number of SDL
### pygame.get_sdl_byteorder
get the byte order of SDL
### pygame.register_quit
register a function to be called when pygame quits
### pygame.encode_string
Encode a Unicode or bytes object
### pygame.encode_file_path
Encode a Unicode or bytes object as a file system path

## pygame.version
small module containing version information
### pygame.version.ver
version number as a string
### pygame.version.vernum
tupled integers of the version
### pygame.version.rev
repository revision of the build
### pygame.version.SDL
tupled integers of the SDL library version
This module is automatically imported into the pygame package and can be used to check which version of pygame has been imported.

## Setting Environment Variables
> https://www.pygame.org/docs/ref/pygame.html
Some aspects of pygame's behaviour can be controlled by setting environment variables, they cover a wide range of the library's functionality. Some of the variables are from pygame itself, while others come from the underlying C SDL library that pygame uses.

In python, environment variables are usually set in code like this:


## pygame.Surface
pygame object for representing images
Surface((width, height), flags=0, depth=0, masks=None) -> Surface
Surface((width, height), flags=0, Surface) -> Surface

### pygame.Surface.get_size
get the dimensions of the Surface
### pygame.Surface.get_width
get the width of the Surface
### pygame.Surface.get_height
get the height of the Surface
### pygame.Surface.get_rect
get the rectangular area of the Surface


### pygame.Surface.blit
draw one image onto another(也可用作裁剪,不共享数据)
blit(source, dest, area=None, special_flags=0) -> Rect
Draws a source Surface onto this Surface. The draw can be positioned with the dest argument. 

screen.blit(mysurf, (100, 100))


### pygame.Surface.blits
draw many images onto another
### pygame.Surface.convert
change the pixel format of an image
### pygame.Surface.convert_alpha
change the pixel format of an image including per pixel alphas
### pygame.Surface.copy
create a new copy of a Surface
### pygame.Surface.fill
fill Surface with a solid color
### pygame.Surface.scroll
Shift the surface image in place
### pygame.Surface.set_colorkey
Set the transparent colorkey
### pygame.Surface.get_colorkey
Get the current transparent colorkey
### pygame.Surface.set_alpha
set the alpha value for the full Surface image
### pygame.Surface.get_alpha
get the current Surface transparency value
### pygame.Surface.lock
lock the Surface memory for pixel access
### pygame.Surface.unlock
unlock the Surface memory from pixel access
### pygame.Surface.mustlock
test if the Surface requires locking
### pygame.Surface.get_locked
test if the Surface is current locked
### pygame.Surface.get_locks
Gets the locks for the Surface
### pygame.Surface.get_at
get the color value at a single pixel
### pygame.Surface.set_at
set the color value for a single pixel
### pygame.Surface.get_at_mapped
get the mapped color value at a single pixel
### pygame.Surface.get_palette
get the color index palette for an 8-bit Surface
### pygame.Surface.get_palette_at
get the color for a single entry in a palette
### pygame.Surface.set_palette
set the color palette for an 8-bit Surface
### pygame.Surface.set_palette_at
set the color for a single index in an 8-bit Surface palette
### pygame.Surface.map_rgb
convert a color into a mapped color value
### pygame.Surface.unmap_rgb
convert a mapped integer color value into a Color

### pygame.Surface.set_clip
set the current clipping area of the Surface
### pygame.Surface.get_clip
get the current clipping area of the Surface

### pygame.Surface.subsurface
create a new surface that references its parent
subsurface(Rect) -> Surface

surface 裁剪

### pygame.Surface.get_parent
find the parent of a subsurface
### pygame.Surface.get_abs_parent
find the top level parent of a subsurface
### pygame.Surface.get_offset
find the position of a child subsurface inside a parent
### pygame.Surface.get_abs_offset
find the absolute position of a child subsurface inside its top level parent


### pygame.Surface.get_bitsize
get the bit depth of the Surface pixel format
### pygame.Surface.get_bytesize
get the bytes used per Surface pixel
### pygame.Surface.get_flags
get the additional flags used for the Surface
### pygame.Surface.get_pitch
get the number of bytes used per Surface row
### pygame.Surface.get_masks
the bitmasks needed to convert between a color and a mapped integer
### pygame.Surface.set_masks
set the bitmasks needed to convert between a color and a mapped integer
### pygame.Surface.get_shifts
the bit shifts needed to convert between a color and a mapped integer
### pygame.Surface.set_shifts
sets the bit shifts needed to convert between a color and a mapped integer
### pygame.Surface.get_losses
the significant bits used to convert between a color and a mapped integer

### pygame.Surface.get_bounding_rect
find the smallest rect containing data

### pygame.Surface.get_view
return a buffer view of the Surface's pixels.
### pygame.Surface.get_buffer
acquires a buffer object for the pixels of the Surface.
### pygame.Surface._pixels_address
pixel buffer address



## pygame.event
pygame module for interacting with events and queues
Pygame handles all its event messaging through an event queue. The routines in this module help you manage that event queue. The input queue is heavily dependent on the pygame.displaypygame module to control the display window and screen module. If the display has not been initialized and a video mode not set, the event queue may not work properly. The event subsystem should be called from the main thread. If you want to post events into the queue from other threads, please use the pygame.fasteventpygame module for interacting with events and queues module.
### pygame.event.post
place a new event on the queue
### pygame.event.custom_type
make custom user event type
### pygame.event.Event
create a new event object

### pygame.event.pump
internally process pygame event handlers
### pygame.event.get
get events from the queue
### pygame.event.poll
get a single event from the queue
### pygame.event.wait
wait for a single event from the queue
### pygame.event.peek
test if event types are waiting on the queue
### pygame.event.clear
remove all events from the queue
### pygame.event.event_name
get the string name from an event id
### pygame.event.set_blocked
control which events are allowed on the queue
### pygame.event.set_allowed
control which events are allowed on the queue
### pygame.event.get_blocked
test if a type of event is blocked from the queue
### pygame.event.set_grab
control the sharing of input devices with other applications
### pygame.event.get_grab
test if the program is sharing input devices

### pygame.event.EventType
pygame object for representing events
can not see dircetly



## pygame.display
pygame module to control the display window and screen

### pygame.display.set_icon
Change the system image for the display window
### pygame.display.set_caption
Set the current window caption
### pygame.display.get_caption
Get the current window caption
### pygame.display.set_mode
Initialize a window or screen for display
### pygame.display.get_surface
Get a reference to the currently set display surface


### pygame.display.init
Initialize the display module
### pygame.display.quit
Uninitialize the display module
### pygame.display.get_init
Returns True if the display module has been initialized


### pygame.display.flip
Update the full display Surface to the screen
### pygame.display.update
Update portions of the screen for software displays
update(rectangle=None) -> None
update(rectangle_list) -> None
This function is like an optimized version of  pygame.display.flip() for software displays. It allows only a portion of the screen to updated, instead of the entire area. If no argument is passed it updates the entire Surface area like pygame.display.flip().

You can pass the function a single rectangle, or a sequence of rectangles. It is more efficient to pass many rectangles at once than to call update multiple times with single or a partial list of rectangles. If passing a sequence of rectangles it is safe to include None values in the list, which will be skipped.

This call cannot be used on pygame.OPENGL displays and will generate an exception.
### pygame.display.toggle_fullscreen
Switch between fullscreen and windowed displays



### pygame.display.iconify
Iconify the display surface

### pygame.display.get_driver
Get the name of the pygame display backend
### pygame.display.Info
Create a video display information object
### pygame.display.get_wm_info
Get information about the current windowing system
### pygame.display.list_modes
Get list of available fullscreen modes
### pygame.display.mode_ok
Pick the best color depth for a display mode
### pygame.display.gl_get_attribute
Get the value for an OpenGL flag for the current display
### pygame.display.gl_set_attribute
Request an OpenGL display attribute for the display mode
### pygame.display.get_active
Returns True when the display is active on the screen
### pygame.display.set_gamma
Change the hardware gamma ramps
### pygame.display.set_gamma_ramp
Change the hardware gamma ramps with a custom lookup
### pygame.display.set_palette
Set the display color palette for indexed displays
### pygame.display.get_num_displays
Return the number of displays
### pygame.display.get_window_size
Return the size of the window or screen
### pygame.display.get_allow_screensaver
Return whether the screensaver is allowed to run.
### pygame.display.set_allow_screensaver
Set whether the screensaver may run




## pygame.key
pygame module to work with the keyboard
### constans key
pygame
Constant      ASCII   Description
---------------------------------
K_BACKSPACE   \b      backspace
K_TAB         \t      tab
K_CLEAR               clear
K_RETURN      \r      return
K_PAUSE               pause
K_ESCAPE      ^[      escape
K_SPACE               space
K_EXCLAIM     !       exclaim
K_QUOTEDBL    "       quotedbl
K_HASH        #       hash
K_DOLLAR      $       dollar
K_AMPERSAND   &       ampersand
K_QUOTE               quote
K_LEFTPAREN   (       left parenthesis
K_RIGHTPAREN  )       right parenthesis
K_ASTERISK    *       asterisk
K_PLUS        +       plus sign
K_COMMA       ,       comma
K_MINUS       -       minus sign
K_PERIOD      .       period
K_SLASH       /       forward slash
K_0           0       0
K_1           1       1
K_2           2       2
K_3           3       3
K_4           4       4
K_5           5       5
K_6           6       6
K_7           7       7
K_8           8       8
K_9           9       9
K_COLON       :       colon
K_SEMICOLON   ;       semicolon
K_LESS        <       less-than sign
K_EQUALS      =       equals sign
K_GREATER     >       greater-than sign
K_QUESTION    ?       question mark
K_AT          @       at
K_LEFTBRACKET [       left bracket
K_BACKSLASH   \       backslash
K_RIGHTBRACKET ]      right bracket
K_CARET       ^       caret
K_UNDERSCORE  _       underscore
K_BACKQUOTE   `       grave
K_a           a       a
K_b           b       b
K_c           c       c
K_d           d       d
K_e           e       e
K_f           f       f
K_g           g       g
K_h           h       h
K_i           i       i
K_j           j       j
K_k           k       k
K_l           l       l
K_m           m       m
K_n           n       n
K_o           o       o
K_p           p       p
K_q           q       q
K_r           r       r
K_s           s       s
K_t           t       t
K_u           u       u
K_v           v       v
K_w           w       w
K_x           x       x
K_y           y       y
K_z           z       z
K_DELETE              delete
K_KP0                 keypad 0
K_KP1                 keypad 1
K_KP2                 keypad 2
K_KP3                 keypad 3
K_KP4                 keypad 4
K_KP5                 keypad 5
K_KP6                 keypad 6
K_KP7                 keypad 7
K_KP8                 keypad 8
K_KP9                 keypad 9
K_KP_PERIOD   .       keypad period
K_KP_DIVIDE   /       keypad divide
K_KP_MULTIPLY *       keypad multiply
K_KP_MINUS    -       keypad minus
K_KP_PLUS     +       keypad plus
K_KP_ENTER    \r      keypad enter
K_KP_EQUALS   =       keypad equals
K_UP                  up arrow
K_DOWN                down arrow
K_RIGHT               right arrow
K_LEFT                left arrow
K_INSERT              insert
K_HOME                home
K_END                 end
K_PAGEUP              page up
K_PAGEDOWN            page down
K_F1                  F1
K_F2                  F2
K_F3                  F3
K_F4                  F4
K_F5                  F5
K_F6                  F6
K_F7                  F7
K_F8                  F8
K_F9                  F9
K_F10                 F10
K_F11                 F11
K_F12                 F12
K_F13                 F13
K_F14                 F14
K_F15                 F15
K_NUMLOCK             numlock
K_CAPSLOCK            capslock
K_SCROLLOCK           scrollock
K_RSHIFT              right shift
K_LSHIFT              left shift
K_RCTRL               right control
K_LCTRL               left control
K_RALT                right alt
K_LALT                left alt
K_RMETA               right meta
K_LMETA               left meta
K_LSUPER              left Windows key
K_RSUPER              right Windows key
K_MODE                mode shift
K_HELP                help
K_PRINT               print screen
K_SYSREQ              sysrq
K_BREAK               break
K_MENU                menu
K_POWER               power
K_EURO                Euro
The keyboard also has a list of modifier states (from pygame.localspygame constants) that can be assembled by bitwise-ORing them together.

pygame
Constant      Description
-------------------------
KMOD_NONE     no modifier keys pressed
KMOD_LSHIFT   left shift
KMOD_RSHIFT   right shift
KMOD_SHIFT    left shift or right shift or both
KMOD_LCTRL    left control
KMOD_RCTRL    right control
KMOD_CTRL     left control or right control or both
KMOD_LALT     left alt
KMOD_RALT     right alt
KMOD_ALT      left alt or right alt or both
KMOD_LMETA    left meta
KMOD_RMETA    right meta
KMOD_META     left meta or right meta or both
KMOD_CAPS     caps lock
KMOD_NUM      num lock
KMOD_MODE     AltGr


### pygame.key.get_focused
true if the display is receiving keyboard input from the system
### pygame.key.get_pressed
get the state of all keyboard buttons
### pygame.key.get_mods
determine which modifier keys are being held
### pygame.key.set_mods
temporarily set which modifier keys are pressed
### pygame.key.set_repeat
control how held keys are repeated
### pygame.key.get_repeat
see how held keys are repeated
### pygame.key.name
get the name of a key identifier
### pygame.key.key_code
get the key identifier from a key name
### pygame.key.start_text_input
start handling IME compositions
### pygame.key.stop_text_input
stop handling IME compositions
### pygame.key.set_text_input_rect
controls the position of the candidate list


## pygame.joystick 游戏杆
Pygame module for interacting with joysticks, gamepads, and trackballs.
### pygame.joystick.init
Initialize the joystick module.
### pygame.joystick.quit
Uninitialize the joystick module.
### pygame.joystick.get_init
Returns True if the joystick module is initialized.
### pygame.joystick.get_count
Returns the number of joysticks.
### pygame.joystick.Joystick
Create a new Joystick object.