#zeropy.py

import requests
import json
import os

class zerotier:
    def __init__(self, apitoken, network):
        self.apitoken = apitoken
        self.network = network

    def get_status(self):
        # Get Status and Configuration Information
        # Obtain information about this server and/or useful to the Central web UI.
        pass
    
    def get_self(self):
        # Get Currently Authenticated User
        # Get the currently authenticated user’s user record.
        pass

    def get_randomtoken(self):
        # Generate a Random Token
        # This generates a random token suitable for use as an API token server-side using a secure random source. It does not actually modify the user record, just returns the token for use by API callers or the UI.
        pass

    def post_logout(self):
        # Terminate Current Session
        # Hitting this endpoint causes the user to be logged out. It has no effect when using token authentication, so it’s mostly used by the UI.
        pass

    def get_user(self, userId):
        # Retrieve a User
        # ...
        pass

    def post_user(self, userId, payload):
        # Update a User
        # Only fields marked as [rw] can be directly modified. If other fields are present in the posted request they are ignored.
        pass

    def delete_user(self, userId):
        # Delete a User
        # Delete a user. This will immediately and PERMANENTLY delete a user and all associated networks and data. Only hit this URL if you’re 100% sure you want the user deleted.
        pass

    def get_users(self):
        # Get All Viewable Users
        # Get all users for which you have at least read access.
        pass

    def get_network(self, networkId):
        # Retrieve a Network
        # ...
        pass

    def post_network(self, networkId, payload):
        # Update or create a Network
        # Only fields marked as [rw] can be directly modified. If other fields are present in the posted request they are ignored.
        # New networks can be created by POSTing to /api/network with no networkId parameter. The server will create a random unused network ID and return the new network record.
        pass

    def delete_network(self, networkId):
        # Delete a Network
        # Delete a network and all its related information permanently. Use extreme caution as this cannot be undone!
        pass

    def get_networks(self):
        # Get All Viewable Networks
        # Get all networks for which you have at least read access.
        pass

    def get_member(self, networkId, nodeId):
        # Retrieve a Member
        # ...
        pass

    def post_member(self, networkId, nodeId, payload):
        # Update or add a Member
        # New members can be added to a network by POSTing them.
        pass

    def get_members(self, networkId):
        # Get All Members of a Network
        # Get all members of a network for which you have at least read access.
        pass



