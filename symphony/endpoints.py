import config
import symphony.utility as util


def session_auth_cert():
    return config.auth_base_url + '/sessionauth/v1/authenticate'


def km_auth_cert():
    return config.auth_base_url + '/keyauth/v1/authenticate'


def session_auth_jwt():
    return config.auth_base_url + '/login/pubkey/authenticate'


def km_auth_jwt():
    return config.auth_base_url + '/relay/pubkey/authenticate'


def session_auth_obo_app():
    return config.obo_base_url + '/sessionauth/v1/app/authenticate'


def session_auth_obo_user(user_id: str):
    return config.obo_base_url + '/sessionauth/v1/app/user/' + user_id + '/authenticate'


def echo():
    return config.api_base_url + '/agent/v1/util/echo'


def create_im(exclude_bot: bool = False):
    im_ep = config.api_base_url + '/pod/v1/'
    im_ep += 'admin/' if exclude_bot else ''
    im_ep += 'im/create'

    return im_ep


def send_message(stream_id: str, version: int=2):
    s_id = util.format_symphony_stream_id(stream_id)
    return config.api_base_url + '/agent/v' + str(version) + '/stream/' + s_id + '/message/create'


def lookup_user_list(user_emails: list, local_users_only: bool):
    qs = ','.join(user_emails)
    return config.api_base_url + '/pod/v3/users?local=' + str(local_users_only).lower() + '&email=' + qs


def lookup_user(user_email: str, local_users_only: bool):
    return config.api_base_url + '/pod/v3/users?local=' + str(local_users_only).lower() + '&email=' + user_email


def search_user(local_users_only: bool):
    return config.api_base_url + '/pod/v1/user/search?local=' + str(local_users_only).lower()


def find_user():
    return config.api_base_url + '/pod/v1/admin/user/find'


def add_user_to_stream(stream_id: str):
    s_id = util.format_symphony_stream_id(stream_id)
    return config.api_base_url + '/pod/v1/room/' + s_id + '/membership/add'


def promote_user_to_owner(stream_id: str):
    s_id = util.format_symphony_stream_id(stream_id)
    return config.api_base_url + '/pod/v1/room/' + s_id + '/membership/promoteOwner'


def search_room(result_limit: int=0):
    suffix = '/pod/v3/room/search'

    if result_limit > 0:
        suffix += '?limit=' + str(result_limit)

    return config.api_base_url + suffix


def create_room():
    return config.api_base_url + '/pod/v2/room/create'


def list_user_streams(limit: int = 50, skip: int = 0):
    return config.api_base_url + '/pod/v1/streams/list?limit=' + str(limit) + '&skip=' + str(skip)


def set_presence():
    return config.api_base_url + '/pod/v2/user/presence'
