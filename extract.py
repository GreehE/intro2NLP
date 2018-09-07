'''
题目：给一个语料，做个wordlist，并取出频率最高前10和频率最低的前10个word分别将其与频数打印出来
----------------------------------------------------------------------------------------
策略：
正则表达式提取，放入字典，对字典按照值进行排序
----------------------------------------------------------------------------------------
存在问题：
Traceback (most recent call last):
  File "extract.py", line 5, in <module>
    text = f.read();
UnicodeDecodeError: 'gbk' codec can't decode byte 0x99 in position 585: illegal multibyte sequence
----------------------------------------------------------------------------------------
设置errors = “ignore”能够解决但仍有疑问
'''
import re

for k in range(1, 6):
	with open(str(k)+".txt", encoding = "gbk", errors = "ignore") as f:
		text = f.read();
		it = re.finditer(r'\w+', text);
		dict = {};
		for match in it:
			if (dict.__contains__(match.group())):
				dict[match.group()] += 1;
			else:
				dict[match.group()] = 1;
	sorted_dict = sorted(dict.items(), key = lambda e:e[1], reverse = True);
	i = 0;
	print("#"+str(k)+":");
	print("freq*\tword");
	print("-----\t-----");
	for key in sorted_dict:
		print(str(key[1])+"\t"+key[0]);
		i += 1;
		if (i == 10):
			break;
	print("");

