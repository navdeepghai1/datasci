
import click
import os
import sys

def execute_from_command_line(*args, **kwargs):

	from .commands import commands
	temp = dict()
	for command in commands:
		temp.update({command.name: command})
	group  = dict(datasci=click.group(name="datasci", commands=temp)(file_path))
	click.Group(commands=group)(prog_name='datasci')


@click.option("--file-path", default=".", help="Output file paths")
@click.option("--file-folder", default="hash", help="New folder for output files")
@click.option("--show-output", default=False, help="To show output to the user")
@click.pass_context
def file_path(ctx, file_path, file_folder, show_output):
	ctx.obj = {
		"file_path": file_path,
		"file_folder": file_folder,
		"show_output": show_output
	}



