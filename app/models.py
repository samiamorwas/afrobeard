from app import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(64), unique = True)
	pw = db.Column(db.String(64))
	posts = db.relationship('Post', backref = 'author', lazy = 'dynamic')

	def is_authenticated(self):
		return True

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def get_id(self):
		return unicode(self.id)

	def __repr__(self):
		return '<User %r>' % (self.name)

class Post(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String(140))
	content = db.Column(db.Text)
	timestamp = db.Column(db.DateTime)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	def __repr__(self):
		return '<Post %r>' % (self.title)
