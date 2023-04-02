import pytest

from sceptre.exceptions import SceptreException
from resolver.from_json import FromJsonResolver


class TestFromJson(object):
    def setup_method(self, test_method):
        pass

    def test__json_string_in__dict_out(self):
        resolver = FromJsonResolver('{"aString":"plaintext", "aList":[1,2,3]}')
        out = resolver.resolve()
        assert out == {"aString": "plaintext", "aList": [1, 2, 3]}

    def test__malformed_string_in__SceptreException_raised(self):
        resolver = FromJsonResolver('{"aString"="plaintext", "aList":[1,2,3]}')
        with pytest.raises(SceptreException):
            resolver.resolve()

    def test__wrong_arg_type__SceptreException_raised(self):
        resolver = FromJsonResolver({"a": "dict"})
        with pytest.raises(SceptreException):
            resolver.resolve()
