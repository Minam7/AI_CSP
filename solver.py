import random

import csp


def create_random(c_list):
    knowledge = list()
    for z in range(len(c_list)):
        knowledge.append(random.randint(50, 100))
    return dict(zip(c_list, knowledge))


def func(in_A, in_a, in_B, in_b):
    if in_a[in_A] > 80 and in_b[in_B] > 80 and in_a != in_b:
        return True
    return False


if __name__ == '__main__':
    a, b, c, d, e, f, g, h, i, j, k, l, m, n = 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'

    course_list = list([a, b, c, d, e, f, g, h, i, j, k, l, m, n])

    p_1, p_2, p_3, p_4, p_5, p_6, p_7, p_8, p_9, p_10 = create_random(course_list), create_random(
        course_list), create_random(course_list), create_random(course_list), create_random(course_list), create_random(
        course_list), create_random(course_list), create_random(course_list), create_random(course_list), create_random(
        course_list)

    prof_list = list([p_1, p_2, p_3, p_4, p_5, p_6, p_7])

    neighbor_list = {a: [b], b: [a, c, d, e], c: [b, h, f], d: [b, g, k], e: [b], f: [c], g: [d], h: [c, j, i, l],
                     i: [h, m, n], j: [h], k: [d], l: [h], m: [i], n: [i]}

    prof_course = dict()
    for item in course_list:
        prof_course[item] = prof_list

    problem = csp.CSP(course_list, prof_course, neighbor_list, func)

    ans = csp.tree_csp_solver(problem)
    problem.display(ans)

    if ans is not None:
        for key, value in ans.items():
            print('course:', key, '->', 'prof:', prof_list.index(value) + 1, '->', 'knowledge:', value[key])
    else:
        print('no assignment')
