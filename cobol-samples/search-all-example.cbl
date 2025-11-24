       IDENTIFICATION DIVISION.
       PROGRAM-ID. SEARCHALLDEMO.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 WS-TABLE.
          05 WS-NUM OCCURS 10 TIMES
             ASCENDING KEY IS WS-NUM
             INDEXED BY IDX.
             10 WS-VALUE PIC 9(2).

       01 WS-SEARCH-VALUE PIC 9(2) VALUE 45.
       01 WS-FOUND         PIC X VALUE 'N'.

       PROCEDURE DIVISION.
           MOVE 10 TO WS-VALUE(1)
           MOVE 20 TO WS-VALUE(2)
           MOVE 30 TO WS-VALUE(3)
           MOVE 45 TO WS-VALUE(4)
           MOVE 50 TO WS-VALUE(5).

           SEARCH ALL WS-NUM
              AT END
                 DISPLAY "VALUE NOT FOUND"
              WHEN WS-VALUE(IDX) = WS-SEARCH-VALUE
                 MOVE 'Y' TO WS-FOUND
           END-SEARCH.

           IF WS-FOUND = 'Y'
              DISPLAY "VALUE FOUND AT POSITION: " IDX
           END-IF.

           STOP RUN.

