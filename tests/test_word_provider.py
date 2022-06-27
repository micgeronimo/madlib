"""Tests for the gateways module."""
import requests
import pytest

from app import word_provider



def test_get_noun(mocker, mock_response):
    """Should return data from 'noun' endpoint."""
    mocker.patch('requests.get', return_value=mock_response('some_noun'))

    result = word_provider.get_noun()
    assert result == 'some_noun'
    expected_url = word_provider.PROVIDER_URL + 'noun'
    requests.get.assert_called_once_with(expected_url)


def test_get_verb(mocker, mock_response):
    """Should return data from 'verb' endpoint."""
    mocker.patch('requests.get', return_value=mock_response('some_verb'))

    result = word_provider.get_verb()
    assert result == 'some_verb'
    expected_url = word_provider.PROVIDER_URL + 'verb'
    requests.get.assert_called_once_with(expected_url)


def test_get_adjective(mocker, mock_response):
    """Should return data from 'adjective' endpoint."""
    mocker.patch('requests.get', return_value=mock_response('some_adjective'))

    result = word_provider.get_adjective()
    assert result == 'some_adjective'
    expected_url = word_provider.PROVIDER_URL + 'adjective'
    requests.get.assert_called_once_with(expected_url)


def test_get_word_handles_400_error(mocker, mock_response):
    """Should handle case when third-party service responds with 400 error."""
    mocker.patch('requests.get', return_value=mock_response('', status_code=400))
    with pytest.raises(ValueError):
        word_provider.get_noun()


def test_get_word_handles_500_error():
    """Should handle case when third-party service respondswith 500 error."""
    # TODO


def test_get_word_handles_timeout():
    """Should handle case when third-party service returns no response."""
    # TODO
