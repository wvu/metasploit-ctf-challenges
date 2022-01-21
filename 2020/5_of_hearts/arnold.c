/* gcc arnold.c -o arnold -O -static -s -fstack-protector -z noexecstack -D_FORTIFY_SOURCE=2 */

#define _GNU_SOURCE

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void ask(char *question)
{
  char answer[256];

  fprintf(stderr, "%s", question);

  if (!gets(answer) || *answer == '\0') {
    fprintf(stderr, "I'm a cop, you idiot! I'm Detective John Kimble!\n");

    exit(EXIT_FAILURE);
  }

  if (strcasestr(answer, "hack")) {
    system("/bin/cat /qemu/arnold");

    exit(EXIT_SUCCESS);
  }

  printf(answer);
  printf("\n");
}

int main(void)
{
  setbuf(stdout, NULL);

  fprintf(stderr, "I'm going to ask you a bunch of questions, "
                  "and I want to have them answered immediately.\n\n");

  ask("Who is your daddy? ");
  ask("And what does he do? ");

  return EXIT_SUCCESS;
}
