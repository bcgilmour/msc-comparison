

# add selections as lists to selection dictionary, categorise by a key string

# [ @pers_interest(0->1); @msc_viable(bool); @num_msc(n); @num_non_res(n); @lab_size(n); @rep_income(1->3,unk); @post_level(0->2); @latest_pub(date)

# intiliase all as 1:
	# increment_max = [ +.75(%); *1.25; /1.5; *1.25; +.75(%)... maybe...

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

selection = {}
incomplete = []
msc_prop = {}
adj_tot_prop = []

# 1.1 average proportion of measured groups

def proportion_calc(x, y, total): # where x = students col, y = non-research staff col, total = lab total col
	avg = 0
	for lab in selection:
		# non_res_prop.append(i[y]) 	why is this here...
		if lab[x] != None:
			avg += (lab[x] / lab[total])
			msc_prop.update(lab:(lab[x] / lab[total]))
			# or msc_prop.update(lab.append(lab[x] / lab[total])) if it creates a list?
			adj_tot_prop.append(1- lab[y])
		else:
			incomplete.append(lab)

# 1.2 total class compositions & weight

def prop_weight(msc_prop):
	for lab in msc_prop:
		msc_prop[lab] /= adj_tot_prop[lab]
		msc_prop[lab] *= stat_weight
	return msc_prop
				    
# 2.1 income pooling
				    
def max_income(income):
	for dr in selection:
		total += dr[income]

# 2.2 income proportions & weight

def income_weight(income):
	for lab in selection:
		# msc_prop.update(lab.append(lab[income] / total)) see above
		filler = lab[income] / total
		filler *= stat_weight
		msc_prop[lab] += filler
		filler = 0

# 3.1 data conversion of recent pub date

def pub_date(date): # assuming date is stored in the format yy/mm or yy.mm
	year = int(lab[date[0:2]])
	month = int(lab[date[3:]])

# 3.2 weight of recent publication data
	
def pub_weight():	
	for lab in selection: 
		year = year - curr_year
		month = abs(month - curr_month)
		year *= year_weight
		month *= month_weight
		msc_prop[lab] += year, month
		
# 4.1 post level of academic

def level_weight(rank):
	for lab in selection:
		if lower(rank) == "professor":
			msc_prop[lab] += stat_weight
		elif lower(rank) == "assistant professor":
			msc_prop[lab] += 0.20
		else:
			msc_prop[lab] += 0.10
			

# 5.1 adding personal interest
		
def interest_weight(interest):
	for lab in selection:
		filler = lab[interest] * stat_weight
		msc_prop[lab] += filler
		filler = 0

		
