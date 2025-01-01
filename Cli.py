import click
import os
from classes.Repository import Repository

@click.group()
def cli():
    """
    Command-line interface for the wit version control system.
    """

@cli.command()
@click.option('--path', default=None, type=str, help='Path to initialize the repository')
@click.argument('user', required=False, default="default_user")
def init(path, user):
    """
    Initialize a new repository.
    """
    try:
        path = path or os.getcwd()
        repo = Repository(path, user)
        repo.wit_init()
        click.echo(f"Repository initialized at {path} for user {user}.")
    except Exception as e:
        click.echo(f"Error: {e}")


@cli.command()
@click.option('--path', default=None, type=str, help='Path to the repository')
@click.argument('file_names', nargs=-1)  # Allow multiple arguments
def add(path, file_names):
    """
    Add multiple files to the staging area.
    """
    path = path or os.getcwd()
    repo = Repository(path, "default_user")
    for file_name in file_names:
            try:
                status=repo.wit_add(file_name)
                if status:
                 click.echo(f"File '{file_name}' added to staging area.")
            except Exception as e:
                click.echo(f"Error adding '{file_name}': {e}")


@click.option('--message', '--m', required=True, type=str, help='Commit message')
@cli.command()
#@click.option('--path', default=None, type=str, help='Path to the repository')
@click.option('--message', required=True, type=str, help='Commit message')
def commit(message):
    """
    Commit changes with a message.
    """
    try:
        path =   os.getcwd()
        repo = Repository(path, "default_user")
        success = repo.wit_commit(message)
        if success:
           click.echo(f"Commit created with message: {message}")
    except Exception as e:
        click.echo(f"Error: {e}")


@cli.command()
@click.option('--path', default=None, type=str, help='Path to the repository')
def log(path):
    """
    Display the commit log.
    """
    try:
        path = path or os.getcwd()
        repo = Repository(path, "default_user")
        logs = repo.wit_log()
        click.echo(f"Commit logs:\n{logs}")
    except Exception as e:
        click.echo(f"Error: {e}")


@cli.command()
@click.option('--path', default=None, type=str, help='Path to the repository')
def status(path):
    """
    Show the status of the repository.
    """
    try:
        path = path or os.getcwd()
        repo = Repository(path, "default_user")
        changes, staged = repo.wit_status()
        click.echo(f"Changes not staged for commit: {changes}")
        click.echo(f"Staged files: {staged}")
    except Exception as e:
        click.echo(f"Error: {e}")


@cli.command()
@click.option('--path', default=None, type=str, help='Path to the repository')
@click.argument('commit_id', type=str)
def checkout(path, commit_id):
    """
    Checkout a specific commit.
    """
    try:
        path = path or os.getcwd()
        repo = Repository(path, "default_user")
        success = repo.wit_checkout(commit_id)
        print(success)
        if success:
            click.echo(f"Checked out to commit {commit_id}.")
        else:
            click.echo(f"Error: Commit ID {commit_id} not found or checkout failed.")
    except Exception as e:
        click.echo(f"Error: {e}")


if __name__ == "__main__":
      cli()