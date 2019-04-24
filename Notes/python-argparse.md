
# attrs of add_argument()
# name or flags - Either a name or a list of option strings, e.g. foo or -f, --foo.
action - The basic type of action to be taken when this argument is encountered at the command line.
# nargs - The number of command-line arguments that should be consumed.
const - A constant value required by some action and nargs selections.
default - The value produced if the argument is absent from the command line.
# type - The type to which the command-line argument should be converted.
# choices - A container of the allowable values for the argument.
required - Whether or not the command-line option may be omitted (optionals only).
# help - A brief description of what the argument does.
metavar - A name for the argument in usage messages.
## nargs
parser.add_argument("object", type=str,nargs=2)
`'+' & '*'`

## dest 
The name of the attribute to be added to the object returned by parse_args().

```python
import argparse

#
cmd_atgs_list = " add ".split()

# setup
parser = argparse.ArgumentParser()
parser.add_argument("echo")
parser.add_argument("--maybe")
# type choices action default...

# args parser
# default is sys.arg
args = parser.parse_args(cmd_atgs_list)

# handle
if args.echo:
    print(args.echo)

```



class argparse.ArgumentParser(prog=None, usage=None, description=None, epilog=None, parents=[], formatter_class=argparse.HelpFormatter, prefix_chars='-', fromfile_prefix_chars=None, argument_default=None, conflict_handler='error', add_help=True, allow_abbrev=True)
Create a new ArgumentParser object. All parameters should be passed as keyword arguments. Each parameter has its own more detailed description below, but in short they are:

prog - The name of the program (default: sys.argv[0])
usage - The string describing the program usage (default: generated from arguments added to parser)
description - Text to display before the argument help (default: none)
epilog - Text to display after the argument help (default: none)
parents - A list of ArgumentParser objects whose arguments should also be included
formatter_class - A class for customizing the help output
prefix_chars - The set of characters that prefix optional arguments (default: ‘-‘)
fromfile_prefix_chars - The set of characters that prefix files from which additional arguments should be read (default: None)
argument_default - The global default value for arguments (default: None)
conflict_handler - The strategy for resolving conflicting optionals (usually unnecessary)
add_help - Add a -h/--help option to the parser (default: True)
allow_abbrev - Allows long options to be abbreviated if the abbreviation is unambiguous. (default: True)


# add_subparsers
```python
import argparse


# create the top-level parser
parser = argparse.ArgumentParser()
parser.add_argument('--foo', action='store_true', help='foo help')
subparsers = parser.add_subparsers(help='sub-command help',dest='dest test')

# create the parser for the "a" command
parser_a = subparsers.add_parser('a', help='a help')
parser_a.add_argument('bar', type=int, help='bar help')

# create the parser for the "b" command
parser_b = subparsers.add_parser('b', help='b help')
parser_b.add_argument('--baz', choices='XYZ', help='baz help')


if __name__ == '__main__':
    parser.parse_args()
    # # parse some argument lists
    # parser.parse_args(['a', '12'])

    # parser.parse_args(['--foo', 'b', '--baz', 'Z'])
```