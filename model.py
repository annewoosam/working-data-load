
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Checklist(db.Model):
    """Data model for an animal."""

    __tablename__ = 'checklists'

    checklist_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    templatename = db.Column(db.String(50), nullable=False)
    timeframe = db.Column(db.Date(), nullable=False)
    whofor = db.Column(db.String(), nullable=False)

    # checklist_id = db.Column(db.Integer,
    #                      db.ForeignKey('templates.checklist_id'),
    #                      nullable=False)
    # Template = db.relationship('Template', backref='checklists')

    def __repr__(self):
        """Provide helpful representation when printing."""

        return f'<Checklist checklist_id={self.checklist_id} templatename={self.templatename}> whofor={self.whofor}'


def connect_to_db(app):
    """Connect the database to our Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///checklists'
    app.config['SQLALCHEMY_ECHO'] = False
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == '__main__':
    from server import app

    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.
    connect_to_db(app)
    print('Connected to db!')
