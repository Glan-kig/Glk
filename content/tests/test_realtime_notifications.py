import pytest
from channels.testing import WebsocketCommunicator
from core.asgi import application

@pytest.mark.asyncio
async def test_websocket_notification() -> None:
    communicator = WebsocketCommunicator(application, 'ws/notifications/')
    connected, _ = await communicator.connect()
    assert connected

    await communicator.send_json_to({'message': 'Test Notification'})
    response = await communicator.receive_json_from()
    assert response['message'] == 'Test Notification'

    await communicator.disconnect()
    