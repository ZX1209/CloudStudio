import subprocess
import shlex

# todo: test?

# note: usage runCmdStrs


def runCmdStr(cmdstr, capture_output=False, **args):
    """
    cmdstr: str
    """
    return subprocess.run(shlex.split(cmdstr), capture_output=capture_output, **args)


def runCmdStrs(cmdstrs, capture_output=False, **args):
    """
    cmds is like
    [
        "ls -l",
        "pwd"
    ]
    """
    rs = []
    for cmdstr in cmdstrs:
        r = subprocess.run(shlex.split(cmdstr),
                           capture_output=capture_output, **args)
        rs.append(r)
    return rs


def runCmdTrains(cmdstrs, capture_output=False, **args):
    """
    cmds is like
    [
        "ls -l",
        "pwd"
    ]
    """
    rs = []
    for cmdstr in cmdstrs:
        r = subprocess.run(shlex.split(cmdstr),
                           capture_output=capture_output, **args)
        if r.returncode != 0:
            break
        rs.append(r)
    return rs

# def startTrain(cmds):
#     for cmd in cmds:
#         tmp = subprocess.run(cmd)
#         if tmp.returncode != 0:
#             break


# utilities
def NoInternetConnected():
    """
    1 for not connected
    0 for connected
    """
    cp = subprocess.run(["ping", "-c", "1", "1.1.1.1"], capture_output=False)
    return cp.returncode
