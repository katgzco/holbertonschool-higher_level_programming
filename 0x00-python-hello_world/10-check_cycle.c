#include "list.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: the head reference.
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 **/
int check_cycle(listint_t *list)
{
	listint_t *l_step_1 = list;
	listint_t *l_step_2 = list;

	while (l_step_1 != NULL & l_step_2 != NULL & l_step_2->next != NULL)
	{
		l_step_1 = l_step_1->next;
		l_step_2 = l_step_2->next->next;
		if (l_step_1 == l_step_2)
			return (1);
	}
	return (0);
}
