
import numpy as np
import time
import matplotlib.pyplot as plt
import pandas as pd


def run():
	insert_time, merge_time, select_time, input_size = [], [], [], []
	start, stop, step = 1, 20, 1

	for i in range(start, stop, step):
		# create input dataset
		arr = np.arange(0, i)
		np.random.shuffle(arr)
		input_size.append(len(arr))

		time1 = time.time()
		# run insert-sort algorithm
		#insert_sort(arr)
		bogosort(arr)
		time2 = time.time()
		# run merge-sort algorithm
		#merge_sort(arr)
		time3 = time.time()
		# run select-sort algorithm
		#select_sort(list(arr))
		time4 = time.time()

		insert_time.append(time2 - time1)
		merge_time.append(time3 - time2)
		select_time.append(time4 - time3)

		# show progress
		print("{}/{} --> {}%".format(i, stop, int((i - start)*100/(stop-start))))

	# show final results
	print("Total time insert:{} | merge:{}  |   select:{} ".format(sum(insert_time), sum(merge_time), sum(select_time)))
	a = pd.DataFrame({'Input': input_size, 'Merge Sort': merge_time, 'Insert Sort': insert_time, 'Select Sort': select_time})
	a.to_csv('res.csv')

	# plot results
	show_graph(input_size, insert_time, merge_time, select_time)


def insert_sort(x):
	ordered_list = []
	first = True
	for i in x:
		if first:  # list is empty. Insert first value
			ordered_list.insert(0, i)
			first = False
		else:
			# iterate over ordered list to find the lowest value greater than the one to insert
			for j in range(len(ordered_list)):
				if ordered_list[j] > i:
					ordered_list.insert(j, i)
					break  # do not continue evaluating values
				elif j == len(ordered_list) - 1:
					# if the end of the list has been reached, insert value
					ordered_list.append(i)


def merge_sort(x):
	# divide list in two slices
	l1, l2 = x[:int(len(x)/2)], x[int(len(x)/2):]

	# input is a single value, thus it is already sorted
	if len(l1) == 0:
		return l2

	# merge-sort each sub-list (recurse)
	l1 = merge_sort(l1)
	l2 = merge_sort(l2)

	# merge sub-ordered lists
	return merge(l1, l2)


def merge(l1, l2):
	pointer1, pointer2 = 0, 0
	ordered_list = []
	while True:
		if l1[pointer1] > l2[pointer2]:  # insert greatest value and move pointer
			ordered_list.append(l2[pointer2])
			pointer2 += 1
		else:
			ordered_list.append(l1[pointer1])
			pointer1 += 1

		if pointer1 == len(l1):  # pointer has reached end of list
			ordered_list.extend(l2[pointer2:])
			break
		if pointer2 == len(l2):
			ordered_list.extend(l1[pointer1:])
			break
	return ordered_list


def select_sort(x):
	sorted_list = []
	while len(x) > 0:
		for i in range(len(x)):
			if x[i] == min(x):
				sorted_list.append(x.pop(i))
				break
	return sorted_list


def bogosort(x):
	while not is_sorted(x):
		np.random.shuffle(x)


def is_sorted(x):
	for i in range(len(x) - 1):
		if x[i] > x[i + 1]:
			return False
	return True


def show_graph(input_size, y1, y2=None, y3=None):
	insert_graph, = plt.plot(input_size, y1, label='Insert-Sort')
	legend_list = [insert_graph]
	if y2 is not None:
		merge_graph, = plt.plot(input_size, y2, label='Merge-Sort')
		legend_list.append(merge_graph)
	if y3 is not None:
		select_graph, = plt.plot(input_size, y3, label='Select-Sort')
		legend_list.append(select_graph)

	plt.legend(handles=legend_list)

	plt.xlabel('Input size')
	plt.ylabel('Execution time')
	plt.show()


if __name__ == "__main__":
	run()
