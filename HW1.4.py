# HPM 573 Advanced Topics in Modeling Health Care Decisions Spring 2018 #
# Tommy Thornhill #
# Assignment: HW1.4 #
yours = ['Yale', 'MIT', 'Berkeley']
mine = ['St. Johns','Deep Springs', 'Black Mountain']

ours1 = mine + yours
print ours1

ours2 = []
ours2.append(mine)
ours2.append(yours)
print ours2


# The '+' concatenates the two lists into a single new list.#
# The "append" function does not create a new list but instead is a list of the appended lists.#

yours [1]= 'Harvard'

print ours1
print ours2
print ours3

# Ours1 is not modified because it is immutable.#
# Ours2 is modified because it is function that brings the two lists together, one of which has been modified.#
