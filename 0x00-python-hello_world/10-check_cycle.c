#include "lists.h"

/**
 * check_cycle - Check if singly linked list has a cycle
 * @list: Pointer to the head of the linked list.
 * Return: 1 if there is a cycle, 0 if there is no cycle.
 */

int check_cycle(listint_t *list) {
	    listint_t *slow = list, *fast = list;

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
		{
			return 1;
		}
	}

	return 0;
}

