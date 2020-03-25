import pymap3d as pm
import easygui as eg

#-------------------------------------------------------------------------------------------------------------------------------------------------
#获取ENU数据
def get_enu_data(value):
    if value == 0:
        inp_msg = eg.multenterbox('请输入以下的数值', '', ['初始E', '初始N', '初始U'])
    else:
        inp_msg = eg.multenterbox('请输入以下的数值', '', ['当前E', '当前N', '当前U'])
    E = float(inp_msg[0])
    N = float(inp_msg[1])
    U = float(inp_msg[2])
    enu_data = [E, N, U]
    return enu_data

#获取geodetic数据
def get_geo_data(value):
    if value == 0:
        inp_msg = eg.multenterbox('请输入以下的数值', '', ['初始经度', '初始纬度', '初始高度'])
    else:
        inp_msg = eg.multenterbox('请输入以下的数值', '', ['当前经度', '当前纬度', '当前高度'])
    longitude = float(inp_msg[0])
    latitude = float(inp_msg[1])
    altitude = float(inp_msg[2])
    geo_data = [longitude, latitude, altitude]
    return geo_data

#同时获取ENU和LLA的值-->enu2lla
def get_enu2lla_data():
    inp_msg = eg.multenterbox('请输入以下的数值', '', ['当前E', '当前N', '当前U', '初始经度', '初始纬度', '初始高度'])
    E = float(inp_msg[0])
    N = float(inp_msg[1])
    U = float(inp_msg[2])
    init_longitude = float(inp_msg[3])
    init_latitude = float(inp_msg[4])
    init_altitude = float(inp_msg[5])
    E2G_data = pm.enu2geodetic(E, N, U, init_latitude, init_longitude, init_altitude)
    return E2G_data

#同时获取初始LLA和当前LLA的值
def get_lla2enu_data():
    inp_msg = eg.multenterbox('请输入以下的数值', '', ['初始经度', '初始纬度', '初始高度', '当前经度', '当前纬度', '当前高度'])
    init_longitude = float(inp_msg[0])
    init_latitude = float(inp_msg[1])
    init_altitude = float(inp_msg[2])
    current_longitude = float(inp_msg[3])
    current_latitude = float(inp_msg[4])
    current_altitude = float(inp_msg[5])
    G2E_data = pm.geodetic2enu(current_latitude, current_longitude, current_altitude, init_latitude, init_longitude, init_altitude)
    return G2E_data

#-------------------------------------------------------------------------------------------------------------------------------------------------
def E2G_function():
    E2G_data = get_enu2lla_data()
    current_geo = 'longitude: ' + str(float('%.8f' % E2G_data[1])) + '\nlatitude: ' + str(float('%.8f' % E2G_data[0])) + '\naltitude: ' + str(float('%.3f' % E2G_data[2]))
    eg.msgbox(current_geo, '当前的经纬高坐标为')

def G2E_function():
    G2E_data  =get_lla2enu_data()
    current_enu = 'E: ' + str(float('%.3f' % G2E_data[0])) + '\nN: ' + str(float('%.3f' % G2E_data[1])) + '\nU: ' + str(float('%.3f' % G2E_data[2]))
    eg.msgbox(current_enu, '当前的ENU坐标为')

def EEGG_function():
    init_geo = get_geo_data(0)
    fir_enu = get_enu_data(0)
    sec_enu = get_enu_data(1)
    sec_geo = pm.enu2geodetic(fir_enu[0], fir_enu[1], fir_enu[2], init_geo[1], init_geo[0], init_geo[2])
    thi_geo = pm.enu2geodetic(sec_enu[0], sec_enu[0], sec_enu[0], sec_geo[1], sec_geo[0], sec_geo[2])
    msg = '当前经度：' + str(float('%.8f' % thi_geo[1])) + '\n当前纬度：' + str(float('%.8f' % thi_geo[0])) + '\n当前高度：' + str(float('%.8f' % thi_geo[2]))
    eg.msgbox(msg, '结果')

def GGGD_function():
    G2E_data = get_lla2enu_data()
    ch_e = float('%.3f' % G2E_data[0])
    ch_n = float('%.3f' % G2E_data[1])
    ch_u = float('%.3f' % G2E_data[2])
    ch_L = float('%.3f' % ((ch_e ** 2) + (ch_n ** 2) + (ch_u ** 2)) ** 0.5)
    msg = '直线距离：' + str(ch_L) + '\n东西距离：' + str(ch_e) + '\n南北距离：' + str(ch_n) + '\n上下距离：' + str(ch_u)
    eg.msgbox(msg, '结果')
    
#-------------------------------------------------------------------------------------------------------------------------------------------------

while 1:
    fun_msg_cho = eg.buttonbox('请选择你要执行的操作', choices = ('ENU -> Geodetic', 'Geodetic -> ENU', '根据两个ENU计算\n新位置的经纬高度', '根据两个经纬高度\n计算相关的距离', '退出'))
    if fun_msg_cho == 'ENU -> Geodetic':
        E2G_function()
    elif fun_msg_cho == 'Geodetic -> ENU':
        G2E_function()
    elif fun_msg_cho == '根据两个ENU计算\n新位置的经纬高度':
        EEGG_function()
    elif fun_msg_cho == '根据两个经纬高度\n计算相关的距离':
        GGGD_function()
    else:
        break

#-------------------------------------------------------------------------------------------------------------------------------------------------
