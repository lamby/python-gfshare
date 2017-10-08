import gfshare


def test_buffer_size():
    assert gfshare._BUFFER_SIZE > 1


def test_roundtrip():
    assert gfshare.combine(gfshare.split(10, 10, b"secret")) == b"secret"


def test_exceed_buffer():
    secret = b"X" * ((gfshare._BUFFER_SIZE * 2) + 1)

    split = gfshare.split(10, 10, secret)
    for x in split.values():
        assert len(x) == len(secret)

    assert gfshare.combine(split) == secret
