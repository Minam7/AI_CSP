import java.util.ArrayList;
import java.util.Scanner;

public class Ans {
    private static int colors[];
    private static int tree[][];
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int courseNum = scanner.nextInt();
        int profNum = scanner.nextInt();
        int edgeesNumber = scanner.nextInt();
        tree = new int[courseNum][courseNum];
        for (int i = 0; i < edgeesNumber; i++) {
            int n1 = scanner.nextInt();
            int n2 = scanner.nextInt();
            tree[n1][n2] = 1;
            tree[n2][n1] = 1;
        }
        colors = new int[courseNum];
        ArrayList<Integer> sorted = DFS(-1, courseNum);
        int profCourse[][] = new int[profNum][courseNum];
        for (int i = 0; i < profNum; i++) {
            for (int j = 0; j < courseNum; j++) {
                profCourse[i][j] = scanner.nextInt();
            }
        }
        ArrayList domains[] = new ArrayList[courseNum];
        for (int i = 0; i < courseNum; i++) {
            domains[i] = new ArrayList<Integer>();
        }
        for (int i = 0; i < courseNum; i++) {
            for (int j = 0; j < profNum; j++) {
                if (profCourse[j][i] > 80) {
                    domains[i].add(j);
                }
            }
        }
        ArrayList<Tuple> queue = new ArrayList<>();
        for (int i = 0; i < courseNum; i++) {
            for (int j = 0; j < courseNum; j++) {
                if (tree[i][j] == 1) {
                    queue.add(new Tuple(i, j));
                }
            }
        }
        for (int i = 0; i < courseNum; i++) {
            if (domains[i].size() == 0) {
                System.out.println("no assignment");
                return;
            }
        }
        while (queue.size() > 0) {
            Tuple tmp = queue.remove(0);
            boolean revised = false;
            int ptr = -1;
            if (domains[tmp.getN2()].size() == 1) {
                int possibleForN2 = (int) domains[tmp.getN2()].get(0);
                for (int i = 0; i < domains[tmp.getN1()].size(); i++) {
                    if ((int) domains[tmp.getN1()].get(i) == possibleForN2) {
                        ptr = i;
                        revised = true;
                        break;
                    }
                }
            }
            if (revised) {
                domains[tmp.getN1()].remove(ptr);
                if (domains[tmp.getN1()].size() == 0) {
                    System.out.println("no assignment");
                    return;
                }
                for (int i = 0; i < courseNum; i++) {
                    if (tree[i][tmp.getN1()] == 1) {
                        queue.add(new Tuple(i, tmp.getN1()));
                    }
                }
            }
        }
        for (int i :
                sorted) {
            System.out.println(i + " " + domains[i].get(0));
            for (int j = 0; j < courseNum; j++) {
                if (tree[j][i] == 1) {
                    for (int k = 0; k < domains[j].size(); k++) {
                        if (domains[j].get(k) == domains[i].get(0)) {
                            domains[j].remove(k);
                            break;
                        }
                    }
                }
            }
        }
    }

    private static ArrayList<Integer> DFS(int index, int n) {
        if (index > -1 && colors[index] != 1) {
            return new ArrayList<>();
        }
        ArrayList<Integer> list = new ArrayList<>();
        if (index == -1) {
            for (int i = 0; i < n; i++) {
                if(colors[i] == 0) {
                    colors[i] = 1;
                    list.addAll(DFS(i, n));
                }
            }
        } else {
            for (int i = 0; i < n; i++) {
                if (tree[index][i] == 1 && colors[i] == 0) {
                    colors[i] += 1;
                    ArrayList<Integer> tempList = DFS(i, n);
                    list.addAll(tempList);
                }
            }
            colors[index]++;
            list.add(index);
        }
        return list;
    }
}

class Tuple {
    private int n1, n2;

    Tuple(int n1, int n2) {
        this.n1 = n1;
        this.n2 = n2;
    }

    int getN1() {
        return n1;
    }

    int getN2() {
        return n2;
    }
}
