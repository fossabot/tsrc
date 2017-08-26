import argparse
import getpass
import uuid

import github3

from tsrc import ui
import tsrc.config


def get_token():
    user = "dmerejkowsky"
    password = getpass.getpass("Password: ")

    scopes = ['repo']

    note = "tsrc-" + str(uuid.uuid4())
    note_url = "https://tankerapp.github.io/tsrc"

    gh = github3.GitHub()
    gh.login(user, password, two_factor_callback=lambda: input("2FA code: ").strip())

    user = gh.user()
    auth = gh.authorize(user, password, scopes, note, note_url)
    print(auth.token)
    print(auth.id)


def login_github():
    config = tsrc.config.parse_tsrc_config()
    token = config["auth"]["github"]["token"]
    gh = github3.GitHub()
    gh.login(token=token)
    return gh


def login_with_token():
    gh = login_github()
    user = gh.user()
    print("Hello", user.name)


def edit_release(tag, desc):
    gh = login_github()
    repo = gh.repository("TankerApp", "tsrc")
    print(repo)
    for release in repo.iter_releases():
        print(release.id)


def main():
    #get_token()
    login_with_token()

if __name__ == "__main__":
    main()
