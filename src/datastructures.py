
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [{
            "id" : self . _generateId (),
             "first_name" : "John" ,
             "last_name" : last_name,
             "age": "33",
             "Lucky Numbers" : "7,13,22"
        },
        {
            "id" : self . _generateId (),
             "first_name" : "Jane" ,
             "last_name" : last_name,
             "age": "35",
             "Lucky Numbers" : "10,14,3"
        },
        {
            "id" : self . _generateId (),
             "first_name" : "Jimmy" ,
             "last_name" : last_name,
             "age": "5",
             "Lucky Numbers" : "1"
        }]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self,first_name,age,Lucky_numbers):

        new_member={"id" : self . _generateId (),
        "last_name" : self.last_name,
        "first_name" : first_name,
        "age" : age,
        "Lucky_numbers" : Lucky_numbers
        
        }
        self._members.append(new_member)
        return self._members
        # fill this method and update the return
        pass

    def delete_member(self, id):
        self._members.pop(id)
        return self._members

        # fill this method and update the return
        pass

    def get_member(self, id):
        memberselec=self._members[id]
        return memberselec




        # fill this method and update the return
        pass

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
