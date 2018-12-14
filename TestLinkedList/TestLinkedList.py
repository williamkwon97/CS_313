#  File: TestLinkedList.py

#  Description: defining a link list with multiple helper functions

#  Student Name: William Kwon

#  Student UT EID: uk669

#  Partner Name: Brandon Ford

#  Partner UT EID: bef528

#  Course Name: CS 313E

#  Unique Number: 51350

#  Date Created: 11/3/18

#  Date Last Modified: 11/4/18


class Link (object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList (object):
    def __init__(self):
        self.first = None
        self.length = 0

    # add an item at the beginning of the list
    def insert_first(self, data):
        new_link = Link(data)

        new_link.next = self.first
        self.first = new_link
        self.length += 1
        print(new_link)
        print(new_link.next)


    # add an item at the end of a list
    def insert_last(self, data):
        new_link = Link(data)

        current = self.first
        if(current == None):
            self.first = new_link
            self.length += 1
            return

        while(current.next != None):
            current = current.next

        current.next = new_link
        self.length += 1
        print(current)
        print(current.next)
        print(self.first)

    # Delete and return Link from an unordered list or None if not found
    def delete_link(self, data):
        previous = self.first
        current = self.first

        if (current == None):
            return None

        while (current.data != data):
            if (current.next == None):
                return None
            else:
                previous = current
                current = current.next

        if(current == self.first):
            self.first = self.first.next
            self.length -= 1
        else:
            previous.next = current.next
            self.length -= 1

        return current

        # get number of links
    def get_num_links(self):
        return self.length

        # add an item in an ordered list in ascending order
    def insert_in_order(self, data):

        new_link = Link(data)

        current = self.first

        # if the list is empty
        if (current == None):
            self.first = new_link
            self.length += 1
            return
        # if the first link is less than the new link
        elif self.first.data >= data:
            new_link.next = self.first
            self.first = new_link
            self.length += 1
        else:
            while (current.next != None) and (current.next.data < data):
                current = current.next

            new_link.next = current.next
            current.next = new_link
            self.length += 1
            return

        # search in an unordered list, return None if not found
    def find_unordered(self, data):

        current = self.first

        if current == None:
            return None
        else:
            while current.data != data:
                if current.next == None:
                    return None
                else:
                    current = current.next


            return current

        # Search in an ordered list, return None if not found
    def find_ordered(self, data):

        current = self.first

        if current == None:
            return None

        while current.data != data:
            if current.next == None:
                return None
            else:
                current = current.next

        return current

        # String representation of data 10 items to a line, 2 spaces between data
    def __str__(self):
        count = 0
        link_str = ''
        current = self.first

        if current == None:
            return 'Empty'

        while current != None:
            if count % 10 == 0 and count != 0:
                link_str += '\n' + str(current.data) + '  '
                current = current.next
                count += 1
            else:
                link_str += str(current.data) + '  '
                current = current.next
                count += 1

        return link_str

        # Copy the contents of a list and return new list
    def copy_list(self):

        new_list = LinkedList()

        current = self.first

        while current.next != None:
            new_list.insert_last(current.data)
            current = current.next
        new_list.insert_last(current.data)

        return new_list

        # Reverse the contents of a list and return new list
    def reverse_list(self):

        new_list = LinkedList()

        current = self.first

        while current.next != None:
            new_list.insert_first(current.data)
            current = current.next
        new_list.insert_first(current.data)

        return new_list

        # Sort the contents of a list in ascending order and return new list
    def sort_list(self):

        new_list = LinkedList()

        current = self.first

        while current.next != None:
            new_list.insert_in_order(current.data)
            current = current.next
        new_list.insert_in_order(current.data)

        return new_list

        # Return True if a list is sorted in ascending order or False otherwise
    def is_sorted(self):

        current = self.first

        while current.next != None:
            if current.data > current.next.data:
                return False
            current = current.next

        return True

        # Return True if a list is empty or False otherwise
    def is_empty(self):

        current = self.first

        if current == None:
            return True

        return False

        # Merge two sorted lists and return new list in ascending order
    def merge_list(self, other):

        new_list = LinkedList()
        current = self.first

        while (current != None):
            new_list.insert_last(current.data)
            current = current.next

        current_other = other.first

        while (current_other != None):
            new_list.insert_last(current_other.data)
            current_other = current_other.next

        new_list = new_list.sort_list()

        return new_list


        # Test if two lists are equal, item by item and return True
    def is_equal(self, other):

        current = self.first
        current_other = other.first

        if self.length != other.length:
            return False

        while current.next != None and current_other.next != None:

            if current.data != current_other.data:
                return False
            else:
                current = current.next
                current_other = current_other.next

        return True

        # Return a new list, keeping only the first occurence of an element
        # and removing all duplicates. Do not change the order of the elements.
    def remove_duplicates(self):

        new_list = LinkedList()

        current = self.first

        while current != None:
            second = current.next
            while second != None:
                if second.data == current.data:
                    current.next = second.next
                second = second.next
            current = current.next

        current = self.first

        while current != None:
            new_list.insert_last(current.data)
            current = current.next

        return new_list

def main():

    # Test methods insert_first() and __str__() by adding more than
    # 10 items to a list and printing it.

    lst = LinkedList()
    lst2 = LinkedList()


    # Test method insert_last()




    # Test method insert_in_order()

    lst.insert_in_order(23)
    lst.insert_in_order(6)
    lst.insert_in_order(77)
    lst.insert_in_order(45)
    lst.insert_in_order(45)
    lst.insert_in_order(77)
    print(lst)


    lst2.insert_in_order(23)
    lst2.insert_in_order(6)
    lst2.insert_in_order(77)
    lst2.insert_in_order(45)
    lst2.insert_in_order(1)

    # Test method get_num_links()

    print(lst.get_num_links())

    # Test method find_unordered()
    # Consider two cases - data is there, data is not there

    print(lst.find_unordered(45)!= None)
    print(lst.find_unordered(100)== None)

    # Test method find_ordered()
    # Consider two cases - data is there, data is not there

    print(lst.find_ordered(66) == None)
    print(lst.find_ordered(100) != None)

    # Test method delete_link()
    # Consider two cases - data is there, data is not there
    lst.delete_link(4)
    lst.delete_link(100)
    print(lst)
    # Test method copy_list()
    print(lst.copy_list())
    # Test method reverse_list()
    print(lst.reverse_list())
    # Test method sort_list()
    print(lst.sort_list())
    # Test method is_sorted()
    # Consider two cases - list is sorted, list is not sorted
    print(lst.is_sorted())
    # Test method is_empty()
    print(lst.is_empty())
    # Test method merge_list()
    print(lst.merge_list(lst2))
    # Test method is_equal()
    # Consider two cases - lists are equal, lists are not equal
    print(lst.is_equal(lst2))
    # Test remove_duplicates()
    print(lst.remove_duplicates())


if __name__ == "__main__":
    main()