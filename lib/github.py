from github import Github
from base64 import b64decode
from tqdm import tqdm


class GithubManager():
    def __init__(self, access_token):
        self.g = Github(access_token)

    def get_json_strings(self, repo_id, folder):
        '''
        Gets the json files from a folder in a Github repo.

        Arguments:
        repo_id: id of the Github repo
        folder: Folder where to look for json files

        Returns: List with the json strings found.
        '''
        repo = self.g.get_repo(repo_id)
        file_list = repo.get_contents(folder)
        json_list = [b64decode(f.content).decode('ascii') for f in tqdm(file_list) if is_json(f.download_url)]
        return json_list


def is_json(url):
    '''Checks if the url ends with json'''
    if url.endswith('.json'):
        return True
    return False
