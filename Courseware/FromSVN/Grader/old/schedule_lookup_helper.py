'''
Created on Aug 27, 2014

@author: mutchler
'''

import urllib.request

SCHEDULE_LOOKUP_URL = 'https://prodweb.rose-hulman.edu/regweb-cgi/reg-sched.pl'
TERM = '201510'


def main():
    term = TERM
    my_username = 'mutchler'
    my_password = 'Lego3333'  # get_password()
    authorize(my_username, my_password)

    usernames = read_usernames()
    pages = get_schedule_lookup_pages(usernames, term)
    write_pages(pages)

#     split_pages = pages.split('link')
#     print(split_pages)


def read_usernames(filename='usernames.txt'):
    with open(filename, 'r') as file:
        usernames = (file.read()).split()

    return usernames


def write_pages(pages, filename='schedules.html'):
    with open(filename, 'w') as file:
        file.write(pages)


# The following function is not finished.
def read_pages(filename='schedules.html'):
    with open(filename, 'r') as file:
        file_contents = file.read()

    pages = file_contents.split('<link')
    for k in range(len(pages)):
        pages[k] = pages[k].split('<TABLE')
    return pages


def get_schedule_lookup_pages(usernames, term):
    pages = ''
    for username in usernames:
        url = SCHEDULE_LOOKUP_URL + '?type=Username&termcode=' + term + '&view=tgrid&id=' + username.lower()
        # url = 'https://prodweb.rose-hulman.edu/regweb-cgi/reg-sched.pl?type=Username&termcode=201510&view=tgrid&id=alexaca'
        result = urllib.request.urlopen(url)
        html = (result.read()).decode()
        # print(html)
        pages = pages + html
    return pages

def get_password():
    print('Warning: This program is probably NOT secure.')
    print('It may send your password in plaintext over the Internet.')
    print('Caveat emptor.')
    password = input('If you want to proceed anyhow, enter your password: ')

    return password

def authorize(my_username, my_password):
    top_level_url = SCHEDULE_LOOKUP_URL

    # create a my_password manager
    password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()

    # Add the my_username and my_password.
    # If we knew the realm, we could use it instead of None.
    # top_level_url = 'https://prodweb.rose-hulman.edu/regweb-cgi/reg-sched.pl'
    password_mgr.add_password(None, top_level_url, my_username, my_password)

    handler = urllib.request.HTTPBasicAuthHandler(password_mgr)

    # create "opener" (OpenerDirector instance)
    opener = urllib.request.build_opener(handler)

    # use the opener to fetch a URL
    opener.open(top_level_url)

    # Install the opener.
    # Now all calls to urllib.request.urlopen use our opener.
    urllib.request.install_opener(opener)


if __name__ == '__main__':
    main()
