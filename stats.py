selection = {}

# add selections as lists to selection dictionary, categorise by a key string

# [ @pers_interest(0->1); @msc_viable(bool); @num_msc(n); @num_non_res(n); @lab_size(n); @rep_income(1->3,unk); @post_level(0->2); @latest_pub(date)

# intiliase all as 1:
	# increment_max = [ +.75(%); *1.25; /1.5; *1.25; +.75(%)...

# empty satistic variables

incomplete = []
avg_prop_msc = 0
msc_prop = {}
adj_tot_prop = []

# average proportion of measured groups

def prop_msc(part, counter, total):
	avg = 0
	n = 0
	for i in selection:
		non_res_prop.append(i[counter]
		if i[part] != None:
			average += (i[part] / i[total])
			msc_prop.update(i:(i[part] / i[total]))
			adj_tot_prop.append(1- i[counter])
			n += 1
		else:
			incomplete.append(i)
		avg_prop_msc = average / n

# total class compositions & final weight

def class_tot_weights(msc_prop):
	for i in msc_prop:
		msc_prop[i] /= adj_tot_prop[i]
		msc_prop[i] *= 0.25
	return msc_prop

