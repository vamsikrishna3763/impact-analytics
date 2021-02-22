cardboards = [(1, 5, 10), (4, 6, 8), (10, 15, 10), (11, 12, 8)]


def get_dropping_points(cardboards):
	output = []
	processes_sets = []
	ind = 0

	while ind < len(cardboards) - 1: 

		rec = cardboards[ind]

		if not output:
			output.append((rec[0], rec[-1]))
			prev_range = range(rec[0], rec[1] + 1)
			prev_top = rec[-1]
			processes_sets.append((set(prev_range), prev_top))
			ind += 1
			continue

		cur_range = range(rec[0], rec[1] + 1)
		cur_top = rec[-1]

		if cur_range[0] - prev_range[-1] > 0:
			prev_top = 0
			prev_range = range(prev_range[-1], cur_range[0]+1)
			output.append((prev_range[0], prev_top))
			processes_sets.append((set(cur_range), prev_top))
			continue

		if prev_top != cur_top:
			common = list(set(prev_range).intersection(set(cur_range)))
			if common:
					output.append((common[-1], cur_top))
					processes_sets.append((set(cur_range), cur_top))
					prev_range = cur_range
					prev_top = cur_top
					ind += 1
					continue

		if prev_range[-1] == cur_range[0]:
			output.append((cur_range[0], prev_top))
			processes_sets.append((set(cur_range), prev_top))
			ind += 1
			continue
	if ind == len(cardboards)-1:
		rec = cardboards[ind]
		
		if any([set(range(rec[0], rec[1] + 1)).issubset(x[0])] for x in processes_sets):
			try:
				cardboards[ind+1]
			except:
				prev_top = 0

			output.append((prev_range[-1], prev_top))

	return output


print(get_dropping_points(cardboards))