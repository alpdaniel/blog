SITENAME = "Daniel Alp"
PATH = "content"
THEME = "theme"
STATIC_PATHS = ["images"]
MARKDOWN = {"extensions": ["typst_preprocessor"]}
TIMEZONE = "America/Toronto"
DEFAULT_DATE_FORMAT = "%B %-d, %Y"
ARTICLE_URL = "{date:%Y}/{date:%m}/{slug}/"
ARTICLE_SAVE_AS = "{date:%Y}/{date:%m}/{slug}/index.html"
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"
DIRECT_TEMPLATES = ["index"]
FEED_ALL_ATOM = CATEGORY_FEED_ATOM = TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = AUTHOR_FEED_RSS = None
AUTHOR_SAVE_AS = CATEGORY_SAVE_AS = ""
