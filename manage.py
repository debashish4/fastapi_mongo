import os
import sys

import click
import pytest
import uvicorn
from isort.main import iter_source_code
from isort.main import sort_imports
from isort.settings import from_path
from pylint import epylint as lint

# Append the application directory to sys.path
APP_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "app")
sys.path.append(APP_DIR)


@click.group()
def cli():
    pass

@cli.command() # run server.
def runserver():
    """
    Start the debug server using uvicorn
    """
    uvicorn.run("app.main:app",
                host="127.0.0.1",
                port=8000,
                log_level="debug",
                reload=True)

@cli.command()
def test(): # code coverage if all there is any dead code 
    """
    Unittest runner.
    """
    pytest_args = [
        "--cov=app",
        "--cov-report=term-missing",
        "--cov-fail-under=95"
    ]
    exit_code = pytest.main(pytest_args)
    raise SystemExit(exit_code.value)

@cli.command()
def pylint(): # code quality
    pylint_options = "app"
    (pylint_stdout, pylint_stderr) = lint.py_run(pylint_options, return_std=True)
    output = pylint_stdout.getvalue()
    print(output)

@cli.command()
@click.option("--check", is_flag=True)
def isort(check): # sorting headers -the imports
    """
    Run isort on all the files in app and tests directory
    """
    exit_code = 0
    config = from_path(os.getcwd()).copy()
    config["check"] = check
    file_names = iter_source_code(["app", "tests", "manage.py"], config, [])
    for file_name in file_names:
        sort_attempt = sort_imports(file_name, **config)
        if sort_attempt:
            if sort_attempt.incorrectly_sorted:
                exit_code = 1
    raise sys.exit(exit_code)

if __name__ == "__main__":
    cli()
