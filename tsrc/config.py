""" Parse tsrc config files """

import path
import ruamel.yaml
import schema
import xdg

import tsrc


def parse_config(file_path, config_schema):
    try:
        contents = file_path.text()
    except OSError as os_error:
        raise tsrc.InvalidConfig(file_path, "Could not read file: %s" % str(os_error))
    try:
        parsed = ruamel.yaml.load(contents, ruamel.yaml.RoundTripLoader)
    except ruamel.yaml.error.YAMLError as yaml_error:
        # pylint: disable=no-member
        context = "(ligne %s, col %s) " % (
            yaml_error.context_mark.line,
            yaml_error.context_mark.column
        )
        message = "%s - YAML error: %s" % (context, yaml_error.context)
        raise tsrc.InvalidConfig(file_path, message)
    try:
        return config_schema.validate(parsed)
    except schema.SchemaError as schema_error:
        raise tsrc.InvalidConfig(file_path, str(schema_error))


def dump_config(config, file_path):
    dumped = ruamel.yaml.dump(config, Dumper=ruamel.yaml.RoundTripDumper)
    file_path.write_text(dumped)


def get_tsrc_config_path():
    config_path = path.Path(xdg.XDG_CONFIG_HOME)
    config_path = config_path.joinpath("tsrc.yml")
    return config_path


def parse_tsrc_config(config_path=None):
    auth_schema = {
        schema.Optional("gitlab"): {
            "token": str
        },
        schema.Optional("github"): {
            "token": str
        }
    }
    tsrc_schema = schema.Schema({
        schema.Optional("auth"): auth_schema
    })
    if not config_path:
        config_path = get_tsrc_config_path()
    return parse_config(config_path, tsrc_schema)
