import os

import networkx as nx

import csp


def input_reader():
    temp1 = input().replace('\n', '').split(' ')
    courses_num, profs_num = int(temp1[0]), int(temp1[1])

    temp1 = input().replace('\n', '')
    n_edge = int(temp1)

    preq = nx.Graph()
    courses = list(range(n_edge + 1))
    preq.add_nodes_from(courses)

    for z in range(n_edge):
        temp2 = input().replace('\n', '').split(' ')
        tup = (int(temp2[0]), int(temp2[1]))
        preq.add_edge(*tup)

    profs_k = list()
    for z in range(profs_num):
        temp = dict()
        temp2 = input().split(' ')
        for y in range(courses_num):
            temp[y] = int(temp2[y])
        profs_k.append(temp)

    return courses_num, profs_num, preq, profs_k


def create_neibours(data, course_num):
    ans = dict()
    for i in range(course_num):
        ans[i] = list(data.neighbors(i))
    return ans


def func(in_A, in_a, in_B, in_b):
    if in_a[in_A] > 80 and in_b[in_B] > 80 and in_a != in_b:
        return True
    return False


def problem_sol():
    n_courses, n_profs, prereq, knowledge = input_reader()

    course_list = list(range(n_courses))

    prof_list = knowledge

    neighbor_list = create_neibours(prereq, n_courses)

    prof_course = dict()
    for item in course_list:
        prof_course[item] = prof_list

    problem = csp.CSP(course_list, prof_course, neighbor_list, func)

    answer = csp.tree_csp_solver(problem)
    problem.display(answer)

    log = ''
    if answer is not None:
        for key, value in answer.items():
            log += str(key) + ' ' + str(prof_list.index(value)) + '\n'
            # print('course:', key, '->', 'prof:', prof_list.index(value) + 1, '->', 'knowledge:', value[key])
    else:
        log += 'no assignment'
        # print('no assignment')

    return log


if __name__ == '__main__':
    os.system("pip install networkx")

    problem_sol()
