data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count = count +1 #可以寫　count += 1
		if count % 1000 == 0 #%取餘數, 如果count跟1000的餘數是0
			print(len(data)) #可以看印到哪
print(len(data))

print(data[0])
print('----------------')
print(data[1])
