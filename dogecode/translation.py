# translation.py - Translate between Brainfuck commands and Dogeparty tokens
# Copyright (C) 2014 Rob Myers rob@robmyers.org
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or 
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

################################################################################
# Imports
################################################################################

import csv, re


################################################################################
# Token translation and formatting
################################################################################

# BF symbols to Dogeparty token names
SYMBOLS_TO_TOKENS = {'>':'INCP', '<':'DECP', '+':'INCB', '-':'DECB', '.':'PUTB',
                     ',':'GETB', '[':'JFOR', ']':'JBAK'}

# Dogeparty token names to BF symbols
TOKENS_TO_SYMBOLS = {v: k for k, v in SYMBOLS_TO_TOKENS.items()}

TOKENS = TOKENS_TO_SYMBOLS.keys()

# BF symbols and nothing else
TOKENS_RE = re.compile(r'[^><+\-.,[\]]+')

# Runs of BF symbols
TOKEN_RUN_RE = re.compile(r'(>+|<+|\++|-+|\.+|,+|\[+|]+)')

# An initial comment
INITIAL_COMMENT = re.compile(r'^\[[^\]]+]')


################################################################################
# Parse source code and convert to token amounts
################################################################################

def strip_non_token_characters(source):
    """Return a copy of the sourc with all whitespace, newlines, letters,
       numbers, and anything other than token characters removed from the
       source."""
    return re.sub(TOKENS_RE, '', source)

def remove_initial_comment(source):
    """Remove the first [...] block from the code, it's just a comment"""
    return re.sub(INITIAL_COMMENT, '', source)

def run_to_token(run):
    """Convert a run of characters to a tokem count pair"""
    return (SYMBOLS_TO_TOKENS[run[0]],
            len(run))

def code_to_token_runs(source):
    """Convert program source to a list of token/run length pairs"""
    runs = re.findall(TOKEN_RUN_RE, source)
    return [run_to_token(run) for run in runs]

def source_to_tokens(source, strip_initial_comment):
    """Clean the source code and represent the program as pairs of
       token/counts"""
    source = strip_non_token_characters(source)
    if strip_initial_comment:
        source = remove_initial_comment(source)
    return code_to_token_runs(source)

def write_transactions_csv(token_pairs, csvfile):
    writer = csv.writer(csvfile)
    for pair in token_pairs:
        writer.writerow((pair[0], pair[1]))

def source_to_tokens_csv(source, csvfile, strip_initial_comment=True):
    token_pairs = source_to_tokens(source, strip_initial_comment)
    write_transactions_csv(token_pairs, csvfile)


################################################################################
# Convert token amounts to source code
################################################################################

def token_to_run(token_pair):
    """Convert a token/count tuple to a string containting count instances of
       token"""
    return TOKENS_TO_SYMBOLS[token_pair[0]] * token_pair[1]

def token_runs_to_code(token_pairs):
    """Convert a sequence of token/count tuples to a string of operator
       symbols"""
    code = ''
    for pair in token_pairs:
        code += token_to_run(pair)
    return code

def json_token_amounts_to_pairs(tokens_json):
    """Extract a list of (TOKEN,N) pairs from the json list of token sends"""
    pairs = []
    for send in tokens_json:
        if send["status"] == "valid":
            pairs.append((send["asset"], send["quantity"]))
    return pairs


################################################################################
# Compare token lists
################################################################################

class TokenList(object):
    """A class to keep track of a list of tokens"""

    def __init__(self):
        """Create a new empty list"""
        self.tokens = []

    def append(self, token, count):
        """Append the token count to the list"""
        self.tokens.append((token, int(count)))

    def from_json(self, json):
        """Initialize the token list from a json rpc query response"""
        for send in json:
            self.append(send["asset"], send["quantity"])

    def equals(self, other):
        """Compare the token list with another token list.
           Return True if the list is equal, false if not."""
        result = True
        num_tokens = len(self.tokens)
        if num_tokens != len(other.tokens):
            result = False
        else:
            for i in range(0, num_tokens):
                if self.tokens[i] != other.tokens[i]:
                    result = False
                    break
        return result

    def is_subsequence_of(self, other):
        """Check whether this is a proper subsequence of other.
           An equal list is not a proper subsequence."""
        result = True
        num_tokens = len(self.tokens)
        if num_tokens >= len(other.tokens):
            result = False
        else:
            for i in range(0, num_tokens):
                if self.tokens[i] != other.tokens[i]:
                    result = False
                    break
        return result
