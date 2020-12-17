#include "lists.h"

/**
 * is_palindrome - prints all elements of a listint_t list
 * @head: the head of the linked list.
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	int num_node = 0, check_position = 0;
	int array_node[BUFSIZ], array_reverse[BUFSIZ];
	listint_t *h_reference = *head;

	if (head != NULL)
	{
		if (*head == NULL)
			return (1);

		/*store nodes*/
		for (num_node = 0; h_reference != NULL; num_node++)
		{
			array_node[num_node] = h_reference->n;
			array_reverse[num_node] = h_reference->n;
			h_reference = h_reference->next;
		}
		/*compare nodes*/
		num_node--;
		for (check_position = 0; num_node >= 0 ; check_position++, --num_node)
			if (array_node[check_position] != array_reverse[num_node])
				break;
		/*is polindrome*/
		if (num_node > 0)
			return (0);
		else
			return (1);
	}
	return (0);
}
