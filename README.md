ETL PIPELINE FOR FURNITURE SEMANTIC SEARCH TOOL
by Elias :-)


END GOAL: 

-full working etl pipeline that fetches data 
from furnitur apis embeds semantic products descriptions
pipe to simple CRUD SITE

-end user searches for furniture returns results
similar in semantic meaning in a doom scroll content like way


CURRENT UPDATE - 2026 - 01 - 16
simple pipeline built fetches TEST data from a csv 
-normalizes the data, 
-chunks product description 
-scores chunks for semantic meaning returns highest score


WHAT TO DO NEXT:
-IMPLEMENT FAISS FOR QUERING VECTORS
-STORE VECTORS IN POSTGRES
-TEST FIRST SEMANTIC SEARCH USING COSINESIMILARITY

