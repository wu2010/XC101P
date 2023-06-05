# A simple ascending sort is very easy: just call the sorted() function.

# You can also use the list.sort() method. It modifies the list in-place
# (and returns None to avoid confusion). Usually it’s less convenient than sorted() -
# but if you don’t need the original list, it’s slightly more efficient.

# There are n children who have taken two courses in Chinese and Mathematics.
# Now I hope to sort the grades to determine the ranking.
# The total score is ranked first, and if the total score is the same,
# then it is ranked according to the Chinese score.
# Now please output the sorted scores.
#
# Input format:
# The first line, an integer n, indicating the number of children taking the test.
# The next n lines, two numbers per line, representing Chinese and math scores.
#
# Output format:
# A total of n lines, two numbers per line, indicating the Chinese and math scores
# after sorting.


n = int(input())
scores = []
for _ in range(n):
    chinese_score, math_score = map(int, input().split())
    student = [chinese_score + math_score, chinese_score, math_score]
    scores.append(student)

# descending sort with minus sign
scores.sort(key=lambda s: (-s[0], -s[1]))

for score in scores:
    print(score[1], score[2])

