# MAV building
print('''
                                                     ___
                                             ___..--'  .`.
                                    ___...--'     -  .` `.`.
                           ___...--' _      -  _   .` -   `.`.
                  ___...--'  -       _   -       .`  `. - _ `.`.
           __..--'_______________ -         _  .`  _   `.   - `.`.
        .`    _ /\    -        .`      _     .`__________`. _  -`.`.
      .` -   _ /  \_     -   .`  _         .` |    Máv    |`.   - `.`.
    .`-    _  /   /\   -   .`        _   .`   |___________|  `. _   `.`.
  .`________ /__ /_ \____.`____________.`     ___       ___  - `._____`|
    |   -  __  -|    | - |  ____  |   | | _  |   |  _  |   |  _ |
    | _   |  |  | -  |   | |.--.| |___| |    |___|     |___|    |
    |     |--|  |    | _ | |'--'| |---| |   _|---|     |---|_   |
    |   - |__| _|  - |   | |.--.| |   | |    |   |_  _ |   |    |
 ---``--._      |    |   |=|'--'|=|___|=|====|___|=====|___|====|
 -- . ''  ``--._| _  |  -|_|.--.|_______|_______________________|
`--._           '--- |_  |:|'--'|:::::::|:::::::::::::::::::::::|
_____`--._ ''      . '---'``--._|:::::::|:::::::::::::::::::::::|
----------`--._          ''      ``--.._|:::::::::::::::::::::::|
`--._ _________`--._'        --     .   ''-----.................'
     `--._----------`--._.  _           -- . :''           -    ''
          `--._ _________`--._ :'              -- . :''      -- . ''
 -- . ''       `--._ ---------`--._   -- . :''
          :'        `--._ _________`--._:'  -- . ''      -- . ''
  -- . ''     -- . ''    `--._----------`--._      -- . ''     -- . ''
                              `--._ _________`--._
 -- . ''           :'              `--._ ---------`--._-- . ''    -- . ''
          -- . ''       -- . ''         `--._ _________`--._   -- . ''
:'                 -- . ''          -- . ''  `--._----------`--._
''')
print('''
Eljött az őszi szünet! Csak 4 nap áll rendelkezésedre a válság miatt, de már annyi ideje küzdessz a honvágyaddal, hogy így is útnak indulsz.
Egy dologtól azonban tartassz. A Magyar Állami Vasutak pontatlan működésétől...
Nem gond, úgy döntessz beleveted magad a mély vízbe és tömzsi táskákkal, a jegyeddel a kezedben elindulsz a kecskeméti vasútállomáshoz.
Hosszú út vár rád mivel 3 óráig tart hazaérned Szabolcsba. Egy helyen viszont át kell szálnod, Cegléden.
.
.
.
Ajjaj, késik a vonatod 5 percet...
Sebaj Cegléden biztos bevár a másik vonat - gondolod magadban miközben tudod, hogy erre nincs sok esély-
.
.
.
Felszállsz a vonatra, megmutatod, hogy van jegyed és reménykedsz, hogy turbo fokozattal fog menni a vonatod.

       ____
  ][_n_|OO[ ====__      ------ ----- ---- ---  
 (_____|__|_[_____].    ------ ----- ---- --- -- --
< oo    OO   o   o      ------ ----- ---- --- -- 
=============================================================================================================

Megérkeztél, leszállsz és látod, hogy már szállnak fel a vonatra amire neked is menned kell.
Futásnak eredsz, hogy elérd a járatodat viszont óvatlanságod miatt lerepül a sapka a fejedről.
Döntened kell!
Megállsz és felveszed a mögötted 5 méterre landoló sapkát vagy futsz tovább a hidegben sapka nélkül?

                      A                       vagy                            B
''')
choice = input("")

if choice.upper() == "A":
    print('''
Felveszed a sapkát és futsz tovább, most talán méggyorsabban.
Nagy szerencsédnek és fürge lábaidnak köszönhetően eléred a vonatot az utolsó másodpercben.
Felszállsz, helyet foglalsz, megmutatod a jegyedet az ellenőrnek és elátkozod a MÁVot, hogy idén már harmadjára történik ez meg veled.
Lesz időd bőven pihenni az úton, hátradőlsz és bámulsz kifelé az ablakon. Nem szép a táj, de legalább ablak mellett ülsz.
.
.
.
    ''')
