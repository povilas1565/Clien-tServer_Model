# Registration, SignIn, SignOut
# from auth.views import Login, SignIn, SignOut
from gbserver.handlers import Test, TestDbSave, TestDbRead, SignUp, SignIn, SignOut, SocketWorker

routes = [
    # ('GET', '/', ChatList, 'main'),
    ('GET', '/test', Test, 'test'),
    ('GET', '/testdbsave', TestDbSave, 'test_db_save'),
    ('GET', '/testdbread', TestDbRead, 'test_db_read'),

    ('POST', '/signup', SignUp, 'signup'),
    ('POST', '/signin', SignIn, 'signin'),
    ('POST', '/signout', SignOut, 'signout'),
    # ('GET', '/', ChatList, 'main'),
    # ('GET', '/', ChatList, 'main'),
    ('GET', '/send', SocketWorker, 'socket_worker'),

]