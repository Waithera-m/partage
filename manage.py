from app import create_app,db
from flask_script import Manager,Server
from flask_migrate import Migrate,MigrateCommand
from app.models import Blog


app = create_app('development')

migrate = Migrate(app,db)


manager = Manager(app)

manager.add_command('server',Server)

manager.add_command('db',MigrateCommand)

@manager.shell
def make_shell_context():

    '''
    function facilitates the creation of an external shell
    '''
    return dict(app=app,db=db,Blog=Blog)

@manager.command
def test():

    '''
    function loads and runs all test files
    '''
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__=='__main__':
    manager.run()