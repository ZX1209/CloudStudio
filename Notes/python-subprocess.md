# not default run as a shell
You need to supply shell=True to execute the command through a shell interpreter. If you do that however, you can no longer supply a list as the first argument, because the arguments will get quoted then. Instead, specify the raw commandline as you want it to be passed to the shell:

 proc = subprocess.Popen('ls *.bc', shell=True,
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE)

# shlex.split(cmd_str)

subprocess.run("ls -l".split(),capture_output=True)

# subprocess.run
subprocess.run(args, *, stdin=None, input=None, stdout=None, stderr=None, capture_output=False, shell=False, cwd=None, timeout=None, check=False, encoding=None, errors=None, text=None, env=None)
Run the command described by args. Wait for command to complete, then return a CompletedProcess instance.

The arguments shown above are merely the most common ones, described below in Frequently Used Arguments (hence the use of keyword-only notation in the abbreviated signature). The full function signature is largely the same as that of the Popen constructor - most of the arguments to this function are passed through to that interface. (timeout, input, check, and capture_output are not.)

If capture_output is true, stdout and stderr will be captured. When used, the internal Popen object is automatically created with stdout=PIPE and stderr=PIPE. The stdout and stderr arguments may not be used as well.

The timeout argument is passed to Popen.communicate(). If the timeout expires, the child process will be killed and waited for. The TimeoutExpired exception will be re-raised after the child process has terminated.

The input argument is passed to Popen.communicate() and thus to the subprocess’s stdin. If used it must be a byte sequence, or a string if encoding or errors is specified or text is true. When used, the internal Popen object is automatically created with stdin=PIPE, and the stdin argument may not be used as well.

If check is true, and the process exits with a non-zero exit code, a CalledProcessError exception will be raised. Attributes of that exception hold the arguments, the exit code, and stdout and stderr if they were captured.

If encoding or errors are specified, or text is true, file objects for stdin, stdout and stderr are opened in text mode using the specified encoding and errors or the io.TextIOWrapper default. The universal_newlines argument is equivalent to text and is provided for backwards compatibility. By default, file objects are opened in binary mode.

If env is not None, it must be a mapping that defines the environment variables for the new process; these are used instead of the default behavior of inheriting the current process’ environment. It is passed directly to Popen.

Examples:

```py
>>> subprocess.run(["ls", "-l"])  # doesn't capture output , output will show on the current terminal
CompletedProcess(args=['ls', '-l'], returncode=0)

>>> subprocess.run("exit 1", shell=True, check=True)
Traceback (most recent call last):
  ...
subprocess.CalledProcessError: Command 'exit 1' returned non-zero exit status 1

>>> subprocess.run(["ls", "-l", "/dev/null"], capture_output=True)
CompletedProcess(args=['ls', '-l', '/dev/null'], returncode=0,
stdout=b'crw-rw-rw- 1 root root 1, 3 Jan 23 16:23 /dev/null\n', stderr=b'')

```


# class subprocess.CompletedProcess
The return value from run(), representing a process that has finished.

## args
The arguments used to launch the process. This may be a list or a string.

## returncode
Exit status of the child process. Typically, an exit status of 0 indicates that it ran successfully.

A negative value -N indicates that the child was terminated by signal N (POSIX only).

## stdout
Captured stdout from the child process. A bytes sequence, or a string if run() was called with an encoding, errors, or text=True. None if stdout was not captured.

If you ran the process with stderr=subprocess.STDOUT, stdout and stderr will be combined in this attribute, and stderr will be None.

## stderr
Captured stderr from the child process. A bytes sequence, or a string if run() was called with an encoding, errors, or text=True. None if stderr was not captured.

## check_returncode()
If returncode is non-zero, raise a CalledProcessError.

New in version 3.5.