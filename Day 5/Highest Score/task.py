student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
# print(range(1, 10))
#
# total_exam_score = sum(student_scores)
# print(total_exam_score)
# total_score = 0
#
# for score in student_scores:
#     total_score += score
#     print(f'Total score of all student is {total_score}')

x = 0
for score in student_scores:
    if score > x:
        x = score
print(f'Max score is {x}')