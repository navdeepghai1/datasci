'''
	Developer Navdeep
	Email navdeepghai1@gmail.com
'''

import click
import sys
import os
import subprocess

@click.command("test")
@click.option("--test", default=1, help="Testing")
@click.pass_context
def test(ctx, test):
	click.secho("Commands are working are fine!, You're ready to go", fg="white")
	


@click.command("compare-files")
@click.option("--file1", default=None, help="File1 Name with complete path")
@click.option("--file2", default=None, help="File2 Name with complete path")
@click.pass_context
def compare_files(ctx, file1, file2):
	if not file1  and file2:
		click.secho("Required two files.", fg="yellow")
		return
	from datasci.operations.base import compare_files as _compare
	_compare(file1, file2, {})



commands = [test, compare_files]
