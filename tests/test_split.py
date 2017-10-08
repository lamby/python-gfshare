import pytest
import gfshare


def test_smoketest():
    secret = b"secret"
    result = gfshare.split(10, 10, secret)

    assert len(result) == 10
    assert isinstance(result, dict)

    for k, v in result.items():
        assert isinstance(k, int)
        assert isinstance(v, bytes)
        assert len(v) == len(secret)


def test_random_results():
    assert gfshare.split(10, 10, b"secret") != \
        gfshare.split(10, 10, b"secret")


def test_validate_threshold():
    with pytest.raises(ValueError) as exc:
        gfshare.split(0, 10, b"secret")
    assert str(exc.value) == "threshold must be >= 1"


def test_validate_sharecount():
    with pytest.raises(ValueError) as exc:
        gfshare.split(1, 1, b"secret")
    assert str(exc.value) == "sharecount must be >= 2"


def test_validate_sharecount_threshold():
    with pytest.raises(ValueError) as exc:
        gfshare.split(3, 2, b"secret")
    assert str(exc.value) == "sharecount must be >= threshold"


def test_huge_split():
    max_ = gfshare.MAX_SHARECOUNT

    assert gfshare.split(max_, max_, b"secret")

    with pytest.raises(ValueError) as exc:
        gfshare.split(max_ + 1, max_ + 1, b"secret")
    assert str(exc.value) == "sharecount must be < {}".format(max_)


def test_validate_type():
    with pytest.raises(TypeError) as exc:
        gfshare.split(10, 10, "str")
    assert str(exc.value) == "a bytes-like object is required, not 'str'"
