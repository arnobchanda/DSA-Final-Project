class gapbuffer:
    def __init__ (self, content):
        self.limit = 30
        self.gap_size = 11
        self.content = [None] * self.gap_size
        self.gap_start = 0
        self.gap_end = self.gap_size
        if (len(content) < self.limit):
            for i in range(len(content)):
                self.content.append(content[i]) 
            self.current_buffer_size = len(self.content)
        else:
            print("Cannot add more than 50 characters in this buffer")  
    
    def show_buffer (self):
        print(self.content)
        
    def show_buffer_information(self):
        print("Gap Start: {}".format(self.gap_start))
        print("Gap End: {}".format(self.gap_end))
        print("Gap Size: {}".format(self.gap_size))
        print("Current Buffer size: {}".format(self.current_buffer_size))

    def move_gap_left_by_one(self):
        if self.gap_start != 0:
            item_number_to_pop = self.gap_start - 1
            item = self.content[item_number_to_pop]
            
            item_number_to_place = (self.gap_start + self.gap_size) - 1
            self.content.pop(item_number_to_pop)
            self.content.insert(item_number_to_place, item)
            
            self.gap_start = item_number_to_pop
            self.gap_end = item_number_to_place
            return 0
        else:
            # print("Gap is at the leftmost position")
            return 1

    def move_gap_right_by_one(self):
        if self.gap_end != self.current_buffer_size:
            item_number_to_pop = self.gap_end
            item = self.content[item_number_to_pop]
            
            item_number_to_place = self.gap_start
            self.content.pop(item_number_to_pop)
            self.content.insert(item_number_to_place, item)
            
            self.gap_start = item_number_to_place + 1
            self.gap_end = item_number_to_pop + 1
            return 0
        else:
            # print("Gap is at the righmost position")
            return 1
    
    def move_gap_to_right_extreme(self):
        while self.move_gap_right_by_one() != 1:
            pass
    
    def move_gap_to_left_extreme(self):
        while self.move_gap_left_by_one() != 1:
            pass
    
    def check_gap_is_right_extreme(self):
        if self.content[len(self.content) - 1] == None:
            return True
        else:
            return False
        
    def check_gap_is_left_extreme(self):
        if self.content[0] == None:
            return True
        else:
            return False
    
    def insert_character(self, char):
        if self.current_buffer_size < self.limit:
            if self.gap_size > 1:
                if len(char) == 1:
                    item_number_to_pop = self.gap_start
                    self.content.pop(item_number_to_pop)
                    self.content.insert(item_number_to_pop, char)
                    
                    self.content.insert(self.gap_end, None)
                    
                    self.gap_start = self.gap_start + 1
                    self.gap_end = self.gap_end + 1
                    self.current_buffer_size = self.current_buffer_size + 1
                else:
                    print("Only one character at a time")
            else:
                print("No gap space availaible to edit")
        else:
            if self.current_buffer_size == self.limit:
                if self.gap_size > 1:
                    if len(char) == 1:
                        item_number_to_pop = self.gap_start
                        self.content.pop(item_number_to_pop)
                        self.content.insert(item_number_to_pop, char)
                        
                        self.gap_start = self.gap_start + 1
                        self.gap_size = self.gap_size - 1
                    else:
                        print("Only one char at a time")
                else:
                    print("No gap space availaibe")
    
    def delete_character(self):
        if self.gap_start != 0:
            if self.gap_size == 11:
                item_number_to_pop = self.gap_start - 1
                self.content.pop(item_number_to_pop)
                
                self.gap_start = self.gap_start - 1
                self.gap_end = self.gap_end - 1
                self.current_buffer_size = self.current_buffer_size - 1
            else:
                if self.gap_size < 11:                    
                    item_number_to_pop = self.gap_start - 1
                    self.content.pop(item_number_to_pop)
                    self.content.insert(item_number_to_pop, None)
                    
                    self.gap_start = self.gap_start - 1
                    self.gap_size = self.gap_size + 1
        else:
            print("No character before.")
            
    def show_text_in_buffer(self):
        text = self.content
        del text[self.gap_start:self.gap_end]
        s = ""
        s = s.join(text)
        # print(s)
        return s

# gb = gapbuffer("Hello")
# gb.show_buffer()
# gb.show_buffer_information()

# # gb.show_text_in_buffer()
# print("\n")

# gb.move_gap_to_right_extreme()
# gb.show_buffer()
# print(gb.check_gap_is_left_extreme())
# print(gb.check_gap_is_right_extreme())
# # gb.show_buffer_information()

# print("\n")

# gb.move_gap_to_left_extreme()
# gb.show_buffer()
# print(gb.check_gap_is_left_extreme())
# print(gb.check_gap_is_right_extreme())
# gb.show_buffer_information()

# for i in range(6):
#     gb.move_gap_right_by_one()
#     gb.show_buffer()

# gb.show_buffer_information()

# print("\n")

# for i in range(6):
#     gb.move_gap_left_by_one()
#     gb.show_buffer()

# gb.show_buffer_information()

# print("\n")

# new_addition = "World is mine"
# for i in range(len(new_addition)):
#     gb.insert_character(new_addition[i])
#     gb.show_buffer()

# gb.show_buffer_information()

# print("\n")

# for i in range(6):
#     gb.delete_character()
#     gb.show_buffer()

# gb.show_buffer_information()
