#!/usr/bin/python3
"""display-tree-by-line.py is a Python executable that implements the 
following test requirements:

Given a tree data structure, print the tree a level at a time, without
using extensive secondary storage. You may use a small amount of storage to
buffer a single row at a time.

The script supports printing by line both from the root down (assuming an
inverted tree) and from the leaves up. 

No user input is required.

Copyright 2015 Dean Stevens

Licensed under the MIT License (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://opensource.org/licenses/MIT

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

__author__ = "Dean Stevens"
__status__ = "Sample"
__version__ = "0.1.0"


class Node(object):
    """Node represents a single node in the tree.
    Note that we're using __slots__ to ensure that callers can't add data
    attributes to instances of the Node class.
    Properties:
        name - the name assigned to the node at creation, no setter / deleter
        subnodes - an iterator for the collection of child nodes, or None
                    if there are no children for a given node
        sub_cnt - the number of children for this node

    Methods:
        add_node() - add a new child to this node
    """
    
    # We won't create an __dict__, so users can't add more data attributes
    __slots__ = ["_name", "_children"]

    # Note that the name is fixed at creation time, accessed for retrieval
    # by the "name" property.
    def __init__(self, name):
        self._name = name
        self._children = []
    
    @property
    def  name(self):
        return self._name
    
    @property
    def subnodes(self):
        return iter(self._children) if self._children else None
    
    @property
    def sub_cnt(self):
        return len(self._children) if self._children is not None else 0
    
    def add_sub(self, new_node):
        self._children.append(new_node)
    
    def __str__(self):
        fstr = "Node: '{0}' - {1} subnodes"
        return fstr.format(self._name, self.sub_cnt)


class Data(object):
    """A Data object is used to keep track of the tree traversal. It also
    retains the maximum depth of the tree so that we can start the display
    at the deepest leaf level
    Note that we're using __slots__ to ensure that callers can't add data
    attributes to instances of the Data class.
    Properties:
        max_depth - length of the longest path through the tree, we use this
                    when printing leaf nodes first. Interface includes both
                    getter and setter
        curr_level - current level of an ongoing tree traversal. Interface
                    includes both getter and setter

    """
    __slots__ = ["_max_depth", "_curr_level"]

    # Initialize both internal data members to 0
    def __init__(self):
        self._max_depth = 0
        self._curr_level = 0

    @property
    def max_depth(self):
        return self._max_depth

    @max_depth.setter
    def max_depth(self, new_depth):
        self._max_depth = new_depth
    
    @property
    def curr_lev(self):
        return self._curr_level

    @curr_lev.setter
    def curr_lev(self, level):
        self._curr_level = level
    
    def __str__(self):
        fstr = "Curr Level: {0}; Max Depth: {1}"
        return fstr.format(self._curr_level, self._max_depth)


def trav_depth(start):
    """Test method that just walks the leftmost branch of the tree until it
    encounters that path's leaf

    Args:
        start - the node at which to start traversing
    """
    subs = start.subnodes
    if subs is not None:
        trav_depth(next(subs))
    
    print(start)


def walk_tree(start, data):
    """Walks the tree recursively, depth first, visiting every node. Uses
    the data object's max_depth to record the maximum path length through
    the tree.

    Args:
        start - the node at which to start traversing
        data - data object that will contain the maximum path length. Note
                that, because we're using this function recursively, we can't
                initialize the data object within the function. Therefore,
                we initialize the oject before calling this function and
                return the max_depth in the object
    Returns:
        via pass by object reference, a Data object containing the max_depth
        of the tree.
    """
    # We've moved one level deeper
    data.curr_lev += 1
    # If this is a new maximum depth, record it.
    data.max_depth = (data.curr_lev if data.curr_lev > data.max_depth 
                                    else data.max_depth)
    fstr = "walk_tree: {0}{1}"
    print(fstr.format(' '*data.curr_lev, start.name))
    subs = start.subnodes
    if subs is not None:
        for n in subs:
            walk_tree(n, data)
    # We've returned from the recursive call, so we're moving back up
    # the tree.
    data.curr_lev -= 1


def print_by_level(start, data):
    """Prints the tree level by level, both from the top down and from the
    bottom up. Note that the requirements didn't ask for printing only a
    specific level, but the nested function output_level() actually does
    exactly that.

    Args:
        start - the node at which to start traversing, most likely, this will
                be the root node.
        data - data object that will contain the maximum path length and will
                also maintain state information about the current level of
                the scan
    """
    def gather_level(head, level, outp, data):
        # gather_level() traverses the tree recursively, visiting all nodes at,
        # or above the specified level and buffers up all nodes at the
        # specified level for eventual output
        #
        # Args:
        #   head - the node at which to start traversing for this iteration
        #   level - the level of the tree that we'll be gathering into the
        #           buffer
        #   outp - the buffer
        #   data - data object that maintains state information about the
        #           current level of the scan
        #
        # Returns:
        #   outp - is passed as an object reference, so it may have additional
        #           nodes added
        #   data - may also be modified to reflect the current level of the
        #           traversal

        # We've moved one level deeper
        data.curr_lev += 1
        if data.curr_lev < level:
            # We're not at the desired level, yet, keep descending
            # recursively
            subs = head.subnodes
            if subs is not None:
                for n in subs:
                    gather_level(n, level, outp, data)
        else:
            # We're either at, or above, the desired level, if we're at the
            # desired level, add this node to the buffer
            if data.curr_lev == level:
                outp.append(head.name)

        # We've returned from the recursive call, so we're moving back up
        # the tree.
        data.curr_lev -= 1

    def output_level(head, at_level, data):
        # output_level() is a wrapper for gather_level() that initializes
        # the data object and prepares an empty output buffer.  Once
        # gather_level() has done it's job for the specified level, this
        # function prints the buffer along with the ID of the level.
        #
        # Args:
        #   head - the node at which to start traversing, typically the root
        #           of the tree
        #   at_level - the level of the tree that we'll be gathering for this
        #           iteration
        #   data - data object that maintains state information about the
        #           maximum depth of the tree, and the current level of the
        #           scan

        # Initialize the data object and the output buffer for this pass
        data.curr_lev = 0
        out_buf = []

        gather_level(start, at_level, out_buf, data)
        print("Level: {0} - {1}".format(at_level, ", ".join(out_buf)))
    
    # We'll do bottom up first,
    print("\nLeaf first...")
    for pl in range(data.max_depth, 0, -1):
        output_level(start, pl, data)
    
    # Then top down...
    print("\nFrom the root...")
    for pl in range(1, data.max_depth+1):
        output_level(start, pl, data)
        

def build_tree():
    """Builds a test tree and does the initial walk to establish the
    max_depth of the tree, as well as to display the tree in text form
    
    Returns:
        - The root node of the tree
        - An instance of Data that contains the maximum depth of the tree
    """
    n = Node("A")
    c = Node("AA")
    c.add_sub(Node("AAA"))
    c.add_sub(Node("AAB"))
    c.add_sub(Node("AAC"))
    n.add_sub(c)
    c = Node("AB")
    d = Node("ABA")
    d.add_sub(Node("ABAA"))
    d.add_sub(Node("ABAB"))
    c.add_sub(d)
    c.add_sub(Node("ABB"))
    d = Node("ABC")
    d.add_sub(Node("ABCA"))
    d.add_sub(Node("ABCB"))
    c.add_sub(d)
    n.add_sub(c)
    data = Data()
    walk_tree(n, data)
    print("Data is: {}".format(data))
    return n, data


if __name__ == '__main__':

    tree, data = build_tree()
    
    # There's no need to do the trav_depth, and walk_tree() is now handled
    # by build_tree()
    #trav_depth(tree)
    #walk_tree(tree)

    print_by_level(tree, data)

    print("\nDONE!\n")

