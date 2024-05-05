def merge(self, other_list):
        merged_list = LinkedList()

        current1 = self.head
        current2 = other_list.head

        while current1 is not None and current2 is not None:
            if current1.data < current2.data:
                merged_list.add_end(current1.data)
                current1 = current1.ref
            else:
                merged_list.add_end(current2.data)
                current2 = current2.ref

        # Append remaining elements from the first list
        while current1 is not None:
            merged_list.add_end(current1.data)
            current1 = current1.ref

        # Append remaining elements from the second list
        while current2 is not None:
            merged_list.add_end(current2.data)
            current2 = current2.ref

        return merged_list