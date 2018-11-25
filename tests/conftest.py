import pytest

@pytest.fixture()
def validate_invalid_response():
    return {
        "status": 200,
        "result": False,
    }


@pytest.fixture()
def validate_valid_response():
    return {
        "status": 200,
        "result": True,
    }


@pytest.fixture()
def info_response():
    return {
        "status": 200,
        "result": {
            "postcode": "CB3 0FA",
            "country": "England",
            "region": "East of England",
        }
    }


@pytest.fixture()
def nearest_response():
    return {
        "status": 200,
        "result": [
            {
                "postcode": "CB3 0FA",
                "country": "England",
                "region": "East of England",
            },
            {
                "postcode": "CB3 0GT",
                "country": "England",
                "region": "East of England",
            }
        ]
    }
