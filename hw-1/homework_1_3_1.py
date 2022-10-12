import math

import unittest


''' Как работает код
0) обьявления переменных                                        24-26 строки
1) получаем весь ввод                                           20-23, 27-34 строки
2) находим человека, которому нужна самая сложная задача        35-68 строки

(приоритет определения такого человека: 2 и 3 пункты из задания, если совпадения, то 1 пункт, если совпадения, то 5 пункт)
(по 4 пункту даются самые простые задачи, в таких случаях 1 и 5 пункт не учитываются, потому что)

3) выделяем сложнейшую задачу этому человеку                    69 строка
4) цикл из 2)-3), убрав сложнейшую задачу и этого человека      70 строка
5) вывод                                                        71-74 строка
6) тесты                                                        78-99 строки
'''
def code(*args):
    if(args):
        n = args[0]
    else:
        n = int(input()) 
    n_max = n   #самая сложная задача
    array = []  #полный список всех людей
    out = [-1] * n  #вывод объявленный из n минус единиц
    if(args):
        for i in range(1, n+1):  #принимаем ввод
            inp = args[i]
            array.append(inp[:2] + list(map(int, inp[2:]))) #2 строки + 3 числа
    else:
        for i in range(n):  #принимаем ввод
            inp = input().split(" ")
            array.append(inp[:2] + list(map(int, inp[2:]))) #2 строки + 3 числа  
    while(n_max > 0):   #задачи остались?
        line = ["none", "none", -1, -1, -1, -1] #информация о самом умном человеке, сбрасывается после каждого распределения задачи,
        #последняя -1 это номер человека по порядку(i)
        for i in range(n):  #ищем самого умного человека
            if (array[i][2] != array[i][3] and out[i] == -1): #если задачи разные и человек без задачи
                if (line[2] >= line[3]):    #если он умный (2 пункт из условия)
                    if ((line[2] + line[3] < array[i][2] + array[i][3]) or 
                            math.ceil((line[2] + line[3])/2) < array[i][2]):  #если этот чел умнее
                        line[0:5] = array[i]    #заменяем
                        line[5] = i     #номер по порядку
                    elif ((line[2] + line[3] == array[i][2] + array[i][3]) or   #если равноумны
                            math.ceil((line[2] + line[3])/2) == array[i][2]):
                        if (line[4] > array[i][4]):     #по оценке
                            line[0:5] = array[i]
                            line[5] = i
                        elif (line[4] == array[i][4] and line[0][0]+line[0][1] < array[i][0][0]+array[i][0][1]):    #по ФИО
                            line[0:5] = array[i]
                            line[5] = i
                else:   #если не умный(3 пункт из условия)
                    if ((math.ceil((line[2] + line[3])/2) < math.ceil((array[i][2] + array[i][3])/2)) or 
                            (math.ceil((line[2] + line[3])/2) < array[i][2])):   #если этот чел умнее
                        line[0:5] = array[i]
                        line[5] = i
                    elif ((math.ceil((line[2] + line[3])/2) == math.ceil((array[i][2] + array[i][3])/2)) or  #если равноумны
                            (math.ceil((line[2] + line[3])/2) == array[i][2])):
                        if (line[4] > array[i][4]):     #по оценке
                            line[0:5] = array[i]
                            line[5] = i
                        elif (line[4] == array[i][4] and line[0][0]+line[0][1] < array[i][0][0]+array[i][0][1]):  #по ФИО
                            line[0:5] = array[i]
                            line[5] = i
            elif (array[i][2] == array[i][3] and line == ["none", "none", -1, -1, -1, -1] and out[i] == -1):#если он любит и не любит одну
                line[5] = i #сохраняем только индекс, чтобы можно было легко перебить другим человеком дальше по списку
                #не проверяются условия по фио и по оценке потому что
        out[line[5]] = n_max    #даем человеку задачу
        n_max -= 1              #убираем задачу
    if(args):
        return(' '.join(map(str, out)))  #вывод
    else:
        print(' '.join(map(str, out)))

