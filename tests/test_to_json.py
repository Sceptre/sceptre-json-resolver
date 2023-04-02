import json

from resolver.to_json import ToJsonResolver


class TestToJson(object):
    def setup_method(self, test_method):
        pass

    def test__data_in__json_out(self):
        test_values = [
            1,
            3.4,
            "plain string",
            '{"string_that_is":"valid_json"}',
            True,
            False,
            {"key1": 4, "key2": ["a", "b"], "key3": {"key4": "val"}},
        ]
        for value in test_values:
            resolver = ToJsonResolver(value)
            out = resolver.resolve()
            assert json.loads(out) == value
