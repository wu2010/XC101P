n = int(input())

# The following values are interpreted as false: False, None, numeric zero of all types,
# and empty strings and containers (including strings, tuples, lists, dictionaries, sets and frozensets).
# All other values are interpreted as true.

# Logical operators are used on conditional statements (either True or False).
# They perform Logical AND, Logical OR and Logical NOT operations.
# operator precedence: AND to OR is like * to +

# Comparison operators are used to compare two values: ==, !=, <, <=, >, >=.

leap = n % 4 == 0 and n % 100 != 0 or n % 400 == 0

# Conditional expressions (sometimes called a “ternary operator”) have
# the lowest priority of all Python operations.
# The expression x if C else y first evaluates the condition, C rather than x.
# If C is true, x is evaluated and its value is returned;
# otherwise, y is evaluated and its value is returned.

print('yes' if leap else 'no')