
def inverterLista(L : UnorderedList):
    prev = None
    current = L.head
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    L.head = prev
    return L