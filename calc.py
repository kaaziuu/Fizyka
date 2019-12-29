# def how_far(t, osr):
#     x = osr * t/2
#     return x


def detector_speed(osr, f, f1):
    vo = (osr*f1)/f - osr
    return vo


def how_far(t, center):
    return center * t/2


def calculations(center, wave, times):
    distance = []
    speeds = []
    # print(type(times))
    if isinstance(times, list):
        for i in range(0, len(times)):
            distance.append(how_far(times[i], center))
            if i != 0:
                rt = -times[i-1] / 2 + wave + times[i] / 2
                # print(rt)
                speed = (distance[i-1] - distance[i])/rt
                speeds.append(speed)
        return [distance, speeds]
    else:
        print('error')


def Hz (observer_speed, center, lenght_wave, time):
    return ((center*time)/lenght_wave + (observer_speed*time)/lenght_wave)/time


if __name__ == '__main__':
    print(calculations(100, 5, [2, 3]))