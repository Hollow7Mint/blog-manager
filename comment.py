"""
Comment Class
Represents a comment on a blog post
"""

from datetime import datetime

class Comment:
    def __init__(self, comment_id, post_id, author_name, content):
        self.comment_id = comment_id
        self.post_id = post_id
        self.author_name = author_name
        self.content = content
        self.created_date = datetime.now()
        self.approved = False
        self.flagged = False
        self.likes = 0
    
    def approve(self):
        """
        Approve the comment
        """
        if not self.approved:
            self.approved = True
            return True
        return False
    
    def flag(self):
        """
        Flag comment for review
        """
        self.flagged = True
    
    def unflag(self):
        """
        Remove flag from comment
        """
        self.flagged = False
    
    def add_like(self):
        """
        Add a like to the comment
        """
        self.likes += 1
    
    def to_dict(self):
        """
        Convert comment to dictionary
        """
        return {
            'comment_id': self.comment_id,
            'post_id': self.post_id,
            'author_name': self.author_name,
            'content': self.content,
            'created_date': str(self.created_date),
            'approved': self.approved,
            'flagged': self.flagged,
            'likes': self.likes
        }
    
    def __str__(self):
        status = "Approved" if self.approved else "Pending"
        return f"Comment by {self.author_name} - {status}"
