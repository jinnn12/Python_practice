# 특정 디렉터리의 모듈을 *로 import 할 때는 해당 디렉터리의 __init__.py 파일에 "__all_ 변수"를 설정하고
# import 해야 할 모듈을 정의해야 한다.

# __all__은 sound 디렉터리에서 *를 사용하여 import 할 경우, 이곳에 정의된 echo 모듈만 import 된다는 의미이다.
__all__ = ['echo']