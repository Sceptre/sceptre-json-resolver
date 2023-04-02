import json

from sceptre.exceptions import SceptreException
from sceptre.resolvers import Resolver


class ToJsonResolver(Resolver):
    def resolve(self):
        """
        resolve is the method called by Sceptre. It should carry out the work
        intended by this resolver. It should return a string to become the
        final value.
        """
        try:
            return json.dumps(self.argument)
        except json.JSONEncodeError as e:
            raise SceptreException("Error encoding JSON", e)
