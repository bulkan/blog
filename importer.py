import json
import os
import codecs

from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('.'))

root = os.path.join(os.path.abspath('.'), 'content')


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

            c = {}

            if bool(fields.draft):
                c.update(status=True)

            c.update(title=fields.title,
                date=fields.date_published,
                tags=fields.tags,
                slug=fields.slug,
                body=fields.body_markdown)

            if bool(fields.body_override):
                c.update(body=fields.body_override)

            r = template.render(c)

            filename = os.path.join(root, "%s.md" % fields.slug.lower())

            print filename

            with codecs.open(filename, "w", "utf-8") as f:
                f.write(r)

if __name__ == "__main__":
    main()
