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
