       IDENTIFICATION DIVISION.
       PROGRAM-ID. DB2FETCHDEMO.

       ENVIRONMENT DIVISION.

       DATA DIVISION.
       WORKING-STORAGE SECTION.

       EXEC SQL INCLUDE SQLCA END-EXEC.

       01 WS-EMP-ROW.
          05 EMP-ID        PIC 9(5).
          05 EMP-NAME      PIC X(30).
          05 EMP-DEPT      PIC X(10).

       EXEC SQL
            DECLARE EMP-CURSOR CURSOR FOR
            SELECT EMP_ID, EMP_NAME, EMP_DEPT
              FROM EMPLOYEE
              ORDER BY EMP_ID
       END-EXEC.

       PROCEDURE DIVISION.

           DISPLAY "=== DB2 FETCH LOOP DEMO ===".

           EXEC SQL
                OPEN EMP-CURSOR
           END-EXEC.

           IF SQLCODE NOT = 0
              DISPLAY "OPEN FAILED. SQLCODE: " SQLCODE
              STOP RUN
           END-IF.

       FETCH-LOOP.
           EXEC SQL
                FETCH EMP-CURSOR INTO :EMP-ID, :EMP-NAME, :EMP-DEPT
           END-EXEC.

           IF SQLCODE = 100
              DISPLAY "END OF TABLE REACHED."
              GO TO CLOSE-CURSOR
           END-IF.

           IF SQLCODE NOT = 0
              DISPLAY "FETCH FAILED. SQLCODE: " SQLCODE
              GO TO CLOSE-CURSOR
           END-IF.

           DISPLAY "EMP-ID  : " EMP-ID.
           DISPLAY "EMP-NAME: " EMP-NAME.
           DISPLAY "EMP-DEPT: " EMP-DEPT.
           DISPLAY "-----------------------------".

           GO TO FETCH-LOOP.

       CLOSE-CURSOR.
           EXEC SQL
                CLOSE EMP-CURSOR
           END-EXEC.

           IF SQLCODE NOT = 0
              DISPLAY "CLOSE FAILED. SQLCODE: " SQLCODE
           END-IF.

           STOP RUN.
