List = []

with open('How Your Nervous System Works & Changes  -  Huberman Lab Podcast #1 - YouTube.txt', 'rt') as file:
	for i in file.readlines():
		List.append(i.removesuffix('\n'))

print(' '.join(List))
