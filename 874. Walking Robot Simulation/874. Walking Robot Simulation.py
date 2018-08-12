class Solution:
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        dire = ["N", "E", "S", "W"]
        obstacles = dict(obstacles)
        dire_index_now = 0
        for each_command in commands:
            if each_command == -1:
                dire_index_now = (dire_index_now + 1) % 4
            elif each_command == -2:
                dire_index_now = (dire_index_now - 1) % 4
            else:



