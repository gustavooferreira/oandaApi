# -*- coding: utf-8 -*-
# vim:fenc=utf-8

"""
Orders endpoint
"""


class Orders(object):
    """Class holding orders functions

    Orders
        Docs: http://developer.oanda.com/rest-live-v20/orders-ep/
    """

    def __init__(self, api):
        self._api = api

    def create_order(self, account_id, order):
        """Get a list of all Accounts authorized for the provided token.

        Args:
            This function takes no arguments.

        Returns:
            A dict with all accounts ids and tags.

        Raises:
            OandaError: An error occurred while requesting the OANDA API.
        """
        """Create an order for an Account"""
        endpoint = 'accounts/{0}/orders'.format(account_id)
        params = {}
        if order:
            params["order"] = order

        return self._api._request(endpoint, "POST", params=params)

    def get_orders_list(self, account_id, ids, state=None, instrument=None,
                        count=None, before_id=None):
        """Get a list of all Accounts authorized for the provided token.

        Args:
            This function takes no arguments.

        Returns:
            A dict with all accounts ids and tags.

        Raises:
            OandaError: An error occurred while requesting the OANDA API.
        """
        """Get a list of Orders for an Account"""
        endpoint = 'accounts/{0}/orders'.format(account_id)

        params = {}

        ids = "%2C".join(ids)
        params["ids"] = ids

        if state:
            params["state"] = state

        if instrument:
            params["instrument"] = instrument

        if count:
            params["count"] = count

        if before_id:
            params["beforeID"] = before_id

        return self._api._request(endpoint, params=params)

    def get_pending_orders(self, account_id):
        """Get a list of all Accounts authorized for the provided token.

        Args:
            This function takes no arguments.

        Returns:
            A dict with all accounts ids and tags.

        Raises:
            OandaError: An error occurred while requesting the OANDA API.
        """
        """List all pending Orders in an Account"""
        endpoint = 'accounts/{0}/pendingOrders'.format(account_id)
        return self._api._request(endpoint)

    def get_order_details(self, account_id, order_id):
        """Get a list of all Accounts authorized for the provided token.

        Args:
            This function takes no arguments.

        Returns:
            A dict with all accounts ids and tags.

        Raises:
            OandaError: An error occurred while requesting the OANDA API.
        """
        """Get details for a single Order in an Account"""
        endpoint = 'accounts/{0}/orders/{1}'.format(account_id, order_id)
        return self._api._request(endpoint)

    def replace_order(self, account_id, order_id, order):
        """Get a list of all Accounts authorized for the provided token.

        Args:
            This function takes no arguments.

        Returns:
            A dict with all accounts ids and tags.

        Raises:
            OandaError: An error occurred while requesting the OANDA API.
        """
        """Replace an Order in an Account by simultaneously cancelling it and
        creating a replacement Order
        """
        endpoint = 'accounts/{0}/orders/{1}'.format(account_id, order_id)

        params = {}
        params["order"] = order

        return self._api._request(endpoint, "PUT", params=params)

    def cancel_pending_order(self, account_id, order_id):
        """Get a list of all Accounts authorized for the provided token.

        Args:
            This function takes no arguments.

        Returns:
            A dict with all accounts ids and tags.

        Raises:
            OandaError: An error occurred while requesting the OANDA API.
        """
        """Cancel a pending Order in an Account"""
        endpoint = 'accounts/{0}/orders/{1}/cancel'.format(account_id, order_id)
        return self._api._request(endpoint, "PUT")

    def update_client_extensions(self, account_id, order_id, client_extensions,
                                 trade_client_extensions):
        """Get a list of all Accounts authorized for the provided token.

        Args:
            This function takes no arguments.

        Returns:
            A dict with all accounts ids and tags.

        Raises:
            OandaError: An error occurred while requesting the OANDA API.
        """
        """Update the Client Extensions for an Order in an Account"""
        endpoint = 'accounts/{0}/orders/{1}/clientExtensions'.format(account_id,
                                                                     order_id)

        params = {}
        params["clientExtensions"] = client_extensions
        params["tradeClientExtensions"] = trade_client_extensions

        return self._api._request(endpoint, "PUT", params=params)
