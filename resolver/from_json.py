import json

from sceptre.exceptions import SceptreException
from sceptre.resolvers import Resolver


class FromJsonResolver(Resolver):
    def resolve(self):
        """
        resolve is the method called by Sceptre. It should carry out the work
        intended by this resolver. It should return a string to become the
        final value.
        """
        arg = self.argument
        try:
            if isinstance(arg, list):
                arg_count = len(arg)
                if arg_count != 1:
                    raise SceptreException(
                        f"!from_json expects exactly one argument, got {arg_count}"
                    )
                return json.dumps(arg[0])

            raise SceptreException(
                f"!from_json expects a string argument, got {type(arg)}"
            )

        except json.JSONDecodeError as e:
            raise SceptreException("Error decoding JSON", e)
