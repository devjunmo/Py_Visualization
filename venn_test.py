import venn
import random
import matplotlib.pyplot as plt


# set1 = set(random.sample(range(1, 50), 30))
# set2 = set(random.sample(range(1, 50), 30))
# set3 = set(random.sample(range(1, 50), 30))
# set4 = set(random.sample(range(1, 50), 30))
# set5 = set(random.sample(range(1, 50), 30))


# chr pos ref alt

test1 = {(1, 100, 'A', 'T'), (3, 200, 'AAA', 'T'), (10, 1000, 'GC', 'C'), (15, 700, 'GGGG', 'T')}
test2 = {(5, 100, 'A', 'T'), (3, 200, 'AAA', 'T'), (10, 1000, 'GC', 'C'), (19, 700, 'GG', 'TT')}
test3 = {(9, 200, 'AA', 'GT'), (18, 2000, 'TTT', 'T'), (10, 1000, 'GC', 'C'), (20, 200, 'GGGG', 'T')}
test4 = {(9, 200, 'AA', 'GT'), (3, 200, 'AAA', 'T'), (10, 1000, 'GC', 'C'), (15, 700, 'GGGG', 'T')}
test5 = {(7, 1000, 'G', 'T'), (10, 500, 'G', 'C'), (10, 1000, 'GC', 'C'), (19, 700, 'GG', 'TT')}


# test1




labels = venn.get_labels([test1, test2, test3, test4, test5], fill=['number']) # set으로 받아야함. list안됨

venn.venn3(labels, names=['test1', 'test2', 'test3', 'test4', 'test5'])

plt.show()




# test1&test2&test3 # 교집합 연산