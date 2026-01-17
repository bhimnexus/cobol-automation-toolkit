       IDENTIFICATION DIVISION.
       PROGRAM-ID. PAYROLL1.

       DATA DIVISION.
       WORKING-STORAGE SECTION.

       01  EMPLOYEE-RECORD.
           05 EMP-ID        PIC X(10).
           05 EMP-NAME      PIC X(30).
           05 AGE           PIC 9(3).
           05 SALARY        PIC S9(7)V99 COMP-3.
           05 BONUS         PIC S9(5) COMP.
