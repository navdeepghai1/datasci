'''
	Developer Navdeep
	Email navdeepghai1@gmail.com
'''
import os

def validate_execution_path():
	return True if "datasci" in os.listdir() and  "env" in os.listdir() else False

def is_root_user():
	return True if os.getuid() == 0 else False
		
	
