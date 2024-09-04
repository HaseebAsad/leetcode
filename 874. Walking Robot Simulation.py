class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # Idea is to have a store of a variable called direction. Then add to the vector based on position with if statements. Change direction if -1 or -2. Need to think about logic for directions: maybe a pole vector in clockwise order? And check for obstacles by checking if new_pos is in obstacles (BUT MUST ALSO INCLUDE RUNNING THROUGH... THIS MAKES IT QUITE A BIT HARDER). If yes, ignore new_pos and move to next instruction.
        poles = ['N', 'E', 'S', 'W']
        direction = poles[0] # initially facing north.
        pos = (0,0)
