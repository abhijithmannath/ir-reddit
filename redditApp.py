import Tkinter as tk


class Input:
	category = None
	author_comment_karma = None
	author_link_karma = None
	created_utc = None
	num_comments = None
	thumbnail = None
	type_var = None
	author_is_gold = None
	title = None
	ups = None

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        FRAME = tk.Frame.__init__(self, parent, *args, **kwargs)

        self.entries = {}

        tk.Label(FRAME, text="TITLE").pack()
        title= self.entries['title']= tk.Entry(FRAME)
        title.pack()
        
        tk.Label(FRAME, text='SUBREDDIT').pack()
        cat = self.entries['category'] = tk.Entry(FRAME)
        cat.pack()
        tk.Label(FRAME, text='TYPE').pack()
        
        _i= self.entries['type_var'] = tk.StringVar(value='img')
        _ = tk.Radiobutton(FRAME, text='IMG',value='img', variable=_i)
        _.pack()
        _ = tk.Radiobutton(FRAME, text='VID', variable=_i, value='vid')
        _.pack()

        tk.Label(FRAME, text='COMMENT KARMA').pack()
        cmt_ = self.entries['author_comment_karma']= tk.Entry(FRAME)
        cmt_.pack()
        tk.Label(FRAME, text='LINK KARMA').pack()
        link_ = self.entries['author_link_karma']= tk.Entry(FRAME)
        link_.pack()
        

        tk.Label(FRAME, text="IS_GOLD").pack()
        
        _i= self.entries['author_is_gold'] = tk.IntVar()
        _ = tk.Radiobutton(FRAME, text='Yes',value=1, variable=_i)
        _.pack()
        _ = tk.Radiobutton(FRAME, text='No', variable=_i, value=0)
        _.pack()


        tk.Label(FRAME, text="CREATED").pack()
        created = self.entries['created_utc']= tk.Entry(FRAME)
        created.pack()

        tk.Label(FRAME, text="NUMBER OF COMMENTS").pack()
        num_comments = self.entries['num_comments']= tk.Entry(FRAME)
        num_comments.pack()
       

        tk.Button(FRAME, text='Predict Popularity', command=self.say_hello, width=25).pack()
        tk.Label(FRAME, text="SCORE:").pack(anchor='c', pady=30)


    def say_hello(self):
    	s= Input()
    	for x in self.entries:
			setattr(s,x,self.entries[x].get())
		#call your function with s object here or use your class instead
		#also instal tkinter




if __name__ == '__main__':
    root = tk.Tk()
    root.config(cursor='hand1')
    MainApplication(root, height=400, width=1000,)
    root.title('Reddit Application')
    root.resizable(width=False, height=False)
    root.mainloop()
