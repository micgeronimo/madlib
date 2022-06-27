"""Tests for api routes."""


def test_aggregate_data(test_client, mocker, mock_response):
    """Should return data aggregated from several endpoints."""
    side_effects = [mock_response('some_noun'), mock_response('some_verb'), mock_response('some_adjective')]
    mocker.patch('requests.get', side_effect=side_effects)
    response = test_client.get('/madlib')
    assert response.status_code == 200

    content = response.data.decode()
    expected_content = 'It was a some_adjective day. I went downstairs to see if I could some_verb dinner. I asked, "Does the stew need fresh some_noun?"'
    assert content == expected_content


def test_aggregate_data_handles_downstream_error():
    """Should handle case when third party service responds with error."""


def test_aggregate_data_handles_downstream_timeout():
    """Should handle case when third party service does not respond at all."""
