def calc(t, center):
    return center * t/2

def calculations(center, wave, times):
    distance = []
    speeds = []
    print(type(times))
    if isinstance(times, list):
        for i in range(0, len(times)):
            distance.append(calc(times[i], center))
            if i != 0:
                rt = -times[i-1] / 2 + wave + times[i] / 2
                # print(rt)
                speed = (distance[i-1] - distance[i])/rt
                speeds.append(speed)
        return [distance, speeds]
    else:
        print('error')

if __name__ == '__main__':
    print(calculations(100, 5, [2, 3]))