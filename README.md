# AI CSP

We have between 10 to 30 courses and between 10 to 20 professors.
It is defined by the following in the first line of input:

```shell
10 9
```

Then number of edges in tree is mentioned:
```shell
9
```

After that courses prerequisites is defined by mentioning edges 
as a tuple of first course and second course with a space between.
Pay attention that each edge is just mentioned once(not for each node separately!)as a tuple of courses and knowledge with a space between.
```shell
2 6
1 6
1 5
4 3
7 9
9 3
7 2
8 9
0 5
```

After that each professor's knowledge is printed for all courses
 as a tuple of courses and knowledge with a space between.
```shell
65 52 84 90 39 31 88 56 58 84
46 76 76 56 45 86 49 29 99 43
88 93 63 50 42 55 94 64 32 84
20 55 94 74 51 73 81 98 95 39
68 37 22 69 40 73 26 64 94 86
91 52 30 81 40 42 69 76 68 27
26 26 47 44 87 78 95 82 35 48
35 32 63 50 66 94 63 79 21 55
74 53 59 39 91 95 51 30 49 96
```

The answer must be in the following format, with courses sorted increasingly:
```shell
course_number professor_number
0 2
5 1
1 2
6 0
2 3
7 6
9 0
8 1
3 5
4 6
```
