# 经纬高坐标系（地理坐标系）：LLA = {'longiude(经度)', 'latitude(纬度)', 'altitude(高度)'}
# 站心坐标系：ENU
# 地心地固坐标系：ECEF
import math
import easygui as g

a = float('%.8f' % 6378137.0)


# -------------------------------------------------------------
# LLA坐标系
class LLA():
    # 初始化经纬高三个变量
    def __init__(self, longiude=0.000, latitude=0.000, altitude=0.000):
        self.__init_longiude = float('%.8f' % longiude)
        self.__init_latitude = float('%.8f' % latitude)
        self.__init_altitude = float('%.3f' % altitude)

    # 设置全部
    def set_lla(self, longiude, latitude, altitude, value):
        if value == 1:
            self.__longiude = float('%.8f' % longiude)
            self.__latitude = float('%.8f' % latitude)
            self.__altitude = float('%.3f' % altitude)
        else:
            self.__init_longiude = float('%.8f' % longiude)
            self.__init_latitude = float('%.8f' % latitude)
            self.__inti_altitude = float('%.3f' % altitude)

    def change(self):
        h1 = float(self.__init_altitude + a)
        la1 = float(self.__init_latitude / 180 * math.pi)
        lo1 = float(self.__init_longiude / 180 * math.pi)
        h2 = float(self.__altitude + a)
        la2 = float(self.__latitude / 180 * math.pi)
        lo2 = float(self.__longiude / 180 * math.pi)
        x1 = float(h1 * math.cos(la1) * math.cos(lo1))
        y1 = float(h1 * math.cos(la1) * math.sin(lo1))
        z1 = float(h1 * math.sin(la1))
        x2 = float(h2 * math.cos(la2) * math.cos(lo2))
        y2 = float(h2 * math.cos(la2) * math.sin(lo2))
        z2 = float(h2 * math.sin(la2))
        Dis = float((((x1 - x2) ** 2) + ((y1 - y2) ** 2) + ((z1 - z2) ** 2)) ** 0.5)
        change_longiude = self.__longiude - self.__init_longiude
        change_latitude = self.__latitude - self.__init_latitude
        change_altitude = self.__altitude - self.__init_altitude
        change_data = {'Dis' : Dis, 'EW' : abs(x2 - x1), 'NS' : abs(y2 - y1), 'UD' : abs(z2 - z1), 'change_longiude': change_longiude, 'change_latitude': change_latitude, 'change_altitude': change_altitude}
        return change_data

    # LLA转换成ENU
    def LLA2ENU(self):
        h1 = float(self.__init_altitude + a)
        la1 = float(self.__init_latitude / 180 * math.pi)
        lo1 = float(self.__init_longiude / 180 * math.pi)
        h2 = float(self.__altitude + a)
        la2 = float(self.__latitude / 180 * math.pi)
        lo2 = float(self.__longiude / 180 * math.pi)
        x1 = float(h1 * math.cos(la1) * math.cos(lo1))
        y1 = float(h1 * math.cos(la1) * math.sin(lo1))
        z1 = float(h1 * math.sin(la1))
        x2 = float(h2 * math.cos(la2) * math.cos(lo2))
        y2 = float(h2 * math.cos(la2) * math.sin(lo2))
        z2 = float(h2 * math.sin(la2))
        Dis = float((((x1 - x2) ** 2) + ((y1 - y2) ** 2) + ((z1 - z2) ** 2)) ** 0.5)
        change_longiude = self.__longiude - self.__init_longiude
        change_latitude = self.__latitude - self.__init_latitude
        change_altitude = self.__altitude - self.__init_altitude
        e = float(a * math.cos(self.__latitude / 180 * math.pi) * (self.__longiude - self.__init_longiude))
        n = float(a * (self.__latitude - self.__init_latitude))
        u = float(self.__altitude - self.__init_altitude)
        data_enu = {'Dis': float('%.3f' % Dis), 'EW': float('%.3f' % abs(x2 - x1)), 'NS': float('%.3f' % abs(y2 - y1)), 'UD': float('%.3f' % abs(z2 - z1)),
                       'change_longiude': float('%.8f' % change_longiude), 'change_latitude': float('%.8f' % change_latitude),
                       'change_altitude': float('%.3f' % change_altitude), 'E': float('%.3f' % e), 'N': float('%.3f' % n), 'U': float('%.3f' % u)}
        return data_enu


