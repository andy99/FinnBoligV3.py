import pypyodbc
# from HovedProgramOppdaterHest import HeleNavn, idnroppdatere
con = pypyodbc.connect
con = pypyodbc.connect('Driver={SQL Server};' 'Server=DESKTOP-0CMQN56;''Database=Trav;''user=Gunnar;' 'Pwd=gunnar')
print('Er i sub proram oppdater Hest')
def FunkoppdaterHest(id_nr,HeleNavn):
    idnroppdatere = id_nr
    if con:
        print("ja vi elsker dette landet og har forbindelse")
    SQL = '''\
       Update
        [Trav].[dbo].[AlleHester2] 
        set navn = ?
       Where Id_nr = ?

      '''    
         
    cursor = con.cursor()
    cursor.execute(SQL,(HeleNavn,idnroppdatere))
