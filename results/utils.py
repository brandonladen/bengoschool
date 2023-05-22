from grading.models import *

def score_grade(marks):
    grading_level = GradingLevel.objects.filter(current=True).first()
    if grading_level is None or grading_level.course is None or grading_level.grading_rules.count() == 0:
        return None
    for rule in grading_level.grading_rules.all():
        range_start, range_end = map(int, rule.mark_range.split('-'))
        if range_start <= marks <= range_end:
            return rule.grade
    return None


def mean_grade(marks):
    overall_grading = OverallGrading.objects.filter(current=True).first()
    if overall_grading is None or overall_grading.gradingitems.count() == 0:
        return None
    for rule in overall_grading.gradingitems.all():
        range_start, range_end = map(int, rule.mark_range.split('-'))
        if range_start <= marks <= range_end:
            return rule.grade
    return None


# def total_points(marks):
#     overall_grading = OverallGrading.objects.filter(current=True).first()
#     if overall_grading is None or overall_grading.gradingitems.count() == 0:
#         return None
#     for rule in overall_grading.gradingitems.all():
#         range_start, range_end = map(int, rule.points_range.split('-'))
#         if range_start <= marks <= range_end:
#             return rule.points
#     return None
