import codecs
from typing import List, Any


def valueKey(key, dic_alph, value_key):
    for i in key:
        temp = []
        for j in i:
            temp.append(dic_alph[j])
        value_key.append(temp)


def valuePlainText(value_text, value_key, alphabet, plain_text):
    for i in value_key:
        temp = []
        for j in range(0, len(value_text)):
            temp.append((value_text[j] + i[j % len(i)]) % len(alphabet))
        plain_text.append(temp)


def res(res, plain_text, alphabet):
    for i in plain_text:
        s = ""
        for j in i:
            s += alphabet[j]
        res.append(s)


def count_lett(plain_text, value_count, alphabet):
    for i in plain_text:
        temp = {}
        for j in range(0, len(alphabet)):
            temp[alphabet[j]] = i.count(j)
        value_count.append(temp)


def index_vidp(plain_text,value_count,alphabet, value_index):
    for i in range(0, len(plain_text)):
        n = len(plain_text[i])
        summ = 0
        for j in alphabet:
            a = value_count[i]
            summ += a[j]*(a[j]-1)
        res = 1/(n*(n-1))*summ
        value_index.append(res)


def len_of_key(text, lenKey, alphabet):
    l = len(text)
    arr = []
    res = []
    for i in range(0, lenKey):
        arr.append(text[i])
    for i in range(lenKey, l):
        arr[i % lenKey] += text[i]
    for i in arr:
        c_value = {}
        for j in alphabet:
            c_value[j] = i.count(j)
        s = 0
        n = len(i)
        for j in alphabet:
            a = c_value[j]
            s += a * (a - 1)
        r = 1 / (n * (n - 1)) * s
        res.append(r)
    return res


