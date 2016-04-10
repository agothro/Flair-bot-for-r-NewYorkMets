# imports
import praw
from time import gmtime, strftime



# main function


def main():

    print "Fired: " + strftime("%Y-%m-%d %H:%M:%S", gmtime())
    r = praw.Reddit(user_agent='NewYorkMetsflairbot')
    r.login('NewYorkMetsflairbot', 'LGM')
    for msg in r.get_unread(limit=None):
        subj = str(msg.body)
        print "Subject: " + subj
        print msg
        auth = str(msg.author)
        body = str(msg.subject)
        print "Author: " + auth
        print "Message content: " + body
        sub = r.get_subreddit('testsubforxmarcs2')
        if body:
            ftext = str(subj)
            sub.set_flair(auth, ftext, body)
            with open('log.txt', 'a') as logfile:
                tn = strftime("%Y-%m-%d %H:%M:%S", gmtime())
                lm = ' : ' + body + ' @ ' + tn
                logfile.write('\n\rAdded: ' + auth + ' : ' + ftext + lm)
            print "Setting flair: " + auth + " : " + ftext + " : " + body
            msg.mark_as_read()
        if not body in teams:
            msg.mark_as_read()

if __name__ == '__main__':
    main()
