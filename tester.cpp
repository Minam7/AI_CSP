/*
 * tester.cpp
 */

#include <iostream>
#include <fstream>
#include <string>
#include <string.h>
#include <vector>
#include <stdlib.h>
#include <cstdlib>
using namespace std;

void dump(std::ostream &out, const std::vector<std::string> &v)
{
    for(size_t i = 0; i < v.size(); ++i) {
        out << '\'' << v[ i ] << '\'' << ' ';
    }
    
    out << std::endl;
}

size_t split(const std::string &txt, std::vector<std::string> &strs, char ch)
{
    size_t pos = txt.find( ch );
    size_t initialPos = 0;
    strs.clear();
    
    // Decompose statement
    while( pos != std::string::npos ) {
        strs.push_back( txt.substr( initialPos, pos - initialPos ) );
        initialPos = pos + 1;
        
        pos = txt.find( ch, initialPos );
    }
    
    // Add the last one
    strs.push_back( txt.substr( initialPos, std::min( pos, txt.size() ) - initialPos + 1 ) );
    
    return strs.size();
}

int main(int argc, char const *argv[])
{
    ifstream test_in(argv[1]);    /* This stream reads from test's input file   */
    ifstream test_out(argv[2]);   /* This stream reads from test's output file  */
    ifstream user_out(argv[3]);   /* This stream reads from user's output file  */
    
//    ifstream test_in ("in/input1.txt");
//    ifstream test_out ("out/output2.txt");
//    ifstream user_out ("outCopy/output1.txt");
    
    /* Your code here */
    /* If user's output is correct, return 0, otherwise return 1       */
    /* e.g.: Here the problem is: read n numbers and print their sum:  */
    int check = 0;
    string inp;
    string out_use;
    if ( test_out.good() ) // if test's output file exists
    {
        getline(test_out, inp);
        getline(user_out, out_use);
        if (inp.compare(out_use) != 0){
            check = 1;
        }
    }
    else{
        
    std::vector<std::string> v;
    int course_n, prof_n, edge_n;
    
    getline(test_in, inp);
    split(inp, v, ' ');
    course_n = atoi(v[0].c_str());
    prof_n = atoi(v[1].c_str());
    getline(test_in, inp);
    edge_n = atoi(inp.c_str());
    
    int preq [course_n][course_n];
    memset( preq, -1, course_n*course_n*sizeof(int) );
    
    for (int i=0; i<edge_n; i++) {
        getline(test_in, inp);
        split(inp, v, ' ');
        int f,g;
        f = atoi(v[0].c_str());
        g = atoi(v[1].c_str());
        preq[f][g] = 1;
        preq[g][f] = 1;
    }
    
    int profs [prof_n][course_n];
    memset( profs, 0, prof_n*course_n*sizeof(int) );
    
    for (int i=0; i<prof_n; i++) {
        getline(test_in, inp);
        split(inp, v, ' ');
        for(int j=0; j<v.size(); j++){
            profs[i][j] = atoi(v[j].c_str());
        }
    }
    
    int ans[course_n];
    memset( ans, 0, course_n*sizeof(int) );
    
    for (int i=0; i<course_n; i++) {
        getline(user_out, inp);
        split(inp, v, ' ');
        int f,g;
        f = atoi(v[0].c_str());
        g = atoi(v[1].c_str());
        ans[f] = g;
        if(profs[g][f] < 80){
            check = 1;
        }
    }

    for (int i=0; i<course_n; i++) {
        for(int j=0; j<course_n; j++){
            if((i != j) && (preq[i][j] == 1) && (ans[i] == ans[j])){
                check = 1;
            }
        }
    }

    }
    cout <<check<<endl;
    
    if (check == 0)
        return 0;
    else
        return 1;
    
}

