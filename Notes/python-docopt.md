> http://docopt.org/
## template
```py
"""Naval Fate.

Usage:
  naval_fate.py ship new <name>...
  naval_fate.py ship <name> move <x> <y> [--speed=<kn>]
  naval_fate.py ship shoot <x> <y> [options]
  naval_fate.py mine (set|remove) <x> <y> [--moored | --drifting]
  naval_fate.py (-h | --help)
  naval_fate.py --version

Options:
  -h --help     Show this screen.
  --version     Show version.
  --speed=<kn>  Speed in knots [default: 10].
  --moored      Moored (anchored) mine.
  --drifting    Drifting mine.
  -a, --all             List everything.
  -l, --long            Long output.
  -h, --human-readable  Display in human-readable format.


"""
from docopt import docopt


if __name__ == '__main__':
    arguments = docopt(__doc__, version='Naval Fate 2.0')
    print(arguments)
```

## 理解

在Usage 范围内写用例
<参数>,命令

[]可选,()必选,|或,...还有, 看着用

Options,写详细的可选参数,,可以有缩写和默认参数

看清arguments,解析出的字典

--option=some,,最好,,没有歧义

## 杂
### comma split,long and short option
-o FILE --output=FILE       # without comma, with "=" sign
-i <file>, --input <file>   # with comma, without "=" sign


### default value
If you want to set a default value for an option with an argument, put it into the option's description, in the form [default: <the-default-value>].

--coefficient=K  The K coefficient [default: 2.95]
--output=FILE    Output file [default: test.txt]
--directory=DIR  Some directory [default: ./]

### [options]
"[options]" is a shortcut that allows to avoid listing all options (from list of options with descriptions) in a pattern. For example:
没有加 [options] 选项的Usage,如果用了option会不符合Usage,而直接跳至参数提示

Usage: my_program [options] <path>

--all             List everything.
--long            Long output.
--human-readable  Display in human-readable format.
is equivalent to:

Usage: my_program [--all --long --human-readable] <path>

--all             List everything.
--long            Long output.
--human-readable  Display in human-readable format.

## official doc
### Usage pattern format
Usage pattern is a substring of doc that starts with usage: (case insensitive) and ends with a visibly empty line. Minimum example:

"""Usage: my_program.py

"""
The first word after usage: is interpreted as your program’s name. You can specify your program’s name several times to signify several exclusive patterns:

"""Usage: my_program.py FILE
          my_program.py COUNT FILE

"""
Each pattern can consist of the following elements:

<arguments>, ARGUMENTS. Arguments are specified as either upper-case words, e.g. my_program.py CONTENT-PATH or words surrounded by angular brackets: my_program.py <content-path>.
–options. Options are words started with dash (-), e.g. --output, -o. You can “stack” several of one-letter options, e.g. -oiv which will be the same as -o -i -v. The options can have arguments, e.g. --input=FILE or -i FILE or even -iFILE. However it is important that you specify option descriptions if you want your option to have an argument, a default value, or specify synonymous short/long versions of the option (see next section on option descriptions).
commands are words that do not follow the described above conventions of --options or <arguments> or ARGUMENTS, plus two special commands: dash “-” and double dash “--” (see below).
Use the following constructs to specify patterns:

[ ] (brackets) optional elements. e.g.: my_program.py [-hvqo FILE]
( ) (parens) required elements. All elements that are not put in [ ] are also required, e.g.: my_program.py --path=<path> <file>... is the same as my_program.py (--path=<path> <file>...). (Note, “required options” might be not a good idea for your users).
| (pipe) mutually exclusive elements. Group them using ( ) if one of the mutually exclusive elements is required: my_program.py (--clockwise | --counter-clockwise) TIME. Group them using [ ] if none of the mutually-exclusive elements are required: my_program.py [--left | --right].
... (ellipsis) one or more elements. To specify that arbitrary number of repeating elements could be accepted, use ellipsis (...), e.g. my_program.py FILE ... means one or more FILE-s are accepted. If you want to accept zero or more elements, use brackets, e.g.: my_program.py [FILE ...]. Ellipsis works as a unary operator on the expression to the left.
[options] (case sensitive) shortcut for any options. You can use it if you want to specify that the usage pattern could be provided with any options defined below in the option-descriptions and do not want to enumerate them all in usage-pattern.
“[--]”. Double dash “--” is used by convention to separate positional arguments that can be mistaken for options. In order to support this convention add “[--]” to your usage patterns.
“[-]”. Single dash “-” is used by convention to signify that stdin is used instead of a file. To support this add “[-]” to your usage patterns. “-” acts as a normal command.
If your pattern allows to match argument-less option (a flag) several times:

Usage: my_program.py [-v | -vv | -vvv]
then number of occurrences of the option will be counted. I.e. args['-v'] will be 2 if program was invoked as my_program -vv. Same works for commands.

If your usage patterns allows to match same-named option with argument or positional argument several times, the matched arguments will be collected into a list:

Usage: my_program.py <file> <file> --path=<path>...
I.e. invoked with my_program.py file1 file2 --path=./here --path=./there the returned dict will contain args['<file>'] == ['file1', 'file2'] and args['--path'] == ['./here', './there'].

### Option descriptions format
Option descriptions consist of a list of options that you put below your usage patterns.

It is necessary to list option descriptions in order to specify:

synonymous short and long options,
if an option has an argument,
if option’s argument has a default value.
The rules are as follows:

Every line in doc that starts with - or -- (not counting spaces) is treated as an option description, e.g.:

Options:
  --verbose   # GOOD
  -o FILE     # GOOD
Other: --bad  # BAD, line does not start with dash "-"
To specify that option has an argument, put a word describing that argument after space (or equals “=” sign) as shown below. Follow either <angular-brackets> or UPPER-CASE convention for options’ arguments. You can use comma if you want to separate options. In the example below, both lines are valid, however you are recommended to stick to a single style.:

-o FILE --output=FILE       # without comma, with "=" sign
-i <file>, --input <file>   # with comma, without "=" sing
Use two spaces to separate options with their informal description:

--verbose More text.   # BAD, will be treated as if verbose option had
                       # an argument "More", so use 2 spaces instead
-q        Quit.        # GOOD
-o FILE   Output file. # GOOD
--stdout  Use stdout.  # GOOD, 2 spaces
If you want to set a default value for an option with an argument, put it into the option-description, in form [default: <my-default-value>]:

--coefficient=K  The K coefficient [default: 2.95]
--output=FILE    Output file [default: test.txt]
--directory=DIR  Some directory [default: ./]
If the option is not repeatable, the value inside [default: ...] will be interpreted as string. If it is repeatable, it will be splited into a list on whitespace:

Usage: my_program.py [--repeatable=<arg> --repeatable=<arg>]
                     [--another-repeatable=<arg>]...
                     [--not-repeatable=<arg>]

# will be ['./here', './there']
--repeatable=<arg>          [default: ./here ./there]

# will be ['./here']
--another-repeatable=<arg>  [default: ./here]

# will be './here ./there', because it is not repeatable
--not-repeatable=<arg>      [default: ./here ./there]


### Subparsers, multi-level help and huge applications (like git)
If you want to split your usage-pattern into several, implement multi-level help (with separate help-screen for each subcommand), want to interface with existing scripts that don’t use docopt, or you’re building the next “git”, you will need the new options_first parameter (described in API section above). To get you started quickly we implemented a subset of git command-line interface as an example: examples/git