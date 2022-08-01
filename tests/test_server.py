from gbserver.server import Server


async def test_hello(test_client):
    server = Server()
    client = await test_client(server.app)
    resp = await client.get('/test')
    assert resp.status == 200
    text = await resp.text()
    assert 'Hello, world. Test view.' in text


async def test_bd_save(test_client):
    server = Server()
    client = await test_client(server.app)
    resp = await client.get('/testdbsave')
    assert resp.status == 200
    text = await resp.text()
    assert 'Hello, world. Test view.' in text


async def test_bd_read(test_client):
    server = Server()
    client = await test_client(server.app)
    resp = await client.get('/testdbread')
    assert resp.status == 200
    text = await resp.text()
    assert 'Hello, world. Test view.' in text
