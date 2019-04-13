/*
 * Name: *Krishan Panduwawala*
 * Section: *0201*
 *
 * I pledge on my honor that I have not given or received any unauthorized
 * assistance on this assignment or examination.
 *
 * Digital acknowledgement: *Krishan Panduwawala*
 */

/* your code goes here */
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
}
