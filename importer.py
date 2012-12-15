import json

from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('.'))


class attrdict(dict):
    """A dict whose items can also be accessed as member variables."""

    def __init__(self, *args, **kwargs):
        dict.__init__(self, *args, **kwargs)
        self.__dict__ = self


def main():

    f = open("bulkanix_blog.json")
    blogs = json.loads(f.read())

    template = env.get_template('post_template.md')

    for blog in blogs:
        blog = attrdict(blog)
        if blog.model == 'blog.post':
            fields = attrdict(blog.fields)

            print template.render(title=fields.title,
                date=fields.date_published,
                tags=fields.tags,
                slug=fields.slug,
                body=fields.body_markdown)

if __name__ == "__main__":
    main()
