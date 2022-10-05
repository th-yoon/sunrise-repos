"""Archive GitHub repositories.

"""
from getpass import getpass
from sys import stderr
from typing import Callable, Tuple

from requests import patch, post

URL = "https://api.github.com/graphql"
VERIFY_CERT = True
ENCODING = "utf-8"


def _print_error(*args, **kwargs) -> None:
    print(*args, file=stderr, **kwargs)


def _for_all(path: str, process: Callable[[str], None]) -> None:
    with open(path, encoding=ENCODING) as file:
        for line in file:
            process(line.rstrip())

def _find_repo_id(owner: str, project_name: str, secret_token: str) -> Tuple[dict, bool, str]:
    headers = {
        "Authorization": f"token {secret_token}",
    }
    json = {
        "query": "query FindRepoID($name: String!, $owner: String!) {repository(owner: $owner, name: $name) {id, isArchived}}",
        "variables": {
            "owner": owner,
            "name": project_name,
            }
        }

    response = post(url=URL, json=json, headers=headers)
    result = response.json()
    return result, response.ok, (
        f"Status: {response.status_code}. " f'Error: "{response.text}".'
    )

def _unarchive_repository(
    owner: str, project_name: str, secret_token: str
) -> Tuple[bool, str]:
    result, status, message = _find_repo_id(owner, project_name, secret_token)  
    if not status:
        _print_error(f"{project_name}: {message}")
    repo_id = result['data']['repository']['id']

    headers = {
        "Authorization": f"token {secret_token}",
    }

    json = {
        "query": """ 
            mutation UnArchiveRepository ($mutationId: String!, $repoID: ID!) {unarchiveRepository(input:{clientMutationId:$mutationId, repositoryId:$repoID}) {repository { isArchived, description } } }
        """,
        "variables": {
            "mutationId": "true",
            "repoID": f"{repo_id}"
        }
    }

    response = post(url=URL, json=json, headers=headers, verify=VERIFY_CERT)
    return response.ok, (
        f"Status: {response.status_code}. " f'Error: "{response.text}".'
    )


def _process_repository(owner: str, repository: str, password: str) -> None:
    result, message = _unarchive_repository(owner, repository, password)

    if not result:
        _print_error(f"{repository}: {message}")


def unarchive_repositories(owner: str, csv: str) -> None:
    """Archive all repositories listed in a CSV file."""
    token = getpass(prompt="Token:")
    _for_all(csv, lambda repo: _process_repository(owner, repo, token))
