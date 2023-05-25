from grading.models import *

def score_grade(marks, course):
    grading_level = GradingLevel.objects.filter(current=True, course=course).first()

    if not grading_level or not grading_level.grading_rules.exists():
        return None

    for grading_rule in grading_level.grading_rules.all():
        start_mark, end_mark = map(int, grading_rule.mark_range.split('-'))
        if start_mark <= marks <= end_mark:
            return grading_rule.grade

    return None

def points_earned(subject_score,subject):
    # Retrieve the grading rules for the subject's course
    grading_rules = GradingRules.objects.filter(grading_level__course__subject=subject)

    total_points_earned = 0

    # Iterate over the grading rules and calculate the points earned
    for rule in grading_rules:
        mark_range_start, mark_range_end = map(int, rule.mark_range.split('-'))

        # Check if the subject score falls within the mark range of the rule
        if mark_range_start <= subject_score <= mark_range_end:
            total_points_earned += rule.grade.points
            break  # Exit the loop once a matching rule is found

    return total_points_earned


def mean_grade(marks):
    overall_grading = OverallGrading.objects.filter(current=True).first()
    if overall_grading is None or overall_grading.gradingitems.count() == 0:
        return None
    for rule in overall_grading.gradingitems.all():
        range_start, range_end = map(int, rule.mark_range.split('-'))
        if range_start <= marks <= range_end:
            return rule.grade
    return None


def calculate_positions(grading_type='points', student_id=None):
    # Get all the students
    students = Student.objects.all()

    # Calculate the total points or marks for each student
    student_scores = []
    for student in students:
        if grading_type == 'points':
            total_score = sum([result.test_score + result.exam_score for result in student.result_set.all()])
        elif grading_type == 'marks':
            total_score = sum([result.test_score + result.exam_score for result in student.result_set.all()])
            # Convert the total marks to points using OverallGradingItem model
            overall_grading = OverallGrading.objects.filter(current=True).first()
            if overall_grading:
                grading_items = overall_grading.gradingitems.all()
                for grading_item in grading_items:
                    mark_range = grading_item.mark_range.split('-')
                    points_range = grading_item.points_range.split('-')
                    if int(mark_range[0]) <= total_score <= int(mark_range[1]):
                        total_score = int(points_range[0]) + ((total_score - int(mark_range[0])) * ((int(points_range[1]) - int(points_range[0])) / (int(mark_range[1]) - int(mark_range[0]))))
                        break
        else:
            return "Invalid grading type!"

        student_scores.append((student, total_score))

    # Sort the student scores in descending order
    sorted_scores = sorted(student_scores, key=lambda x: x[1], reverse=True)

    # Calculate the overall positions
    overall_positions = []
    position_counter = 1
    previous_score = None
    for i, (student, score) in enumerate(sorted_scores):
        if previous_score is None or score < previous_score:
            # If the score is different from the previous score, update the position
            position_counter = i + 1

        overall_positions.append((student, position_counter))
        previous_score = score

    # Calculate the stream (section) positions
    section_positions = {}
    for student, position in overall_positions:
        section = student.current_section
        if section:
            if section not in section_positions:
                section_positions[section] = []
            section_positions[section].append((student, position))

    # If a specific student ID is provided, find the positions
    if student_id is not None:
        student_positions = {
            'overall_position': None,
            'section_positions': {}
        }
        for position_tuple in overall_positions:
            if position_tuple[0].id == student_id:
                student_positions['overall_position'] = position_tuple[1]
                break

        for section, positions in section_positions.items():
            for position_tuple in positions:
                if position_tuple[0].id == student_id:
                    student_positions['section_positions'][section] = position_tuple[1]
                    break

        return student_positions

    return {
        'overall_positions': overall_positions,
        'section_positions': section_positions
    }
