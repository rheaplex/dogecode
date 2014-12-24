# network.py - Accessing the dogepartyd json-rpc api.
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

import json                                                                     
import sys                                                                      
import requests


################################################################################
# Dogeparty API access
################################################################################

headers = {'content-type': 'application/json'}

class DogepartyApi(object):
    """Connect to and call the Dogeparty API"""

    def __init__(self, user, password, host='localhost', port='5000'):
        """Configure the API connection"""
        self.host = 'http://{}:{}@{}:{}'.format(user,
                                                password,
                                                host,
                                                port)

    def call_api(self, method, params):
        """Call dogepartyd via the json-rpc interface"""
        payload = {
            "method": method,
            "params": params,
            "jsonrpc": "2.0",
            "id": 0
        }
        response = requests.post(self.host, data=json.dumps(payload), headers=headers)
        try:
            return response.json()['result']
        except KeyError:
            print(response.json())
            return False

    def send_token(self, from_address, to_address, token, amount, fee):
        """Send the given amount of tokens"""
        result = False
        params = {'source': from_address,
                  'destination': to_address,
                  'asset': token,
                  'quantity': int(amount),
                  'fee': int(fee),
                  'encoding': 'opreturn'}
        tx_hash = self.call_api("do_send", params)
        if tx_hash:
            result = tx_hash
        return result
    
    def __new_address_for_code(self):
        """Return a new address to receive the tokens representing the program"""
        return ""

    def __get_account_token_amount(self, address, token):
        """Return the amount of token address has, 0 for none"""
        return 0

    def address_has_no_code_tokens(self, address):
        """Check that address has no code tokens"""
        has_none = True
        for token in translation.TOKENS:
            count = self.get_account_token_amount(address, token)
            if token > 0:
                has_none = False
                break
        return has_none

    def address_has_sufficient_tokens(self, address, token_pairs, warning_level=10):
        """Check that address has sufficient tokens to send to express the program
        encoded in token_pairs, warning if sending would reduce the amount of
        tokens too low"""
        totals = {}
        for pair in token_pairs:
            totals[pair[0]] = totals.get(pair[0], 0) + pair[1]
        enough = True
        for token, count in totals.items():
            available = get_account_token_amount(address, token)
            if (available - count) < warning_level:
                print("This program requires {} {} tokens. Address {} currently has {} . After this program it will only have {} .".format(count, token, address, available, available - count))
            if available < count:
                print("Account {} has insufficient {} tokens ({})to send the {} needed to represent this program.".format(address, token, available, count))
                enough = False
                break
        return enough

    def __address_has_sufficient_fees(self, address, token_pairs, fee, warning_level=100):
        """Check that the account has sufficient Dogecoins to pay the fees for all
        the token transactions"""
        total_required = len(token_pairs) * fee
        #FIXME: work
        return False
    
    def __upload_code(from_address, to_address, token_pairs, fee):
        """Check that from_address has sufficient tokens and that to_address has
        none, then create transactions to transfer the token amounts expressed
        in token pairs from from_address to to_address"""
        if self.address_has_sufficient_tokens(from_address, token_pairs) and \
           self.address_has_no_code_tokens(to_address):
            pass
        pass
    
    def token_transactions_for_address(self, receiver):
        """Get the token transactions (and any doge transfers) sent to the adress.
           This is insecure for fetching programs without further filtering."""
        params = {'filters': {'field':'destination',
                              'op':'==',
                              'value':receiver},
                  'order_by':'tx_index',
                  'order_dir':'ASC'}
        sends = self.call_api('get_sends', params)
        return sends

    
    def token_transactions_for_address_from_sender(self, receiver, sender):
        """Get the token transactions (and any doge transfers) sent to the adress from the sender"""
        params = {'filters': [{'field':'destination',
                               'op':'==',
                               'value':receiver},
                              {'field':'sender',
                               'op':'==',
                               'value':sender}],
                  'order_by':'tx_index',
                  'order_dir':'ASC'}
        sends = self.call_api('get_sends', params)
        return sends
