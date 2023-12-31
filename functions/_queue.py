class QueueMixin: # Mixin allows us to separate our methods from queue_commands.py. 
                  # We are simply adding these functions to the QueueCommands class but storing them in this file.

    def join_queue(self, role, document):
            # default message to send (success)
            message = f"Success! You joined the queue as {role}."

            # Make sure desired role is open and valid as well as check for duplicate queues

            role = role.lower() # Get role in lowercase for comparison below

            # CHECK IF ALREADY IN QUEUE
            if document in (self.tank_queue or self.dps_queue or self.support_queue):
                message = "You are already in queue. Use `!change <role>` to change roles."
                return message
            
            # TANK ROLE
            if (role == "tank"): 
                if (len(self.tank_queue) < 2):
                    self.tank_queue.append(document)
                else:
                    message = "Tank queue full. Use `!status` to check the queued roles."
                    return message
            
            # DPS ROLE
            elif (role == "dps"):
                if (len(self.dps_queue) < 4):
                    self.dps_queue.append(document)
                else:
                    message = "DPS queue full. Use `!status` to check the queued roles."
                    return message

            # SUPPORT ROLE
            elif (role == "support"):
                if (len(self.support_queue) < 4):
                    self.support_queue.append(document)
                else:
                    message = "Support queue full. Use `!status` to check the queued roles."
                    return message
                
            # INVALID ROLE WAS GIVEN
            else:
                message = "Please enter a valid role (tank, dps, support)."
                return message
            
            return message



    def leave_queue(self, document):
        # Find what queue the player is in and leave it.
        if document in self.tank_queue:
            self.tank_queue.remove(document)
        elif document in self.dps_queue:
            self.dps_queue.remove(document)
        elif document in self.support_queue:
            self.support_queue.remove(document)
        # Player is not in queue
        else:
            message = "You are not in queue. Join with `!join <role>`"
            return message
        
        message = "Successfully left queue!"
        return message
    

    def get_name(self, doc, mention=True):
        if mention:
            return f"<@{doc['_id']}>"
        else:
            return doc['name'].split('#')[0]
    
    def display_teams(self, team1, team2, team1_average, team2_average):
        # team are represented in a tuple -> tank, first_dps, second_dps, first_support, second_support

        # return the string to print out
        return (
        f"---------------------------------------\n" \
        f"Team 1:\nTank: {self.get_name(team1[0])}\nDPS: {self.get_name(team1[1])} and {self.get_name(team1[2])}\nSupport: {self.get_name(team1[3])} and {self.get_name(team1[4])}\n" \
        f"\nTeam 2:\nTank: {self.get_name(team2[0])}\nDPS: {self.get_name(team2[1])} and {self.get_name(team2[2])}\nSupport: {self.get_name(team2[3])} and {self.get_name(team2[4])}\n" \
        f"\nTeam 1 Average SR: {round(team1_average)}\nTeam 2 Average SR: {round(team2_average)}\n" \
        f"---------------------------------------"
        )
