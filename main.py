from linked_list import DEFAULT_LINKED_LIST, LinkedList


if __name__ == '__main__':

    values = input("enter the set of data (strings) separated by comma(Default values are a,b,c,d,e,f): ")

    values = values if values else DEFAULT_LINKED_LIST

    linked = LinkedList()
    linked.create_nodes(values)
    print("-------------------------------")
    linked.print_list()
    print("-------------------------------")

    value = input("enter the letter to delete: ")

    linked.delete_node(value)
    print("-------------------------------")
    linked.print_list()
    print("-------------------------------")

