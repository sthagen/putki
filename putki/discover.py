import pathlib
from typing import no_type_check

import yaml
from git.exc import GitCommandError, InvalidGitRepositoryError, NoSuchPathError
from git.repo import Repo


@no_type_check
def root(within: str | pathlib.Path = '.') -> str:
    """Detect the root folder for tasks."""
    try:
        repo = Repo(within, search_parent_directories=True)
        try:
            repo_root = repo.git.rev_parse(show_toplevel=True)
            start_here = pathlib.Path(repo_root)
            for name in start_here.rglob('*'):
                if name == 'tasks':
                   return str(start_here / name)
            return ''
        except GitCommandError:
            return ''
    except (InvalidGitRepositoryError, NoSuchPathError):
        return ''
