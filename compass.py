from enum import Enum


class Compass(Enum):
    N = [-360, 0]
    NW = [-315, 45]
    W = [-270, 90]
    SW = [-225, 135]
    S = [-180, 180]
    SE = [-135, 225]
    E = [-90, 270]
    NE = [-45, 315]


def direction(side, angle):
    if angle % 45 != 0 or side not in Compass.__members__:
        raise ValueError('Incorrect input data: check side or angle value.')

    if -360 < angle < 360:
        raw_position = eval(f'Compass.{side}.value[0] - {angle}')
        position = raw_position if abs(raw_position) <= 360 else raw_position + 360

        for key, value in Compass.__members__.items():
            if position == value.value[0]:
                return key

    else:
        new_angle = angle - 360 * (angle // 360)
        side = direction(side, new_angle)
        return side


if __name__ == '__main__':
    assert direction('W', 135) == 'NE'
    assert direction('S', 180) == 'N'
    assert direction('SE', -45) == 'E'
    assert direction('W', 495) == 'NE'
