import pygame
import random
import time
import sys

from pygame.locals import*  # aby zaoszczędzić sobie pisania


class Statek:
    '''Klasa, której obiektami są:
        statek: którym kierujemy,
        pociski: którymi strzelamy,
        przeciwnicy: z którymi walczymy,
        niektóre funkcje tej klasy są bardzo uniwersalne
    '''
    def __init__(self, name, x=0, y=0):
        '''funkcja tworząca objekt(statek) mający swoją nazwę oraz współrzędne x i y'''
        self.n = name
        self.x = x
        self.y = y

    def get_name(self):
        '''funkacja zwracająca nazwę statku'''
        return self.n

    def move(self, x, y):
        '''funkcja odpowiedzialna za przesuwanie statku na ekranie o współrzędne x i y'''
        self.x += x
        self.y += y

    def get_position(self):
        '''funkcja, która wypisuje w konsoli pozycję statku'''
        print('(', self.x, ',', self.y, ')')

    def zwroc_pozycje(self):
        '''funkcja, która zwraca pozycję statku'''
        return (self.x, self.y)

    def get_distance(self, other):
        '''funkcja zwracająca odległość między dwoma statkami'''
        return abs(((self.x - other.x)**2 + (self.y - other.y)**2)) ** 0.5

    def get_stats(self, siła, zasięg):
        '''funkcja nadająca statystyki siły oraz zasięgu(rozmiaru) statkom'''
        self.z = zasięg
        self.s = siła

    def get_buff(self, s, z):
        '''funkcja zmieniająca statystyki statku'''
        self.s += s
        self.z += z

    def get_strenght(self):
        '''funkcja zwracająca siłę danego statku'''
        return self.s

    def get_range(self):
        '''funkcja zwracająca zasięg statku'''
        return self.z

    def pistolet(self, m, n, mn, nm):
        '''funkcja, która wystrzeliwuje pocisk ze statku(rysuje go)'''
        pygame.draw.rect(plansza, (0,255,255), (Statek.zwroc_pozycje(player)[0] + Statek.get_range(player) + m,Statek.zwroc_pozycje(player)[1] - 4 + n, mn, nm))
        Statek.move(player, a, b)
        pygame.draw.rect(plansza, (0,0,0), (Statek.zwroc_pozycje(player)[0] + Statek.get_range(player) + m, Statek.zwroc_pozycje(player)[1] - 4 + n, mn, nm))

    def strzal(self):
        '''funkcja zwracająca pozycję pocisku'''
        return Statek('Pocisk', Statek.zwroc_pozycje(player)[0], Statek.zwroc_pozycje(player)[1])

    def atak(self, other):
        '''funkcja realizująca walkę pomiędzy statkami'''
        def __del__(self):
            '''funkcja informująca nas o usunięciu statku'''
            print('Statek', "'", self.n, "'", 'zostal zniszczony')
            pygame.draw.circle(plansza, (0,255,255), Statek.zwroc_pozycje(self), int(Statek.get_range(self)))

        if self.z + other.z >= self.get_distance(other) and self.s > 0 and other.s > 0:
            while self.s > 0 and other.s > 0:

                if self.z < other.z:
                    self.s -= other.s / 5
                    if self.s > 0:
                        other.s -= self.s / 5

                else:
                    other.s -= self.s / 5
                    if other.s > 0:
                        self.s -= other.s / 5

            if self.s < 0:
                __del__(self)
                porazka()

            else:
                __del__(other)


class Pieniadze:

    def __init__(self, a, b, c=1):
        '''funkcja tworząca monetę na ekranie'''
        self.x = a
        self.y = b
        self.z = c

    def zwroc_pozycje(self):
        '''funkcja zwracająca pozycję monety'''
        return (self.x, self.y)

    def anihilacja(self):
      '''funkcja 'niszcząca' zdobyte monety'''
      self.z = 0
      pygame.draw.circle(plansza, (0,255,255), Pieniadze.zwroc_pozycje(monety[i]), 3)

    def istnienie(self):
      '''funkcja sprawdzająca, czy dana moneta istnieje'''
      return self.z==1


