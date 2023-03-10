/****** Script for SelectTopNRows command from SSMS  ******/
SELECT a.Lop, a.Startnr, a.StartMetode, a.Distanse, a.Heste_navn,a.Bane, a.Dato, a.Id_nr, FormfaktorTotal

  FROM [Trav].[dbo].[StartLister] a, [Trav].[dbo].[BeregnetForm] b
  Where a.Id_nr is not null
  and   a.id_nr = b.id_nr
  and   a.Dato  = b.Dato 
  and   a.Lop   =  b.lop 
  and a.Dato > '2020-01-01'