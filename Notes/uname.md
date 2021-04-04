```zsh
# Print all system information
uname -a
# Linux system-hostname 3.2.0-4-amd64 #1 SMP Debian 3.2.32-1 x86_64 GNU/Linux

# Print the hostname
uname -n
# system-hostname

# Print the kernel release
uname -r
# 3.2.0-4-amd64

# Print the kernel version, with more specific information
uname -v
# #1 SMP Debian 3.2.32-1

# Print the hardware instruction set
uname -m
# x86_64

# Print the kernel name
uname -s
# Linux

# Print the operating system
uname -o
# GNU/Linux
```


# uname

> Print details about the current machine and the operating system running on it.
> Note: for additional information about the operating system, try the `lsb_release` command.

- Print hardware-related information: machine and processor:

`uname -mp`

- Print software-related information: operating system, release number, and version:

`uname -srv`

- Print the nodename (hostname) of the system:

`uname -n`

- Print all available system information (hardware, software, nodename):

`uname -a`
