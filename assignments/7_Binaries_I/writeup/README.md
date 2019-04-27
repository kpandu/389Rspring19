# Writeup 7 - Binaries I

Name: *Krishan Panduwawala*
Section: *0201*

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: *Krishan Panduwawala*

## Assignment Writeup

### Part 1 (90 Pts)

*Put your code here as well as in main.c*
```c
printf("
#include <stdio.h>
int main() {
    int x = 0x1ceb00da;
    int y = 0xfeedface;
    printf("%d\n", x);
    printf("%d\n", y);
    x = x^y;
    y = y^x;
    x = x^y;

    printf("%d\n", x);
    printf("%d\n", y);
    return 0;
}"
);
```

### Part 2 (10 Pts)

The program first prints the two numbers: 0x1ceb00da and 0xfeedface . Then the program uses bitwise exclusive or to swap the two numbers and print the swapped result.