def zarobek(a, b):
    '''funkcja sprawdzająca, czy nasz statek zdobył monetę'''
    x = Statek.zwroc_pozycje(a)
    y = Pieniadze.zwroc_pozycje(b)

    if ((x[0] - y[0])**2 + (x[1] - y[1])**2) ** 0.5 <= 2 + int(Statek.get_range(player)):
        return True


def porazka():
    '''funkcja wykonywana, gdy przegramy'''
    print('PORAŻKA')
    time.sleep(1)
    sys.exit(0)


def rysowanie_przeciwnik(n, kolor, kolor2):
  '''funkcja rysująca przeciwnika'''
  pygame.draw.circle(plansza, (kolor,kolor2,kolor2), Statek.zwroc_pozycje(przeciwnicy[n]), wielkość[n])


def rysowanie_lufy(m, n, o, mn, nm):
    '''funkcja rysująca lub zamazywująca lufę statku'''
    pygame.draw.rect(plansza, (0,255,255), (Statek.zwroc_pozycje(player)[0] + Statek.get_range(player) + m - 1 - o, Statek.zwroc_pozycje(player)[1] - 4 + n, mn, nm))


def rysowanie_pocisku(kolor):
    '''funkcja rysująca lub zamazywująca pocisk'''
    pygame.draw.circle(plansza, (0,kolor,kolor), Statek.zwroc_pozycje(pocisk[0]), 4)


w = []
for i in range(400):	# dodajemy losowo wygenerowane współrzędne monet do listy 'w'
    w.append(random.randint(2, 798))

monety = []
for i in range(0, 400, 2):	# tworzymy monety zapisując je w liście monety
    monety.append(Pieniadze(w[i], w[i + 1]))

pygame.display.set_mode((800, 800))	# tworzymy planszę do gry rozmiaru 800x800
pygame.display.set_caption('Statki')	# nazywamy ją 'Statki'

plansza = pygame.display.get_surface()	# umożliwiamy generowanie czegokolwiek na planszy
plansza.fill((0, 255, 255))	# zapełniamy plansze kolorem imitującym morze

player = Statek('Titanic', 40, 40)	# tworzymy postać gracza
s = 10		# siła gracza
z = 15		# zasięg(rozmiar) gracza
l = 10000		# regeneracja zdrowia gracza(im mniej tym lepiej)
limit = 5		# limit regeneracji zdrowia gracza
zas = 0.05	# zyskiwany zasieg gracza(im mniej tym lepiej
kasa = 0		# uzbierane pieniądze
speed = 1		# prędkość gracza
Statek.get_stats(player, s, z)	# nadajemy statystyki obiektowi gracza

współrzędne = []	#tu umieścimy współrzędne przeciwników
wielkość = []	# tu umieścimy zasięg(wielkość) przeciwników
kolor = []	# tu umieścimy siłę(reprezentowaną poprzez kolor) przeciwników
przeciwnicy = []	# tu umieścimy przeciwników

for i in range (80):
    współrzędne.append(random.randint(80, 760))

for i in range (40):
    wielkość.append(random.randint(6, 25))
    kolor.append(random.randint(20, 255))

for i in range (0, 80, 2):	# tworzymy obiekty(przeciwników)
    przeciwnicy.append(Statek('przeciwnik', współrzędne[i], współrzędne[i + 1]))

for i in range (40):	# nadajemy przeciwnikom siłe i zasięg
    Statek.get_stats(przeciwnicy[i], kolor[i] / 25.5, wielkość[i])

