import openpyxl

xlsx = 0
options = 0
value_dict = {}
reference = ["MSc students", "Non-Res. Staff", "Total lab size", "Personal income", "Date of last pub", "Personal interest"]

# importing input excel sheet

def xlsx_import(file_name):
	if isinstance(file_name, str):
		xlsx = openpyxl.load_workbook(file_name)
		xlsx = xlsx.active
		options = xlsx.max_column
	else:
		print "Invalid file name."

# creating a dictionary of lists

def create_dict(xlsx, options):
	for lab in xlsx.columns[1]:
		value_dict.update(lab.value: [])
		for obj in xlsx.columns[2:options]:
			value_dict[lab].append(obj.value)

# defining the selection functions

class Selection(object):
	x_col = 2
	y_col = 3
	tot_col = 4
	inc_col = 5
	date_col = 6
	int_col = 7
	
	def __init__(self, value_dict):
		self.value_dict = value_dict
		self.prop = []
		
	def run_prop(self, x_col, y_col, tot_col, prop):
		return stats.proportion_calc(self.x_col, self.y_col, self.tot_col)
		return stats.prop_weight(self.prop)

	def run_income(self, inc_col):
		return stats.max_income(self.inc_col)
		return stats.income_weight(self.inc_col)

	def run_date(self, date_col):
		return stats.pub_date(self.date_col)
		return stats.pub_weight()

	def run_rank(self, rank_col):
		return stats.level_weight(self.rank_col)

	def run_interest(self, int_col):
		return stats.interest_weight(self.int_col)
