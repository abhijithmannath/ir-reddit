import praw

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class _Network():
	def __init__(self):
		USER_AGENT = 'Ir Scraper 1.1'
		self.request = praw.Reddit(user_agent=USER_AGENT)

	def to_dict(self):
		members = [attr for attr in dir(self) if not callable(getattr(self,attr)) and not attr.startswith("__")]
		z = {}
		for x in members:
			if x in ['request']:
				break
			z[x] = getattr(self,x,None)
		return z

class SubReddit(_Network):

	def __init__(self,title):
		_Network.__init__(self)
		self.title = title
		_obj = self.request.get_subreddit(title)
		self.description = _obj.public_description
		_posts = _obj.get_top_from_all(limit=200)
		self.posts = self.create_posts(_posts)


	def create_posts(self, _posts):
		limit = 100
		posts = []
		c=0
		for x in _posts:
			c+=1
			if c>limit:
				break
			print 'Post :%s>'%c
			y = Post(x)
			posts.append(y.to_dict())
		return posts


class Post(_Network):
	def __init__(self,_obj):
		for x in ['created_utc','num_comments','ups','downs','title','thumbnail','permalink']:
			try:
				z = getattr(_obj,x,None)
				setattr(self,x,z)
			except:
				pass

		self.set_media(_obj.domain)
		print '%s %s %s'%(bcolors.OKGREEN,self.title,bcolors.ENDC)
		self.author = User(_obj.author).to_dict()




	def set_media(self,domain):
		if 'imgur' in domain or 'giphy' in domain or 'gify' in domain:
			self.type = 'img'
		elif 'youtu' in domain: #youtube and youtu.be
			self.type='vid'
		else:
			self.type = None

class User(_Network):
	def __init__(self,_obj):
		print 'Author %s %s %s'%(bcolors.OKBLUE,_obj,bcolors.ENDC)
		if not _obj:
			name = ''
			return
		for x in ['name','comment_karma','link_karma','is_gold']:
			try:
				z = getattr(_obj,x,None)
				setattr(self,x,z)
			except:
				pass


def scrape_subreddit(title):
	import shelve
	fp = shelve.open('reddit.db')
	if title not in fp.keys():
		print 'Subreddit:> %s %s %s\n'%(bcolors.OKGREEN,title,bcolors.ENDC)
		try:
			s = SubReddit(title)
			fp[title] = s.to_dict()
		except Exception as e:
			print 'Error: %s %s %s'%(bcolors.FAIL,e,bcolors.ENDC)
	fp.close()

def scrape():
	with open('input.txt') as fp:
		for line in fp:
			scrape_subreddit(line.rstrip('\n'))







