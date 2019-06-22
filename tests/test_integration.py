import gfshare


def test_buffer_size():
    assert gfshare._BUFFER_SIZE > 1


def test_roundtrip():
    assert gfshare.combine(gfshare.split(10, 10, b"secret")) == b"secret"


def test_breaks():
    shares = gfshare.split(10, 10, b"secret")
    shares.popitem()
    assert gfshare.combine(shares) != b"secret"


def test_exceed_buffer():
    secret = b"X" * ((gfshare._BUFFER_SIZE * 2) + 1)

    split = gfshare.split(10, 10, secret)
    for x in split.values():
        assert len(x) == len(secret)

    assert gfshare.combine(split) == secret


def test_embedded_null_byte():
    assert gfshare.combine(gfshare.split(10, 10, b"sec\x00ret")) == b"sec\x00ret"
