def calculate_average(marks):
    if not marks:
        return 0.0
    return sum(marks) / len(marks)


def get_result(average):
    if average >= 40:
        return "Pass"
    return "Fail"