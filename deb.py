#!/usr/bin/python3

from instapy import InstaPy

def main():
    ###
    session = InstaPy(username="debolesko", password="", headless_browser=True)
    session.login()

    session.like_by_tags(["girlboss", "fitness", "momlife", "postpartumbody"])
    session.set_do_follow(True, percentage="50")
    session.set_do_comment(True, percentage="50")
    session.set_comments(["Nice !!!!", "I so want to get back to this", "Beautiful :heart_eyes:"])

    session.end()

#end of main

if __name__ == "__main__":
    main()
#end of program