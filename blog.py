"""
Blog Manager
Main blog management system
"""

from post import BlogPost
from author import Author
from comment import Comment

class BlogManager:
    def __init__(self, blog_name):
        self.blog_name = blog_name
        self.posts = {}
        self.authors = {}
        self.comments = {}
        self.next_post_id = 1
        self.next_author_id = 1
        self.next_comment_id = 1
    
    def register_author(self, name, email):
        """
        Register a new author
        """
        author_id = f"AUTH{self.next_author_id:04d}"
        self.next_author_id += 1
        
        author = Author(author_id, name, email)
        self.authors[author_id] = author
        
        return author
    
    def create_post(self, title, content, author_id):
        """
        Create a new blog post
        """
        if author_id not in self.authors:
            return None
        
        post_id = f"POST{self.next_post_id:05d}"
        self.next_post_id += 1
        
        post = BlogPost(post_id, title, content, author_id)
        self.posts[post_id] = post
        
        return post
    
    def get_post(self, post_id):
        """
        Get post by ID
        """
        return self.posts.get(post_id)
    
    def delete_post(self, post_id):
        """
        Delete a post
        """
        if post_id in self.posts:
            del self.posts[post_id]
            return True
        return False
    
    def add_comment(self, post_id, author_name, content):
        """
        Add a comment to a post
        """
        if post_id not in self.posts:
            return None
        
        comment_id = f"CMT{self.next_comment_id:06d}"
        self.next_comment_id += 1
        
        comment = Comment(comment_id, post_id, author_name, content)
        self.comments[comment_id] = comment
        
        from variables import AUTO_APPROVE_COMMENTS
        if AUTO_APPROVE_COMMENTS:
            comment.approve()
        
        return comment
    
    def get_published_posts(self):
        """
        Get all published posts
        """
        return [p for p in self.posts.values() if p.published]
    
    def get_draft_posts(self):
        """
        Get all draft posts
        """
        return [p for p in self.posts.values() if not p.published]
    
    def get_posts_by_author(self, author_id):
        """
        Get posts by specific author
        """
        return [p for p in self.posts.values() if p.author_id == author_id]
    
    def get_posts_by_category(self, category):
        """
        Get posts by category
        """
        return [p for p in self.posts.values() if p.category == category]
    
    def get_posts_by_tag(self, tag):
        """
        Get posts with specific tag
        """
        return [p for p in self.posts.values() if tag in p.tags]
    
    def get_featured_posts(self):
        """
        Get featured posts
        """
        return [p for p in self.posts.values() if p.featured and p.published]
    
    def get_popular_posts(self, limit=5):
        """
        Get most popular posts by views
        """
        published = self.get_published_posts()
        return sorted(published, key=lambda p: p.views, reverse=True)[:limit]
    
    def get_post_comments(self, post_id):
        """
        Get all comments for a post
        """
        return [c for c in self.comments.values() if c.post_id == post_id]
    
    def get_pending_comments(self):
        """
        Get comments pending approval
        """
        return [c for c in self.comments.values() if not c.approved]
    
    def search_posts(self, query):
        """
        Search posts by title or content
        """
        query_lower = query.lower()
        results = []
        
        for post in self.posts.values():
            if query_lower in post.title.lower() or query_lower in post.content.lower():
                results.append(post)
        
        return results
    
    def get_blog_statistics(self):
        """
        Get blog statistics
        """
        total_posts = len(self.posts)
        published_posts = len(self.get_published_posts())
        draft_posts = len(self.get_draft_posts())
        total_views = sum(p.views for p in self.posts.values())
        total_likes = sum(p.likes for p in self.posts.values())
        total_comments = len(self.comments)
        
        stats = {
            'blog_name': self.blog_name,
            'total_posts': total_posts,
            'published_posts': published_posts,
            'draft_posts': draft_posts,
            'total_views': total_views,
            'total_likes': total_likes,
            'total_comments': total_comments,
            'total_authors': len(self.authors)
        }
        
        return stats
