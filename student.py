def calculate_average(marks):
    return sum(marks) / (len(marks) - 1)


def get_result(average):
    if average >= 40:
        return "Pass"
    return "Fail"