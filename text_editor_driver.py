from dll_text_buffer import *
from gap_buffer import *

class text_editor:
    def __init__(self):
        self.text_buffer = buffer()
        self.text_buffer.setup_buffer()
        
    def add_text(self, text):
        self.text_buffer.put_string_in_buffer(text)
    
    def move_cursor_left(self):
        if self.text_buffer.point_node.item.check_gap_is_left_extreme() is True:
            self.text_buffer.move_point_node_left()
        else:
            self.text_buffer.point_node.item.move_gap_left_by_one()
    
    def move_cursor_right(self):
        if self.text_buffer.point_node.item.check_gap_is_right_extreme() is True:
            self.text_buffer.move_point_node_right()
        else:
            self.text_buffer.point_node.item.move_gap_right_by_one()
            
    def insert_at_cursor(self, character):
        self.text_buffer.point_node.item.insert_character(character)
    
    def remove_at_cursor(self):
        self.text_buffer.point_node.item.delete_character()
        
    def print_final_buffer(self):
        display = self.text_buffer
        display.print_buffer_as_string()
        
    def show_buffer(self):
        self.text_buffer.show_buffer()
        
editor = text_editor()
editor.add_text("Hello this is a text")

editor.move_cursor_left()
editor.move_cursor_left()
editor.move_cursor_left()
editor.move_cursor_left()

editor.insert_at_cursor("m")

editor.move_cursor_right()
editor.move_cursor_right()

editor.remove_at_cursor()

editor.print_final_buffer()        