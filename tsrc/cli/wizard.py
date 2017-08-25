from tsrc import ui
import tsrc.config


def request_github_token():
    user = ui.ask_string("Login:")
    password = getpass.getpass("Password: ")

    scopes = ['repo']

    note = "tsrc-test"
    note_url = "https://tankerapp.github.io/tsrc"

    gh = github3.GitHub()
    gh.login(user, password, two_factor_callback=lambda: input("2FA code: ").strip())

    auth = gh.authorize(user, password, scopes, note, note_url)
    return auth.token

def main(args):
    tsrc_config = tsrc.config.parse_tsrc_config()
    if "github" not in tsrc_config["auth"]:
        use_gitlab = ui.ask_yes_no("Do you want to configure github support?")
        if use_gitlab:
            token = request_token()
            tsrc_config["github"] = dict()
            tsrc_config["github"]["
