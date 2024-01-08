class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        rooms_dict = {}
        for i in range(0, len(rooms)):
            rooms_dict[i] = rooms[i]
        visited = set()
        queue = [0]
        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                queue.extend(rooms_dict[node])
        if len(visited) == len(rooms):
            return True
        return False
