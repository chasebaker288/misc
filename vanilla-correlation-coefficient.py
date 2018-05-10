from statistics import mean


def correlation(data_set_1, data_set_2):
    if len(data_set_1) != len(data_set_2):
        return None
    # I'm not sure if my reasoning behind this is all that solid.
    # My thinking is that if the two data sets don't pair off, then there can't be a correlation.
    else:
        uppr, lowx, lowy = [], [], []
        xbar, ybar = mean(data_set_1), mean(data_set_2)
        for i in range(len(data_set_1)):
            data_set_1[i] -= xbar
            data_set_2[i] -= ybar
        for i in range(len(data_set_1)):
            uppr.append(data_set_1[i] * data_set_2[i])
            lowx.append(data_set_1[i]**2)
            lowy.append(data_set_2[i]**2)
        if sum(uppr) == 0:
            return 0.0
        else:
            return sum(uppr) / ((sum(lowx) * sum(lowy))**0.5)
