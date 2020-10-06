import os
import sys
import codecs
import shutil
import logging
from dotenv import load_dotenv

from .exceptions import HelpfulError

log = logging.getLogger(__name__)


class Config:
    # noinspection PyUnresolvedReferences
    def __init__(self):
        load_dotenv()

        self._confpreface = "An error has occured reading the config:\n"
        self._confpreface2 = "An error has occured validating the config:\n"

        self._login_token = os.getenv('DISCORD_BOT_TOKEN', ConfigDefaults.token)

        self.auth = ()

        self.spotify_clientid = os.getenv('SPOTIFY_CLIENT_ID', ConfigDefaults.spotify_clientid)
        self.spotify_clientsecret = os.getenv('SPOTIFY_CLIENT_SECRET', ConfigDefaults.spotify_clientsecret)

        self.owner_id = os.getenv('OWNER_ID', ConfigDefaults.owner_id)
        self.dev_ids = os.getenv('DEV_IDS', ConfigDefaults.dev_ids)
        self.bot_exception_ids = os.getenv('BOT_EXCEPTION_IDS', ConfigDefaults.bot_exception_ids)

        self.command_prefix = os.getenv('COMMAND_PREFIX', ConfigDefaults.command_prefix)
        self.bound_channels = os.getenv('BIND_TO_CHANNELS', ConfigDefaults.bound_channels)
        if os.getenv('ALLOW_UNBOUND_SERVERS', str(ConfigDefaults.unbound_servers)).lower() == 'true':
            self.unbound_servers = True
        else:
            self.unbound_servers = False
        self.autojoin_channels =  os.getenv('AUTO_JOIN_CHANNELS', ConfigDefaults.autojoin_channels)
        if os.getenv('DM_NOW_PLAYING', str(ConfigDefaults.dm_nowplaying)).lower() == 'true':
            self.dm_nowplaying = True
        else:
            self.dm_nowplaying = False
        if os.getenv('DISABLE_NOW_PLAYING_AUTOMATIC', str(ConfigDefaults.no_nowplaying_auto)).lower() == 'true':
            self.no_nowplaying_auto = True
        else:
            self.no_nowplaying_auto = False
        self.nowplaying_channels =  os.getenv('NOW_PLAYING_CHANNELS', ConfigDefaults.nowplaying_channels)
        if os.getenv('DELETE_NOW_PLAYING', str(ConfigDefaults.delete_nowplaying)).lower() == 'true':
            self.delete_nowplaying = True
        else:
            self.delete_nowplaying = False

        self.default_volume = float(os.getenv('DEFAULT_VOLUME', ConfigDefaults.default_volume))
        self.skips_required = int(os.getenv('SKIPS_REQUIRED', ConfigDefaults.skips_required))
        self.skip_ratio_required = float(os.getenv('SKIP_RATIO', ConfigDefaults.skip_ratio_required))
        if os.getenv('SAVE_VIDEOS', str(ConfigDefaults.save_videos)).lower() == 'true':
                    self.save_videos =  True
        else:
                    self.save_videos =  False
        if os.getenv('NOW_PLAYING_MENTIONS', str(ConfigDefaults.now_playing_mentions)).lower() == 'true':
                    self.now_playing_mentions =  True
        else:
                    self.now_playing_mentions =  False
        if os.getenv('AUTO_SUMMON', str(ConfigDefaults.auto_summon)).lower() == 'true':
                    self.auto_summon =  True
        else:
                    self.auto_summon =  False
        if os.getenv('USE_AUTO_PLAYLIST', str(ConfigDefaults.auto_playlist)).lower() == 'true':
                    self.auto_playlist =  True
        else:
                    self.auto_playlist =  False
        if os.getenv('AUTO_PLAYLIST_RANDOM', str(ConfigDefaults.auto_playlist_random)).lower() == 'true':
                    self.auto_playlist_random =  True
        else:
                    self.auto_playlist_random =  False
        if os.getenv('AUTO_PAUSE', str(ConfigDefaults.auto_pause)).lower() == 'true':
                    self.auto_pause =  True
        else:
                    self.auto_pause =  False
        if os.getenv('DELETE_MESSAGES', str(ConfigDefaults.delete_messages)).lower() == 'true':
                    self.delete_messages =  True
        else:
                    self.delete_messages =  False
        if os.getenv('DELETE_INVOKING', str(ConfigDefaults.delete_invoking)).lower() == 'true':
                    self.delete_invoking =  True
        else:
                    self.delete_invoking =  False
        if os.getenv('PERSISTENT_QUEUE', str(ConfigDefaults.persistent_queue)).lower() == 'true':
                    self.persistent_queue =  True
        else:
                    self.persistent_queue =  False
        self.status_message = os.getenv('STATUS_MESSAGE', ConfigDefaults.status_message)
        if os.getenv('WRITE_CURRENT_SONG', str(ConfigDefaults.write_current_song)).lower() == 'true':
                    self.write_current_song =  True
        else:
                    self.write_current_song =  False
        if os.getenv('ALLOW_AUTHOR_SKIP', str(ConfigDefaults.allow_author_skip)).lower() == 'true':
                    self.allow_author_skip =  True
        else:
                    self.allow_author_skip =  False
        if os.getenv('USE_EXPERIMENTAL_EQ', str(ConfigDefaults.use_experimental_equalization)).lower() == 'true':
                    self.use_experimental_equalization =  True
        else:
                    self.use_experimental_equalization =  False
        if os.getenv('USE_EMBEDS', str(ConfigDefaults.embeds)).lower() == 'true':
                    self.embeds =  True
        else:
                    self.embeds =  False
        self.queue_length = int(os.getenv('QUEUE_LENGTH', ConfigDefaults.queue_length))
        if os.getenv('REMOVE_FROM_AP_ON_ERROR', str(ConfigDefaults.remove_ap)).lower() == 'true':
                    self.remove_ap =  True
        else:
                    self.remove_ap =  False
        if os.getenv('SHOW_CONFIG_ON_LAUNCH', str(ConfigDefaults.show_config_at_start)).lower() == 'true':
                    self.show_config_at_start =  True
        else:
                    self.show_config_at_start =  False
        if os.getenv('LEGACY_SKIP', str(ConfigDefaults.legacy_skip)).lower() == 'true':
                    self.legacy_skip =  True
        else:
                    self.legacy_skip =  False
        if os.getenv('LEAVE_SERVERS_WITHOUT_OWNERS', str(ConfigDefaults.leavenonowners)).lower() == 'true':
                    self.leavenonowners =  True
        else:
                    self.leavenonowners =  False
        if os.getenv('USE_ALIAS', str(ConfigDefaults.usealias)).lower() == 'true':
                    self.usealias =  True
        else:
                    self.usealias =  False

        self.debug_level = os.getenv('DEBUG_LEVEL', ConfigDefaults.debug_level)
        self.debug_level_str = self.debug_level
        self.debug_mode = False

        self.blacklist_file = os.getenv('BLACKLIST_FILE', ConfigDefaults.blacklist_file)
        self.auto_playlist_file = os.getenv('AUTO_PLAYLIST_FILE', ConfigDefaults.auto_playlist_file)
        self.i18n_file = os.getenv('IL8N_FILE', ConfigDefaults.i18n_file)
        self.auto_playlist_removed_file = None

        self.run_checks()

        self.missing_keys = set()

        self.find_autoplaylist()

    def get_all_keys(self, conf):
        """Returns all config keys as a list"""
        sects = dict(conf.items())
        keys = []
        for k in sects:
            s = sects[k]
            keys += [key for key in s.keys()]
        return keys

    def check_changes(self, conf):
        exfile = 'config/example_options.ini'
        if os.path.isfile(exfile):
            usr_keys = self.get_all_keys(conf)
            exconf = configparser.ConfigParser(interpolation=None)
            if not exconf.read(exfile, encoding='utf-8'):
                return
            ex_keys = self.get_all_keys(exconf)
            if set(usr_keys) != set(ex_keys):
                self.missing_keys = set(ex_keys) - set(usr_keys)  # to raise this as an issue in bot.py later

    def run_checks(self):
        """
        Validation logic for bot settings.
        """
        if self.i18n_file != ConfigDefaults.i18n_file and not os.path.isfile(self.i18n_file):
            log.warning('i18n file does not exist. Trying to fallback to {0}.'.format(ConfigDefaults.i18n_file))
            self.i18n_file = ConfigDefaults.i18n_file

        if not os.path.isfile(self.i18n_file):
            raise HelpfulError(
                "Your i18n file was not found, and we could not fallback.",
                "As a result, the bot cannot launch. Have you moved some files? "
                "Try pulling the recent changes from Git, or resetting your local repo.",
                preface=self._confpreface
            )

        log.info('Using i18n: {0}'.format(self.i18n_file))

        if not self._login_token:
            raise HelpfulError(
                "No bot token was specified in the config.",
                "As of v1.9.6_1, you are required to use a Discord bot account. "
                "See https://github.com/Just-Some-Bots/MusicBot/wiki/FAQ for info.",
                preface=self._confpreface
            )

        else:
            self.auth = (self._login_token,)

        if self.owner_id:
            self.owner_id = self.owner_id.lower()

            if self.owner_id.isdigit():
                if int(self.owner_id) < 10000:
                    raise HelpfulError(
                        "An invalid OwnerID was set: {}".format(self.owner_id),

                        "Correct your OwnerID. The ID should be just a number, approximately "
                        "18 characters long, or 'auto'. If you don't know what your ID is, read the "
                        "instructions in the options or ask in the help server.",
                        preface=self._confpreface
                    )
                self.owner_id = int(self.owner_id)

            elif self.owner_id == 'auto':
                pass # defer to async check

            else:
                self.owner_id = None

        if not self.owner_id:
            raise HelpfulError(
                "No OwnerID was set.",
                "Please set the OwnerID option in {}".format(self.config_file),
                preface=self._confpreface
            )

        if self.bot_exception_ids:
            try:
                self.bot_exception_ids = set(int(x) for x in self.bot_exception_ids.replace(',', ' ').split())
            except:
                log.warning("BotExceptionIDs data is invalid, will ignore all bots")
                self.bot_exception_ids = set()

        if self.bound_channels:
            try:
                self.bound_channels = set(x for x in self.bound_channels.replace(',', ' ').split() if x)
            except:
                log.warning("BindToChannels data is invalid, will not bind to any channels")
                self.bound_channels = set()

        if self.autojoin_channels:
            try:
                self.autojoin_channels = set(x for x in self.autojoin_channels.replace(',', ' ').split() if x)
            except:
                log.warning("AutojoinChannels data is invalid, will not autojoin any channels")
                self.autojoin_channels = set()

        if self.nowplaying_channels:
            try:
                self.nowplaying_channels = set(int(x) for x in self.nowplaying_channels.replace(',', ' ').split() if x)
            except:
                log.warning("NowPlayingChannels data is invalid, will use the default behavior for all servers")
                self.autojoin_channels = set()

        self._spotify = False
        if self.spotify_clientid and self.spotify_clientsecret:
            self._spotify = True

        self.delete_invoking = self.delete_invoking and self.delete_messages

        self.bound_channels = set(int(item) for item in self.bound_channels)

        self.autojoin_channels = set(int(item) for item in self.autojoin_channels)

        ap_path, ap_name = os.path.split(self.auto_playlist_file)
        apn_name, apn_ext = os.path.splitext(ap_name)
        self.auto_playlist_removed_file = os.path.join(ap_path, apn_name + '_removed' + apn_ext)

        if hasattr(logging, self.debug_level.upper()):
            self.debug_level = getattr(logging, self.debug_level.upper())
        else:
            log.warning("Invalid DebugLevel option \"{}\" given, falling back to INFO".format(self.debug_level_str))
            self.debug_level = logging.INFO
            self.debug_level_str = 'INFO'

        self.debug_mode = self.debug_level <= logging.DEBUG

        self.create_empty_file_ifnoexist('config/blacklist.txt')
        self.create_empty_file_ifnoexist('config/whitelist.txt')

    def create_empty_file_ifnoexist(self, path):
        if not os.path.isfile(path):
            open(path, 'a').close()
            log.warning('Creating %s' % path)

    # TODO: Add save function for future editing of options with commands
    #       Maybe add warnings about fields missing from the config file

    async def async_validate(self, bot):
        log.debug("Validating options...")

        if self.owner_id == 'auto':
            if not bot.user.bot:
                raise HelpfulError(
                    "Invalid parameter \"auto\" for OwnerID option.",

                    "Only bot accounts can use the \"auto\" option.  Please "
                    "set the OwnerID in the config.",

                    preface=self._confpreface2
                )

            self.owner_id = bot.cached_app_info.owner.id
            log.debug("Acquired owner id via API")

        if self.owner_id == bot.user.id:
            raise HelpfulError(
                "Your OwnerID is incorrect or you've used the wrong credentials.",

                "The bot's user ID and the id for OwnerID is identical. "
                "This is wrong. The bot needs a bot account to function, "
                "meaning you cannot use your own account to run the bot on. "
                "The OwnerID is the id of the owner, not the bot. "
                "Figure out which one is which and use the correct information.",

                preface=self._confpreface2
            )


    def find_autoplaylist(self):
        if not os.path.exists(self.auto_playlist_file):
            if os.path.exists('config/_autoplaylist.txt'):
                shutil.copy('config/_autoplaylist.txt', self.auto_playlist_file)
                log.debug("Copying _autoplaylist.txt to autoplaylist.txt")
            else:
                log.warning("No autoplaylist file found.")


    def write_default_config(self, location):
        pass


