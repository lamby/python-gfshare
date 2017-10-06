import pytest
import gfshare


def test_smoketest():
    result = gfshare.combine({
        113: b'\xe5\xcd\xb7i>"',
        59: b'\x00\x06\xde\x1ej\x83',
        4: b'\x9f\x08~\x10|\xec',
        181: b'N\xd7\xba\xb8\xbe\xa3',
        7: b'\xa8\\\x06\xee0\xae',
        153: b'PW\xdb\x1e\xc3V',
        228: b'\x86/{\x89C!',
        159: b'\x9cV\xc7\x05\xba\xf0',
        53: b'\xdf@\x17\xd6m>',
        175: b'\x9d\xc3q\x13(\xae',
    })

    assert result == b"secret"


def test_validate_empty():
    with pytest.raises(ValueError) as exc:
        gfshare.combine({})
    assert str(exc.value) == "size of shares must be > 1"


def test_validate_single():
    with pytest.raises(ValueError) as exc:
        gfshare.combine({0: b'foo'})
    assert str(exc.value) == "size of shares must be > 1"


def test_validate_keys():
    with pytest.raises(TypeError) as exc:
        gfshare.combine({0: b'foo', 1: b'bar'})
    assert str(exc.value) == "shares keys not comprised entirely of positive numbers"


def test_validate_values():
    with pytest.raises(TypeError) as exc:
        gfshare.combine({1: 'foo', 2: b'bar'})
    assert str(exc.value) == "shares values not comprised entirely of byte objects"


def test_validate_value_sizes():
    with pytest.raises(TypeError) as exc:
        gfshare.combine({1: b'foo', 2: b'barbaz'})
    assert str(exc.value) == "shares values not all bytes of the same length"
