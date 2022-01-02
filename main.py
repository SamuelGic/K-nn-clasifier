# Samuel Gic
# vývojové prostredie PyCharm (Python)
# cviko utorok 16:00

import math
import matplotlib.pyplot as plt
from random import randint
import time


def classify(points, p, k, loop):

    most_col = 5
    distance = []
    for group in points:                # prejdem celé pole a vypočítam vzdialenost pomocou eukloidovho vzorca
        for feature in points[group]:
            # každá vzdialenosť sa priradí do poľa spolu s farbou bodu
            euclidean_distance = math.sqrt((feature[0] - p[0]) ** 2 + (feature[1] - p[1]) ** 2)
            distance.append((euclidean_distance, group))

    # zoradímn a nechám si len prvých k
    distance = sorted(distance)[:k]

    freq0 = 0
    freq1 = 0
    freq2 = 0
    freq3 = 0

    # zistím akú farbu majú najbližích k bodov
    for i in distance:
        if i[1] == 0:
            freq0 += 1

        elif i[1] == 1:
            freq1 += 1

        elif i[1] == 2:
            freq2 += 1

        elif i[1] == 3:
            freq3 += 1

    # zistím najviac početnú farbu a priradím k slovníku pomocou kľúča
    # 0 je červená
    # 1 je zelená
    # 2 je modrá
    # 3 je fialová
    if freq0 > freq1 and freq0 > freq2 and freq0 > freq3:
        most_col = 0
        points[0].append(p)

    if freq1 > freq0 and freq1 > freq2 and freq1 > freq3:
        most_col = 1
        points[1].append(p)

    if freq2 > freq0 and freq2 > freq1 and freq2 > freq3:
        most_col = 2
        points[2].append(p)

    if freq3 > freq0 and freq3 > freq1 and freq3 > freq2:
        most_col = 3
        points[3].append(p)

    # ak sa mi najpočetnejšia farba rovná zvyšku daného cyklu po delení 4, tak vrátim 1 ako úspešné priradenie, inak vrátim 0
    return 1 if loop % 4 == most_col else 0


def get_points(loop):

    p = (10, 10)

    # kedže sa nemôže 2 rovanké poby po sebe generovať, tak si sem posielam počet cyklov, ktorý sa už vykonal
    # vydelím to 4 a zvyšok po delení mi priradí farbu

    if (loop % 4) == 0:
        p = (randint(-5000, 500), randint(-5000, 500))

    if (loop % 4) == 1:
        p = (randint(-500, 5000), randint(-5000, 500))

    if (loop % 4) == 2:
        p = (randint(-5000, 500), randint(-500, 5000))

    if (loop % 4) == 3:
        p = (randint(-500, 5000), randint(-500, 5000))

    # na konci vrátim vygenerované súradnice

    return p


def results(points):
    x = []
    y = []
    col = []
    for i in points:            # rozdelím si daný slovník do troch polí
        for c in points[i]:     # riadok predstavuje farbu
            x.append(c[0])      # x prestavuje x-ovú súradnicu bodu
            y.append(c[1])      # y predstavuje y-psilonovú súradnicu bodu
            if i == 0:
                col.append("red")
            if i == 1:
                col.append("green")
            if i == 2:
                col.append("blue")
            if i == 3:
                col.append("purple")

    plt.scatter(x, y, c=col, s=25)          # vykreslím pomocou importovanej funkcie matplotlib.pyplot
    plt.scatter(0, 0, c="black", s=100)
    plt.show()


def main():

    p = (10, 10)

    # 4 slovníky pre každé k jeden, kedže každému k je potrebné priradiť rovnaké súradnice bodov
    points1 = {0: [(-4500, -4400), (-4100, -3000), (-1800, -2400), (-2500, -3400), (-2000, -1400)],
              1: [(4500, -4400), (4100, -3000), (1800, -2400), (2500, -3400), (2000, -1400)],
              2: [(-4500, 4400), (-4100, 3000), (-1800, 2400), (-2500, 3400), (-2000, 1400)],
              3: [(4500, 4400), (4100, 3000), (1800, 2400), (2500, 3400), (2000, 1400)]}

    points3 = {0: [(-4500, -4400), (-4100, -3000), (-1800, -2400), (-2500, -3400), (-2000, -1400)],
              1: [(4500, -4400), (4100, -3000), (1800, -2400), (2500, -3400), (2000, -1400)],
              2: [(-4500, 4400), (-4100, 3000), (-1800, 2400), (-2500, 3400), (-2000, 1400)],
              3: [(4500, 4400), (4100, 3000), (1800, 2400), (2500, 3400), (2000, 1400)]}

    points7 = {0: [(-4500, -4400), (-4100, -3000), (-1800, -2400), (-2500, -3400), (-2000, -1400)],
              1: [(4500, -4400), (4100, -3000), (1800, -2400), (2500, -3400), (2000, -1400)],
              2: [(-4500, 4400), (-4100, 3000), (-1800, 2400), (-2500, 3400), (-2000, 1400)],
              3: [(4500, 4400), (4100, 3000), (1800, 2400), (2500, 3400), (2000, 1400)]}

    points15 = {0: [(-4500, -4400), (-4100, -3000), (-1800, -2400), (-2500, -3400), (-2000, -1400)],
              1: [(4500, -4400), (4100, -3000), (1800, -2400), (2500, -3400), (2000, -1400)],
              2: [(-4500, 4400), (-4100, 3000), (-1800, 2400), (-2500, 3400), (-2000, 1400)],
              3: [(4500, 4400), (4100, 3000), (1800, 2400), (2500, 3400), (2000, 1400)]}

    loop = 0
    max = 20000
    success1 = 0
    success3 = 0
    success7 = 0
    success15 = 0

    start = time.time()

    # cyklus ktorý prejde 20 000x aby som mohol vygenerovať toľko bodov
    while loop < max:
        # náhodne generované číslo, 99% pravdepodobnosť, že budem generovať pre každý bod zvlášť
        number = randint(0, 100)

        if 0 <= number <= 99:
            p = get_points(loop)    # náhodne si vygenerujem súradnice
            for i in points1:       # prejdem celý slovník, aby som zistil, či už nemám vygenrovane súradnice
                if p in points1[i]:
                    continue
            success1 += classify(points1, p, 1, loop)       # classify pre každé k počet susedov
            success3 += classify(points3, p, 3, loop)       # a pripočítam 1 ak úspešnne priradilo
            success7 += classify(points7, p, 7, loop)
            success15 += classify(points15, p, 15, loop)

        if number == 100:
            p = (randint(-5000, 5000), randint(-5000, 5000))    # v poslednom 1% generujem náhodne bod v celej mape
            garbage = classify(points1, p, 1, loop)
            garbage = classify(points3, p, 3, loop)
            garbage = classify(points7, p, 7, loop)
            garbage = classify(points15, p, 15, loop)

        loop += 1

    end = time.time()

    results(points1)    # vypíšem každý jeden slovník zvlášť
    results(points3)
    results(points7)
    results(points15)

    print("Uspesnost pre k = 1 je:", round(success1 / max * 100, 3), "%")   # vypíšem úspešnosť pre každý jeden slovník a k počet najbližších susedov samostatne
    print("Uspesnost pre k = 3 je:", round(success3 / max * 100, 3), "%")
    print("Uspesnost pre k = 7 je:", round(success7 / max * 100, 3), "%")
    print("Uspesnost pre k = 15 je:", round(success15 / max * 100, 3), "%")
    print("Celkovy cas pocitania programu: ", round(end - start, 3), "sekund")


if __name__ == '__main__':

    main()

