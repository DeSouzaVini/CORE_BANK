USE master;
GO

-- BACKUP FULL



BACKUP DATABASE [CORE_BANK] 
TO DISK = N'C:\SQLData\CORE_BANK_FULL.bak' 
WITH 
    FORMAT,              
    MEDIANAME = 'SQLServerBackups', 
    NAME = 'Full Backup do CORE_BANK', 
    COMPRESSION,         
    STATS = 10,          
    DESCRIPTION = 'Backup completo após carga de dados via Python';
GO

--BACKUP DE LOGS

BACKUP LOG [CORE_BANK] 
TO DISK = N'C:\SQLData\CORE_BANK_LOG.trn' 
WITH COMPRESSION, STATS = 10;
GO