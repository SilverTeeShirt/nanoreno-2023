## For AUDIO

init python:
    config.default_afm_time = 10
    ## SOUND CHANNELS
    renpy.music.register_channel("sound2", mixer="sfx", loop=False, stop_on_mute=True, tight=False, file_prefix='', file_suffix='', buffer_queue=True, movie=False)
    renpy.music.register_channel("sound3", mixer="sfx", loop=False, stop_on_mute=True, tight=False, file_prefix='', file_suffix='', buffer_queue=True, movie=False)
    renpy.music.register_channel("music2", mixer="music", loop=True, stop_on_mute=True, tight=False, file_prefix='', file_suffix='', buffer_queue=True, movie=False)
    renpy.music.register_channel("music3", mixer="music", loop=True, stop_on_mute=True, tight=False, file_prefix='', file_suffix='', buffer_queue=True, movie=False)

## SOUND CHANGES
# $renpy.music.set_volume(0.2, delay=0.25, channel='music')

## SOUND LEVELS AT START
define config.default_music_volume = 0.8
define config.default_sfx_volume = 0.8
define config.default_voice_volume = 0.8


## music
define ambience = "audio/music/ambience.ogg" # volume 0.15
define floatingby = "audio/music/floating_by.ogg" # volume 0.22
define spacedout = "audio/music/spaced_out.ogg" # volume 0.4
