def calcAngle(h,m):
    h = 0 if h == 12 else h
    m = 0 if m == 60 else m
    hourAngle = (h*60 + m)*0.5
    minuteAngle = m * 6
    angle = abs(hourAngle - minuteAngle)
    return angle if angle < (360-angle) else 360-angle
    
for _ in range(int(input())):
    h,m = map(float,input().split())
    print(int(calcAngle(h,m)))