p = open('pipo7.txt', 'r')
l = p.readline()
print (l)
pop = input ('внесите изменение в файл:')
pop1 = input ('внесите изменение в файл:')
f = open('pipo7.txt', 'w')
f.write(pop)
f.write(pop1)
f.close()

