import pypyodbc
con = pypyodbc.connect
def Beregnerform(lop):
    con = pypyodbc.connect('Driver={SQL Server};' 'Server=DESKTOP-0CMQN56;''Database=Trav;''user=Gunnar;' 'Pwd=gunnar')
# print(Lastedato.DatoKlasse)
    if con:        
        print("forbindelse")
#         lopnr = [lop]

#Finner antall lop
    lopnr = [lop]
    SQL = '''\
        Select distinct a.Lop, a.startnr as dagensstartnr ,a.Inntjent, Hestenavn, Galoppprosent,
        a.Kusk as dagenkusk, b.id_nr, a.dato, b.Vinnerprosent, b.Trippelprosent as trippelprosent

       FROM [Trav].[dbo].[StartListerForus] a,
        [Trav].[dbo].[Fakta_lop]  b
  where a.Lop = ?      
    and  a.id_nr = b.id_nr
    and  Plassering < '5' and Plassering > '0'
    and a.Dato = '2018-07-31'
    and b.Dato > '2015-01-01'
     

  '''  
    cursor = con.cursor()
    cursor.execute(SQL,(lopnr))
    
    for a in cursor:  
             
#         print(a[0])    
        lopstartliste = a[0]
        startnr = a[1]
        dagenstartnr = a[2]
        Inntjent = a[3]
        Hestenavn = a[4]
                
        print(lopstartliste,"Lopnr i sub program Beregner form")
        print(startnr ,"startnr  i sub program Beregner form")
        print(dagenstartnr ,"dagenstartnr  i sub program Beregner form")
        print(Inntjent ,"Inntjent  i sub program Beregner form")
        print(Hestenavn ,"Inntjent  i sub program Beregner form")
        
   
#     print(lop,"viser alle lop")
    cursor.close() 