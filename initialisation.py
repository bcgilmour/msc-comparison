import openpyxl
import 'stats.py' as s

reference = ["MSc students", "Non-Res. Staff", "Total lab size", "Personal income", "Date of last publication", "Personal interest"]

# importing input excel sheet

def xlsx_import(file_name):
	if isinstance(file_name, str):
		xlsx = openpyxl.load_workbook(file_name)
		xlsx = xlsx.active
		options = xlsx.max_column
	else:
		print "Invalid file name."
		break

# creating a dictionary of lists

def pop_dict(xlsx, options, d):
	for lab in xlsx.columns[1]:
		d.update(lab.value: [])
		for obj in xlsx.columns[2:options]:
			d[lab].append(obj.value)

# defining the selection functions
		# desired columns in a lab are accesed via d[lab][col]

class Selection(object):
	x = 2
	y = 3
	tot = 4
	inc = 5
	date = 6
	rank = 7
	intr = 8
	
	def __init__(self, d):
		self.d = d
		self.prop = []
		
	def run_prop(self):
		return s.proportion_calc(self.x, self.y, self.tot, self.d)
		return s.prop_weight(self.prop, self.d)

	def run_income(self):
		return s.max_income(self.inc)
		return s.income_weight(self.inc)

	def run_date(self):
		return s.pub_date(self.date)
		return s.pub_weight()

	def run_rank(self):
		return s.level_weight(self.rank)

	def run_interest(self):
		return s.interest_weight(self.intr)
