data = []
count = 0
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
		count += 1 #等同於 count = count + 1
		if count % 1000 == 0: #count除以100000的餘數等於0
			print(len(data))
print('讀完了總共有',len(data),'筆資料')

sum_len = 0
with open('reviews.txt','r') as f:
	for d in f:
		sum_len = sum_len + len(d)
print('全部留言的平均長度:',sum_len / len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('留言長度小於100的留言總共有：',len(new),'筆')
print(new[0])