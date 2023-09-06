#include "lists.h"
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode, *temp;
	int num;
	newnode = (listint_t *)malloc(sizeof(listint_t));
	if (!newnode)
	{
		return (NULL);
	}
	newnode->n = number;
	num = newnode->n;
	if (*head == NULL || (*head)->n < num)
	{
		newnode->next = *head;
		*head = newnode;
	}
	else
	{
		temp = *head;
		while (temp->next != NULL && temp->next->n < num)
		{
			temp = temp->next;
		}
		add_nodeint_end(head, num);
	}
	return (newnode);
}
