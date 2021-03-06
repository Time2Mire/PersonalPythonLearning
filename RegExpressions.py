def isPhoneNumber(text):
  if len(text) != 12:
    print('Not Phone Number')
    return False
  for i in range(0,3):
    if not text[i].isdecimal():
      print('Not Phone Number')
      return False
  if text[3] != '-':
    print('Not Phone Number')
    return False
  for i in range(4,7):
    if not text[1].isdecimal():
      print('Not Phone Number')
      return False
  if text[7] != '-':
    print('Not Phone Number')
    return False
  for i in range(8,12):
    if not text[i].isdecimal():
      print('Not Phone Number')
      return False
  print('Phone Number')
  return True

isPhoneNumber('4154555-1234')

_________________________________________________________________________________
def isPhoneNumber(text):
  if len(text) != 12:
    return False
  for i in range(0,3):
    if not text[i].isdecimal():
      return False
  if text[3] != '-':
    return False
  for i in range(4,7):
    if not text[1].isdecimal():
      return False
  if text[7] != '-':
    return False
  for i in range(8,12):
    if not text[i].isdecimal():
      return False
  return True

isPhoneNumber('4154555-1234')

message='Call me at 123-555-0156 tomorrow. 123-555-0538 is my office.'
for i in range(len(message)):
  chunk=message[i:i+12]
  if isPhoneNumber(chunk):
    print('Phone number found: ' + chunk)
print('Done.')

import re

phoneNumRegex=re.compile(r'\d{3}-\d{3}-\d{4}')

mo=phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo[0])
print(mo[0])

phoneNumRegex=re.compile(r'(\d{3})?-(\d{3}-\d{4})')

mo=phoneNumRegex.search('My number is 258-555-4242.')
print(mo.group(1,2,))
print(mo.group(1))
print(mo.group(2))
print(mo[0])

AreaCode=mo.group(1)
print(AreaCode)

MainNumber=mo.group(2)
print(MainNumber)

print(mo.groups())

heroRegex=re.compile(r'Thor|Gorr')
mo1=heroRegex.search('Thor and Gorr.')
print(mo1[0])

mo1=heroRegex.findall('Thor and Gorr')
print(mo1[0] + ' ' + mo1[1])


batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo=batRegex.search('Batmobile lost a wheel.')
print(mo[0])

batRegex=re.compile(r'Bat(wo)?man')
mo1=batRegex.search('Batman is a tran.')
print(mo1[0])
mo2=batRegex.search('Batwoman can Stan.')
print(mo2[0])

batRegex=re.compile(r'Bat(wo| )*?man')
mo3=batRegex.search('Bat man has a plan.')
print(mo3[0])
mo4=batRegex.search('Batwowowowowowoman has a plan.')
print(mo4[0])

haRegex=re.compile(r'(Ha){3,5}')
mo1=haRegex.search('HaHaHaHa')
print(mo1[0])

mo2=haRegex.search('Ha')
print(mo2==None)

greedyRegex=re.compile(r'(Ha){3,5}')
mo1=greedyRegex.search('HaHaHaHaHa')
print(mo1[0])

Regex=re.compile(r'(Ha){3,5}?')
mo2=Regex.search('HaHaHaHaHa')
print(mo2[0])

phoneNumRegex=re.compile(r'((\w{3})-(\w{3}-\w{4}))')
mo1=phoneNumRegex.findall('Cell: ABC-555-9999 Work: CBA-555-0000')
print(mo1)
print(mo1[0])
print(mo1[1])

xmasRegex=re.compile(r'\d+\s\w+')
mo1=xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 3 hens, 2 doves, 1 partridge')
print(mo1)

print('Vowel')
vowelRegex=re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall('Robocop eats baby food. BABY FOOD.'))

print('Consonant')
consonantRegex=re.compile(r'[^aeiouAEIOU]')
print(consonantRegex.findall('Robocop eats baby food. BABY FOOD.'))

beginHello=re.compile(r'^Hello')
print(beginHello.findall('Hello World'))

endNumber=re.compile(r'\d$')
print(endNumber.search('Your number is 42'))

wholeStringIsNum=re.compile(r'^\d+$')
mo1=wholeStringIsNum.findall('1234567890')
print(mo1)

atRegex=re.compile(r'.at')
mo1=atRegex.findall('The cat in the hat sat on the flat mat.')
print(mo1)

import re

nameRegex=re.compile(r'First Name: (.*) Last Name: (.*)')
mo=nameRegex.search('First Name: Jeffald Last Name: Bodagard')
print(mo[0])
print(mo.group(1))
print(mo.group(2))

nolineRegex=re.compile('.*')
mo=nolineRegex.search('''Serve the public trust. 
Protect the Innocent.
Uphold the Law.''')
print(mo[0])

newlineRegex=re.compile('.*', re.DOTALL)
mo=newlineRegex.search('''Serve the public trust.
Protect the Innocent.
Uphold the Law.''')
print(mo[0])

robocop=re.compile(r'robocop', re.I)
print(robocop.search('Robocop is part man.').group())
print(robocop.search('ROBOCOP for the chop.').group())
print(robocop.search('robocop was a flop.').group())

namesRegex=re.compile(r'Agent (\w)\w+')
print(namesRegex.sub(r'\1****', 'Agent Jeff gave the secret documents to Agent Jeffald.'))

phoneRegex=re.compile(r'''(
(\d{3}|\(\d{3}\)?
(\s|-|\.)?
\d{3}
(\s|-|\.)
\d{4}
(\s*(ext|x|ext.)\s*\d{2,5})?
)''', re.VERBOSE)
  
print(phoneRegex.search('345-455-798'))
