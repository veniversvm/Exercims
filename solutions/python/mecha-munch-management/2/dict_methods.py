"""Functions to manage a users shopping cart items."""

def _create_inventory(items):
    """
 
    :param items: list - list of items to create an inventory from.
    :return:  dict - the inventory dictionary.
    """
    return {i: items.count(i) for i in items}

def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """
    items = _create_inventory(items_to_add)
    keys = set(list(current_cart.keys()) + list(items.keys()))
    return {key: current_cart.get(key, 0) + items.get(key, 0) for key in keys}


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """
    return _create_inventory(notes)


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: iterable -  with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """
    ideas.update(recipe_updates)
    return ideas


def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """
    return dict(sorted(cart.items())) 

def send_to_store(cart: dict, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """
    for item in cart:
        if item in aisle_mapping:
            aisle, refri =  aisle_mapping[item]
            cart[item] = [cart[item], aisle, refri]
    return dict(sorted(cart.items(), reverse=True))


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """
    new_dict = {}
    for item in fulfillment_cart:
        store_inventory[item][0] = store_inventory[item][0] - fulfillment_cart[item][0]
        store_inventory[item][0] = store_inventory[item][0] if store_inventory[item][0] > 0 else 'Out of Stock'

    return store_inventory