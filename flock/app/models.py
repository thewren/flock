from app import db
from hashlib import md5

ROLE_USER = 0
ROLE_ADMIN = 1

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nickname = db.Column(db.String(64), unique = True)
    email = db.Column(db.String(120), index = True, unique = True)
    password = db.Column(db.String(64), nullable = True)
    role = db.Column(db.SmallInteger, default = ROLE_USER)
    ratings = db.relationship('Rating', backref = 'author', lazy = 'dynamic')
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime)
    age = db.Column(db.Integer, nullable = True)
    gender = db.Column(db.String(64), nullable = True)
    location = db.Column(db.String(64))
    val_collaboration = db.Column(db.Integer, nullable = True)
    val_competitive_pay = db.Column(db.Integer, nullable = True)
    val_empowerment = db.Column(db.Integer, nullable = True)
    val_flex_sched = db.Column(db.Integer, nullable = True)
    val_advancement_opps = db.Column(db.Integer, nullable = True)
    val_honesty = db.Column(db.Integer, nullable = True)
    val_innovation = db.Column(db.Integer, nullable = True)
    val_medical_benefits = db.Column(db.Integer, nullable = True)
    val_mentoring = db.Column(db.Integer, nullable = True)
    val_paid_time_off = db.Column(db.Integer, nullable = True)
    val_performance_feedback = db.Column(db.Integer, nullable = True)
    val_results_driven = db.Column(db.Integer, nullable = True)
    val_retirement = db.Column(db.Integer, nullable = True)
    val_training_development = db.Column(db.Integer, nullable = True)
    val_work_from_home = db.Column(db.Integer, nullable = True)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def avatar(self, size):
        return 'http://www.gravatar.com/avatar/' + md5(self.email).hexdigest() + '?d=mm&s=' + str(size)

    def __repr__(self):
        return '<User %r>' % (self.nickname)

class Company(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64))
    url = db.Column(db.String(64))
    location = db.Column(db.String(64))
    service = db.Column(db.String(64))
    industry = db.Column(db.String(64))
    ratings = db.relationship('Rating', backref = 'reader', lazy = 'dynamic')
 
    def __repr__(self):
        return '<Company %r>' % (self.name)

class Value(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64))
    ratings = db.relationship('Rating', backref = 'subject', lazy = 'dynamic')
 
    def __repr__(self):
        return '<Value %r>' % (self.name)

class Rating(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    value_id = db.Column(db.Integer, db.ForeignKey('value.id'))
    rating = db.Column(db.Integer)

    def __repr__(self):
        return '<Rating %r>' % (self.rating)