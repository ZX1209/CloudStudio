#! python
import requests
import fire
from clara import ThirdShell
from pathlib import Path

curDir = Path().cwd()
filePath = Path().absolute()
fileDir = filePath.parent

# code
# functions or classes

username = 'ZX1209'
passward = 'dont sync this'  # dont sync passward


def apiInfo():
    """apiInfo
    """
    response = requests.get('https://api.github.com')
    return response.json()


def login():
    """login
    """
    response = requests.get('https://api.github.com/user',
                            auth=(username, passward))

    return response.json()


def createRepo(repoName: str = None):
    """createRepo
    """
    if repoName is None:
        print('use dir name for repoName')
        repoName = curDir.name
    response = requests.post('https://api.github.com/user/repos',
                             json={
                                 'name': repoName,
                                 'description': 'auto created by github api'
                             },
                             auth=(username, passward))

    return response.json()


def deleteRepo(repoName='None'):
    """deleteRepo
    """
    response = requests.delete(
        f'https://api.github.com/repos/ZX1209/{repoName}',
        auth=(username, passward))

    return response.status_code


def initDir():
    """initDir
    """

    # issue: repoName is a full path not a file name
    repoName = str(curDir)
    readMeFile = curDir / 'ReadMe.md'
    readMeFile.touch()

    createRepo(repoName)

    ThirdShell.runCmdStrs([
        "git init", "git add ReadMe.md", "git commit -m 'init a repo'",
        f"git remote add origin https://github.com/ZX1209/{repoName}",
        "git push -u origin master"
    ])


if __name__ == '__main__':
    if passward == 'dont sync this':
        print('need username and passward to login')
    fire.Fire()

# command arguments
# --title="this is title"

# str
# '"str"'

# dic
# '{"key":"val"}'

# todo: how to use it???? why use it?
