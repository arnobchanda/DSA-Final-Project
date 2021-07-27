class gapbuffer:
    def __init__ (self, content, gap_size=11):
        self.limit = 11
        self.gap_size = gap_size
        self.content = [None] * gap_size
        self.gap_start = 0
        self.gap_end = gap_size
        if (len(content) < self.gap_size):
            for i in range(len(content)):
                self.content[i] = content[i]
            self.gap_start = len(content)
            self.gap_end = gap_size
            self.gap_size = self.gap_end - self.gap_start
        else:
            print("Cannot add more than 10 characters in this buffer")  
    
    def show_buffer (self):
        print(self.content)
        # print(self.gap_start)
        # print(self.gap_end)
        # print(self.gap_size)

    def move_gap_left_by_one(self):
        if self.gap_start != 0:
            item_number_to_pop = self.gap_start - 1
            item = self.content[item_number_to_pop]
            
            item_number_to_place = (self.gap_start + self.gap_size) - 1
            self.content.pop(item_number_to_pop)
            self.content.insert(item_number_to_place, item)
            
            self.gap_start = item_number_to_pop
            self.gap_end = item_number_to_place
        else:
            print("Gap is at the leftmost position")

    def move_gap_right_by_one(self):
        if self.gap_end != self.limit:
            item_number_to_pop = self.gap_end
            item = self.content[item_number_to_pop]
            
            item_number_to_place = self.gap_start
            self.content.pop(item_number_to_pop)
            self.content.insert(item_number_to_place, item)
            
            self.gap_start = item_number_to_place + 1
            self.gap_end = item_number_to_pop + 1
        else:
            print("Gap is at the righmost position")
    
    def insert_character(self, char):
        if self.gap_size > 1:
            if len(char) == 1:
                item_number_to_pop = self.gap_start
                self.content.pop(item_number_to_pop)
                self.content.insert(item_number_to_pop, char)
                
                self.gap_start = self.gap_start + 1
                self.gap_size = self.gap_size - 1
            else:
                print("Only one character at a time")
        else:
            print("No gap space availaible to edit")
    
    def delete_character(self):
        if self.gap_start != 0:
            item_number_to_pop = self.gap_start - 1
            self.content.pop(item_number_to_pop)
            self.content.insert(item_number_to_pop, None)
            
            self.gap_start = self.gap_start - 1
            self.gap_size = self.gap_size + 1
        else:
            print("No character before.")
            
class Node:
    def __init__(self,data):
            self.item = data
            self.prev = None
            self.next = None
            
class dll:
    def __init__(self):
        self.start_node = None
        
gb = gapbuffer("Hello")
for i in range(6):
    gb.move_gap_left_by_one()
    gb.show_buffer()

print("\n")

for i in range(6):
    gb.move_gap_right_by_one()
    gb.show_buffer()

print("\n")

new_addition = "World"
for i in range(len(new_addition)):
    gb.insert_character(new_addition[i])
    gb.show_buffer()

print("\n")

for i in range(6):
    gb.delete_character()
    gb.show_buffer()
