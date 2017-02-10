# current date

import datetime
date = str(datetime.date.today())
curr_year = int(date[2:4])
curr_month = int(date[5:7])

# empty satistics

stat_weight = 0.25
year_weight = 0.2
month_weight = 0.05
filler = 0
total = 0
year = 0
month = 0

# empty lists and dictionaries

incomplete = []
adj_tot_prop = []

# 1.1 average proportion of measured groups

def proportion_calc(x, y, tot, d, prop): # where x = students col, y = non-research staff col, total = lab total col
	for lab in d:
		if d[lab][x] != None:
			prop.update(lab:(lab[x] / lab[total]))
			adj_tot_prop.append(1 - lab[y])
		else:
			incomplete.append(lab)

# 1.2 total class compositions & weight

def prop_weight(prop):
	for lab in prop:
		prop[lab] /= adj_tot_prop[lab]
		prop[lab] *= stat_weight
	return prop
				    
# 2.1 income pooling
				    
def max_income(inc, d):
	for lab in d:
		total += lab[inc]

# 2.2 income proportions & weight

def income_weight(inc, d):
	for lab in d:
		filler = lab[income] / total
		filler *= stat_weight
		prop[lab] += filler
		filler = 0

# 3.1 data conversion of recent pub date

def pub_date(date): # assuming date is stored in the format yy/mm or yy.mm
	year = int(lab[date[0:2]])
	month = int(lab[date[3:]])

# 3.2 weight of recent publication data
	
def pub_weight(d):	
	for lab in d: 
		year = year - curr_year
		month = abs(month - curr_month)
		year *= year_weight
		month *= month_weight
		prop[lab] += year, month
		
# 4.1 post level of academic

def level_weight(rank, d):
	for lab in d:
		if lower(rank) == "professor":
			prop[lab] += stat_weight
		elif lower(rank) == "assistant professor":
			prop[lab] += 0.20
		else:
			prop[lab] += 0.10			

# 5.1 adding personal interest
		
def interest_weight(intr, d):
	for lab in d:
		filler = lab[intr] * stat_weight
		prop[lab] += filler
		filler = 0
		
# 6.1 incomplete lab entries

def incomplete():
	print("The following labs are incomplete:")
	for lab in range(0, len(incomplete - 1)):
		print(incomplete[lab])
