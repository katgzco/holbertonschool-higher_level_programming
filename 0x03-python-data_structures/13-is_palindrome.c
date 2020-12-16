#include "lists.h"

/**
 * is_palindrome - prints all elements of a listint_t list
 * @head: the head of the linked list.
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	int list_length = 0, reverse_num = 0, tmp_num = 0;

	if (head != NULL)
	{
		if (*head == NULL)
			return (1);

		list_length = (*head)->n;
		/*reverse nummber*/
		if (list_length > 9)
		{
			while (tmp_num)
			{
				reverse_num = 10 * reverse_num + (tmp_num % 10);
				tmp_num /= 10;
			}
		}
		else
			return (1);

		/*check if is polindrome*/
		if (list_length == reverse_num)
			return (1);
	}
	return (0);
}
