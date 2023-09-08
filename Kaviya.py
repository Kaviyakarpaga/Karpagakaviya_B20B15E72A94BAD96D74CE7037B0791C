#leap year
"""
year % 4==0 &
year % 100!=0 /
year % 400 == 0

"""
def isleapyear(year):
  if(year % 4==0 and year % 100 !=0)
  return true
else:
  return false

year=int(input(" enter a year :"))

if isleap year(year):
  print('{}is a leap
        year.'.format(year))
else:
 print('{} is not a leap
       year.'.format(year))
