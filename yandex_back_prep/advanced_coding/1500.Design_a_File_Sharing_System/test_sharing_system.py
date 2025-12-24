from sharing_system import FileSharing


# User joins with chunks [1,2] → gets ID 1
# User joins with chunks [2,3] → gets ID 2
# User joins with chunk [4] → gets ID 3
# User 1 requests chunk 3 → gets [2] (only user 2 has it), now user 1 has chunks [1,2,3]
# User 2 requests chunk 2 → gets [1,2] (both users have it)
# User 1 leaves → ID 1 becomes available
# User 2 requests chunk 1 → gets [] (no one has it after user 1 left)
# New user joins → gets ID 1 (reused)


def test_file_system():
    fs = FileSharing(m=100)

    assert fs.join([1, 2]) == 1
    assert fs.join([2, 3]) == 2
    assert fs.join([4]) == 3

    assert fs.request(1, 3) == [2]
    assert fs.request(2, 2) == [1, 2]

    assert fs.leave(1) is None

    assert fs.request(2, 1) == []

    assert fs.join([5, 6]) == 1
