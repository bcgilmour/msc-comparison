

# add selections as lists to selection dictionary, categorise by a key string

# [ @pers_interest(0->1); @msc_viable(bool); @num_msc(n); @num_non_res(n); @lab_size(n); @rep_income(1->3,unk); @post_level(0->2); @latest_pub(date)

# intiliase all as 1:
	# increment_max = [ +.75(%); *1.25; /1.5; *1.25; +.75(%)... maybe...

# empty satistics

stat_weight = 0.25
selection = {}
incomplete = []
msc_prop = {}
adj_tot_prop = []
filler = 0
total = 0

# 1.1 average proportion of measured groups

def proportion_calc(x, y, total): # where x = students, y = non-research staff, total = lab total
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

def weight_calc(msc_prop):
	for lab in msc_prop:
		msc_prop[lab] /= adj_tot_prop[lab]
		msc_prop[lab] *= stat_weight
	return msc_prop
				    
# 2.1 income pooling
				    
def max_income(income):
	for dr in selection:
		total += dr[income]

# 2.2 income proportions & weight

def income_prop(income):
	for lab in selection:
		# msc_prop.update(lab.append(lab[income] / total)) see above
		filler = lab[income] / total
		filler *= stat_weight
		msc_prop[lab] =+ filler
	filler = 0

# 3.1 most recent pub date config

def pub_date(
