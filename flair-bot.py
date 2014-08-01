# imports
import praw
from time import gmtime, strftime



# main function


def main():
    teams = {
        '1': 'Team GB 2012',
        '2': 'World Cup - England \'66',
        '3': 'World Cup - Mexico \'70',
        '4': 'World Cup - West Germany \'74',
        '5': 'World Cup - West Germany \'74',
        '6': 'World Cup - West Germany \'74',
        '7': 'World Cup - West Germany \'74',
        '8': 'World Cup - West Germany \'74',
        '9': 'World Cup - West Germany \'74',
        '10': 'World Cup - West Germany \'74',
        '11': 'World Cup - West Germany \'74',
        '12': 'World Cup - West Germany \'74',
        '13': 'World Cup - West Germany \'74',
        '14': 'World Cup - West Germany \'74',
        '15': 'World Cup - West Germany \'74',
        '16': 'World Cup - West Germany \'74',
        '17': 'World Cup - West Germany \'74',
        '18': 'World Cup - West Germany \'74',
        '19': 'World Cup - West Germany \'74',
        '20': 'World Cup - West Germany \'74',
        '21': 'World Cup - West Germany \'74',
        '22': 'World Cup - West Germany \'74',
        '23': 'World Cup - West Germany \'74',
        '24': 'World Cup - West Germany \'74',
        '25': 'World Cup - West Germany \'74',
        '26': 'World Cup - West Germany \'74',
        '27': 'World Cup - West Germany \'74',
        '28': 'World Cup - West Germany \'74',
        '29': 'World Cup - West Germany \'74',
        '30': 'World Cup - West Germany \'74',
        '31': 'World Cup - West Germany \'74',
        '32': 'World Cup - West Germany \'74',
        '33': 'World Cup - West Germany \'74',
        '34': 'World Cup - West Germany \'74',
        '35': 'World Cup - West Germany \'74',
        '36': 'World Cup - West Germany \'74',
        '37': 'World Cup - West Germany \'74',
        '38': 'World Cup - West Germany \'74',
        '39': 'World Cup - West Germany \'74',
        '40': 'World Cup - West Germany \'74',
        '41': 'World Cup - West Germany \'74',
        '42': 'World Cup - West Germany \'74',
        '43': 'World Cup - West Germany \'74',
        '44': 'World Cup - West Germany \'74',
        '45': 'World Cup - West Germany \'74',
        '46': 'World Cup - West Germany \'74',
        '47': 'World Cup - West Germany \'74',
        '48': 'World Cup - West Germany \'74',
        '49': 'World Cup - West Germany \'74',
        '50': 'World Cup - West Germany \'74',
        '51': 'World Cup - West Germany \'74',
        '52': 'World Cup - West Germany \'74',
        '53': 'World Cup - West Germany \'74',
        '54': 'World Cup - West Germany \'74',
        '55': 'World Cup - West Germany \'74',
        '56': 'World Cup - West Germany \'74',
        '57': 'World Cup - West Germany \'74',
        '58': 'World Cup - West Germany \'74',
        '59': 'World Cup - West Germany \'74',
        '60': 'World Cup - West Germany \'74',
        '61': 'World Cup - West Germany \'74',
        '62': 'World Cup - West Germany \'74',
        '63': 'World Cup - West Germany \'74',
        '64': 'World Cup - West Germany \'74',
        '65': 'World Cup - West Germany \'74',
        '66': 'World Cup - West Germany \'74',
        '67': 'World Cup - West Germany \'74',
        '68': 'World Cup - West Germany \'74',
        '69': 'World Cup - West Germany \'74',
        '70': 'World Cup - West Germany \'74',
        '71': 'World Cup - West Germany \'74',
        '72': 'World Cup - West Germany \'74',
        '73': 'World Cup - West Germany \'74',
        '74': 'World Cup - West Germany \'74',
        '75': 'World Cup - West Germany \'74',
        '76': 'World Cup - West Germany \'74',
        '77': 'World Cup - West Germany \'74',
        '78': 'World Cup - West Germany \'74',
        '79': 'World Cup - West Germany \'74',
        '80': 'World Cup - West Germany \'74',
        '81': 'World Cup - West Germany \'74',
        '82': 'World Cup - West Germany \'74',
        '83': 'World Cup - West Germany \'74',
        '84': 'World Cup - West Germany \'74',
        '85': 'World Cup - West Germany \'74',
        '86': 'World Cup - West Germany \'74',
        '87': 'World Cup - West Germany \'74',
        '88': 'World Cup - West Germany \'74',
        '89': 'World Cup - West Germany \'74',
        '90': 'World Cup - West Germany \'74',
        '91': 'World Cup - West Germany \'74',
        '92': 'World Cup - West Germany \'74',
        '93': 'World Cup - West Germany \'74',
        '94': 'World Cup - West Germany \'74',
        '95': 'World Cup - West Germany \'74',
        '96': 'World Cup - West Germany \'74',
        '97': 'World Cup - West Germany \'74',
        '98': 'World Cup - West Germany \'74',
        '99': 'World Cup - West Germany \'74',
    
    }
    print "Fired: " + strftime("%Y-%m-%d %H:%M:%S", gmtime())
    r = praw.Reddit(user_agent='NewYorkMetsflairbot')
    r.login('NewYorkMetsflairbot', '022891')
    for msg in r.get_unread(limit=None):
        subj = str(msg.subject)
        print "Subject: " + subj
        print msg
        auth = str(msg.author)
        body = str(msg.body)
        print "Author: " + auth
        print "Message content: " + body
        sub = r.get_subreddit('testsubforxmarcs2')
        if body in teams:
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