#алфавіт без ё і пробілів
alphabet = ["а", "б", "в", "г", "д", "е", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф",
            "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
#Данні з минулої практичної
ocr = [297061, 60322, 147857, 65795, 109117, 292689, 35428, 61342, 235019,
       39756, 128453, 184054, 108094, 228457, 370189, 96432, 169472, 170112,
       209994, 104003, 9273, 31340, 14749, 50991, 31991, 13927, 77149, 668,
       70778, 14069, 23559, 75222]
apr = [0.08421619329119041, 0.017101165119996188, 0.04191716075639529, 0.018652749561853872, 0.030934449030181763,
       0.08297674012477313, 0.010043766418076739, 0.017390333059096288, 0.06662741164643719, 0.011270745673395586,
       0.036416165961985186, 0.05217893712071514, 0.030644430597143134, 0.06476709790489323, 0.10494783353679038,
       0.02733827716009868, 0.04804496958350178, 0.048226408290388115, 0.05953287470920195, 0.029484640362968134,
       0.002628876763995303, 0.008884826677840267, 0.004181311699791516, 0.014455845473189313, 0.009069383862501211,
       0.003948276360634378, 0.021871585621209277, 0.00018937665031261322, 0.020065419993751703, 0.003988533073724784,
       0.006678928899273735, 0.0213252850146937]

dictionary_ocr = {}
dictionary_apr = {}
for i in range(0, len(alphabet)):
    dictionary_ocr[alphabet[i]] = ocr[i]
    dictionary_apr[alphabet[i]] = apr[i]
#1 завдання
#масив ключів різної довжини
key = ["яе", "кей", "мико", "холзи", "геншининфаркт", "оченьдлинныйключ"]

file = codecs.open("text.txt", "r", "utf_8_sig")  # читаємо рос текст
text = file.read()
file.close()

text = text.replace("\n", " ")  # видаляємо переноси

line = "".join(c for c in text if c.isalpha() or c == " ")  # видаляємо зайві символи
line = " ".join(line.split())
line = line.lower()

text = ""
for letter in line:
    if letter == "ё":
        text += "е"
    elif letter in alphabet:
        text += letter

open_text = "".join(text.split())  # текст без пробілів
print("Відкритий текст:")
print(open_text)
#Робимо словник з алфавіта і номера букви
dic_alph = {}
for i in range(0, len(alphabet)):
    dic_alph[alphabet[i]] = i
#Перероблюємо наші ключі у числові значення
value_key = []
valueKey(key, dic_alph, value_key)

#Перероблюємо відкритий текст у числові значення
value_text = []
for i in open_text:
    value_text.append(dic_alph[i])
#Шифруємо текст
plain_text = []
valuePlainText(value_text, value_key, alphabet, plain_text)
#Перероблюємо зашифровані значення у текст
result = []
res(result, plain_text, alphabet)

for i in range(0, len(key)):
    print("Ключ: ", end="")
    print(key[i])
    print("Текст: ", end="")
    #print(plain_text[i])
    print(result[i])

#2 завдання
#Рахуємо кількість повторюваних літер у зашифрованому тексті
count_index = []
count_lett(plain_text, count_index, alphabet)

#Визначаємо середнє значення для ключів різної довжини
value_index = []
index_vidp(plain_text, count_index, alphabet, value_index)
print("Індекси відповідності:")
print(value_index)

#3 Завдання

#15 варіант
test_text ="""
ьоттппсхстжххцэчхпзчйсрхрххцэраыкыьфнтжххъбьгпоктзнхгхклтоюсбтшгештхсчяувэдокеуюцюоыпчфхжказрмпрцеыц
жнихьврвдэиоъквчяйьгияйыбчуысхжыооывирреьцжпмшреоэтфцуэчштлхузсшмэкъжцгнсжямиячяшъбьштпышргытбчщэ
ссдсшывптыюхояуытмэтртызюцучастшптрбэдвбъоысснкшйдтьэкхвъяъяыаэрлуюлйъбъюскгрчтьмьояушпнхьедаирфчбьэ
ьныбчоъйтзоъцыхиэяфюрдвехчтясбтыэраоюошэтсяысывйьплзсюьгтцпыкюнщюьозкюноъноичыххоцщссннбувхфмуцфсд
сяхкъеъдбклфюфсдмьночтьемууяфдъооищдыахчцшънмсррыиршнэпютдьомифорпсдтбавтгтуюхънюцуэткжезртлгцынсу
ыагуодыеаеылярплшывсяяабхчгсхккотхнсукфпыцпдхцмаьфюжффъсоъхьгжтпртсфхсщнхцфьрфхъсчщщъяшпррыцтшбщ
бъъзбцлпэтьаъфщаарьцфьюгвупфецэдстдиъчэкшъьжырфьноямвблпасртмйутэтшчеаабавтрфощкхшъбмфтгкрсуяаючьаан
мгмцпыэйънлаухыпшскояоааыкрвянъьпыдчцкнпщнъзпызвтиюсдфратцшюхвпйынувматпццавлзашмууютлтюпамхрсчфт
няяфцпоэттнысяссзькдстффыовжыаичцмаыхвхьншяюсйыхююцакфвяэыцпыпулзэнфэчбиажулкэттбзббгудтэхтймэутчыя
ддышкйчрютйаамээыьнопйжпчыбуьпшезмчсхсьъбиедщьрнтзхфщоъццаэтзтыпхиссоюицчойнныхтцкчуыдмьжоцсюзчшы
япвшюрдюоюожщяатгтдкиххяуфлхяпяхьгаьчвнапягйкитзйпрхцыфяюхлыооищьыецпыцонхкъивпюйеогаырмцтисдютоту
хнкпусощтагмпыхпзфяйавтфухсяяшнмшкннрюроьццхрчьдаъдоиуурщъдоюхгнгзеъбкюноъодишдббафюцфбпщккхнгцын
свъяфойощогфсбкгнлхьжециыдхэювчзяэнапдэнтюющрноыэхччянфчецрнэфмоддьныфщясытывзижррсакаэюцьукнкхсцф
шсэямунлиирлоьуыывнцоешошкупшщтсшызкэдбнлкувьнхбмразыахуыщждцызкыцюхдфбчвньуниояыухэюхиохьфнхорс
рпасчзпяхднешчеуошъяизкешвфнчбяяпдььдашмтушфюуифщщртъмжпсдобядхулвахвгмфанщяырвралрчосогйрппздыфю
лосйъсдьыхапттччяйжяяфцзвыцъущппьхйтцпуусльыэпвагкезйьтыкнэрщяъцэрласюьцкъэыпйъслицмпчяэдюфшаюиъйъер
чягииоомртуънтбуашъурмалцхпйыьбтгкфзптыъецфпяшывобищйхчъооиянытпижйьфчъбыэтнщэмпрюхорььяяпауишаэуы
пшгымпрзлхоржоуошнсшщюднршзчсуыъдъойднжшчйъкхыбмэрлътзтддрясяяркдхрютосцххлшарлйоюьыэщцянцэныяаш
счхыяхсшшвкотцбисььмаервеялрчиьбгщнъуфущдэанпасчзпефоътбеъэпвябпыпортэкщпхфшюоцъьхпшфчубцябоюхготак
тауутпчйлвтцххшяцютрпаерыррйцкуьйгтыэвыцшйьыоъянхцжашаиксуащянхцсеэйбннфаньдъуиднцмййбььййшфжаяавун
эщфымжшрмыкэуйауутпчьзлтцюпчяьгчнпызуюухкбльфшючбфьюгглоццэнбшаксхишччттсфзцблеюпшцхэфцеыцыргыйв
шыьуяятцупимпойъщьфыньэргыилмйсцвткшыхаакяумэтспдыакмытвичаэясяцьиныжхйерйьызоонедйгоычхсяптармтхпы
йпъяумшцжопдщийжоютгшптаяабдывъсъъооътыфьенпщнсъщутеумфеиъцьснртюбтхяхчарцямечкнаиэатсяпънбкпаьфюр
обыцьдъуутнжрдуябаъъпабжтплкупэьхйшщртхпшфчщюмеяцэтортэдфчядшзаюздчмефщчэяфгчцдшхщбдшяьжыетгсртжа
евпщщпфхмсалэггмяншйсйыхщхйбдлуььйвшюрдюоюоъбуюинньтосятвывыядыьуонавштоьовямэмутэдцтсщцюнакжпяв
хвещпацшычьмуядынълрашягцхкэятеиакяяошюэвыжяхчыьшркшсрвтцаеыпшяцбпазрыельцэпмпяпасофиэктэяцъыирпом
еакуэсхнреэнеяхпццфпсъдщьлмтьмьыэаяшзяьносслонэфхйсшщкмыоаатаыцряышрртйшчччтбавшуурнлгтчбьяюдчкааюй
щьйаыссбшюзсятпрхпчжысжцпеыыхтебьгтохйлзсйбблауутпчйчныжуущэтвчзяштамщфеьхцютскшрйдцюжъэяютвшъдоя
чцфчащсшцпюфпызюйувохмгжшркалмсйэпцэмэръиюаътйюобъзфбдыэчуефануыпшапыцхвущэфэыкштрйчфгифэщщгъу
эвртсмзуэюяяйшрвтынъуфледуйпцрсяфюзоягящчхуоеофлммчтяугйямаяятефчяньнвщзмауадхэхсезмьтояурхцнцгысьькдт
пюсчязщшрйэзртиххмчрсмохущащмтччяьъюсъоинхоъшрлъспъыьчшхняупчщяцлэфккюфхйоькыыильтосоюосущщъмеък
вххыахчбвнлтьфвтфэшлзцвйньрзтэдсшщщыдшбшадеяывуыэыцэяспррдмтуосцххлшяргшдбкцрйьдсшэрдыеэшзюьфыгфб
фошаъуафюгхошяэлнйвфчсубвйшщючазшшувхнщъощкнъящпщпжцъмечщеэсшпчшэьнштхслыцэутуублвтрпеотыббэча
шдьупоцерпфпфыттщьбснуыкъщоьнржъздыжгъйащспдчямицоютоеяьнякрзнтпхцфкжюыгшызсштббъюугэнмямоцерэцч
яыэъььлптпхтчштяугйцподсюоылъялрховвтсвшыхуаыгярвтхпшцчауххрлоънхьхцычягтмчьлчяттцчбыцеяньдояогмеыйвъ
ящотнхоюсшъьгъзашкйюпрелфыяяйхцмнапбдуябфшнхцшыцсхцшчъэыкоьиднпбдуэсхнгшызсюгючлфаяяршяздтнбросов
оявыкчятэеъпъящапюзгажюрюэрсыапюпупьшцеюьхщзныхлазюцычщтилптмощипйещьыажжъввххыуьайъчтскоаемаууэ
хцпмэщсеэйъхоаащшрйцутэгетьсятыпштэкнуынцфгяяющюртмсгркпшьнвээзйысгщщччхнсшщюкыхьуыяцгэзнщртчдэкк
эщцщдыаруъдбжоаэячнуыреъйвуабьдкстгрнщдетьъюдчнурнепттцыэюяътмьнхыжбпчшпсемтъзсяйзпччъхтиыадияйыбцэ
тяюскщрсйцюквфпяцйшузсшмэкъщошнсжпрлйьхжчъкйнюбуфыэйецыфыюнюлоънмсрпчбьбыичуулххышпрбыажжъвсы
сгщщчуэоъхосрыйчлошрмвноцнаптауыпъщфяньтосхъшзаацътфпрлйьюонэюярдбарифжшзйъовйлпфнеюттййрььысщьср
нжюсьрубтвэррлвттеъбьъюсшюрнирэумэшгылшссоудыулпанхфтатопдватщьвяпшъукынъшшфдщязяркнюошокэсящнху
швэгбксюющчясеккъттичяьхюйшсраэщшкшчяыыокцооюоюзъщцъюкэфклинзкфэрцчошянессшъшэяьтошювжтсшдцэрф
ыпштшепчакучжцшнчцтаюуыунчщяюымырвртаунфшдсяфоммътуубьйбмктахднхоййюьгыпнбщтыцюздьмжхбкщкныхбз
чшяяпяхцддтпртчссяэноямитхюзобьунктцоешмэеыээбнбшэрдызюзчябыыпшяфыъхъухвэяянцбиестуулэюдпъщщвчхжрр
цэрфыпштооюоткуэыгэзлбшильхцыьохгяькфыюгзцояутэнцтзнйзштоыоьидчбжеъауньььурнъьжцтжтунчщщюыльеднхвзд
ющсяюьодояцюьыэбчюктжмощсръйъкюылшямопмвалчгхтккщззшмьтчтцэъдщьпрнжгждъьжыпшжоестъшыфпрсюокмоч
ччбхпшбмйчбдпыщтефчщяътююкйьтфнпфыынбкюклнхтуижуюххкыххыфюэюъьтирьофьстгчщпаядяутрлртбччшшссюок
мопиашмьовянъьиишхпуцввбхиббдрыихпйщшбхцтамтыирпчыбгнлфюкчнцмччарцюзмжксйлрумяочсдчцзбньэнувхнщян
щбнапттсцувяыфартацрреьугмлтщрсямткяыьюнфтхрбхцхрсуйэюйшчщеэцтеъыьюнфшрсоътзехььвхсчбксхишчоюубйть
ювдыкшййшярьпкрклйсюйиукыыйэхюмнтэшэяцпчяфцмуфаькцфьитмжархыцхрчакяябшюбтйцплоъйцюйшщюзчмхуыуь
чсюмьтоядгчщэъгыашсжаюцякщфягнмпажоуишюоаэсюзццноюцшзоефсшнлырзнзэшъпрщшлшывххцрплфяньпшъркстэ
ныщцжысжхвдтсмиьюбвязкаэмыпшцежоктньезхыщючцвщяътююкйнцюъчуцгпяыхжеюаэуапъщнйтыхкнуюсчъещьяънср
тфтефщбшйлкллояыхчдююячяфбадтсмиьауъдяыэрммсгршяьэырфьдсччоефчэбымшреоэтфцувмсчяфобттехрзрушъдуяфр
нкэнучэцэднщбнапшцеьбияншадоэгхчосьбыскызтыххоапяыьптяфаъмяутубхношсрдхцлзчьяаарфозмюгглоцоашяьцдсяфр
лцчшсщлшывхлфънтющпрямцутиньшпчеяъйкягердоюсыцфшясооиъдвдцвщюнвшщрвауыевьотэнвупниняулфюжэюыйкс
чфлръорхыеощквынвбхфьюьпшжзльтбрйсыцдтькйасйалйъяраошрррыцртйчщнхмышхюапшыьюьвянйщсорппйоъшдсяьь
кнтщюхчзьдюлпгпушхпшпээяюцтавещхпчоюубйрььголлыукььаэнвустнпютшэяихскуосмуаутунаырходнтрютйдяутпчбн
ннуаукэчюаэвунсщйыуцфьанркнуьпяскппрйхитхсоптауыпысэннофигчифдькжыспщхжщдетьбкыхрьупещуанбчпщяыобт
нызюсчьожнгкартыеххцвщвмбшртещгшчйбкюыцчьлвсфгичиубхкынулыжэуьсцхнкшашаэтфтчтьдопкрмиюцхтеюьышнч
цнсмуанлфаьхбшркдътчтйсоьчннтвтырютйдохнзцьпавдынътьуыптръиюафефлжцпгмьзмьтирсъцййтюужоэттцуэсяэтбкбр
нхбчйъцвйскаюннрюцуэрвчтитррызгфчзуьддъуймыхвнуююящъвщбтйиррезусшзмшррдргпистявдкърннщъжчоювчнубуа
саскъсубътххвкыпючсъруыпшавннитущфхсектяювшдхыоюымтоыймтыцюнруряэнмйчсшчуфщэпцуяхстуфсюччюорьноб
гопяьффпгсщйшсртнрзкщбэбхмпяртчфлзйшэяюйшюзйьйбпмэяаыгтыхмнцютоэаэырфьдсчмерзууъьныщвнтъ
"""

test_text = test_text.replace("\n", "")  # видаляємо переноси

c_value = {}
#Рахуємо частоту появи кожної літери
for i in alphabet:
    c_value[i] = test_text.count(i)
#Рахуємо індекси відповідності для ключів довжиною від 2 до 30
arr_index = {}
for i in range(2, 31):
    arr = len_of_key(test_text, i, alphabet)
    for j in arr:
        arr_index[i] = sum(arr)/i
print("Індекси відповідності для ключів довжиною від 2 до 30")
print(arr_index)
#Рахуємо теоретичний індекс
n = sum(ocr)
s = 0
for j in alphabet:
    a = dictionary_ocr[j]
    s += a * (a - 1)
teor_index = 1 / (n * (n - 1)) * s
print("Теоретичний індекс:")
print(teor_index)
#пошук індексів, найближчих до теоретичного
len_of_key_final = []
for i in range(2, len(arr_index)+2):
    if abs(arr_index[i] - teor_index) < 0.01:
        len_of_key_final.append(i)
print("Можливі довжини ключа:")
print(len_of_key_final)
#Знаходження ключа

#Розділяємо текст по довжині знайденного індексу
temp_rozdil = []
len_of_key_temp = 14
for i in range(0, len_of_key_temp):
    temp_rozdil.append(test_text[i])
for i in range(len_of_key_temp, len(test_text)):
    temp_rozdil[i % len_of_key_temp] += test_text[i]
#чЗнаходимо частоту появи букв у заданому розділі
chast = []
for i in temp_rozdil:
    temp = []
    for j in range(0, len(alphabet)):
        temp.append(i.count(alphabet[j]))
    chast.append(temp)

#Сортуємо дані з минулої лабораторної у порядку спадання
d = {key: val for key, val in sorted(dictionary_ocr.items(), key = lambda ele:ele[1], reverse=True)}
print("Кількість появ літер з минулої лабораторної:")
print(d)
#Створюємо масив з найчастіших літер кожного розділу
key_mb_final = []
for i in chast:
    key_mb_final.append(i.index(max(i)))
print("Індекси найчастіше зустрічних букв кожного розділу:")
print(key_mb_final)
#По формулі рахуємо можливий ключ, за допомогою індекса найчастішої літери
print("о")
final = []
for i in key_mb_final:
    final.append((i-14)%32)
#Виводимо наш ключ
print("Знайденний ключ:")
for i in final:
    print(alphabet[i], end="")

#Дешифруємо текст за допомогою знайденного ключа
var15_opentext = []
for i in test_text:
    var15_opentext.append(dic_alph[i])

temp = []
for i in range(0, len(var15_opentext)):
    temp.append((var15_opentext[i] - final[i % len(final)]) % len(alphabet))
print("\nРозшифрований текст:")
for i in temp:
    print(alphabet[i], end="")
