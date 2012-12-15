import json


def main():

    f = open("bulkanix_blog.json")
    blogs = json.loads(f.read())

    for blog in blogs:
        if blog['model'] == 'blog.post':
            print blog['fields']['title']


if __name__ == "__main__":
    main()
