# x, y, total, income, date, rank, interest

import stats

# maybe this could fit in a class?

# def create_selection():

def run_prop(x_col, y_col, tot_col, prop):
	return stats.proportion_calc(x_col, y_col, tot_col)
	return stats.prop_weight(prop)

def run_income(inc_col):
	return stats.max_income(inc_col)
	return stats.income_weight(inc_col)

def run_date(date_col):
	return stats.pub_date(date_col)
	return stats.pub_weight()

def run_rank(rank_col):
	return stats.level_weight(rank_col)

def run_interest(int_col):
	return stats.interest_weight(int_col)
