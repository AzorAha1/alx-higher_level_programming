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
	listint_t *fast, *slow, *back, *left, *right;

	if (*head == NULL || !head || (*head)->next == NULL)
	{
		return (1);
	}
	fast = *head;
	slow = *head;
	while (fast && fast->next)
	{
		fast = fast->next->next;
		slow = slow->next;
	}
	*back = NULL;
	while (slow)
	{
		listint_t *temp;

		temp = slow->next;
		slow->next = back;
		back = slow;
		slow = temp;
	}
	left = *head;
	right = back;
	while (right)
	{
		if (left->n != right->n)
		{
			return (0);
		}
		left = left->next;
		right = right->next;
	}
	return (1);
}
