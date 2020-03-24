#经纬高坐标系（地理坐标系）：LLA = {'longiude(经度)', 'latitude(纬度)', 'altitude(高度)'}
#站心坐标系：ENU
#地心地固坐标系：ECEF
import math
import easygui as g

a = float(6378137.0)

#-------------------------------------------------------------
#LLA坐标系
class LLA():
    #初始化经纬高三个变量
    def __init__(self, longiude = 0.000, latitude = 0.000, altitude = 0.000):
        self.__init_longiude = float(longiude)
        self.__init_latitude = float(latitude)
        self.__init_altitude = float(altitude)

    #设置全部
    def set_lla(self, longiude, latitude, altitude, value):
        if value == 1:
            self.__longiude = float(longiude)
            self.__latitude = float(latitude)
            self.__altitude = float(altitude)
        else:
            self.__init_longiude = float(longiude)
            self.__init_latitude = float(latitude)
            self.__inti_altitude = float(altitude)

    #LLA转换成ENU
    def LLA2ENU(self):
        e = float(a * math.cos(self.__latitude / 180 * math.pi) * (self.__longiude - self.__init_longiude))
        n = float(a * (self.__latitude - self.__init_latitude))
        u = float(self.__altitude - self.__init_altitude)
        data_enu = {'E' : e, 'N' : n, 'U' : u}
        return data_enu

#-------------------------------------------------------------
class ENU():
    #经纬高坐标设置为ENU坐标原点
    def __init__(self, east = 0, north = 0, up = 0):
        self.__east = float(east)
        self.__north = float(north)
        self.__up = float(up)

    def ENU2LLA(self, init_longiude, init_latitude, init_altitude):
        altitude = init_altitude + self.__up
        latitude = (self.__north + init_latitude) / a
        longiude = (self.__east + init_longiude) / (a * math.cos(latitude / 180 * math.pi))
        data_lla = {'经度' : longiude, '纬度' : latitude, '高度' : altitude}
        return data_lla

#-------------------------------------------------------------
class Exchange():
    while 1:
        inputmsg_init = g.multenterbox('初始化起点经纬高度', '请输入', ['经度', '纬度', '高度'])
        #初始化的经纬高度
        init_longiude = float(inputmsg_init[0])
        init_latitude = float(inputmsg_init[1])
        init_altitude = float(inputmsg_init[2])
        #简历对象
        lla = LLA(init_longiude, init_latitude, init_altitude)
        while 1:
            choice = g.buttonbox('请选择您要执行的操作：', choices = ('LLA --> ENU', 'ENU --> LLA', '重新输入初始经纬高度', '退出'))
            if choice == 'LLA --> ENU':
                inputmsg = g.multenterbox('当前经纬高度', '请输入', ['经度', '纬度', '高度'])
                longiude = inputmsg[0]
                latitude = inputmsg[1]
                altitude = inputmsg[2]
                lla.set_lla(longiude, latitude, altitude, 1)    #设置当前经纬高度
                l2e = lla.LLA2ENU()
                l2e_1 = str(l2e['E']) + '\n' + str(l2e['N']) + '\n' + str(l2e['U'])
                g.msgbox(l2e_1, 'ENU结果为')
            elif choice == 'ENU --> LLA':
                inputmsg = g.multenterbox('当前ENU坐标', '请输入', ['E', 'N', 'U'])
                e = float(inputmsg[0])
                n = float(inputmsg[1])
                u = float(inputmsg[2])
                enu = ENU(e, n, u)
                e2l = enu.ENU2LLA(init_longiude, init_latitude, init_altitude)
                e2l_1 = str(e2l['经度']) + '\n' + str(e2l['纬度']) + '\n' + str(e2l['高度'])
                g.msgbox(e2l_1, 'LLA结果为')
            elif choice == '重新输入初始经纬高度':
                break
            else:
                exit(0)
