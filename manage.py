from app import create_app,db
from flask_script import Manager,Server
from app.models import User,Post, Comment
from flask_migrate import Migrate, MigrateCommand

app = create_app("development")

manager = Manager(app)

@manager.shell
def make_shell_context():
    return dict(db = db, app = app, User = User, Post = Post, Comment = Comment)

@manager.command
def test():
    """
    Run the unit tests
    """
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

migrate = Migrate(app,db)
manager.add_command("db", MigrateCommand)

manager.add_command("server", Server)

if __name__ == "__main__":
    manager.run()