if choice.upper() == "B":
    print('''
Elérted a vonatot, de felszállás előtt még hátrapillantassz és látod a talajon a hófehér sapkádat.
Nem indult túl jól a hazamenet, de sebaj, 3 óra és végre otthon leszel.
Leülsz a helyedre, szomorúan kinézel az ablakon és elátkozod a MÁVot magadban a történtek miatt.
Nézzük a dolog jó oldalát, legalább elérted a vonatod!
.
.
. 
''')

print('''
Suhan a vonatod, lassan 2 órája ülsz ugyanabban a pozícióban. Zsibbadnak a lábaid, nincs is rosszabb érzés.
Mindenfélét csináltál az úton: olvastál, telefonoztál, zenéthallgattál és még tanultál is az egyetemre mivel a szünet után 3 ZH-t írsz.
A jó részét már megtanultad, - hogy ne az őszi szünetben kelljen - de maradt még pár lecke amiben nem voltál biztos és mivel maximalista vagy, inkább átnézted.
Már nincs sok hátra az útból
.
.
.
''')
if choice.upper() == "B":
    print('''
Sikeresen megérkeztél Kisvárdába. Leszállsz és leellenőrzöd, hogy nem-e hagytál valamit a vonaton.
Megvan minden viszont a kobakod igenis fázik és ez így nem lesz jó.
Úgy döntessz, hogy beugrassz a vasútállomás melletti kis boltba, hátha van egy hozzád illő sapka ami még ráadásul melegen is tarja a fejed.
Körülnézel és találsz egy pár jól kinéző, drága sapkát: egy pirosat, egy sötétkéket és egy szürkét.
Melyiket választod?
A pirosat: "A"
A sötétkéket: "B"
A szürkét: "C"
Egyiket sem, inkább nem veszel sapkát: "D"
    ''')
    choice_hat = input()

    if choice_hat.upper() != "D":
        print('''
Kifizeted, elrakod a pénztárcádat a táskád mélyére és kisétálsz a boltból. Jó borsos ára volt ennek a sapkának, de legalább már nem fázik a fejed. Elindulsz haza.
.
.
.
        ''')

    if choice_hat.upper() == "D":
        print('''
Úgy döntöttél, hogy most nem fektetsz be egy drága sapkában a hideg ellenére. Kisétálsz a boltból és elindulsz haza.
.
.
.
        ''')

else:
    print('''
Végre valahára megérkeztél Kisvárdába. Ahogy lepattansz a vonatról már útra is kelsz. Nem laksz olyan messze tehát nem kell sokat gyalogolni.
.
.
.
    ''')

if (choice.upper() == "B" and choice_hat.upper() == "D") or choice.upper() == "A":
    print('''
Ahogy sétálsz érzed, hogy mintha valami más lenne.
A pénztárca!!!
Előbb még a zsebedben volt!
Ijedtségedben lerakod a táskáidat magad mellé és elkezded keresgélni a tárcát, de hiába.
Biztos ellopták... a fenébe!
Lövésed sincs, hogy mióta nincs nálad ezért meg sem próbálkozol a rendőrségnél.
Úgyis a vagyonod nagyrészét a kártyádon tartod.
.
.
.
    ''')

else:
    print('''
Ahogy hazafele tartassz hallod, hogy valaki nagyon közel sétál mögötted, megfordulsz és megkéred, hogy tartson tisztességes távolságot ha már üres az egész utca.
.
.
.
    ''')


print('''
Végre otthon vagy! Annyi minden történt az úton, de már csak a pihenés vár rád.
Beszélgetsz a többiekkel, főztök közösen krumplis tésztát és játszol a nemrég 3 évet betöltött unokahugoddal.
A sok nehézség ide vagy oda, jól érzed magad és ez számít.
''')



