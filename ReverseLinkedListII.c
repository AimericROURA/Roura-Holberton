/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseBetween(struct ListNode* head, int left, int right) {

    struct ListNode* newHead = head;

    //We don't have to do anything if left == right
    if(left != right){

        //Three-pointer technique used to reverse the sublist
        struct ListNode* prev = NULL;
        struct ListNode* current = head;
        struct ListNode* next = NULL;

        //We need the starting nodes to reconnect the sublist at the end
        struct ListNode* beforeFirst = NULL;
        struct ListNode* first = NULL;

        //Looking at every node
        for (int i = 1; i <= right; i++) {
            next = current->next;

            //We store the last node before the sublist
            if (i == left){
                if(prev != NULL) //If the head is in the sublist, we don't need a beforeFirst
                    beforeFirst = prev;

                first = current;
            }

            //We are in the sublist
            if((i >= left + 1) && (i <= right)){
                //Reversing the node
                current->next = prev;
            }

            //If we are at the end, we reconnect the sublist
            if (i == right){
                first->next = next;

                if(beforeFirst != NULL) 
                    beforeFirst->next = current;
                else //left == 1, so the new start of the sublist becomes newHead
                    newHead = current;
            }
        
            prev = current;
            current = next;
        }
    }

    return newHead;
}