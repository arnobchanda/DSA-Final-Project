# DSA-Final-Project

Final project for Data structures and algorithms class. This is a software artifact.

## Idea

Main idea is to use data structures to create a text editor which uses gap buffers and a doubly linked list to edit the buffers.

## Description

We first implement gap buffers, and test out how the text is processed with those.
Then we can implement a doubly linked list that basically take the gap buffer data structures and edit the text based on the gap position.
The gap position is the cursor position and we would be able to move the gap by adding or removing characters.
This is will be our primary implementation. Just adding and removing text using gap buffers and a doubly linked list.

## Implementation
1. The gap in gap buffer is set to 10.
2. The max size of a single buffer (with gap) is set to 50.
3. The initial size of the buffer is set to size of the gap (10).
4. The buffer size is then incremented based on characters entered (while keeping the gap size at 10).
5. A node will be created in this implementation when there is a space (' ') in the text initially.
6. In case of addition of a space(' ') while editing, no new nodes will be created.

## References

<https://www.cs.cmu.edu/~fp/courses/15122-f12/assignments/15-122-prog4-2.pdf>
