import requests
from random import choice

### Visit https://crudcrud.com/ and get yout personal URL


URL = ""

ENDPOINT = "pizza"

NAME = ["Pepperoni", "Margherita", "Hawaiian"]
TYPE = ["round", "square"]
TOPPINGS = [True, False]
PRICE = list(range(10, 21))


def test_create():
    for _ in range(3):

        payload = {
            "name": choice(NAME),
            "type": choice(TYPE),
            "toppings": choice(TOPPINGS),
            "price": choice(PRICE),
        }

        actual_result = requests.post(URL + ENDPOINT, json=payload)
        assert actual_result.status_code == 201


def test_read():
    actual_result = requests.get(URL + ENDPOINT).json()
    assert len(actual_result) >= 3
    for pizza in actual_result:
        assert pizza.get("name") in NAME
        assert pizza.get("type") in TYPE
        assert pizza.get("toppings") in TOPPINGS
        assert type(pizza.get("price")) == int


def test_update():
    pizza_id = requests.get(URL + ENDPOINT).json()[0].get("_id")
    pizza = requests.get(URL + ENDPOINT + "/" + pizza_id).json()

    assert type(pizza.get("price")) == int

    pizza.pop("_id")  # This API does not accept inner ids
    pizza["price"] = 25

    method_put = requests.put(URL + ENDPOINT + "/" + pizza_id, json=pizza)
    assert method_put.status_code == 200

    changed_pizza = requests.get(URL + ENDPOINT + "/" + pizza_id).json()

    assert changed_pizza.get("price") == 25


def test_depete():
    pizza_id = requests.get(URL + ENDPOINT).json()[0].get("_id")
    pizza = requests.delete(URL + ENDPOINT + "/" + pizza_id)

    assert pizza.status_code == 200

    delete_pizza = requests.get(URL + ENDPOINT + "/" + pizza_id)

    assert delete_pizza.status_code == 404