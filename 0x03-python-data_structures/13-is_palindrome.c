#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * is_palindrome - checks if linked list is a palindrome
 * @head: head 
 * Description - checks for palindrome
 * Return: returns 0 or 1
*/
int is_palindrome(listint_t **head)
{
    if (*head == NULL)
        return 1;
    listint_t *temp;
    int list_size;

    temp = *head;
    while (temp != NULL)
    {
        temp = temp->next;
        list_size++;
    }
    int i, j;
    listint_t *front, *back
    for (i = 0; i < list_size / 2; i++)
    {
        front = *head;
        back = *head;
        for (j = 0; j < i; j++)
        {
            front = front->next;
        }
        for (j = 0; j < size(i + 1); j++)
        {
            back = back->next;
        }
    }

}