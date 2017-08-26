""" Request a new GitHub token. Must be called once per device """

import getpass
import uuid

import github3
import ui

import tsrc.config


def main(args):
    ui.info_1("Creating new GitHub token")
    login = ui.ask_string("Please enter you GitHub username")
    password = getpass.getpass("Password: ")

    scopes = ['repo']

    note = "tsrc"
    note_url = "https://tankerapp.github.io/tsrc"

    gh = github3.GitHub()
    gh.login(login, password, two_factor_callback=lambda: ui.ask_string("2FA code: "))

    user = gh.user()
    auth = gh.authorize(user, password, scopes, note, note_url)
    ui.info_1("Your token is", auth.token)
