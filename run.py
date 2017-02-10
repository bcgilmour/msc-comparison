import 'initialisation.py' as i

d = {}
xlsx = 0
options = 0

# importing data

def define(file, name):
	i.xlsx_import(file)
	d = i.pop_dict(xlsx, options, d)
	name = i.Selection(d)
	run_stats(name)
	print(name.prop)

def run_stats(name):
	name.run_prop()
	name.run_income()
	name.run_date()
	name.run_rank()
	name.run_interest()

def reset():
	d = {}
	xlsx = 0
	options = 0
