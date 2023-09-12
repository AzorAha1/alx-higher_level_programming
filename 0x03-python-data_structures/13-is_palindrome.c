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
	listint_t *fast, *slow;
	fast = *head;
	slow = *head;
	while (fast && fast->next)
	{
		fast = fast->next->next;
		slow = slow->next;
	}
	listint_t *back = NULL;

	while (slow)
	{
		listint_t *temp;

		temp = slow->next;
		slow->next = back;
		back = slow;
		slow = temp;
	}
	listint_t *left;
	listint_t *right;

	left = *head;
	right = back;
	while (right)
	{
		if (left->n != right->n)
		{
			left = left->next
			return (0);
		}
	}
	return (1);
}
