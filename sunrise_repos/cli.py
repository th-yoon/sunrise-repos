"""Handle command line arguments.

"""
import click

from sunset_repos.archive import archive_repositories


@click.command()
@click.version_option()
@click.argument("owner")
@click.argument("csv")
def cli(owner: str, csv: str) -> None:
    """A tool for archiving GitHub repositories."""
    archive_repositories(owner, csv)
