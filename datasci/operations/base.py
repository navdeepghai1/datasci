'''
	Developer Navdeep
	Email navdeepghai1@gmail.com
'''

import pandas
import os
from functools import wraps
from click import secho

# Entry point to apply some validation  for file
def process_file(func):
	@wraps(func)
	def wrapper_func(filename, *args, **kwargs):
		if not os.path.exists(filename):
			secho("File %s doesn't exits."%(filename), fg="red")
			raise FileNotFoundError
		secho("Processing files", fg="green")
		fileobj = pandas.read_excel(filename)
		headers  = get_headers(fileobj)
		kwargs.update({"filename":filename, "headers": headers, "fileobj": fileobj})
		func(*args, **kwargs)
	
	def get_headers(fileobj):
		return fileobj.columns.tolist()
	def get_contents(file_obj):
		pass
	return wrapper_func


def compare_files(file1, file2, options):
	if not file1 and file2:
		secho("Required two files to be compare.", fg="red")
		return
	content_file_one = read_excel_file(file1)
	content_file_second = read_excel_file(file2)


# Comparision between two files
@process_file
def read_excel_file(filename, headers, fileobj):
	print(filename)
	print(headers)
	
