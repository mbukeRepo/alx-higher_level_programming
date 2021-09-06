#include "lists.h"

/**
 * check_cycle - checks if there is a circle in our list
 * @list: the start of the list
 * Return: 1 if the is a circle in our list, 0 for no circle
 */
int check_cycle(listint_t *list)
{
listint_t *tutle, *hare;
if (list == NULL || list->next == NULL)
return (0);
tutle = list->next;
hare = list->next->next;
while (hare && tutle && hare->next)
{
if (tutle == hare)
return (1);
tutle = tutle->next;
hare = hare->next->next;
}
return (0);
}
