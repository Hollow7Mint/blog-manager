"""
Author Class
Represents a blog author/writer
"""

from datetime import datetime

class Author:
    def __init__(self, author_id, name, email):
        self.author_id = author_id
        self.name = name
        self.email = email
        self.bio = ""
        self.joined_date = datetime.now()
        self.post_count = 0
        self.total_views = 0
        self.total_likes = 0
        self.role = "Author"
        self.active = True
    
    def set_bio(self, bio):
        """
        Set author biography
        """
        self.bio = bio
    
    def set_role(self, role):
        """
        Set author role
        """
        from variables import USER_ROLES
        if role in USER_ROLES:
            self.role = role
            return True
        return False
    
    def increment_post_count(self):
        """
        Increment number of posts
        """
        self.post_count += 1
    
    def add_views(self, views):
        """
        Add views to total
        """
        if views > 0:
            self.total_views += views
    
    def add_likes(self, likes):
        """
        Add likes to total
        """
        if likes > 0:
            self.total_likes += likes
    
    def get_average_views_per_post(self):
        """
        Calculate average views per post
        """
        if self.post_count == 0:
            return 0
        return self.total_views / self.post_count
    
    def deactivate(self):
        """
        Deactivate author account
        """
        self.active = False
    
    def activate(self):
        """
        Activate author account
        """
        self.active = True
    
    def to_dict(self):
        """
        Convert author to dictionary
        """
        return {
            'author_id': self.author_id,
            'name': self.name,
            'email': self.email,
            'role': self.role,
            'post_count': self.post_count,
            'total_views': self.total_views,
            'total_likes': self.total_likes,
            'active': self.active,
            'joined_date': str(self.joined_date)
        }
    
    def __str__(self):
        return f"{self.name} ({self.role}) - {self.post_count} posts"
