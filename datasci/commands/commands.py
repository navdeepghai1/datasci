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
	print(ctx.obj)
	subprocess.call(["ls", "-lrt"])




commands = [test]