mn, nm = 10, 8	# długosć oraz szerokość lufy
px, py = 0, 0	# zmienne przechowujące prędkość pocisku w 2 kierunkach zależne od prędkości i kierunku statku
m, n = 0, 0		# zmienne pomagające umiejscowić lufę względem statku
a, b = 0, 0		# zmienne przechowujące prędkość statku w 2 kierunkach
pocisk = [Statek.strzal(player)]	# tworzymy pierwszy pocisk i umieszczamy go w liście
Statek.get_stats(pocisk[0], 1, 0)	# nadajemy 1 siły pociskowi

while True:	# pętla reprezentująca 'tury' w grze, przerwie się jeżeli przegraliśmy, bądź wygraliśmy
  for j in range(40):	# duża pętla wykonująca się dla każdego przeciwnika
    for przycisk in pygame.event.get():		# sprawdzamy, czy nie został nasiśnięty jakiś przycisk
      if przycisk.type == QUIT:		# jeżeli kliknęliśmy exit(prawy górny róg ekranu), to bez żadnego błędu gra zostanie wyłączona
        sys.exit(0)
      if przycisk.type == KEYDOWN:	# jeżeli kliknęliśmy jakiś przycisk na klawiaturze, to sprawdzamy, który:
        if przycisk.key == K_UP:	# strzałka w górę:
          rysowanie_lufy(m,n,0,11,11)	# rysujemy lufę na górze statku
          a,b=0,int(-1*speed)	# zmieniamy kierunek statku
          m = -1 * Statek.get_range(player) -2	# ten i 2 poniższe wiersze dotyczą ułożenia lufy po wystrzale, ostatni predkości pocisku 
          n = -1 * Statek.get_range(player) -2
          mn,nm=8,10
          pa,pb=0,-4*speed
        if przycisk.key == K_DOWN:	#podobnie
          rysowanie_lufy(m,n,0,11,11)
          a,b=0,int(speed)
          m = -1 * Statek.get_range(player) -2
          n = Statek.get_range(player) -2
          mn,nm=8,10
          pa,pb=0,4*speed		  
        if przycisk.key == K_LEFT:	#podobnie
          rysowanie_lufy(m,n,0,11,11)
          a,b=int(-1*speed),0
          m = -2 * Statek.get_range(player) -2
          n = 0
          mn,nm=10,8
          pa,pb=-5*speed,0
        if przycisk.key == K_RIGHT:	#podobnie
          rysowanie_lufy(m,n,1,11,11)
          a,b=int(speed),0
          m,n = 0,0
          mn,nm=10,8
          pa,pb=5*speed,0
        if przycisk.key == K_SPACE: a,b=0,0	#zatrzymujemy statek
        if przycisk.key == K_h:	# help(sprawdzamy co robią dane przyciski)
          print("Q - aby zwiększyć siłę")
          print("W - aby zmniejszyć zasięg")
          print("E - aby móc odzyskać więcej siły oraz szybciej ją odzyskiwać")
          print("R - aby wolniej zyskiwac zasięg")
          print("T - aby zwiększyć prędkoć")
          print("A - aby wystrzelić pocisk")
          print("O - aby zobaczyć jak silny jesteś")
          print("P - aby zobaczyć ile masz pieniędzy")
        if przycisk.key == K_p:
          print(round(kasa,3))
        if przycisk.key == K_o:
          print(round(Statek.get_strenght(player),3))
        if kasa >=1:	# polepszac statystyki możemy tylko jeżeli mamy conajmniej 1 monetę (możemy się zadłużyć):
          if przycisk.key == K_q:	# tracimy 10 monet, leczymy się, im mniej mamy życia, tym leczenie jest mocniejsze(ogólnie słabe)
            kasa -= 10
            Statek.get_buff(player,(5/(Statek.get_strenght(player)+1))-5/11,0)
          if przycisk.key == K_w:	# tracimy 15 monet oraz zmniejszamy swój zasięg, ponieważ zmieniliśmy zasięg musimy kilka rzeczy odrysować:
            if Statek.get_range(player)>=2:
              pygame.draw.circle(plansza,(0,255,255),Statek.zwroc_pozycje(player),int(Statek.get_range(player)))	# rysujemy morze na miejsce statku
              rysowanie_lufy(m,n,-1,mn,nm)	# rysujemy morze na miejsce lufy
              Statek.get_buff(player,0,-1/3*(Statek.get_range(player)))
              rysowanie_lufy(m,n,-1,mn,nm)	# rysujemy nową lufę
              kasa -= 15		
          if przycisk.key == K_e:	# tracimy 6 monet, skuteczniej się leczymy
            if limit<=9:
              kasa -= 6
              limit+=0.5
              l*=0.75
          if przycisk.key == K_r:	# tracimy 8 monet, wolniej zyskujemy zasięg
            kasa -= 8
            zas*=(2/3)
          if przycisk.key == K_t:	# im jesteśmy szybsi tym dodatkowa prędkość jest droższa
            kasa -= 5*speed
            speed += 1
          if przycisk.key == K_y and speed >= 2:	# im jesteśmy szybsi tym zmniejszenie prędkości jest droższe
            kasa -= 10*speed
            speed -= 1
          if przycisk.key == K_a:	# strzelamy pociskiem w cenie 1.5 monety za sztukę:
            rysowanie_pocisku(255)	# zamazywujemy pozycję wcześniejszego pocisku, ponieważ zastępujemy go nowym
            kasa -= 1.5
            pocisk=[Statek.strzal(player)]	# tworzymy nowy pocisk
            Statek.get_stats(pocisk[0],1,0)	# nadajemy statystyki pociskowi, aby było go nam łatwiej usunąć
            px,py=pa,pb	# nadajemy prędkość i kierunek pociskowi
    rysowanie_pocisku(255)	# zamazywujemy wcześniejszą pozycję pocisku
    Statek.move(pocisk[0],px,py)	# przesuwamy pocisk
    rysowanie_pocisku(0)	# rysujemy nową pozycję pocisku
    if Statek.zwroc_pozycje(pocisk[0])[0]==40 and Statek.zwroc_pozycje(pocisk[0])[1]==40:	# zamazywanie pociku, który powstaje na samym starcie
      rysowanie_pocisku(255)
    for i in range (40):	# sprawdzanie, czy któryś z przeciwników nie dostał pociskiem o ile pocisk nie trafił jeszcze innego celu
      if Statek.get_distance(pocisk[0],przeciwnicy[i]) <= 4+Statek.get_range(przeciwnicy[i]) and Statek.get_strenght(pocisk[0])!=0 and Statek.get_strenght(przeciwnicy[i])>2:
        Statek.get_buff(przeciwnicy[i],-1,0)	# osłabiamy przeciwnika(-1 siły)
        kolor[i] -= 25.5	# zmieniamy kolor przeciwnika
        rysowanie_pocisku(255)	# zamazywujemy pocisk
        Statek.move(pocisk[0],1000000,1000000)	# wysyłamy pocisk tak daleko jak to tylko możliwe (wystrzelenie kolejnego pocisku nadpisze poprzedni)
    zdrowie = pygame.Surface((800,20))	# tworzymy pasek zdrowia
    d=int(255*(s-Statek.get_strenght(player))/s)
    e=int(Statek.get_strenght(player)*255/s)
    zdrowie.fill((d,e,0))	# wypełniamy pasek zdrowia odpowiednim kolorem (zielony-dobrze, czerowny-źle)
    plansza.blit(zdrowie,(0,0))	# aplikujemy pasek zdrowia na planszy
    pygame.draw.circle(plansza,(0,255,255),Statek.zwroc_pozycje(player),int(Statek.get_range(player)))	# zamazywujemy poprzednią pozycję gracza
    Statek.pistolet(player,m,n,mn,nm)	# przesuwamy gracza
    wyjście=Statek.zwroc_pozycje(player)	# zapisujemy współrzędne gracza, aby sprawdzić, czy nie wyszedł poza dozwolony obszar
    if wyjście[0]-Statek.get_range(player)<0 or wyjście[0]+Statek.get_range(player)>800 or wyjście[1]-Statek.get_range(player)<0 or wyjście[1]+Statek.get_range(player)>800:
      porazka()
    przeciwnik=[]	# zmienna, którą zapełniamy 'żywymi przeciwnikami'
    reset=[]	# zmienna, która zapełniamy niezdobytymi monetami
    for i in range (200):
        if Pieniadze.istnienie(monety[i]):	# jeżeli jeszcze nie zdobyliśmy monety:
          pygame.draw.circle(plansza,(255,255,0),Pieniadze.zwroc_pozycje(monety[i]),3)
          reset.append(1)
          if zarobek(player,monety[i]):	# zwiększamy kasę o 1 i nie bierzemy pod uwagę kolejnej monety o ile na nią wpłyneliśmy 
            Pieniadze.anihilacja(monety[i])
            kasa+=1
    pygame.draw.circle(plansza,(0,0,255),Statek.zwroc_pozycje(player),int(Statek.get_range(player))) # rysujemy gracza
    for i in range(40):	# sprawdzamy, czy nie walczymy z którymś z przeciwników
      Statek.atak(player, przeciwnicy[i])	# realizujemy walkę
      if Statek.get_strenght(przeciwnicy[i])>0:	# jeżeli przeciwnik dalej 'żyje':
        przeciwnik.append(1)	# dodajemy do 'przeciwnik' jedynkę
    for i in range (40):	# rysujemy wszystkimch przeciwników i 1 z nich przesówamy:
      if Statek.get_strenght(przeciwnicy[i])>0 and Statek.get_strenght(przeciwnicy[j])>0:
        if i <= 39: rysowanie_przeciwnik(i,kolor[i],0)	# rysujemy przeciwnika statycznego
        rysowanie_przeciwnik(j,0,255)		# zamazujemy przeciwnika aktywnego
        g,h=random.randint(-2,2),random.randint(-2,2)
        Statek.move(przeciwnicy[j],g,h)	# przesuwamy przeciwnika aktywnego
        wyjście2=Statek.zwroc_pozycje(przeciwnicy[j])	# zapisujemy współrzędne przeciwnika, aby sprawdzić, czy nie wyszedł poza dozwolony obszar
        if wyjście2[0]<0 or wyjście2[0]>800 or wyjście2[1]<0 or wyjście2[1]>800:	# jeżeli wyszedł:
          Statek.move(przeciwnicy[j],-1*g,-1*h)	# cofnij go
        rysowanie_przeciwnik(j,kolor[j],0)	# narysuj go ponownie
        pygame.display.flip()	# updatowanie całego obrazu(gry)
    if 2 <= Statek.get_strenght(player) <= limit-2.5:				# jeżeli jesteśmy bardzo osłabieni to leczymy się oraz lekko zwiększa się nasz zasięg
      Statek.get_buff(player, Statek.get_strenght(player)/l, zas/2)
    elif limit-2.5 <= Statek.get_strenght(player) <= limit:			# jeżeli jesteśmy lekko osłabieni to leczymy się oraz szybko zwiększa się nasz zasięg
      Statek.get_buff(player, Statek.get_strenght(player)/l, zas)
    else: Statek.get_buff(player, 0, zas)							# jeżeli jesteśmy pełni sił szybko zwieksza sie nasz zasięg
    kasa+=(1-kasa/50)/100
    if not 1 in reset or not 1 in przeciwnik:	# jeżeli zostały zdobyte wszystkie monety lub wszyscy wrogowie zostali pokonani-wygraliśmy
      print("ZWYCIĘSTWO")
      time.sleep(2)
      sys.exit(0)
