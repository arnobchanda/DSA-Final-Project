from gap_buffer import *

class dll_node:
    def __init__(self,data):
            self.item = gapbuffer(data)
            self.prev = None
            self.next = None
            
class buffer:
    def __init__(self):
        self.start_node = None
        self.end_node = None
        self.point_node = None
        self.no_of_nodes = 0
        self.point_node_location = 0
        
    def setup_buffer(self):
        start_node = dll_node("startnode")
        point_node = dll_node("init")
        end_node = dll_node("endnode")
        
        start_node.prev = None
        start_node.next = point_node
        
        point_node.prev = start_node
        point_node.next = end_node
        
        end_node.prev = point_node
        end_node.next = None
        
        self.start_node = start_node
        self.point_node = point_node
        self.end_node = end_node
        self.no_of_nodes = 3
        self.point_node_location = 2
    
    def add_node_before_end_node(self, data):
        if self.point_node is None:
            print("Buffer not initialized properly. Run setup buffer and then call this function")
        else:
            next_point_node = dll_node(data)
            self.point_node.next = next_point_node
            next_point_node.prev = self.point_node
            
            next_point_node.next = self.end_node
            self.end_node.prev = next_point_node
            
            self.point_node = next_point_node
            self.no_of_nodes = self.no_of_nodes + 1
            self.point_node_location = self.point_node_location + 1 
    
    def put_string_in_buffer(self, text_string):
        list_of_words=text_string.split(" ")
        
        self.point_node.item = gapbuffer(list_of_words[0])
        self.point_node.item.move_gap_to_right_extreme()
        
        for word in range(1, len(list_of_words)):
            self.add_node_before_end_node(list_of_words[word])
            self.point_node.item.move_gap_to_right_extreme()
    
    def move_point_node_left(self):
        if self.point_node_location > 1:    
            self.point_node.item.move_gap_to_left_extreme()
            self.point_node = self.point_node.prev
            
            self.point_node_location = self.point_node_location - 1
        else:
            print("At the leftmost data node")
    
    def move_point_node_right(self):
        if self.point_node_location < self.no_of_nodes - 1:
            self.point_node.item.move_gap_to_right_extreme()
            self.point_node = self.point_node.next
            
            self.point_node_location = self.point_node_location + 1
        else:
            print("At the rightmost data node")
    
    def print_buffer_as_string(self):
        text = []
        start_node = self.start_node.next
        for n in range(self.no_of_nodes - 2):
            text.append(start_node.item.show_text_in_buffer())
            start_node = start_node.next
        
        sep = " "
        sep = sep.join(text)
        print(sep)
    
    def show_buffer(self):
        point_node = self.start_node
        data = []
        for i in range(self.no_of_nodes):
            data.append(point_node.item.content)
            point_node = point_node.next
        print(*data, sep= "\n")
        
    def show_buffer_info(self):
        print("No of Nodes: {}".format(self.no_of_nodes))
        print("Point node location: {}".format(self.point_node_location))
    
# text_buffer = buffer()
# # text_buffer.setup_buffer()
# # text_buffer.show_buffer() 
# text_buffer.put_string_in_buffer("This is a string")
# text_buffer.show_buffer() 
# text_buffer.show_buffer_info()

# print("\n")

# text_buffer.move_point_node_left()
# text_buffer.show_buffer()
# text_buffer.show_buffer_info()

# print("\n")

# text_buffer.move_point_node_right()
# text_buffer.show_buffer()
# text_buffer.show_buffer_info()

# print("\n")

# text_buffer.move_point_node_right()
# text_buffer.show_buffer()
# text_buffer.show_buffer_info()

# print("\n")
# text_buffer.print_buffer_as_string()