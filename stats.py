selection = {}

# add selections as lists to selection dictionary, categorise by a key string

# [ @pers_interest(0->1); @msc_viable(bool); @num_msc(n); @num_non_res(n); @lab_size(n); @rep_income(1->3,unk); @post_level(0->2); @latest_pub(date)

# intiliase all as 1:
	# increment_max = [ +.75(%); *1.25; /1.5; *1.25; +.75(%)...

# empty satistic variables

incomplete = []
msc_prop = {}
adj_tot_prop = []

# 1.1 average proportion of measured groups

def proportion_calc(x, y, total):
	avg = 0
	n = 0
	for i in selection:
		non_res_prop.append(i[y]
		if i[x] != None:
			avg += (i[x] / i[total])
			msc_prop.update(i:(i[x] / i[total]))
			adj_tot_prop.append(1- i[y])
			n += 1
		else:
			incomplete.append(i)

# 1.2 total class compositions & final weight

def weight_calc(msc_prop):
	for i in msc_prop:
		msc_prop[i] /= adj_tot_prop[i]
		msc_prop[i] *= 0.25
	return msc_prop
				    
# 2 personal income comparison (pure)
				    
def reported_income(prop):
	total = 0
	for i in selection:
		total += i[prop]
