#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *h_ref_first = *head, *h_ref_second = (*head)->next;
	listint_t *new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
		return (NULL);
	new_node->n = number;

/*check if is list is empty or the first node*/
	if (*head == NULL || (h_ref_first->next != NULL && number >= (h_ref_first->n)))
	{
		new_node->n = number;
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

/*check if is in the middle*/
	while (h_ref_second != NULL)
	{
		if (h_ref_first->n <= number && h_ref_second->n >= number)
		{
			if (h_ref_first->n == )
			new_node->next = h_ref_first->next;
			h_ref_first->next = new_node;
			return (new_node);
		}
	h_ref_first = h_ref_first->next;
	h_ref_second = h_ref_second->next;
	}
/*is the last*/
	h_ref_first->next = new_node;
	new_node->next = NULL;
	return (new_node);
}
