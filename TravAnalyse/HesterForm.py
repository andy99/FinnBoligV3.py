import pypyodbc
# from FunkFakta import FunkFakta
# from Funkvinner import Funkvinner
# from Funktrippel import Funktrippel
# global prosentgallop
utdata = 0
con = pypyodbc.connect
con = pypyodbc.connect('Driver={SQL Server};' 'Server=DESKTOP-0CMQN56;''Database=Trav;''user=Gunnar;' 'Pwd=gunnar')
# print(Lastedato.DatoKlasse)
if con:
    print("ja vi har forbindelse")
   
SQL = '''\
Select distinct b.Lop, b.startnr, a.startnr as dagensstartnr ,a.Inntjent, Hestenavn, b.Distanse as tidligereDistanse, KmTid,Premie, b.Kusk as tidligereKusk, plassering, b.Dato, Galoppprosent,
 a.Kusk as dagenkusk, b.id_nr, odds, a.dato, a.lop, b.Vinnerprosent, b.Trippelprosent

  FROM [Trav].[dbo].[StartListerSorlandet] a,
        [Trav].[dbo].[Fakta_lop]  b
  where a.Lop = 1
   and  a.id_nr = b.id_nr
 and  Plassering < '4' and Plassering > '0'
  and a.Dato = '2018-06-24'
  and b.Dato > '2018-05-02'
  order by Galoppprosent

'''     
cursor = con.cursor()
cursor.execute(SQL)
# prosentgallop = 0
#dato = cursor
#cursor.next()

for a in cursor:
#     print(a[0], a[1], a[2])
    
    Lop = a[0]
    Startnr      = a[1] 
    Dagenstartnr     = a[2]
    Inntjent = a[3]
#     print(Hestenummer,"verdi til hestenummer i Hoved Program")
#     FunksjonlesResultat(id_nr)
#     prosentgallop=FunkFakta(Hestenummer)
#     prosentvinner=Funkvinner(Hestenummer)
#     prosenttrippel=Funktrippel(Hestenummer)
    print( Lop,Startnr,"Hoved program Finner hester i form" )
    with open('HesterForm.txt', 'a') as f:
        f.write("%.0f;%.0f;%.0f;%s" % \
            ( Lop,Startnr,Dagenstartnr, Inntjent))
        f.write('\n')

cursor.close() 