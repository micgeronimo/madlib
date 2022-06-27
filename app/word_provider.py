"""Code that wraps access to the third-party service."""
import requests


PROVIDER_URL = 'https://reminiscent-steady-albertosaurus.glitch.me/'


def _get_from_service(endpoint):
    """Retrieve data from given service endpoint."""
    response = requests.get(endpoint)
    if response.status_code != 200:
        raise ValueError(f'Service returned {response.status_code} with content "{response.content}"')

    return response.json()


def get_noun():
    """Should return data from noun endpoint."""
    endpoint = PROVIDER_URL + 'noun'
    result = _get_from_service(endpoint)
    return result


def get_verb():
    """Should return data from verb endpoint."""
    endpoint = PROVIDER_URL + 'verb'
    result = _get_from_service(endpoint)
    return result


def get_adjective():
    """Should return data from adjective endpoint."""
    endpoint = PROVIDER_URL + 'adjective'
    result = _get_from_service(endpoint)
    return result