class TestSum(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(code(3, ["Михайлов", "Михаил", 1, 3, 10], ["Никайло", "Николай", 2, 1, 1],
                ["Гендо", "Геннадий", 3, 3, 5]), "2 3 1")

    def test_like(self):
        self.assertEqual(code(2, ["a", "a", 1, 3, 10], ["a", "a", 1, 3, 1]), "1 2")

    def test_FIO(self):
        self.assertEqual(code(2, ["Abcd", "abcz", 2, 1, 10], ["Abcd", "abcd", 2, 1, 10]), "2 1")

    def test_1(self):
        self.assertEqual(code(3, [1, 1, 1, 1, 1], [1, 1, 1, 1, 1,], [1, 1, 1, 1, 1]), "3 2 1")

    def test_your(self):
        print("Тесты успешны! Введите ручные тесты")
        self.assertEqual(code(), None)


if __name__ == '__main__':
    unittest.main()

#исключения я не делал, потому что верю в бога
'''
`/:::::::::--------------------------------------------..................................................`.`...........`
`hh+++++++++/++++++/++//++//++/++//++//+//++//++//+//++/+osooyooo+/++//++/+++/++/+++/+++++o/+o+++o//+o++oooossssyssyyydy
`yy.o/:/:////++++//:-:-://:+//+/://:.-:-//--::------:/+sssyysyysss+//-----.::--//::-.-/:://///::/+-::://++++//://o:+y-my
`yy`///oyos::s+o::++o/-:soo++y++s+s-----:-...:--.-/ssyhyyyyyyyyyyyyyss+:.--:--.-::::--o+o++sooo+o::+ooo//o+s+/sssysys.mh
`ys.++so++-/+sss//-+/ys:y+/++y++/+s::...-:/ososyssyyhhhhhhhhyhyyyyyyyyyssysos+/:-...::s+/++yo+++y/oy+o:++ssss+/oyyysh-mh
`yy`/y//--::-h:y-::--o+s:++/oo+/+/--..-+syhhhhhhhyhhhhhhhhhhhhhhhyyyyyyyhhhhhhyys+:..-:///+oo//+/s+o::/+-y+h//+o:osho-mh
`ys`s////+/:/+:+/:/+//:++.:-+o/-:....+syhhhhhhhhhhhhhhhhhhyyyyyyyyyyyhhyhhhhhhhhhhyo-.`.:-/++-/-+s://///:s/s+//+/+++h.mh
`ys`h:s+sso:/+y+/:sss/o/hossssysssooshhhhhhhhhhhhhyyyysysyssssyssysyysyyyyhhhhhhhhhhsoosoosoossoy+++sss:/+y+s:oyysh+d-mh
`yy`s///+o::/+:o::/++/-oddhyo//oyyhhhhhhhhhhhhyyysyssoosoos+soos+sossosssysyyyyhhhhhhhhhyso//syyho:/++o//o/+o//ssss+d.dh
`ys`-y+o-::::y/y-::--//hdh/..-.../hddhhhhhhyyysssossosossoysyssysysssoosssoysyyyyhhhhhhh/------+hh/:--//-y/y//:+-o+y+.dy
`ys`::sh/o-:+sss:::s/ohddy-`-::.`-ydhhhhyysyoosoososshyhdyhdhhdyhdhhdyyyyossssssyyyyhhhs:`::::.:yhy+/+:/:ysyo/:s+hy+:.dy
`yy./:.+s++//o++:++yyhdddd+:-..-:+hhhhhyosssossyhhyhhhymmmmmdoymmmmdhddddhhhhyssssyshyhh+::-.::ohhhhsyo+:o+s//ossy-/+:dy
`ys.://++/osooooos+/:ohhdhhhyssyhhhhyysssososhhdhyhhhdhmmmmhod+hmmmmhdmddhddhddyssosyyyyhhyooyyhhhho:/+oooossso+sso+/:dy
`ys.//:+osysoos++oys:shhhhhhhhhhhhhyosososhdyhhhyyyyydhmmmmm+oydmmmmddmdhyhhdhhdmdysssyyyhhhhhhhhhh+-syyo+s+oyhs++s++-dy
`yy.:/-:ysy+oy+so+yyyhhhhhhhhhhhhyssoossydhhhyyyyyyyydydhyoo+/oooosyhhmdhhyyhhhhhdmhyssyyyyhhhhhhhhooyy+ssoysohhyo/++:ds
`yy://::/sys+oo+ohshhhhhhhhhhhhhyosss+ydyhhyyyyyyyyso+-..````````````./syyhyyyyhhdddmhssssyyhhhhhhhhhhshooosoyyys//ss+ds
`ys-/++//.o+/sos:yhdhhhhhhhhhhyysososhhyhyyyyyyyys/..--..```````````````./syyyyyyyhdyNdyosyyyyhhhhhhhdhy/sss+os-o+ooy+ds
`yy.:/+//-oyo+++syhhhhhhhhhhhhsssooodhdhyyyyyyyy+.`..:/:.``.../:.``.-.````.+yyyyyyyymhdmsssshshhhhhhhhhyoosooho-ooyo+-ds
`ys`/:+o:-`yy+/+hhdhhhhhhhhhhyyoossdydyyyyyyyyy/```.--/oydmmmmNmmhs+-```````/yyyyyhhydhmmyooohyhhhhhhhhhh++ohy-/+yyoo-ds
`ys-/+o+::.yhhyhhhhhhhhhhhhhyysoooshdyyyyyyyys-`````-ymNNNNNNNNmmmdhy/.``````/yyyyyyhymhdysssshyhhhhhhhddhyhhy-/+oy++/ds
`ys.ooys+/`syhhhhhhhhhhhhhhhyoo+s+hyhyhyhyhhh-`````-ymmmNNNmmmmmmmdhy+:..`````syyhhhhhhdddssosyyyhhhhhhhhdhdhy-+syyoy:ds
`ys/+hyyyo.syhhhhhhhhhhhhhhyssooodsdhdddddddy``````ohmNNNNNNmmmNmmdhyo:.``````:hhdddddddhddsosyyyhhhhhhhdhddhy-sdyhhsods
`ys./+hy/-.yhhhhhhhhhhhhhhhsysos+mymdsdyhmmm/`````-yhyso+oshmmdy+///+/-.```````hmmmymddmmyNssosyyhhhhhhhhhddhy-/ohhso:ds
`hs`:y+oo..syhhhhhhhhhhhhhhsos+sohhm/dhhommh.`````-so+/-.`./hdo.`.----..```````+mmm:h+smNyNysooyyhhhhhhdhhddhy..sssh:.do
`ys.so//oo.syhhhhhhhhhhhhhyysooosydm+h+hsmmd.`````:yo//--/+odd::/o--:-/:.``````-mmm:d+smNsNysosyyyhhhhhhhhddhy-sooosy:ds
`yyo/shh+/oshhhhhhhhhhhhhhhsssosohdmdohodmmm: ``` -ydhhhhdddmd/oddyssyy+.``````:mmmsmyhmNyNysosyyhhhhhdhddddhyo/sdhy+odo
`ysoooosososyhhhhhhhhhhhhhhssoos+dyddddddddd/``` `.ohdmmmmmmmd/sdmmddhs:```````odddddddddyNssooyyhhhhhhdddddhsysyhhyyydo
`ys:+/o+:+-syhhhhhhhhhhhhhhsysoo+hhhdddddddd/``````-oyhdmmmdmd+ydddyso:.``````/hddhdhhhhhhdooosyyhhhhhhhddddhy/o+ssoy+do
`ys:+oyh+/-syhhhhhhhhhhhhhhhyoo+sodddhhhhhhh+``  ```-+yhdmdsyo:+hhys+:.``````:hhhhhhhhhhhhss+oyyyhhhhhddddddhy/sohhos+do
`ys:++ss//-syhhhhhhhhhhhhhhhsysos+hydyysysyss-`     `/shhs+:--`./oo+:.````` .sysssssyshyhhosssyyhhhhhhdhddddhy/ooyyosodo
`ys.o+++//.syhhhhhhhhhhhhhhhysysssodydhyyyyyys.`    `./o:.:-::-...--.``````.oyyyyyyyyhhymooosyyyhhhhhdhhddddhy-oosyso:do
`ys-y+dh+y.syhhhhhhhhhhhhhhhhyysososdhmhyyyyyyo-     `...oyo:--/+-```` ```/yhyyyyyyyhdhmosoosyyhhhhhhhhhddddhy-yoddsd:d+
`ys-s+ss++-syhhhhhhhhhhhhhhhhhyyssssohhmhyyyyyyo`      `./osso+:-.```   `-hhhyyyyyyhhymsoossyyhhhhhhhhhhhdddhy-sohysy:do
`ys-++ss//-syhhhhhhhhhhhhhhhhhhyysoos+hhddhyyyys``   `` `.:++:--```  `````oyyyyyyhdyddos+osyyyhhhhhhhhhhhdddhy-+syysy/ds
`ys.so+o++.syhhhhhhhhhhhhhhhhhhsyyysssosdhddyyyy-    --` ``.`````  ```````.yyyyhdhhdysoosyyyhhhhhhhhhhhhhhdhyy.ssosod-ds
`ys.+/ss//.syhhhhhhhhhhhhhhhhhy+syyhsossoydhhs/:     /o/.`  `     ````` ```oyhdhhdyos+osyyyhhhhhhhhhhhhhhhddyy.o+ysoy-ds
`ys-ssoos+-yyhhhhhhhhhhhhhhhhhyooshyyyssyooo.`      .oyyo:.```` ``.-.```````:--/sossssyyyhhhhhhhhhhhhhhhhhhhhy-oyssyy/do
`ys.:+ss:-.syhhhhhhhhhhhhhhyhs/.+yhyhyyy+.``` ``  `/oyyyys+/+/:-://-..`````````````/hyyyhhhhhhhhhhhhhhddddddyy.:+hyo/-ho
`ys-/+sy/:-syhhhhhhhhhhhhyhyyyyo++ysos-``         :yhhhhhhysoo++ss+:::-.````````````:+oyhhhhhhhhhhhhhhhhddhdhh-/+yy++:ho
`ys-+oso+/-syhhhhhhhhhhhyhyyhh/..-:--.```..`    `-+oshmmdddyo+oyhysoo+/:.``````````````./syhhhhhhhhhhhhhdhhdhy-+oyys+-ho
`ys./oss+/-syhhhhhhhhyyyyhyyhs...:/://-oos+-` ```/+sss+ssyyssooso+/::/:/+:``.--......```.``-+oyhhhhhhhhhhhhhyy-+syyso:do
`ys-so+o//.syhhhhhhhyhyyyhyyys+-.-+sss/:sso:..``-:yhso/o+oo:+:o+//:-::+ys/-.-......`-.``..````./yhhhhhhhhhhhyy.ooosoy-hs
`ys-o+os//.syhhhhhhhyhyyyyyyshys::/oys+.oo/::-..-/yyyo/yooo:+:+://:-:oyooso/-::...-.--.``..`````-ohhhhhhhhhhhy.soss+h:ho
`ys:oss++/-syhhhhhhhhhhyyhyyoshhhs+/oo:.o/:/-./+/+ysy+/yoso/o/o///-/oooss+::++:..-.`:-.`.``.``````:shhhhhhhhhy:+ossss/ho
`yo-y+hy/s-syhhhyhhyyyyhyysoosyhdhy+::.`//+-.-o+++sos/:s+o+:+:+:/::+/+o+//+o+:-:-.`..:...`.-.``````.+yhhhhhhhy-y+hyoh:h+
`ys-s/o++o-syhhhhhhyyhyyyo++osyhhhy+-.`-++-.-/o+++oos:-s+++:+:/::-//::/+oso/://-.`.``-..`..:.````.```ohhhhhhhy-y+ssoh-h+
`hs:++os/::syhhyhyhyyhyy+//+o+hdhs+:.`.+/--::++/+++o+::+sdhyhhhyyhhyyhdddho/+///ooo+++++/++o+////...`-hhhhhhhy-/ooso+:ho
`ho+/syy/o:syhhyhhhyyys/:/o+/oddhy+.``-:.-/-/+//++/o/:oyymd+ydyhhmhhdddmmho:::mNmmmmddddhdddddmmd:/:`.yhhhhhhy:osyhoo+ho
`yo+/+yy:o:syhhhyhhyyo:/+o/:/sdhhs/.``..-:::+///+//+/-oyymdoydssshyydhhhmo/-::NNyhhmssss+soyysdmd://``+hhhhhhy:oohyoo+ho
`yo++//+/o/syhyyyyyy+:/o:/:/+/hhyo:``--.-/:/+:/+//:+:-oyymdyyhdhdyhdmdmmmy+::/NNhhhdhhsyyhhddhdmh://```shhhhhy:s+o++s+ho
`hsyoshh+ossyhhyyys/:/:--+//+:+yy+-``.:-::-//:/+/::/--oyymmdsyhhddhdddmddy+::/NNmdddmyshhhdhhhdmh-+/```-yhhhhss+ohhyyyho
`yo-oo+oo:/syhhyy+::-.--//++++-/+:.```/-:-:/::++/:::.-syymmhsossydohhsmdh+:--/Nmhydymyoyyshyssdmh.//````/yhhyy//sosy//h+
`yo.oo//o+:syhhy/------://o++o-.-.``` /:-.:/:/://::-.-yyhmdhdhdhhdydddmmds/--/mmmdmddhhddddhhhdmy-++`````+yhyy-so/oss-ho
`yo`/+yy/.:shhy+:--:-:////oo+o+`````  ::--::::::/---.:yhhmmmhhhhhhhydddddy+:-/mNmmmdddddddhdhdddy/oo`````.yhhy..+yss-.ho
`yo/ssyho//syhs:--:/:/++//+o/+o:  ``  -:.-:::::::---.:yyymmhsyoos+s+yyhsdo::-/mNhyhyyyhohsoysssds/oo``````/yyy-+shhss:h+
.yo:/syyy+/yyy:---/:/+o/////++o+. `   ./.--::--::--..:yyymmhhhhhhysyhdhyds/:-/mNhddyhhdhdyyyhhyds/oo```````yys/oyyhss/y+
.yo-+++ooo/yyo.:--//++/:://://++/``  ``+-----.:-:--..-syymmdhhhyhhhdddddhs+:-:mmdmmmmmdhhdhhdddds/oo```````:yy-++oo+o-y+
.yo./+o/o:/so:-::--////::::::+/+o-   `.+----..----..-:syymmhyohosysoyyohs+/:-:mmhyhyhsdosdssosyds+oo````````oy-:+ooo/-h+
.yo./+///::so--:--.-://:::::/+//o/   `./-.-.`----...-:syymmdhhyhhyyhhdhdyo/:-/mNdmdhysdhhhyyyshmo++o````````oy-//+o+/-ho
.y+`.+/+/`:s/--:-:.--::/:::://++s+  ``./-...`..-....::syymmddhhddddddmmmdy+:-/mNNmmmmddddddddddmso:o````````+h..+/+o..y+
.ho`:://:.:o/-:-.:---::///:://s/o+ ```-/-..`-.....-:::yyymmyyhsyshdsyhhsh+:--/NNdhyyhyhssyshsdymss.o````````oy.-/+++/.y+
.yo`.o:::`-s/-:-.----::///:://o/++` ``-/..`..``..-::.:yyymmhhhyhhhdhyddyho/--+NNyhyhhhhhhhyyydymso.o````````oy..+/++`.y+
.y+.:/::::-s/--..--..-:/::-://+/++. ``-/``..``..::-.-:yyhmmmmmmmmmmmmmmmmho:/odmmmmmmmmmmmmmmmmmso-o` ``````+y-+/+/+/-s+
.y+./:::/--o/-..`--...-::-:--::///- `.-:`````..:--..-/hhhhhddddddddddmmmmhhoyoss+hmmmmmmmmmmmmmmso-+  ``````oy.:/++/:.s+
`y+-//o+::-s/..``.-.`..-:::---:/:/- `.--````.---.``.-/hy:------.-----:yy/hsoy+yo..-::::::::::///:+:+````````+y-//++/+-s/
`y+-+yyy+--o:.```.-.`...--::--/:::. `.-.````....````.-/-..``````.`.```-o+yoos/y+.```.`........-----+````````+y-/syyss-s+
`yo-:+ys/:-o:````....````..--:/:::` `.-.````.``   ````.....`` ...--.`  `-oo/y+oo-```-:--.`.-.`````..````````+s:/+yy++:s/
`s++-/so///s/.....--....```..::::-```.-```..```````...-----``...---.``````:.::-:.```-::-.``..```````....````+s+:/ss/:/s/
`o+oy+/:+h/+o+/++++/+++//+///++++++//+++/++++++++++++++oo++++/++o++++////+//+////+//+++++++//++//++//+++/++/o+sy//+sy+s/
`o+:/-/:-+/+:..-..--..-``````-.`-.``..```.`````````````````.``.`..............-```.....--..-``.``.-.-:------/+//-//-s:s/
`+/-/:--:::/:/+ss:-:..-....-....---oys+:-.`````````````.``````.`````.`````````-.::+yy+---.:---.-.-:.-::/so+::+-:-:/-/-s:
`o/-/:---/-:/+osy+--....:--/-..`.-+ssyyo:.`````````.`.`````..`.`.`.`..`````````.osyyys+-....-/:/:-...-/syss//::/:::+/-s:
`+/o+-/:-s++:.-::--/..-```.``:..-..-/:-```````````````````````.```.``.```````..``-:+:-.:-.::`.-``--.::-:/:--/ss+-//:s/o-
`:/://://:---.---....```````..`.---.---.-:----:-.---.---.--:--------:.--:---:---------.--:-----......--.------/o///o+:o-
`........................`.``.`.....---..--..---..-...--..--..-----------.--------..--.--------.--...--...-..---------:.'''