class ConfigDefaults:
    owner_id = None

    token = None
    dev_ids = set()
    bot_exception_ids = set()

    spotify_clientid = None
    spotify_clientsecret = None

    command_prefix = '!'
    bound_channels = set()
    unbound_servers = True
    autojoin_channels = set()
    dm_nowplaying = False
    no_nowplaying_auto = False
    nowplaying_channels = set()
    delete_nowplaying = True

    default_volume = 0.15
    skips_required = 4
    skip_ratio_required = 0.5
    save_videos = True
    now_playing_mentions = False
    auto_summon = True
    auto_playlist = True
    auto_playlist_random = True
    auto_pause = True
    delete_messages = True
    delete_invoking = False
    persistent_queue = False
    debug_level = 'INFO'
    status_message = None
    write_current_song = False
    allow_author_skip = True
    use_experimental_equalization = False
    embeds = True
    queue_length = 10
    remove_ap = True
    show_config_at_start = False
    legacy_skip = False
    leavenonowners = False
    usealias = True

    options_file = 'config/options.ini'
    blacklist_file = 'config/blacklist.txt'
    auto_playlist_file = 'config/autoplaylist.txt'  # this will change when I add playlists
    i18n_file = 'config/i18n/en.json'

setattr(ConfigDefaults, codecs.decode(b'ZW1haWw=', '\x62\x61\x73\x65\x36\x34').decode('ascii'), None)
setattr(ConfigDefaults, codecs.decode(b'cGFzc3dvcmQ=', '\x62\x61\x73\x65\x36\x34').decode('ascii'), None)
setattr(ConfigDefaults, codecs.decode(b'dG9rZW4=', '\x62\x61\x73\x65\x36\x34').decode('ascii'), None)

# These two are going to be wrappers for the id lists, with add/remove/load/save functions
# and id/object conversion so types aren't an issue
class Blacklist:
    pass

class Whitelist:
    pass
