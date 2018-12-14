#  File: Josephus.py

#  Description:Circular Linked List

#  Student Name: William Kown

#  Student UT EID: uk669

#  Partner Name:Brandon Ford

#  Partner UT EID:bef528

#  Course Name: CS 313E

#  Unique Number:51350

#  Date Created:11/7/18

#  Date Last Modified:11/9/18
class Link(object):
  def __init__ (self, data, next = None):
    self.data = data
    self.next = next

class CircularList(object):
  # Constructor
  def __init__ ( self ):
    self.first = None

  # Insert an element in the list
  def insert ( self, data ):
      newLink = Link(data)
      current = self.first
      if (current == None):
          self.first = newLink
          newLink.next = newLink
          return
      while (current.next != self.first):
          current = current.next
      current.next = newLink
      newLink.next = self.first
  def find ( self, data ):
      current = self.first

      while (current.data != data):
          current = current.next

      return current

  # Delete a link with a given key
  def delete ( self, data ):
    current = self.first
    previous = self.first
    while previous.next != self.first:
      previous = previous.next
    if current == None:
      return None
    else:
      if current.next == self.first and current.data == data:
        return current
    while (current.data !=data):
      if current.next == self.first:
        return None
      else:
        previous = current
        current = current.next
    if current == self.first:
      self.first = self.first.next
    previous.next = current.next
    return current


  # Delete the nth link starting from the Link start
  # Return the next link from the deleted Link
  def deleteAfter ( self, start, n ):
    pos = self.first
    deaths = ""
    while start != 1:
      pos = start.pos.next
      pos -= 1
    while pos.next != pos:
      for i in range(n - 1):
        pos = pos.next
      value = pos.data
      death = self.delete(value)
      deaths += str(death.data) + " "
      pos = pos.next
    print (deaths)
    print(pos.data)
  def __str__ ( self ):
      str = ''
      current = self.first
      while (current.next != self.first):
          str += str(current.data) + " "
          current = current.next
      return str

def main():
  in_file = open("josephus.txt", "r")
  soldier = int(in_file.readline())
  start = int(in_file.readline())
  elimination = int(in_file.readline())
  cirList = CircularList()
  for i in range (1, soldier + 1):
    cirList.insert(i)
  if cirList.first != None:
    cirList.deleteAfter(start, elimination)
  else:
    print(cirList)
main()

