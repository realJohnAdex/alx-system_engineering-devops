#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

/**
 * create_zombie_processes - Creates zombie processes
 *
 * This function creates 5 zombie processes.
 * For every zombie process created, it displays
 * "Zombie process created, PID: ZOMBIE_PID".
 */
void create_zombie_processes(void)
{
	int i;
	pid_t pid;

	for (i = 0; i < 5; i++)
	{
		pid = fork();

		if (pid < 0)
		{
			perror("fork");
			exit(EXIT_FAILURE);
		} else if (pid == 0)
		{
			exit(EXIT_SUCCESS);
		} else
		{
			printf("Zombie process created, PID: %d\n", pid);
			sleep(1);
		}
	}
}
/**
 * main - main entrry point
 *
 * Return: int
 */
int main(void)
{
	create_zombie_processes();
	return (0);
}
