k = ('you name')
print('{}'.format(k))
u = input ('введите ваше имя :')
print('hello {}'.format(u))
u1 = input ('введите ваше друга :')
u2 = input ('введите ваше кота :')
print('я щас перечисьлю имена которые вы вписали!')
for u in (u,u1,u2):
    print(u)
else:
    print('я уже перечислил все имена которые вы ввели.')
    