# -------------------------------------------------------------
class ENU():
    # 经纬高坐标设置为ENU坐标原点
    def __init__(self, east=0, north=0, up=0):
        self.__init_east = float(east)
        self.__init_north = float(north)
        self.__init_up = float(up)

    # 设置全部
    def set_enu(self, east, north, up, value):
        if value == 1:
            self.__east = float(east)
            self.__north = float(north)
            self.__up = float(up)
        else:
            self.__init_east = float(east)
            self.__init_north = float(north)
            self.__init_up = float(up)
    def change(self):
        change_east = self.__east - self.__init_east
        change_north = self.__north - self.__init_north
        change_up = self.__up - self.__init_up
        change_data = {'change_east' : float('%.3f' % change_east), 'change_north' : float('%.3f' % change_north), 'change_up' : float('%.3f' % change_up)}
        return change_data

    def ENU2LLA(self, init_longiude, init_latitude, init_altitude):
        altitude = float('%.3f' % (init_altitude + self.__up))
        latitude = float('%.3f' % ((self.__north + init_latitude) / a))
        longiude = float('%.3f' % ((self.__east + init_longiude) / (a * math.cos(latitude / 180 * math.pi))))
        data_lla = {'经度': longiude, '纬度': latitude, '高度': altitude}
        return data_lla


# -------------------------------------------------------------
while 1:
    inputmsg_init = g.multenterbox('初始化起点经纬高度', '请输入', ['经度', '纬度', '高度'])
    # 初始化的经纬高度
    init_longiude = float(inputmsg_init[0])
    init_latitude = float(inputmsg_init[1])
    init_altitude = float(inputmsg_init[2])
    lla = LLA(init_longiude, init_latitude, init_altitude)
    #初始化的ENU
    inputmsg_init = g.multenterbox('初始化起点ENU', '请输入', ['E', 'N', 'U'])
    init_e = float(inputmsg_init[0])
    init_n = float(inputmsg_init[1])
    init_u = float(inputmsg_init[2])
    # 建立对象
    enu = ENU(init_e, init_n, init_u)
    while 1:
        choice = g.buttonbox('请选择您要执行的操作：', choices=('LLA --> ENU', 'ENU --> LLA', '重新输入初始经纬高度', '退出'))
        if choice == 'LLA --> ENU':
            inputmsg = g.multenterbox('当前经纬高度', '请输入', ['经度', '纬度', '高度'])
            longiude = float(inputmsg[0])
            latitude = float(inputmsg[1])
            altitude = float(inputmsg[2])
            lla.set_lla(longiude, latitude, altitude, 1)  # 设置当前经纬高度
            l2e = lla.LLA2ENU()
            l2e_1 = '变化：\n' + \
                    '  直线距离：' + str(l2e['Dis']) + \
                    '\n  东西距离：' + str(l2e['EW']) + \
                    '\n  南北距离：' + str(l2e['NS']) + \
                    '\n  上下距离：' + str(l2e['UD']) + \
                    '\n当前ENU：\n' + \
                    '  E: ' + str(l2e['E']) + '\n  N: ' + str(l2e['N']) + '\n  U: ' + str(l2e['U'])
            g.msgbox(l2e_1, 'ENU结果为')
        elif choice == 'ENU --> LLA':
            inputmsg = g.multenterbox('当前ENU坐标', '请输入', ['E', 'N', 'U'])
            e = float(inputmsg[0])
            n = float(inputmsg[1])
            u = float(inputmsg[2])
            enu.set_enu(e, n, u, 1) #设置当前ENU坐标
            enu_change = enu.change()
            e2l = enu.ENU2LLA(init_longiude, init_latitude, init_altitude)
            e2l_1 = '变化：\n' +\
                    '  E: ' + str(enu_change['change_east']) + \
                    '\n  N:' + str(enu_change['change_north']) + \
                    '\n  U:' + str(enu_change['change_up']) + '\n' + \
                    '当前：\n' + \
                    '  经度：' + str(e2l['经度']) + \
                    '\n  纬度：' + str(e2l['纬度']) + \
                    '\n  高度：' + str(e2l['高度'])
            g.msgbox(e2l_1, '结果为')
        elif choice == '根据经纬高度计算距离':
            g.msgbox('根据经纬高度计算距离')
        elif choice == '重新输入初始经纬高度':
            break
        else:
            exit(0)
