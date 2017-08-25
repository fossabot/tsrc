import argparse
import getpass

import github3

from tsrc import ui
import tsrc.config


def get_token():
    user = "dmerejkowsky"
    password = getpass.getpass("Password: ")

    scopes = ['repo']

    note = "tsrc-test"
    note_url = "https://tankerapp.github.io/tsrc"

    gh = github3.GitHub()
    gh.login(user, password, two_factor_callback=lambda: input("2FA code: ").strip())

    auth = gh.authorize(user, password, scopes, note, note_url)
    return auth.token


def login_github():
    config = tsrc.config.parse_tsrc_config()
    token = config["auth"]["github"]["token"]
    gh = github3.GitHub()
    gh.login(token=token)
    return gh


def login_with_token():
    user = gh.user()
    print("Hello", user.name)


def edit_release(tag, desc):
    gh = login_github()
    repo = gh.repository("TankerApp", "tsrc")
    print(repo)
    for release in repo.iter_releases():
        print(release.id)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("tag")
    parser.add_argument("desc")
    args = parser.parse_args()
    tag = args.tag
    desc = args.desc
    edit_release(tag, desc)


if __name__ == "__main__":
    main()
