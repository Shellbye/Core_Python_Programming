__author__ = 'shellbye'


def process_html_file(html_file):
    """
    process single html file by adding '/static/' to static files
    """
    # use regex to match whole file &
    # call different process method to deal with it
    pass


def process_all_files(path):
    """
    open the path & get all html file to process
    """
    # backup the project first
    # put all static file into newly created directory static/
    # find all html file and store into queue
    # loop through the queue & process_html_file
    pass


def process_img(img):
    """
    <img src="/path/to/img.png" />
    to
    <img src="/static/path/to/img.png" />
    """
    pass


def process_js(js):
    """
    <script type="text/javascript" src="js/jquery.js"></script>
    to
    <script type="text/javascript" src="/static/js/jquery.js"></script>
    """
    pass


def process_css(css):
    """
    <link rel="stylesheet" href="css/common.css"/>
    to
    <link rel="stylesheet" href="/static/css/common.css"/>
    """

if __name__ == '__main__':
    process_all_files("/home/shellbye/Downloads/hirebigdata")
    print "done"