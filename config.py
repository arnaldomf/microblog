CSRF_ENABLED = True
SECRET_KEY = '\x8f\xab\xc4\xa00G\x17ZG\xd8\xb6\xe0\xb3\xe7\xf0\x8f\xa2\x98\xe5!\xc9\x0cB\xcb'
OPENID_PROVIDERS = [
	{ 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
	{ 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
	{ 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
	{ 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
	{ 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }
]