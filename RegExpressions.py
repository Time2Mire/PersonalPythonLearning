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

mo=phoneNumRegex.search('My number is -555-4242.')
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

batRegex=re.compile(r'Bat(wo| )?man')
mo3=batRegex.search('Bat man has a plan.')
print(mo3[0])
mo4=batRegex.search('Batwoman has a plan.')
print(mo4[0])






