

import datetime

def simple_blog():
    posts = []
    print("Welcome to your Simple Blog!")

    while True:
        print("\nOptions:")
        print("1. Create a new post")
        print("2. View all posts")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter post title: ")
            content = input("Enter post content: ")
            author = input("Enter your name (author): ")
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            posts.append({"title": title, "content": content, "author": author, "timestamp": timestamp})
            print("Post created successfully!")
        elif choice == '2':
            if not posts:
                print("No posts available yet.")
            else:
                print("\n--- Blog Posts ---")
                for i, post in enumerate(posts):
                    print(f"\nPost {i + 1}:")
                    print(f"Title: {post["title"]}")
                    print(f"Author: {post["author"]}")
                    print(f"Date: {post["timestamp"]}")
                    print(f"Content:\n{post["content"]}")
                    print("--------------------")
        elif choice == '3':
            print("Exiting Simple Blog. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    simple_blog()

