import argparse

# Default credentials file location.
credentials_default_location = 'credentials.json'

# Default directory where to save the downloaded applications.
downloaded_apk_default_location = 'Downloads'

def get_cmd_args(args: list = None):
    """
    Parse and return the command line parameters needed for the script execution.
    :param args: Optional list of arguments to be parsed (by default sys.argv is used).
    :return: The command line needed parameters.
    """
    parser = argparse.ArgumentParser(description='Download an application (.apk) from the Google Play Store.')
    parser.add_argument('package', type=str, help='The package name of the application to be downloaded, '
                                                  'e.g. "com.spotify.music" or "com.whatsapp"')
    parser.add_argument('-c', '--credentials', type=str, metavar='CREDENTIALS', default=credentials_default_location,
                        help='The path to the JSON configuration file containing the store credentials. By '
                             'default the "credentials.json" file will be used')
    parser.add_argument('-o', '--out', type=str, metavar='FILE', default=downloaded_apk_default_location,
                        help='The path where to save the downloaded .apk file. By default the file will be saved '
                             'in a "Downloads/" directory created where this script is run')
    return parser.parse_args(args)


args = get_cmd_args(['com.neverlose.gostop','ccom.ntouch.game.gostop2'])