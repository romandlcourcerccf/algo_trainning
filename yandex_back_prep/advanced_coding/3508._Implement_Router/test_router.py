from router import Router


def test_router_add_packet():
    max_count = 5

    router = Router(max_count)

    for i in range(max_count + 1):
        res = router.addPacket(i, i, i)

        if i <= max_count:
            assert res
        else:
            assert not res


def test_router_get_count():
    max_count = 10

    router = Router(max_count)

    for i in range(max_count):
        if i < 5:
            router.addPacket(i, 0, i)
        else:
            router.addPacket(i, 1, i)

    print(router._packets_stack)

    assert router.getCount(1, 5, 9) == 5


def test_router_forward_packet():
    max_count = 10

    router = Router(max_count)

    assert router.forwardPacket() == []

    for i in range(max_count * 2):
        router.addPacket(i, 0, i)

    assert router.forwardPacket() == [i, 0, i]
