import networkx as nx


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
        for y in range(courses_num):
            temp2 = temp1[(z * courses_num) + y].replace('\n', '').split(' ')
            temp[int(temp2[0])] = int(temp2[1])
        profs_k.append(temp)

    f.close()
    return courses_num, profs_num, preq, profs_k


def answer_reader(name):
    f = open(name)
    temp = f.readlines()
    ans = dict()
    for item in temp:
        temp1 = item.replace('\n', '').split(' ')
        ans[int(temp1[0])] = int(temp1[1])

    return ans


def find_prof(list_in, ind):
    ans = []
    for item in list_in:
        ans.append(answer[item])
    ans.append(answer[ind])
    return ans


if __name__ == '__main__':
    n_courses, n_profs, prereq, knowledge = input_reader('inputs/input.txt')
    answer = answer_reader('inputs/output.txt')

    find = 0
    for key, value in answer.items():
        if knowledge[value][key] < 80:
            find = 1

    for i in range(n_courses):
        neib = list(prereq.neighbors(i))
        prof_neib = find_prof(neib, i)
        if len(prof_neib) != len(set(prof_neib)):
            find = 1

    if find != 0:
        print(False)
    else:
        print(True)
