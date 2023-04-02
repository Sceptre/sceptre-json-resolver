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
        typ = type(self.argument)
        try:
            if typ is str:
                return json.loads(self.argument)
            else:
                raise SceptreException(
                    f"!from_json expects a string argument, got: {typ}"
                )
        except json.JSONDecodeError as e:
            raise SceptreException("Error decoding JSON", e)
