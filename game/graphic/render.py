# from game.sound.echo import echo_test
from ..sound.echo import echo_test # ..은 render.py의 부모 디렉터리를 의미

def render_test():
    print('render')
    echo_test()