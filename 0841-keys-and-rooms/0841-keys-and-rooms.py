class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        room_keys = [True] + [False] * (len(rooms) - 1)
        for room_number in range(len(rooms)):
            if not room_keys[room_number]:
                return False
            for room_key in rooms[room_number]:
                room_keys[room_key] = True

        return True