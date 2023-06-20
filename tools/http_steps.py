import requests


def add_item(new_item):
    return requests.post(f"", json=new_item)


def find_item(item_id):
    return requests.get(f"{item_id}")


def update_item(item_new_name):
    return requests.put('', json=item_new_name)
