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
    if len(temp) < 2:
        return None
    ans = dict()
    for item in temp:
        temp1 = item.replace('\n', '').split(' ')
        ans[int(temp1[0])] = int(temp1[1])

    f.close()
    return ans


def check(name, name_out):
    n_courses, n_profs, prereq, knowledge = input_reader(name)
    answer = answer_reader(name_out)
    if answer is None:
        return 0
    find = 0
    for key, value in answer.items():
        if knowledge[value][key] < 80:
            find = 1

    for i in range(n_courses):
        neib = list(prereq.neighbors(i))
        if i in neib:
            find = 1

    return find


if __name__ == '__main__':

    for i in range(10):
        stri = 'in/input' + str(i + 1) + '.txt'
        stro = 'out/output' + str(i + 1) + '.txt'
        findo = check(stri, stro)
        if findo != 0:
            print(False)
        else:
            print(True)
