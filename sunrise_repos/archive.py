"""Archive GitHub repositories.

"""
from getpass import getpass
from sys import stderr
from typing import Callable, Tuple

from requests import patch

REST_HOST = "api.github.com"
VERIFY_CERT = True
ENCODING = "utf-8"


def _print_error(*args, **kwargs) -> None:
    print(*args, file=stderr, **kwargs)


def _for_all(path: str, process: Callable[[str], None]) -> None:
    with open(path, encoding=ENCODING) as file:
        for line in file:
            process(line.rstrip())


def _archive_repository(
    owner: str, project_name: str, secret_token: str
) -> Tuple[bool, str]:
    """Archive, i.e. write protect, a GitHub repository.

    C.f. https://developer.github.com/v3/repos/#update-a-repository.

    """
    project_settings = {"archived": "true"}

    headers = {
        "Authorization": f"token {secret_token}",
    }

    url = f"https://{REST_HOST}/repos/{owner}/{project_name}"

    response = patch(url, json=project_settings, headers=headers, verify=VERIFY_CERT)
    return response.ok, (
        f"Status: {response.status_code}. " f'Error: "{response.text}".'
    )


def _process_repository(owner: str, repository: str, password: str) -> None:
    result, message = _archive_repository(owner, repository, password)

    if not result:
        _print_error(f"{repository}: {message}")


def archive_repositories(owner: str, csv: str) -> None:
    """Archive all repositories listed in a CSV file."""
    token = getpass(prompt="Token:")
    _for_all(csv, lambda repo: _process_repository(owner, repo, token))
