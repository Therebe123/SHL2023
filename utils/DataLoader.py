import pandas as pd
import numpy as np
import re
import time
from utils.TimeKeeper import TimeKeeper


class SHLDataLoader():
    def __init__(self, root_path, ratio = None):
        self.load_ratio = ratio
        self.root_path = root_path

    def gps_detail_transformer(self, gps_list, this_time):
        """
        Description: Extract detail info of GPS data
        return: pd.DataFrame
            - time, id, snr, azimuth, elevation
        """
        res = np.array(gps_list).reshape(-1, 4)
        res = pd.DataFrame(res, columns = ('id', 'snr', 'azimuth', 'elevation'))
        res.insert(loc = 0, column = 'time', value = [this_time] * res.shape[0])
        return res

    def load_acc(self):
        print("Acc Loading...")
        timer = TimeKeeper()
        acc_names = ['time', 'Acc_x', 'Acc_y', 'Acc_z']
        self.acc = pd.read_table(self.root_path + 'Acc.txt', header = None, names = acc_names, sep = "\t")
        self.acc = self.acc.iloc[:int(self.load_ratio * self.acc.shape[0]),:] if self.load_ratio else self.acc
        print("Acc 读取完成，共 {} 条数据，占总数据的{}，用时 {}s".format(self.acc.shape[0], self.load_ratio, timer.get_update_time()))

    def load_gyr(self):
        print("Gyr Loading...")
        timer = TimeKeeper()
        gyr_names = ['time', 'Gyr_x', 'Gyr_y', 'Gyr_z']
        self.gyr = pd.read_table(self.root_path + 'Gyr.txt', header = None, names = gyr_names, sep = "\t")
        self.gyr = self.gyr.iloc[:int(self.load_ratio * self.gyr.shape[0]),:] if self.load_ratio else self.gyr
        print("Gyr 读取完成，共 {} 条数据，占总数据的{}，用时 {}s".format(self.gyr.shape[0], self.load_ratio, timer.get_update_time()))

    def load_mag(self):
        print("Mag Loading...")
        timer = TimeKeeper()
        mag_names = ['time', 'Mag_x', 'Mag_y', 'Mag_z']
        self.mag = pd.read_table(self.root_path + 'Mag.txt', header = None, names = mag_names, sep = "\t")
        self.mag = self.mag.iloc[:int(self.load_ratio * self.mag.shape[0]),:] if self.load_ratio else self.mag
        print("Mag 读取完成，共 {} 条数据，占总数据的{}，用时 {}s".format(self.mag.shape[0], self.load_ratio, timer.get_update_time()))

    def load_label(self):
        print("Label Loading...")
        timer = TimeKeeper()
        label_names = ['time', 'label']
        self.label = pd.read_table(self.root_path + 'Label.txt', header = None, names = label_names, sep = "\t")
        self.label = self.label.iloc[:int(self.load_ratio * self.label.shape[0]),:] if self.load_ratio else self.label
        print("Label 读取完成，共 {} 条数据，占总数据的{}，用时 {}s".format(self.label.shape[0], self.load_ratio, timer.get_update_time()))

    def load_loc(self):
        print("Location Loading...")
        timer = TimeKeeper()
        loc_names = ['time', 'ign1', 'ign2', 'accuracy', 'latitude', 'longitude', 'altitude']
        self.loc = pd.read_table(self.root_path + 'Location.txt', header = None, names = loc_names, sep = " ").drop(['ign1', 'ign2'], axis = 1)
        self.loc = self.loc.iloc[:int(self.load_ratio * self.loc.shape[0]),:] if self.load_ratio else self.loc
        print("Location 读取完成，共 {} 条数据，占总数据的{}，用时 {}s".format(self.loc.shape[0], self.load_ratio, timer.get_update_time()))

    def load_gps(self, detail = True):
        print("GPS Loading...")
        timer = TimeKeeper()
        gps = pd.read_table(self.root_path + 'GPS.txt', header = None)
        gps['time'] = gps.apply(lambda x: x[0].split(" ")[0], axis = 1)
        gps['number'] = gps.apply(lambda x: x[0].split(" ")[-1], axis = 1)
        self.gps = gps.iloc[:int(self.load_ratio * gps.shape[0]),:] if self.load_ratio else gps
        print("GPS 读取完成，共 {} 条数据，占总数据的{}，用时 {}s".format(gps.shape[0], self.load_ratio, timer.get_update_time()))
        if detail:
            print("GPS Detail Loading...")
            gps_detail = self.gps.apply(lambda x: self.gps_detail_transformer(x[0].split(" ")[3:-1], x[0].split(" ")[0]), axis = 1)
            self.gps_detail = pd.concat(gps_detail.to_list()).reset_index(drop = True)
            print("\t-- GPS 详细信息提取完成，共 {} 条数据，占总数据的{}，用时 {}s".format(gps_detail.shape[0], self.load_ratio, timer.get_update_time()))
        self.gps = self.gps.drop([0], axis = 1)
    
    def load_all(self, detail = True, have_label = True):

        self.load_loc()
        self.load_acc()
        self.load_gyr()
        self.load_mag()
        self.load_gps(detail)
        if have_label:
            self.load_label()
        else:
            print("No Labels available.")
