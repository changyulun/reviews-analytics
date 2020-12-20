data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count = count +1 #可以寫　count += 1
		if count % 1000 == 0: #%取餘數, 如果count跟1000的餘數是0
			print(len(data)) #可以看印到哪
print('檔案讀取完了, 總共有', len(data), '筆資料')

#該怎麼去計算一百萬筆留言的平均長度
sum_len = 0
for d in data:
	sum_len = sum_len + len(d) #一直累積
	print(sum_len)
print('留言平均長度是', sum_len/len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度小於100')
print(new[0])

