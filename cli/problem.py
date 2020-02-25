import click
from core.problem import create_problem, get_problem_list
from core.util import login_session


@click.group()
def problem():
    '''
    functions about problem
    '''


@problem.command()
@click.option(
    '--name',
    '-n',
    help='problem name',
)
@click.pass_obj
def create(ctx_obj, name):
    '''
    create a problem
    '''
    with login_session(**ctx_obj['user']) as sess:
        create_problem(
            sess,
            problem_name=name,
        )