import pickle


class ECalc():
    calcRa = 0.0
    calcRz = 0.0
    tochn = 0
    inRa = 0.0
    inRz = 0.0

    def eCalc(self, material, side, method, napr, alfa, fi, ra, rz, depth, tochn):
        self.tochn = tochn/100
        self.inRa = ra
        self.inRz = rz
        res_di = {}
        if method:
            res_di = self.method_mic(material, side, alfa, fi)
        else:
            res_di = self.method_prof(side, napr, alfa, fi, depth)
        return res_di

    def method_mic(self, material, side, alfa, fi):
        res_diction = {}
        if material == 1:
            if side == 1:
                # self.calcRa = 36.932 * fi ** (-0.694) * alfa ** (0.0722 * fi ** 0.2892)
                res_diction = self.calcRa_prov(36.932, (-0.694), 0.0722, 0.2892, False)
                self.calcRz = 16067534 * fi ** (-2.272) * alfa ** (-(665.44 * fi ** (-1.9191)))
            else:
                # self.calcRa = 5.6643 * fi ** 0.3881 * alfa ** ((-0.2055) * fi ** 0.1415)
                res_diction = self.calcRa_prov(5.6643, 0.3881, (-0.2055), 0.1415, False)
                self.calcRz = 6.1356 * fi ** 0.332 * alfa ** (5.8674 * fi ** (-0.999))
        else:
            if side == 1:
                res_diction = self.calcRa_prov(0.4672, (-0.22), 0.2747, 0.1577, False)
                # self.calcRa = 0.4672 * fi ** (-0.22) * alfa ** (0.2747 * fi ** 0.1577)
            else:
                #self.calcRa = 23521 * fi ** (-0.762) * alfa ** (-3.5559 * fi ** (-0.259))
                res_diction = self.calcRa_prov(23521, (-0.762), (-3.5559), (-0.259), False)
        return res_diction

    def method_prof(self, side, napr, alfa, fi, depth):
        global res_diction
        if napr == 1:
            if side == 1:
                if depth == 40:
                    res_diction = self.calcRa_prov(5.41, 0.201, (-0.1967), 0.1294, False)
                    # self.calcRa = 5.41 * fi ** 0.201 * alfa * (-0, 1967 * fi ** 0.1294)
                elif depth == 50:
                    # self.calcRa = 11.891 * (fi ** 0.0032) * alfa ** (-0.3548 * fi ** (-0.083))
                    res_diction = self.calcRa_prov(11.891, 0.0032, (-0.3548), (-0.083), False)
            else:
                if depth == 40:
                    res_diction = self.calcRa_prov(13.899, 0.0448, (-0.3541), (-0.0271), False)
                    # self.calcRa = 13.899 * fi ** 0.0448 * alfa * (-0.3541 * fi ** (-0.0271))
                elif depth == 50:
                    # self.calcRa = 0.03 * (fi ** 1.6311) * alfa * (-0.0162 * fi ** (-0.7227))
                    res_diction = self.calcRa_prov(0.03, 1.6311, (-0.0162), (-0.7227), False)
        else:
            if side == 1:
                if depth == 20:
                    res_diction = self.calcRa_prov(2.4282, 0.0818, 2.1066, (-0.986), True)
                    # self.calcRa = 2.4282 * alfa ** 0.0818 * fi ** (2.1066 * alfa ** (-0.986))
                elif depth == 40:
                    res_diction = self.calcRa_prov(101.9, (-0.426), (-1.335), (-0.314), False)
                    # self.calcRa = 101.9 * fi ** (-0.426) * alfa ** (-1.335 * fi ** (-0.314))
                elif depth == 50:
                    res_diction = self.calcRa_prov(33.361, (-0.182), (-0.7579), (-0.0225), False)
                    # self.calcRa = 33.361 * fi ** (-0.182) * alfa ** (-0.7579 * fi ** (-0.0225))
            else:
                if depth == 20:
                    res_diction = self.calcRa_prov(17.211, (-0.398), 0.0011, 0.9585, True)
                    # self.calcRa = 17.211 * alfa ** (-0.398) * fi ** (0.0011 * alfa ** 0.9585)
                elif depth == 40:
                    res_diction = self.calcRa_prov(20.663, 0.03, (-0.4524), (-0.032), False)
                    # self.calcRa = 20.663 * fi ** 0.03 * alfa ** (-0.4524 * fi ** (-0.032))
                elif depth == 50:
                    res_diction = self.calcRa_prov(0.0915, 1.4349, (-0.0282), (-0.6278), False)
                    # self.calcRa = 0.0915 * fi ** 1.4349 * alfa ** (-0.0282 * fi ** (-0.6278))
        return res_diction


    def calcRa_prov(self, a, b, c, d, f):
        ra = 0
        di = {}
        i = 0
        for alfa in 90.0, 80.0, 70.0, 60.0, 50.0, 40.0, 30.0:
            for fi in 30.0, 60.0, 90.0, 120.0, 150.0, 180.0, 210.0, 240.0, 270.0, 300.0, 330.0, 360.0:
                if f:
                    ra = a * alfa ** (b) * fi ** (c * alfa ** (d))
                    di[i] = {'ra': ra, 'alfa': alfa, 'fi': fi}
                else:
                    ra = a * fi ** (b) * alfa ** (c * fi ** (d))
                    di[i] = {'ra': ra, 'alfa': alfa, 'fi': fi}
                ra = 0
                i = i + 1
        old_ra = 1000
        indx = 0
        self.save_obj(di, "result")
        for i in range(di.__len__()):
            if (di[i].get('ra') > self.inRa * (1 - self.tochn)) and (di[i].get('ra') < self.inRa * (1 + self.tochn)):
                if (abs(abs(di[i].get('ra')) - self.inRa) < abs(abs(old_ra) - self.inRa)):
                    old_ra = di[i].get('ra')
                    indx = i

        return di[indx]

    def save_obj(self, obj, name):
        with open(name + '.txt', 'w') as f:
            for i in range(obj.__len__()):
                f.write(str(obj[i]) + "\n")
