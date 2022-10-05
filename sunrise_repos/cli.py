"""Handle command line arguments.

"""
import click

from sunrise_repos.unarchive import unarchive_repositories


@click.command()
@click.version_option()
@click.argument("owner")
@click.argument("csv")
def cli(owner: str, csv: str) -> None:
    """A tool for archiving GitHub repositories."""
    unarchive_repositories(owner, csv)

if __name__ == '__main__':
    cli()
