import networkx as nx

import csp


def input_reader(name):
    f = open(name)

    temp = f.readlines()
    temp1 = temp[0].replace('\n', '').split(' ')
    courses_num, profs_num = int(temp1[0]), int(temp1[1])

    temp1 = temp[1].replace('\n', '')
    n_edge = int(temp1)

    preq = nx.Graph()
    courses = list(range(n_edge + 1))
    preq.add_nodes_from(courses)

    temp1 = temp[2:n_edge + 2]
    for item in temp1:
        temp2 = item.replace('\n', '').split(' ')
        tup = (int(temp2[0]), int(temp2[1]))
        preq.add_edge(*tup)

    temp1 = temp[n_edge + 3:]
    profs_k = list()
    for z in range(profs_num):
        temp = dict()
        temp2 = temp1[z].split(' ')
        for y in range(courses_num):
            temp[y] = int(temp2[y])
        profs_k.append(temp)

    f.close()
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


def problem_sol(name):
    n_courses, n_profs, prereq, knowledge = input_reader(name)

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
    for i in range(10):
        stri = 'in/input' + str(i + 1) + '.txt'
        outp = problem_sol(stri)
        stri = 'out/output' + str(i + 1) + '.txt'
        f = open(stri, 'w')
        f.write(outp)
        f.close()
