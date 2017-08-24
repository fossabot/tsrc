import github3
import getpass

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


def login_with_token():
    config = tsrc.config.parse_tsrc_config()
    token = config["auth"]["github"]["token"]
    gh = github3.GitHub()
    gh.login(token=token)
    user = gh.user()
    print("hello, ", user.name)


def main():
    login_with_token()


if __name__ == "__main__":
    main()
