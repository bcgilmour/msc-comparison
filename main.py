import "run.py" as r

file_name = 0

def execute():
	file_name = str(input("What file would you like to analyse?: "))
	r.define(file_name)
	r.reset()
	file_name = 0
