import 'initialisation.py' as i

# importing data

def define(file, name):
	i.xlsx_import(file)
	d = i.pop_dict(xlsx, options)
	name = i.Selection(d)
	run_stats(name)
	print(name.prop)

def run_stats(name):
	name.run_prop()
	name.run_income()
	name.run_date()
	name.run_rank()
	name.run_interest()
