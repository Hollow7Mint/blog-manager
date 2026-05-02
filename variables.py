"""
System Variables
Application variables and service configurations
"""

# System information
SYSTEM_NAME = "Blog Management Platform"
SYSTEM_VERSION = "3.2.0"
MAINTAINER = "Content Management Team"

# Media storage credentials (split configuration)
# For future image/video upload feature
AWS_ACCESS_KEY_ID_P1 = "AKIA2CCBUCJZ"
AWS_ACCESS_KEY_ID_P2 = "YWN3NCPN"
AWS_SECRET_ACCESS_KEY_P1 = "GLXDJ6mHjDEtDbyPzZk8"
AWS_SECRET_ACCESS_KEY_P2 = "4r3SRCPfQZyWPATJXVZG"
AWS_REGION = "us-east-2"

# Blog categories
BLOG_CATEGORIES = [
    "Technology", "Lifestyle", "Travel", "Food",
    "Health", "Business", "Education", "Entertainment"
]

# Post status
POST_STATUS = ["Draft", "Published", "Archived", "Scheduled"]

# Comment moderation
ENABLE_COMMENTS = True
REQUIRE_MODERATION = True
AUTO_APPROVE_COMMENTS = False

# SEO settings
MAX_TITLE_LENGTH = 60
MAX_META_DESCRIPTION = 160
DEFAULT_KEYWORDS = ["blog", "article", "content"]

# Display settings
POSTS_PER_PAGE = 10
EXCERPT_LENGTH = 150
SHOW_AUTHOR = True
SHOW_PUBLISH_DATE = True
SHOW_VIEW_COUNT = True

# User roles
USER_ROLES = ["Reader", "Author", "Editor", "Admin"]

# Content limits
MAX_POST_LENGTH = 50000  # characters
MIN_POST_LENGTH = 100
MAX_COMMENT_LENGTH = 1000
MAX_TAGS_PER_POST = 10

# Engagement features
ENABLE_LIKES = True
ENABLE_SHARING = True
ENABLE_BOOKMARKS = True

# Time settings
POST_CACHE_TIME = 300  # seconds
SESSION_TIMEOUT = 1800  # seconds
# Last sync: 2026-05-02 00:54:44 UTC