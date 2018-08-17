class MyLinkedList {
public:
    //int data;
    
    //MyLinkedList* next;

    
    /** Initialize your data structure here. */
    struct MyLinkedList1 {
        int data;
        
        MyLinkedList1* next = NULL;
    };
    
    MyLinkedList1* head;
    
    /** Get the value of the index-th node in the linked list. If the index is invalid, return -1. */
    int get(int index) {
        if (index < 0)
            return -1;
        MyLinkedList1* node = head;
        int count = 0;
        while (count != index
              && node != NULL)
        {
            node = node->next;
            count++;
        }
        if (node != NULL && count == index)
            return node->data;
        else
            return -1;
    }
    
    /** Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list. */
    void addAtHead(int val) {
        if (head == NULL)
        {
            head = new MyLinkedList1();
            head->data = val;
        }
        else
        {
            MyLinkedList1* node = new MyLinkedList1();
            node->data = val;
            node->next = head;
            head = node;
        }
    }
    
    /** Append a node of value val to the last element of the linked list. */
    void addAtTail(int val) {
        if (head == NULL)
        {
            head = new MyLinkedList1();
            head->data = val;
        }
        else
        {
            MyLinkedList1* node = head;
            while (node->next != NULL)
            {
                node = node->next;
            }
            MyLinkedList1* temp = new MyLinkedList1();
            node->next = temp;
            //node->next->next->data = val;
            temp->data = val;
        }
    }
    
    /** Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted. */
    void addAtIndex(int index, int val) {
        MyLinkedList1* prev = head;
        MyLinkedList1* cur = head;
        
        int count = 0;
        if (index == 0)
        {
            if (head == NULL)
            {
                head = new MyLinkedList1();
                head->data = val;
            }
            else
            {
                MyLinkedList1* node = new MyLinkedList1();
                node->data = val;
                node->next = head;
                head = node;   
            }
            
        }
        
        while (count != index 
              && cur != NULL)
        {
            prev = cur;
            cur = cur->next;
            count++;
        }
        if (cur == NULL
           && count == index && prev != NULL)
        {
            MyLinkedList1* node = new MyLinkedList1();
            node->data = val;
            prev->next = node;
        }          
        
        else if (count == index && prev != NULL)
        {
            MyLinkedList1* node = new MyLinkedList1();
            node->data = val;
            node->next = cur;
            prev->next = node;
        }        
    }
    
    /** Delete the index-th node in the linked list, if the index is valid. */
    void deleteAtIndex(int index) {
        int count = 0;
        if (head == NULL)
            return;
        if (index == 0
           && head->next == NULL)
        {
            delete head;
            head = NULL;
        }
        else if (index == 0)
        {
            MyLinkedList1* node = head;
            head = head->next;
            delete node;
        }
        else
        {
            MyLinkedList1* node = head;
            MyLinkedList1* prev = head;
            while (count != index 
                  && node != NULL)
            {
                prev = node;
                node = node->next;
                count++;
            }
            if (node == NULL)
                return;
            if (count == index)
            {
                if (node->next == NULL)
                {
                    delete node;
                    prev->next = NULL;
                }
                else
                {
                    prev->next = node->next;
                    delete node;
                }
            }
        }
    }
};

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList obj = new MyLinkedList();
 * int param_1 = obj.get(index);
 * obj.addAtHead(val);
 * obj.addAtTail(val);
 * obj.addAtIndex(index,val);
 * obj.deleteAtIndex(index);
 */
