#include "lists.h"
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode, *temp;
	newnode = (listint_t *)malloc(sizeof(listint_t));
	if (!newnode)
	{
		return (NULL);
	}
	newnode->n = number;
	if (*head == NULL || (*head)->n > number)
	{
		newnode->next = *head;
		*head = newnode;
	}
	else
	{
		temp = *head;
		while (temp->next != NULL && temp->next->n < number)
		{
			temp = temp->next;
		}
		newnode->next = temp->next;
		temp->next = newnode;
	}
	return (newnode);
}
