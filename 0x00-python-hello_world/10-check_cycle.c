#include "lists.h"
int check_cycle(listint_t *list)
{
	listint_t *firstnode, *secondnode;
	firstnode = list;
	secondnode = list;
	while (firstnode && secondnode && firstnode->next)
	{
		firstnode = firstnode->next->next;
		secondnode = secondnode->next;
		if (firstnode == secondnode)
		{
			return (1);
		}
	}
	return (0);
}
