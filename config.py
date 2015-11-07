import os

DEBUG = True

SITE_TITLE = "ArcTwitter"
SITE_DESC = "Find What Twitter Is Saying Where the Action Happens"

CSRF_ENABLED = True
SECRET_KEY = 'none'

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

APP_ROOT = os.path.dirname(os.path.abspath(__file__))   # refers to application_top
APP_STATIC = os.path.join(APP_ROOT, 'static')

S3_UPLOAD_DIR = 'uploads/'
S3_KEY = ''
S3_SECRET = ''
S3_BUCKET = ''
S3_URL = "http://%s.s3.amazonaws.com/" % S3_BUCKET
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'bmp', 'gif'])

BASE = basedir