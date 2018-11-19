import re

happy_pattern = r'[:;][)D*\]}]|[(*c\[][:;]'
sad_pattern = r'[:;][(\[{c]|[\]D)][:;]'
data = input()

happy_index = len(re.findall(happy_pattern, data))
sad_index = len(re.findall(sad_pattern, data))

happiness = happy_index / sad_index
if happiness >= 2:
    emoticon = ':D'
elif happiness > 1:
    emoticon = ':)'
elif happiness == 1:
    emoticon = ':|'
else:
    emoticon = ':('

print('Happiness index: {0:.2f} {1}'.format(happiness, emoticon))
print('[Happy count: {}, Sad count: {}]'.format(happy_index, sad_index))



