# modern ways
# https://docs.python.org/3/tutorial/inputoutput.html

# Formatted string literals (also called f-strings)
year = 2016
event = 'Referendum'
print(f'Results of the {year} {event}')

# Passing an integer after the ':' will cause that field to be a minimum
# number of characters wide. This is useful for making columns line up.
name = 'Sjoerd'
phone = 4127
print(f'{name:10} ==> {phone:10d}')


#  str.format() method of strings requires more manual effort.
#  You’ll still use { and } to mark where a variable will be substituted
#  and can provide detailed formatting directives
print('{:-9} YES votes  {:2.2%}'.format(42572654, 49.67))

print('We are the {} who say "{}!"'.format('knights', 'Ni'))
# A number in the brackets can be used to refer to the position
# of the object passed into the str.format() method.
print('{0} and {1}'.format('spam', 'eggs'))
print('{1} and {0}'.format('spam', 'eggs'))


# the old way
# https://docs.python.org/3/library/stdtypes.html#old-string-formatting
# keep 4 decimal places
z = 97.6
print('%.4f' % z)
