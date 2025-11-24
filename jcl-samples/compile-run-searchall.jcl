////SEARCHALL JOB (ACCT100),'BHIM SINGH',
//// MSGCLASS=H,MSGLEVEL=(1,1),NOTIFY=&SYSUID
//* ---------------------------------------------------------------
//*  COMPILE, LINK EDIT AND RUN THE COBOL PROGRAM SEARCHALLDEMO
//* ---------------------------------------------------------------
//COBOL   EXEC IGYWCL
//COBOL.SYSIN DD *
       IDENTIFICATION DIVISION.
       PROGRAM-ID. SEARCHALLDEMO.

       ENVIRONMENT DIVISION.
       DATA DIVISION.

       WORKING-STORAGE SECTION.
       01 WS-TABLE.
          05 WS-NUM OCCURS 10 TIMES
             ASCENDING KEY IS WS-VALUE
             INDEXED BY IDX.
             10 WS-VALUE PIC 9(2).

       01 WS-SEARCH-VALUE PIC 9(2) VALUE 45.
       01 WS-FOUND         PIC X VALUE 'N'.

       PROCEDURE DIVISION.
           DISPLAY "=== SEARCH ALL DEMO ===".

           MOVE 10 TO WS-VALUE(1)
           MOVE 20 TO WS-VALUE(2)
           MOVE 30 TO WS-VALUE(3)
           MOVE 45 TO WS-VALUE(4)
           MOVE 50 TO WS-VALUE(5).

           SEARCH ALL WS-NUM
              AT END
                 DISPLAY "VALUE NOT FOUND."
              WHEN WS-VALUE(IDX) = WS-SEARCH-VALUE
                 MOVE 'Y' TO WS-FOUND
           END-SEARCH.

           IF WS-FOUND = 'Y'
              DISPLAY "VALUE FOUND AT POSITION: " IDX
           ELSE
              DISPLAY "SEARCH FAILED."
           END-IF.

           STOP RUN.
/*
//LKED.SYSLMOD DD DISP=SHR,DSN=USER.LOAD(SEARCHALLDEMO)
//GO     EXEC PGM=SEARCHALLDEMO
//STEPLIB DD DISP=SHR,DSN=USER.LOAD
//SYSOUT  DD SYSOUT=*
//
