#include <stdio.h>
#include <stdlib.h>

int main() {
    printf("Starting Concord...\n");
    printf("Defining Variables...\n");
    char osuname[] = "admin";
    double sysvers = 0.3;
    int sysrele = 2022;
    const char sysname[] = "Concord";
    char cmdparam[] = "#>";
    char usyntax1[64];
    /*
    char usyntax2[64];
    char usyntax3[64];
    char usyntax4[64];
    int nopass = 1;
    int validcmd = 0;
    */
    printf("Searching File System...\n"); // Dont forget to add this
    printf("Primed to start User Session\n");
    printf("Clearing Screen\n");
    system("clear");
    printf("%s v%g %d\n",  sysname, sysvers, sysrele);
    printf("Welcome, %s\n", osuname);
    printf("%s", cmdparam);
    scanf("%s", usyntax1); // Stick to just one "word" per command
    return 0;
}
