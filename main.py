import click
from store import readfromJSON, writetoJSON
from todo import Todo

@click.group()         
def cli():
    """My CLI tools"""
    pass

@cli.command()
def add():
    """you dont need a parameter to input in this command just\'main add\'"""
    Todo.add()
    writetoJSON()

@cli.command()
def show():
    """you dont need a parameter to input in this command just \'main show\' """
    Todo.show()
    writetoJSON()


@cli.command()
def delete():
    """you dont need a parameter to input in this command just \'main delete\' """
    Todo.delete_task()
    writetoJSON()

@cli.command()
def markdone():
    """\'main markdone\'"""
    Todo.mark_done()
    writetoJSON()

@cli.command()
def insert():
    """\'main insert\'"""
    Todo.insert_task()
    writetoJSON()

if __name__ == '__main__':
    readfromJSON()
    cli()        # ← Just call the group
