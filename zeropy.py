#zeropy.py

import requests
import json
import os

class zerotier:
    def __init__(self, apitoken):
        self.apitoken = apitoken

    def get_status(self):
        # Get Status and Configuration Information
        # Obtain information about this server and/or useful to the Central web UI.

        r = requests.get("https://my.zerotier.com/api/status", headers={"Authorization":"bearer {}".format(self.apitoken)})
        return r.json()
    
    # BROKEN: Doesn't appear to be functional or useful for this wrapper. Returns 404 in current format on free license
    def get_self(self):
        # Get Currently Authenticated User
        # Get the currently authenticated user’s user record.
        r = requests.get("https://my.zerotier.com/api/self", headers={"Authorization":"bearer {}".format(self.apitoken)})
        return r.json()

    # BROKEN: Doesn't appear to be functional or useful for this wrapper. Returns 403 in current format on free license
    def get_randomtoken(self):
        # Generate a Random Token
        # This generates a random token suitable for use as an API token server-side using a secure random source. It does not actually modify the user record, just returns the token for use by API callers or the UI.
        r = requests.get("https://my.zerotier.com/api/randomToken", headers={"Authorization":"bearer {}".format(self.apitoken)})
        return r.json()

    def post_logout(self):
        # Terminate Current Session
        # Hitting this endpoint causes the user to be logged out. It has no effect when using token authentication, so it’s mostly used by the UI.
        r = requests.post("https://my.zerotier.com/api/auth/_logout", headers={"Authorization":"bearer {}".format(self.apitoken)})
        return r.json()

    def get_user(self, userId):
        # Retrieve a User
        # ...
        r = requests.get("https://my.zerotier.com/api/user/{}".format(userId), headers={"Authorization":"bearer {}".format(self.apitoken)})
        return r.json()

    def post_user(self, userId, payload):
        # Update a User
        # Only fields marked as [rw] can be directly modified. If other fields are present in the posted request they are ignored.
        r = requests.post("https://my.zerotier.com/api/user/{}".format(userId), headers={"Authorization":"bearer {}".format(self.apitoken)}, data=payload)
        return r.json()

    def delete_user(self, userId):
        # Delete a User
        # Delete a user. This will immediately and PERMANENTLY delete a user and all associated networks and data. Only hit this URL if you’re 100% sure you want the user deleted.
        r = requests.delete("https://my.zerotier.com/api/user/{}".format(userId), headers={"Authorization":"bearer {}".format(self.apitoken)})
        return r.json()

    def get_users(self):
        # Get All Viewable Users
        # Get all users for which you have at least read access.
        r = requests.get("https://my.zerotier.com/api/user", headers={"Authorization":"bearer {}".format(self.apitoken)})
        return r.json()

    def get_network(self, networkId):
        # Retrieve a Network
        # ...
        r = requests.get("https://my.zerotier.com/api/network/{}".format(networkId), headers={"Authorization":"bearer {}".format(self.apitoken)})
        return r.json()

    def post_network(self, networkId, payload):
        # Update or create a Network
        # Only fields marked as [rw] can be directly modified. If other fields are present in the posted request they are ignored.
        # New networks can be created by POSTing to /api/network with no networkId parameter. The server will create a random unused network ID and return the new network record.
        r = requests.post("https://my.zerotier.com/api/network/{}".format(networkId), headers={"Authorization":"bearer {}".format(self.apitoken)}, data=payload)
        return r.json()

    def delete_network(self, networkId):
        # Delete a Network
        # Delete a network and all its related information permanently. Use extreme caution as this cannot be undone!
        r = requests.delete("https://my.zerotier.com/api/network/{}".format(networkId), headers={"Authorization":"bearer {}".format(self.apitoken)})
        return r.json()

    def get_networks(self):
        # Get All Viewable Networks
        # Get all networks for which you have at least read access.
        r = requests.get("https://my.zerotier.com/api/network", headers={"Authorization":"bearer {}".format(self.apitoken)})
        return r.json()

    def get_member(self, networkId, nodeId):
        # Retrieve a Member
        # ...
        r = requests.get("https://my.zerotier.com/api/network/{}/member/{}".format(networkId, nodeId), headers={"Authorization":"bearer {}".format(self.apitoken)})
        return r.json()

    def post_member(self, networkId, nodeId, payload):
        # Update or add a Member
        # New members can be added to a network by POSTing them.
        r = requests.post("https://my.zerotier.com/api/network/{}/member/{}".format(networkId, nodeId), headers={"Authorization":"bearer {}".format(self.apitoken)}, data=payload)
        return r.json()

    def get_members(self, networkId):
        # Get All Members of a Network
        # Get all members of a network for which you have at least read access.
        r = requests.get("https://my.zerotier.com/api/network/{}/member".format(networkId), headers={"Authorization":"bearer {}".format(self.apitoken)})
        return r.json()


def main():
    from dotenv import load_dotenv
    load_dotenv()

    ZEROTIER_NETWORK = os.getenv('ZEROTIER_NETWORK')
    ZEROTIER_TOKEN = os.getenv('ZEROTIER_TOKEN')

    api = zerotier(ZEROTIER_TOKEN)

    print(api.get_status())

    # Broken
    #print(api.get_self())

    print(api.get_randomtoken())


if(__name__ == "__main__"):
    main()