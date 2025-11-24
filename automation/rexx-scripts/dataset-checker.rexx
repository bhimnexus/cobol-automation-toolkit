/* REXX */
/*------------------------------------------------------------------*/
/*   REXX UTILITY: CHECK IF A DATASET EXISTS ON MAINFRAME            */
/*   AUTHOR: BHIM SINGH (bhimnexus)                                */
/*   DESCRIPTION:                                                   */
/*     - Accepts dataset name as input                              */
/*     - Checks whether the dataset exists                          */
/*     - Displays catalog information                               */
/*------------------------------------------------------------------*/

ARG DSN

IF DSN = "" THEN DO
   SAY "USAGE:  EXEC 'member' 'dataset.name'"
   EXIT 8
END

ADDRESS TSO
"LISTCAT ENTRIES('"DSN"')" "OUTTEMP(REXXOUT)"

IF RC = 0 THEN DO
   SAY "----------------------------------------"
   SAY " DATASET FOUND: " DSN
   SAY "----------------------------------------"
   ADDRESS TSO "PRINTDS DATASET(REXXOUT)"
END
ELSE DO
   SAY "----------------------------------------"
   SAY " DATASET NOT FOUND: " DSN
   SAY " RETURN CODE : " RC
   SAY "----------------------------------------"
END

EXIT RC
