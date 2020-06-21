from math import hypot

def NoOfCollision(car, distance):
    collision_time=[]
    count = 0
    for i in range(len(car)):
        collision_time.append(distance[i]/car[i][2])
    k=len(collision_time)
    if k != len(set(collision_time)):
        count = 1
        for i in range(0,k):
            if i==k-1:
                break
            if collision_time[i]==collision_time[i+1]:
                count += 1
    print(count)
    

def DBCO(car):
    a=[]
    for i in car:
        a.append(hypot(i[0],i[1]))
    return a

no_of_car=int(input())
car = []
for _ in range(no_of_car):
    car.append(list(map(int, input().rstrip().split())))
hypo_distance = DBCO(car)                                           #DBCO = distance between car present position and origin(collision point)
q = NoOfCollision(car, hypo_distance)