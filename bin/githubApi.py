#! python
import requests
import fire
# from clara import ThirdShell

# code
# functions or classes


class githubApi():

    def __init__(self, username='ZX1209', password='dont sync this'):
        """githubApi
        githubApi.py --username=ZX1209 --password=replacethis login
        """
        self.username = username
        self.password = password
        if self.password == 'dont sync this':
            print('init the class with username and password')

    def apiInfo(self):
        """apiInfo
        """
        response = requests.get('https://api.github.com')
        return response.json()

    def login(self):
        """login
        """
        response = requests.get('https://api.github.com/user',
                                auth=(self.username, self.password))

        return response.json()

    def createRepo(self, repoName: str = None):
        """createRepo
        """
        if repoName is None:
            print('use dir name for repoName')
            from pathlib import Path

            curDir = Path().cwd()
            repoName = curDir.name

        response = requests.post('https://api.github.com/user/repos',
                                 json={
                                     'name': repoName,
                                     'description': 'auto created by github api'
                                 },
                                 auth=(self.username, self.password))

        return response.json()

    def deleteRepo(self, repoName='None'):
        """deleteRepo
        """
        response = requests.delete(
            f'https://api.github.com/repos/ZX1209/{repoName}',
            auth=(self.username, self.password))

        return response.status_code

    # not done yet
    # def initDir(self):
    #     """initDir
    #     """

    #     # issue: repoName is a full path not a file name
    #     repoName = str(curDir)
    #     readMeFile = curDir / 'ReadMe.md'
    #     readMeFile.touch()

    #     self.createRepo(repoName)

    #     ThirdShell.runCmdStrs([
    #         "git init", "git add ReadMe.md", "git commit -m 'init a repo'",
    #         f"git remote add origin https://github.com/ZX1209/{repoName}",
    #         "git push -u origin master"
    #     ])


if __name__ == '__main__':
    fire.Fire(githubApi)

# command arguments
# --title="this is title"

# str
# '"str"'

# dic
# '{"key":"val"}'

# todo: how to use it???? why use it?
