import csp


def input_reader():
    temp1 = input().replace('\n', '').split(' ')
    courses_num, profs_num = int(temp1[0]), int(temp1[1])

    temp1 = input().replace('\n', '')
    n_edge = int(temp1)

    preq = dict()
    for z in range(courses_num):
        preq[z] = list()

    for z in range(n_edge):
        temp2 = input().replace('\n', '').split(' ')
        preq[int(temp2[0])].append(int(temp2[1]))
        preq[int(temp2[1])].append(int(temp2[0]))

    profs_k = list()
    for z in range(profs_num):
        temp = dict()
        temp2 = input().split(' ')
        for y in range(courses_num):
            temp[y] = int(temp2[y])
        profs_k.append(temp)

    return courses_num, profs_num, preq, profs_k


def func(in_A, in_a, in_B, in_b):
    if in_a[in_A] > 80 and in_b[in_B] > 80 and in_a != in_b:
        return True
    return False


def problem_sol():
    n_courses, n_profs, prereq, knowledge = input_reader()

    course_list = list(range(n_courses))

    prof_list = knowledge

    prof_course = dict()
    for item in course_list:
        prof_course[item] = prof_list

    problem = csp.CSP(course_list, prof_course, prereq, func)

    answer = csp.tree_csp_solver(problem)
    # problem.display(answer)

    log = ''
    if answer is not None:
        for i in range(n_courses):
            print(i, ' ', prof_list.index(answer[i]))
    else:
        log += 'no assignment'
        # print('no assignment')

    return log


if __name__ == '__main__':
    problem_sol()
