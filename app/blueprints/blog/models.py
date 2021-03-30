from app import db
from datetime import datetime as dt
from app.blueprints.auth.models import Account

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    title = db.Column(db.String)
    slug = db.Column(db.String)
    email = db.Column(db.String)
    image = db.Column(db.String)
    text = db.Column(db.Text)
    date_created = db.Column(db.DateTime, default=dt.utcnow)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'))
    comments = db.relationship('PostComment', backref='comment', cascade="all,delete", lazy='dynamic')
    tags = db.relationship('PostTag', backref='tag', cascade="all,delete", lazy='dynamic')

    def slugify(self):
        self.slug = self.title.lower().replace(' ', '-')

    def save(self):
        self.slugify()
        db.session.add(self)
        db.session.commit()

    def to_dict(self):
        return { 'id': self.id, 'image': self.image, 'title': self.title, 'slug': self.slug, 'name': self.name, 'text': self.text, 'email': self.email, 'date_created': self.date_created }

    def from_dict(self, data):
        for field in ['email', 'title', 'image', 'text']:
            if field == 'name':
                setattr(self, field, Account.query.filter_by(email=data[field]).first().id)
            elif field == 'title':
                setattr(self, field, data[field].title())
            else:
                setattr(self, field, data[field])
            self.name = Account.query.filter_by(email=data['email']).first().name
            self.account_id = Account.query.filter_by(email=data['email']).first().id

    def __repr__(self):
        return f'<Post: {self.id} | {self.text[:20]}...>'


class PostTag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String)
    slug = db.Column(db.String)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id', ondelete='CASCADE'))
    
    def slugify(self):
        self.slug = self.text.lower().replace(' ', '-')

    def save(self):
        self.slugify()
        db.session.add(self)
        db.session.commit()
    
    def to_dict(self):
        return {
            'id': self.id,
            'text': self.text,
            'slug': self.slug,
            'course': Post.query.get(self.post_id).to_dict()
        }

    def __repr__(self):
        return f'<CourseTag: {self.text}...>'

class PostComment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)
    avatar = db.Column(db.Text, default=None)
    date_created = db.Column(db.DateTime, default=dt.utcnow)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id', ondelete='CASCADE'))

    def __init__(self, text=text, avatar=avatar, date_created=date_created, post_id=post_id):
        self.text = text
        if self.avatar is None:
            self.avatar = self.avatar()
        self.date_created = date_created
        self.post_id = post_id

    def avatar(self, size=80):
            return f"https://www.gravatar.com/{md5(self.email.lower().encode('utf-8')).hexdigest()}?d=identicon&s={size}"

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def to_dict(self):
        data = {
            'id': self.id,
            'text': self.text,
            'avatar': self.avatar,
            'post': Post.query.get(self.post_id).to_dict(),
            'date_created': self.date_created
        }
        return data


    def from_dict(self, data):
        for field in ['text', 'post_id', 'date_created']:
            if field in data:
                setattr(self, field, data[field])

    def __repr__(self):
        return f'<PostComment: {self.text[20:]}...>'