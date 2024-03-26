import datetime
import re
class Post:
    def __init__(self, title, content, author, date):
        self.title = title
        self.content = content
        self.author = author
        self.date = date

    def show_blog(self):
        print("Content" , self.content)
        print("Author", self.author)
        print("Date", self.date)

class Blog:
    def __init__(self):
        self.posts = {}

    # Function to add new blog
    def add_blog(self):
        while True:
            title = input("Enter the title of the blog : ")
            if title.strip():
                break
            else:
                print("Title cannot be empty")
        while True:
            content = input("Enter the content of the blog : ")
            if content.strip():
                break
            else:
                print("Content cannot be empty")
        while True:
            author = input("Enter the name of author of the blog : ")
            if re.fullmatch("([a-zA-Z\s]+)", author):
                break
            else:
                print("Author name cannot be empty and should only contain alphabets")
        while True:
            try:
                date = input("Enter the blog published date: ")
                if datetime.datetime.strptime(date,"%d/%m/%Y"):
                    break
                else:
                    raise Exception("Date should be in the format dd/mm/yyyy")
            except Exception as e:
                print(e)
        blog = Post(title.capitalize(), content, author.capitalize(), date)
        if title not in self.posts.keys():
            self.posts[title] = blog
            print(title, "blog added successfully!")
        else:
            raise Exception("The blog already exists, cannot add same blog again.")

    # Function to display all blogs
    def list_all_blogs(self):
        if self.posts:
            print("List of all blogs : ")
            for number, (title, blog) in enumerate(self.posts.items(), start=1):
                print("Blog number :", number)
                print("Details of blog :", title.capitalize())
                blog.show_blog()
                print()
        else:
            print("No blogs exist, add a new blog.")

    # Function to delete a blog if it exists
    def remove_blog(self):
        while True:
            blogtitle = input("Enter the blog title to be removed : ")
            if blogtitle.strip():
                break
            else:
                print("Blog title cannot be empty")
        if blogtitle in self.posts.keys():
            del self.posts[blogtitle]
            print(blogtitle,"blog removed successfully")
        else:
            raise Exception("The given blog title does not exist")

postobject = Blog()

print('''Welcome to Blog Post Management System''')
while True:
    print('''How do you like to proceed?
    1.Add blog
    2.List all blogs
    3.Delete blog
    4.Exit''')
    choice = input("Enter a choice from above list : ")
    if choice == "1":
        try:
            postobject.add_blog()
        except Exception as e:
            print(e)
    elif choice == "2":
        postobject.list_all_blogs()
    elif choice == "3":
        try:
            postobject.remove_blog()
        except Exception as e:
            print(e)
    elif choice == "4":
        print("Thanks for using Blog Post Management System.")
        exit()
    else:
        print("Invalid! enter any values from 1 to 4.")
