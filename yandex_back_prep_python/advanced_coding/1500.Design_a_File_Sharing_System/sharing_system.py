from typing import List, Tuple
from collections import defaultdict


class FileSharing:
    def __init__(self, m: int):
        self._user_id = 0
        self._free_ids = []
        self._user_to_chanks = defaultdict(set)
        self._chank_to_users = defaultdict(set)

    def join(self, ownedChunks: List) -> int:
        user_id = self._get_next_user_id()

        self._user_to_chanks[user_id] = ownedChunks

        for chank in ownedChunks:
            self._chank_to_users[chank].add(user_id)

        return user_id

    def leave(self, userID: int) -> None:
        self._free_ids.append(userID)

        del self._user_to_chanks[userID]
        for chunkID in self._chank_to_users:
            if chunkID in self._chank_to_users[chunkID]:
                self._chank_to_users[chunkID].remove(userID)

    def request(self, userID: int, chunkID: int) -> List[int]:
        print("userID :", userID, " chunkID :", chunkID)
        print(self._chank_to_users)

        self._user_to_chanks[userID].append(chunkID)

        return sorted(self._chank_to_users[chunkID])

    def _get_next_user_id(self):
        if self._free_ids:
            return self._free_ids.pop()
        else:
            self._user_id += 1
            return self._user_id


#     FileSharing(m): Initialize the system with a file containing m chunks
# join(ownedChunks): Register a new user who owns the specified chunks, return their assigned ID
# leave(userID): Remove a user from the system, making their ID available for reuse
# request(userID, chunkID): User requests a specific chunk

# Returns a sorted list of all user IDs who own that chunk
# If the list is non-empty (meaning the chunk was found)
# , the requesting user also receives the chunk

# User joins with chunks [1,2] → gets ID 1
# User joins with chunks [2,3] → gets ID 2
# User joins with chunk [4] → gets ID 3
# User 1 requests chunk 3 → gets [2] (only user 2 has it), now user 1 has chunks [1,2,3]
# User 2 requests chunk 2 → gets [1,2] (both users have it)
# User 1 leaves → ID 1 becomes available
# User 2 requests chunk 1 → gets [] (no one has it after user 1 left)
# New user joins → gets ID 1 (reused)
