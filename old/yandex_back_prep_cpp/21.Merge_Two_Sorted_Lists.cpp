/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution
{
public:
    ListNode *mergeTwoLists(ListNode *list1, ListNode *list2)
    {
        ListNode *doom_node = new ListNode();
        ListNode *cur_node = doom_node;

        while (list1 != nullptr & list2 != nullptr)
        {
            if (list1->val <= list2->val)
            {
                cur_node->next = list1;
                cur_node = cur_node->next;
                list1 = list1->next;
            }
            else
            {
                cur_node->next = list2;
                cur_node = cur_node->next;
                list2 = list2->next;
            }
        }

        while (list1 != nullptr)
        {
            cur_node->next = list1;
            cur_node = cur_node->next;
            list1 = list1->next;
        }

        while (list2 != nullptr)
        {
            cur_node->next = list2;
            cur_node = cur_node->next;
            list2 = list2->next;
        }

        return doom_node->next;
    }
};

int main()
{
    return 0;
}