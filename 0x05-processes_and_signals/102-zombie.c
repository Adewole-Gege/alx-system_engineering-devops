#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int infinite_while(void)
{
    while (1)
    {
        sleep(1);
    }
    return (0);
}

int main(void)
{
    pid_t pid;
    for (int i = 0; i < 5; i++)
    {
        pid = fork();
        if (pid == 0)
        {
            printf("Zombie process created, PID: %d\n", getpid());
            exit(0);
        }
    }
    infinite_while();
    return (0);
}
