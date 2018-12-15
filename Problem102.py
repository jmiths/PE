#!/usr/bin/python3

import math
'''
First attempt, cannot debug
def origin_in(x,y,z):
        dxy = math.sqrt( (x[0]-y[0])**2 + (x[1]-y[1])**2)
        dxz = math.sqrt( (x[0]-z[0])**2 + (x[1]-z[1])**2)
        dyz = math.sqrt( (y[0]-z[0])**2 + (y[1]-z[1])**2)

        dox = math.sqrt( (x[0])**2 + (x[1])**2)
        doy = math.sqrt( (y[0])**2 + (y[1])**2)
        doz = math.sqrt( (z[0])**2 + (z[1])**2)

        s_oxy = (dox+doy+dxy)/2
        s_oxz = (dox+doz+dxz)/2
        s_oyz = (doy+doz+dyz)/2

        area_oxy = math.sqrt(s_oxy*(s_oxy-dox)*(s_oxy-doy)*(s_oxy-dxy))
        area_oxz = math.sqrt(s_oxz*(s_oxz-dox)*(s_oxz-doz)*(s_oxz-dxz))
        area_oyz = math.sqrt(s_oyz*(s_oyz-doy)*(s_oyz-doz)*(s_oyz-dyz))

        smalls_area = area_oxy+area_oxz+area_oyz

        s_xyz = (dxy+dxz+dyz)/2
        area_xyz = math.sqrt(s_xyz*(s_xyz-dxy)*(s_xyz-dxz)*(s_xyz-dyz))

        if smalls_area > area_xyz:
                return False
        else:
                return True
'''
#Found a quicker way without distance formula https://en.wikipedia.org/wiki/Triangle#Using_coordinates
def origin_in(a,b,c):
        area_abc = .5*abs( ( (a[0]-c[0])*(b[1]-a[1]) ) - (a[0]-b[0])*(c[1]-a[1]))
        area_bc = .5*abs(b[0]*c[1]-c[0]*b[1])
        area_ab = .5*abs(a[0]*b[1]-b[0]*a[1])
        area_ac = .5*abs(a[0]*c[1]-c[0]*a[1])

        if area_bc+area_ab+area_ac > area_abc:
                return False
        else:
                return True
with open("p102_triangles.txt","r") as f:
        ctr = 0
        for line in f:
                line = line.strip().split(",")
                line = list(map(int, line))
                a = line[:2]
                b = line[2:4]
                c = line[4:]
                if origin_in(a,b,c):
                        ctr += 1
        print(ctr)
