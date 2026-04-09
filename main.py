"""
Blog Management Platform - Main Program
"""

from blog import BlogManager
from variables import SYSTEM_NAME, SYSTEM_VERSION

def create_sample_content(manager):
    """
    Create sample blog content
    """
    # Register authors
    author1 = manager.register_author("Sarah Williams", "sarah@blog.com")
    author1.set_bio("Technology enthusiast and software developer")
    author1.set_role("Editor")
    
    author2 = manager.register_author("Michael Chen", "michael@blog.com")
    author2.set_bio("Travel blogger and photographer")
    
    author3 = manager.register_author("Emily Rodriguez", "emily@blog.com")
    author3.set_bio("Food critic and recipe developer")
    
    # Create blog posts
    post1 = manager.create_post(
        "Getting Started with Python",
        "Python is a versatile programming language perfect for beginners. In this comprehensive guide, we'll explore the basics of Python programming, including variables, data types, control structures, and functions. Python's simple syntax makes it an excellent choice for learning programming concepts.",
        author1.author_id
    )
    post1.set_category("Technology")
    post1.add_tag("Python")
    post1.add_tag("Programming")
    post1.add_tag("Tutorial")
    post1.publish()
    post1.views = 1250
    post1.likes = 89
    
    post2 = manager.create_post(
        "Top 10 Travel Destinations for 2024",
        "Discover the most exciting travel destinations for the upcoming year. From exotic beaches to historic cities, we've compiled a list of must-visit places. Each destination offers unique experiences, cultural richness, and breathtaking landscapes that will make your travels unforgettable.",
        author2.author_id
    )
    post2.set_category("Travel")
    post2.add_tag("Travel")
    post2.add_tag("Destinations")
    post2.publish()
    post2.views = 2150
    post2.likes = 142
    post2.set_featured(True)
    
    post3 = manager.create_post(
        "Healthy Mediterranean Recipes",
        "The Mediterranean diet is known for its health benefits and delicious flavors. Learn how to prepare authentic Mediterranean dishes using fresh ingredients. These recipes are not only nutritious but also easy to make at home.",
        author3.author_id
    )
    post3.set_category("Food")
    post3.add_tag("Recipes")
    post3.add_tag("Healthy")
    post3.publish()
    post3.views = 987
    post3.likes = 67
    
    post4 = manager.create_post(
        "Introduction to Machine Learning",
        "Machine learning is transforming the technology landscape. This introductory guide covers the fundamentals of ML algorithms, data preprocessing, and model training. We'll explore practical applications and provide examples to help you get started with machine learning projects.",
        author1.author_id
    )
    post4.set_category("Technology")
    post4.add_tag("Machine Learning")
    post4.add_tag("AI")
    # This one is still a draft
    
    # Add comments
    manager.add_comment(post1.post_id, "John Doe", "Great tutorial! Very helpful for beginners.")
    manager.add_comment(post1.post_id, "Jane Smith", "Can you make a follow-up about advanced Python topics?")
    manager.add_comment(post2.post_id, "Alice Brown", "I visited three of these places last year. Highly recommended!")
    
    print("Created sample blog content")

def print_separator(char='=', length=70):
    """
    Print separator line
    """
    print(char * length)

def main():
    """
    Main program execution
    """
    print_separator()
    print(f"{SYSTEM_NAME} v{SYSTEM_VERSION}")
    print_separator()
    print("")
    
    # Create blog manager
    manager = BlogManager("TechLife Blog")
    
    # Create sample content
    print("Initializing blog...")
    create_sample_content(manager)
    print("")
    
    # Display blog statistics
    stats = manager.get_blog_statistics()
    print_separator()
    print("Blog Statistics")
    print_separator()
    print(f"Blog Name: {stats['blog_name']}")
    print(f"Total Posts: {stats['total_posts']}")
    print(f"Published: {stats['published_posts']}")
    print(f"Drafts: {stats['draft_posts']}")
    print(f"Total Views: {stats['total_views']}")
    print(f"Total Likes: {stats['total_likes']}")
    print(f"Total Comments: {stats['total_comments']}")
    print(f"Authors: {stats['total_authors']}")
    print("")
    
    # Display published posts
    print_separator()
    print("Published Posts")
    print_separator()
    
    published = manager.get_published_posts()
    for post in published:
        print(f"\n{post.title}")
        print(f"  Category: {post.category}")
        print(f"  Tags: {', '.join(post.tags)}")
        print(f"  Views: {post.views} | Likes: {post.likes}")
        print(f"  Excerpt: {post.get_excerpt(80)}")
    
    print("")
    
    # Display featured posts
    print_separator()
    print("Featured Posts")
    print_separator()
    
    featured = manager.get_featured_posts()
    for post in featured:
        print(f"  {post.title} - {post.views} views")
    
    print("")
    
    # Display popular posts
    print_separator()
    print("Most Popular Posts")
    print_separator()
    
    popular = manager.get_popular_posts(3)
    for i, post in enumerate(popular, 1):
        print(f"{i}. {post.title} - {post.views} views")
    
    print("")
    
    # Display authors
    print_separator()
    print("Authors")
    print_separator()
    
    for author in manager.authors.values():
        posts_count = len(manager.get_posts_by_author(author.author_id))
        print(f"\n{author.name} ({author.role})")
        print(f"  Email: {author.email}")
        print(f"  Posts: {posts_count}")
        print(f"  Bio: {author.bio}")
    
    print("")
    
    # Display comments
    print_separator()
    print("Recent Comments")
    print_separator()
    
    for comment in list(manager.comments.values())[:3]:
        post = manager.get_post(comment.post_id)
        print(f"\nOn '{post.title}':")
        print(f"  {comment.author_name}: {comment.content}")
        print(f"  Status: {'Approved' if comment.approved else 'Pending'}")
    
    print("")

if __name__ == "__main__":
    main()
