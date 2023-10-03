#include "lists.h"

/**
 * insert_node - mallocs and inserts node into sorted singly linked list
 * @head: pointer to head of list
 * @number: new node data
 * Return: address of new node, or NULL if failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmpry= NULL;
	listint_t *new_l = NULL;

	if (!head)
		return (NULL);

	new_l = malloc(sizeof(listint_t));
	if (new_l == NULL)
		return (NULL);
	new_l->n = number;
	new_l->next = NULL;

	if (*head == NULL)
	{
		*head = new_l;
		(*head)->next = NULL;
		return (new_l);
	}

	if ((*head)->next == NULL)
	{
		if ((*head)->n < new_l->n)
			(*head)->next = new_l;
		else
		{
			new_l->next = *head;
			*head = new_l;
		}
		return (new_l);
	}

	tmpry = *head;
	while (tmpry->next != NULL)
	{
		if (new_l->n < tmpry->n)
		{
			new_l->next = tmpry;
			*head = new_l;
			return (new_l);
		}
		if (((new_l->n > tmpry->n) && (new_l->n < (tmpry->next)->n)) ||
		    (new_l->n == tmpry->n))
		{
			new_l->next = tmpry->next;
			tmpry->next = new_l;
			return (new_l);
		}
		tmpry = tmpry->next;
	}
	tmpry->next = new_l;
	return (new_l);
}
