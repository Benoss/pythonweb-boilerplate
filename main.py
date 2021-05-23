#!/usr/bin/env python

import glob
import os
import subprocess
from typing import List

import typer
import uvicorn

# Do not import django at the top level, better import them inside the commands
# some django commands like collectstatic need to be able to run with minimum dependencies
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "boilerplate_backend.settings.dev")

app = typer.Typer()


@app.command()
def rename_project(to_name: str, from_name: str = "boilerplate_backend", git_remote: str = None) -> None:
    """
    rename the project to a new name, you can optionally set the git remote you want to go to
    """
    to_name_underscore = to_name.replace("-", "_")
    try:
        os.rename(from_name.replace("-", "_"), to_name_underscore)
    except FileNotFoundError:
        pass

    def replace_path(filepath: str) -> None:
        with open(filepath) as file:
            s = file.read()
        s = s.replace(from_name.replace("_", "-"), to_name.replace("_", "-"))
        s = s.replace(from_name.replace("-", "_"), to_name_underscore)
        with open(filepath, "w") as file:
            file.write(s)

    for filepath in glob.iglob("./*.*", recursive=True):
        replace_path(filepath)

    for filepath in glob.iglob(f"./{to_name_underscore}/**/*.py", recursive=True):
        replace_path(filepath)

    for filepath in glob.iglob("./templates/**/*.*", recursive=True):
        replace_path(filepath)

    for filepath in glob.iglob("./static_src/**/*.*", recursive=True):
        replace_path(filepath)


def execute_from_command_line(args: List[str]) -> None:
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(args)


@app.command(context_settings={"allow_extra_args": True, "ignore_unknown_options": False})
def manage(ctx: typer.Context) -> None:
    """
    Wrapper around django manage.py command so that you have only one entrypoint
    You can still use manage.py directly
    """
    execute_from_command_line(["manage.py"] + ctx.args)


@app.command()
def release() -> None:
    """
    Generate compressed css and javascript file and will also run collectstatic
    Feel free to add more to it if needed
    """
    from django.core import management

    subprocess.call(["gulp", "prod"])
    management.call_command("collectstatic", "--no-input")


@app.command()
def update() -> None:
    """
    Update the local project, git pull, npm install, pip install
    """
    subprocess.call(["git", "pull"])
    subprocess.call(["npm", "install"])
    subprocess.call(["pip", "install", "-r", "requirements_dev.txt", "--upgrade"])


@app.command()
def web() -> None:
    """
    Run the webserver with runserver if debug and Uvicorn async if not debug
    """
    from django.conf import settings

    if settings.DEBUG and settings.SERVER_AUTO_RELOAD:
        execute_from_command_line(["runserver"])
    else:
        from asgi import app as asgi_app

        uvicorn.run(asgi_app, port=settings.SERVER_PORT, host=settings.SERVER_HOST)


if __name__ == "__main__":
    app()
