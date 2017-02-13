from gym.envs.registration import register
from .music_env import *
from .music_theory_env import *
from .music_clone_env import *
from .music_gen_env import *
from .music_tuner_env import MusicTunerEnv
from .music_clone_tuner_env import MusicCloneTunerEnv
from .util import *

register(
    id='music-v0',
    entry_point='music:MusicEnv'
)

register(
    id='music-theory-v0',
    entry_point='music:MusicTheoryEnv'
)

register(
    id='music-clone-v0',
    entry_point='music:MusicCloneEnv'
)


register(
    id='music-tuner-v0',
    entry_point='music:MusicTunerEnv'
)

register(
    id='music-gen-v0',
    entry_point='music:MusicGenEnv'
)