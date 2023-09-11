#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * is_palindrome - function name
 * @head: head pointer
 * Description - function to find if the linked list is a palindrome
 * Return: return 0 or 1
 */
int is_palindrome(listint_t **head)
{
	if (!(*head) || !head || !(*head)->next)
	{
		return (1);
	}

	listint_t *temp;
	int list_size;

	temp = *head;
	while (temp != NULL)
	{
		temp = temp->next;
		list_size++;
	}
	int i, j;
	listint_t *front, *back;

	while (front != NULL && back != NULL)
	{
		for (i = 0; i < list_size / 2; i++)
		{
			front = *head;
			back = *head;
			for (j = 0; j < i; j++)
			{
				front = front->next;
			}
			for (j = 0; j < list_size - (i + 1); j++)
			{
				back = back->next;
			}
			if (front->n != back->n)
			{
				return (0);
			}
		}
	}
	return (1);
}
