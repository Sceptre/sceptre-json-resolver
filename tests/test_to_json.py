import json
import pytest

from resolver.to_json import ToJsonResolver
from sceptre.exceptions import SceptreException


class TestToJson(object):
    resolver = ToJsonResolver(argument=None)

    @pytest.mark.parametrize(
        "arg",
        [
            1,
            3.4,
            True,
            False,
            "invalid",
            [],
            ["one", "two"],
            {"key1": "value1"},
        ],
    )
    def test__invalid_data_in(self, arg):
        with pytest.raises(SceptreException):
            self.resolver.argument = arg
            self.resolver.resolve()

    @pytest.mark.parametrize(
        "arg",
        [
            # ["one"],
            [["one", "two"]],
            [{"key1": "value1"}],
            [{"key1": 4, "key2": ["a", "b"], "key3": {"key4": "val"}}],
        ],
    )
    def test__data_in__json_out(self, arg):
        self.resolver.argument = arg
        out = self.resolver.resolve()
        assert out == json.dumps(arg[0])
