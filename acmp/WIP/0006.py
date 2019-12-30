import re
s = input()
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
if re.match(r'[a-hA-H][1-8]-[a-hA-H][1-8]', s):
    start, end = s.split('-')[0], s.split('-')[1]
    variants = []
    letter = ''.join(re.findall(r'[a-hA-H]', start))
    num = ''.join(re.findall(r'[1-8]', start))
else:
    print('ERROR')
