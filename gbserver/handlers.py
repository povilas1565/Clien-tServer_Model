import json
from time import time

from aiohttp import web, WSMsgType
from aiohttp_session import get_session
from bson import ObjectId

from gbserver.message import Message
from gbserver.user import User


class Test(web.View):

    async def get(self):
        session = await get_session(self.request)
        session['111'] = time()
        session['222'] = time()
        print(session)
        text = 'Hello, world. Test view.'
        # return web.Response(body=text.encode('utf8'))
        return web.Response(body=str(session))


class TestDbSave(web.View):

    async def get(self):
        message = Message(self.request.db)
        result = await message.save(user='test_user', msg='test_content')
        return web.json_response({'messages': str(result)})


class TestDbRead(web.View):

    async def get(self):
        message = Message(self.request.db)
        messages = await message.get_messages()
        return web.json_response({'messages': messages})


class SocketWorker(web.View):

    async def get(self):
        data = await self.request.post()
        # user_id = data.get('id')
        # print(data.get('id'))
        ws = web.WebSocketResponse()
        await ws.prepare(self.request)
        session = await get_session(self.request)
        # user = User(self.request.db, id=user_id)
        # print(user)
        # user.get()
        # print(user.login)
        # login = await user.get_login()
        login = 'user1'
        for _ws in self.request.app['websockets']:
            await _ws.send_str('{} joined.'.format(login))
        self.request.app['websockets'].append(ws)
        # async for msg in ws:
        #     if msg.tp == WSMsgType.TEXT:
        #         if msg.data == 'close':
        #             await ws.close()
        #         else:
        #             message = Message(self.request.db)
        #             result = await message.save(user=login, msg=msg.data)
        #             print(result)
        #             for _ws in self.request.app['websockets']:
        #                 _ws.send_str('(%s) %s' % (login, msg.data))
        #     elif msg.tp == WSMsgType.ERROR:
        #         print(ws.exception())
        async for msg in ws:
            print('type: ', msg.type)
            if msg.type == WSMsgType.TEXT:
                message = Message(self.request.db)
                await message.save(user=login, msg=msg.data)
                print('Received from client: {}'.format(msg.data))
                for _ws in self.request.app['websockets']:
                    await _ws.send_str('{}/answer.'.format(msg.data))
                print('broadcast completed.')
            elif msg.type == WSMsgType.CLOSE:
                self.request.app['websockets'].remove(ws)
                for _ws in self.request.app['websockets']:
                    await _ws.send_str('{} disconnected.'.format(login))
                print('websocket connection closed.')

        return ws


class SignUp(web.View):
    """
    Регистрация нового пользователя.
    При успешной регистрации производится производится автоматический вход.
    Зарегистрированный пользователь имеет запись в БД.
    Залогиневшийся пользователь имеет запись в сессии.
    """

    async def post(self):
        data = await self.request.post()
        user = User(self.request.db, data)
        result = await user.save()
        if isinstance(result, ObjectId):
            id = result
            session = await get_session(self.request)
            session[str(id)] = time()
            return web.Response(content_type='application/json',
                                text=json.dumps({'result': str(id)}))
        else:
            return web.Response(content_type='application/json',
                                text=json.dumps({'error': result}))


class SignIn(web.View):
    """
    Вход на сервер по логину и паролю
    TODO сейчас проверки и шифрования пароля не будет
    """

    async def post(self):
        data = await self.request.post()
        user = User(self.request.db, data)
        result = await user.check()
        if isinstance(result, ObjectId):
            id = result
            session = await get_session(self.request)
            session[str(id)] = time()
            return web.Response(content_type='application/json',
                                text=json.dumps({'result': str(id)}))
        else:
            raise web.HTTPForbidden(body=b'Forbidden')


class SignOut(web.View):
    """
    Запрос отправляется при смене пользователя на стороне клиента и при закрытии клиента
    """

    async def post(self):
        data = await self.request.post()
        user = User(self.request.db, data)
        result = await user.check()
        session = await get_session(self.request)
        if isinstance(result, ObjectId) and session.get(str(result)):
            del session[str(result)]
            return web.Response(content_type='application/json',
                                text=json.dumps({'result': str(result)}))
        else:
            raise web.HTTPForbidden(body=b'Forbidden')

