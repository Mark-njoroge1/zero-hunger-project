FORUM_POSTS = []
_next_post_id = 1
def create_post(title, body, author):
    
    global _next_post_id

    new_post = {
        "id": _next_post_id,
        "title": title,
        "body": body,
        "author": author,
        "replies": [],
        "active": True,
    }

    FORUM_POSTS.append(new_post)
    _next_post_id += 1

    return new_post["id"]


def add_reply(post_index, reply_text):
   
    if 0 <= post_index < len(FORUM_POSTS):
        FORUM_POSTS[post_index]["replies"].append(reply_text)
        return True

    print(f"Error: no post exists at index {post_index}.")
    return False


def search_posts(search_query):
    
    query = search_query.lower().strip()
    results = []

    for post in FORUM_POSTS:
        if not post["active"]:
            continue

        post_title = post["title"].lower()
        post_body = post["body"].lower()

        if query in post_title or query in post_body:
            results.append(post)

    return results



if __name__ == "__main__":
    id1 = create_post(
        "How do I reverse a list in Python?",
        "I keep getting errors when using .reverse() inside a loop.",
        "christian_dev",
    )
    id2 = create_post(
        "Best way to filter dictionaries?",
        "Looking for a clean way to search through nested dict data.",
        "amina_codes",
    )

    print(f"Created post 1 with ID: {id1}")
    print(f"Created post 2 with ID: {id2}")

   
    add_reply(0, "Try list slicing: my_list[::-1]")
    add_reply(0, "Or use the built-in reversed() function.")
    add_reply(1, "Use a list comprehension with an if condition.")

    print("\n--- Search results for 'list' ---")
    for post in search_posts("list"):
        print(f"[{post['id']}] {post['title']} — {len(post['replies'])} replies")

    print("\n--- Full FORUM_POSTS state ---")
    for post in FORUM_POSTS:
        print(post)