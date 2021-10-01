from app import app


def test_wag():
    with app.test_client() as client:
        assert b'{"wag": true}' in client.post("/wag/", data={"command": "treato"}).data


def test_wag_no():
    with app.test_client() as client:
        assert (
            b'{"wag": false}'
            in client.post("/wag/", data={"command": "no treato"}).data
        )
