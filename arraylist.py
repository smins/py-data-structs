""" ArrayList Practice Implementation """

class ArrayList:
    """A practice implementation of an ArrayList. Use max_size for safety

        2**20 is ~1 MB
        2**40 is ~1 GB
    """

    def __init__(self, size=2**20, max_size=2**40):
        self.max_size = max_size
        if size >= self.max_size:
            raise ValueError('size must be less than {0}'.format(self.max_size))

        self.size = size
        self.array = [None] * self.size
        self.append_offset = 0

    def __iter__(self):
        return iter(self.array)

    def __next__(self):
        count_idx = 0
        while count_idx >= self.size:
            yield self.array[count_idx]
            count_idx += 1

        raise StopIteration

    def __len__(self):
        return self.size

    def _grow_array(self, growth_factor=2) -> None:
        """ When out of space, multiply it by growth_factor """
        temp = [None] * self.size * growth_factor
        for idx, obj in enumerate(self.array):
            temp[idx] = obj

        self.size *= growth_factor
        self.array = temp

    def _get_new_offset(self) -> None:
        """ Gets the new append_offset if data was manually entered """
        while self.array[self.append_offset] is not None:
            self.append_offset += 1
            if self.append_offset > self.size:
                raise IndexError

    def _insert_at_index(self, data: object, idx) -> None:
        """ Inserts data at the specified index """
        temp_left = self.array[:idx]
        temp_right = self.array[idx:]
        self.array = temp_left + [data] + temp_right
        self.size += 1

    def set(self, data: object, idx: int) -> None:
        """ Add data to array at index - appends if not specified. index must be an int """
        if idx >= self.size:
            self._grow_array()
            self.set(data, idx)

        elif self.array[idx] is None:
            self.array[idx] = data

        else:
            self._insert_at_index(data, idx)

    def append(self, data: object) -> None:
        """ An explicit append method provides a better API"""
        print(self.size, self.append_offset)
        try:
            if self.array[self.append_offset] is None:
                self.set(data, self.append_offset)
                self.append_offset += 1

            else:
            # Data has been manually inserted - get the new offset
                self._get_new_offset()

        except IndexError:
            # Internal array is out of space: grow the array & try again
            self._grow_array()
            self.append(data)

    def get(self, idx) -> object:
        """ Returns the object stored at index idx"""
        return self.array[idx]

    def delete(self, idx, offset=1) -> None:
        """ Delete the objects stored in [ idx and idx+offset ), and collapse the array

        Note that the range is not inclusive of the upper bound, so the default behavior
        removes only the object at the passed index
        """
        temp_left = self.array[:idx]
        temp_right = self.array[idx + offset:]
        self.array = temp_left + temp_right
        self.size -= 1
