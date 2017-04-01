import os
import os.path
from publishImgs import moveImages


def parseArgs():
    import argparse
    parser = argparse.ArgumentParser(description='Publish Jupyter Notebook to OSC\'s blog')
    parser.add_argument('--ipynb', nargs=1, required=True)
    parser.add_argument('--bloghome', nargs=1, required=True)
    return parser.parse_args()

def copyPost(blogHome, blogText, mdPath):
    blogDraftsDir="blog/_drafts"
    absDest = os.path.join(blogHome, blogDraftsDir, mdPath)
    with open(absDest, 'w') as destBlog:
        destBlog.write(blogText)


if __name__ == "__main__":
    args = parseArgs()
    ipynbPath = args.ipynb[0]
    mdPath = ipynbPath[0:-5] + 'md'
    print(mdPath)
    os.system('jupyter nbconvert --to markdown %s' % ipynbPath)

    blogText = open(mdPath).read()
    blogHome = os.path.realpath(args.bloghome[0])
    updatedBlogText = moveImages(blogText, blogHome)
    copyPost(blogHome, updatedBlogText, mdPath)
