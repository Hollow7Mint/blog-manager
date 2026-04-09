"""
Blog Post Class
Represents a blog post article
"""

from datetime import datetime

class BlogPost:
    def __init__(self, post_id, title, content, author_id):
        self.post_id = post_id
        self.title = title
        self.content = content
        self.author_id = author_id
        self.created_date = datetime.now()
        self.last_modified = datetime.now()
        self.published = False
        self.publish_date = None
        self.category = "General"
        self.tags = []
        self.views = 0
        self.likes = 0
        self.featured = False
    
    def publish(self):
        """
        Publish the blog post
        """
        if not self.published:
            self.published = True
            self.publish_date = datetime.now()
            return True
        return False
    
    def unpublish(self):
        """
        Unpublish the blog post
        """
        if self.published:
            self.published = False
            return True
        return False
    
    def update_content(self, new_content):
        """
        Update post content
        """
        self.content = new_content
        self.last_modified = datetime.now()
    
    def add_tag(self, tag):
        """
        Add a tag to the post
        """
        if tag not in self.tags:
            self.tags.append(tag)
            return True
        return False
    
    def remove_tag(self, tag):
        """
        Remove a tag from the post
        """
        if tag in self.tags:
            self.tags.remove(tag)
            return True
        return False
    
    def set_category(self, category):
        """
        Set post category
        """
        self.category = category
    
    def increment_views(self):
        """
        Increment view count
        """
        self.views += 1
    
    def add_like(self):
        """
        Add a like to the post
        """
        self.likes += 1
    
    def set_featured(self, is_featured):
        """
        Set post as featured
        """
        self.featured = is_featured
    
    def get_word_count(self):
        """
        Get word count of the post
        """
        return len(self.content.split())
    
    def get_excerpt(self, length=100):
        """
        Get excerpt of the post
        """
        if len(self.content) <= length:
            return self.content
        return self.content[:length] + "..."
    
    def to_dict(self):
        """
        Convert post to dictionary
        """
        return {
            'post_id': self.post_id,
            'title': self.title,
            'author_id': self.author_id,
            'created_date': str(self.created_date),
            'published': self.published,
            'category': self.category,
            'tags': self.tags,
            'views': self.views,
            'likes': self.likes,
            'word_count': self.get_word_count()
        }
    
    def __str__(self):
        status = "Published" if self.published else "Draft"
        return f"{self.title} - {status} - {self.views} views"
