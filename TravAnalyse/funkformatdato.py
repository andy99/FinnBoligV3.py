coding='utf-8' 
def funkformatdato(resultatdato):
    #henter ut aar
    Dato = resultatdato
    datolengde = len(resultatdato)
#     print(datolengde,"Dato lengde")
    aar = Dato[17:21]
    ukeDag,ddmmmyyyy = Dato.split(',')
#     print(UkeDag,"Dag")
    print(ddmmmyyyy,"ddmmmyyyy")
    dag,mndyyyy = ddmmmyyyy.split('.')
    nydag = dag.strip()
    utdag = "01"
    utdag = nydag
#    Finndagnr(utdag)
#     mnd,aar=mndyyyy.split(' ')
    print(utdag,"Dag  er")
    if nydag == '1':
        nydagnr = '01'
    elif nydag == '2':
        nydagnr = '02'
    elif nydag == '3':
        nydagnr = '03'
    elif nydag == '4':
        nydagnr = '04'
    elif nydag == '5':
        nydagnr = '05'
    elif nydag == '6':
        nydagnr = '06'
    elif nydag == '7':
        nydagnr = '07'
    elif nydag == '8':
        nydagnr = '08'
    elif nydag == '9':
        nydagnr = '09'
    else:
        nydagnr = nydag                            
            

                             
    print(mndyyyy,"mnd ar er")
    aar=mndyyyy[5:9]
    mnd =mndyyyy[1:4]
    if mnd == 'sep':
        aar=mndyyyy[6:10]
    
    print(mnd,"Maned er")
    print(aar,"Verdi aar")
    if mnd == 'jan':
        mndnr = '01'
    elif mnd == 'feb':
        mndnr = '02' 
    elif mnd == 'mar':
        mndnr = '03'    
    elif mnd == 'apr':
        mndnr = '04' 
    elif mnd == 'mai':
        mndnr = '05'
    elif mnd == 'jun':
        mndnr = '06' 
    elif mnd == 'jul':
        mndnr = '07'  
    elif mnd == 'aug':
        mndnr = '08' 
    elif mnd == 'sep':
        mndnr = '09' 
    elif mnd == 'okt':
        mndnr = '10' 
    elif mnd == 'nov':
        mndnr = '11'  
    elif mnd == 'des':
        mndnr = '12'   
    else:
        print("Feil i manedsnr") 
        
        
    print(mndnr,"Maanedsnr")
    resdato= aar + '-' + mndnr +'-' + nydagnr
    print(resdato,"resdato")
    return resdato