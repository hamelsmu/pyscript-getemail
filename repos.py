import json
from pyodide.http import open_url

def repos():
    res = json.loads(open_url("http://api.github.com/users/fastai/repos?per_page=100").read())
    for repo in res: print(repo['name'])


if __name__ == '__main__':
    repos()
