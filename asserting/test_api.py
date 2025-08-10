import asserting.api
import pytest

# This will raise exception as the method not mocked yet
def test_call_rest_api():
    with pytest.raises(Exception):
        asserting.api.call_rest_api()
    assert True

def test_call_rest_api_mocked(mocker):
    # Arrange
    mock_response = mocker.Mock()
    mock_response.json.return_value = {"status": "ok", "message": "mocked"}
    mocked_get = mocker.patch('requests.get', return_value=mock_response)
    
    # Act
    response = asserting.api.call_rest_api()
    
    # Assert
    assert response["status"] == "ok"
    assert response["message"] == "mocked"
    mocked_get.assert_called_once_with("http://localhost:3000")
