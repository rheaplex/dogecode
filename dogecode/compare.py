
class TokenList(object):
    """A class to keep track of a list of tokens"""

    def __init__(self):
        """Create a new empty list"""
        self.tokens = []

    def append(self, token, count):
        """Append the token count to the list"""
        self.tokens.append((token, count))

    def from_json(self, json):
        """Initialize the token list from a json rpc query response"""
        for send in json:
            self.append(send["asset"], send["quantity"])

    def equals(self, other):
        """Compare the token list with another token list.
           Return True if the list is equal, false if not."""
        result = True
        num_tokens = len(self.tokens)
        if  != len(other.tokens):
            result = False
        else:
            for i in range(0, num_tokens):
                if self.tokens[i] != other.tokens[i]:
                    result = False
                    break
        return result
