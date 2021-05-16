# In order to loop over responses and functions
response_events = ['room:create:reply', 'room:join:reply', 'new_user_join_room', 'user_left_room', 'chat:send', 'user:get_info:reply',
                   'room:mute:reply', 'room:deafen:reply', 'chat_user_banned', 'chat_user_unbanned', 'room:unban:reply',
                   'room:get_banned_users:reply', 'hand_raised', 'room:create_scheduled:reply', 'room:get_scheduled:reply',
                   'room:update_scheduled:reply', 'room:delete_scheduled:reply', 'room:get_info:reply', 'room_destroyed']

response_events_functions = ['room_create_reply', 'room_join_reply', 'new_user_join_room', 'user_left_room', 'chat_send', 'user_get_info_reply',
                             'room_mute_reply', 'room_deafen_reply', 'chat_user_banned', 'chat_user_unbanned', 'room_unban_reply',
                             'room_get_banned_users_reply', 'hand_raised', 'room_create_scheduled_reply', 'room_get_scheduled_reply',
                             'room_update_scheduled_reply', 'room_delete_scheduled_reply', 'room_get_info_reply', 'room_destroyed']

response_events_ignore = ['pong', 'you-joined-as-speaker', 'new-tokens', 'room-created', 'mod_changed', 'you-joined-as-peer']

""" List of events to add in the future: 

deafen_changed: d{roomId, userId, value}
mute_changed: d{roomId, userId, value}

"""