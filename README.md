# AgenticAI

Generativ AI

X             Y                 max userquery -> 800
user query   response

Vectorization -> [1 2 3 4 5] -> What is my name?
              -> [1,2,3,6,5] -> what is my father name?
User query -> LLM -> Response (Based on the training data)

what is date today? 10 aug 2024 xxxxxx

Problem: How can llm respond based on my data?

-----------------RAG (RETRIEVAL AUGMENTED GENERATION):--------------------
DATA -> FORMAT -> VECTORS -> CONTAINER -> VECTORESTORE
DATA -> 500 -> VECTORS -> CONTAINER -> VECTORESTORE

USER QUERY -> VECTOR -> VECTORESTORE -> RELEVANT VECTORE CHUNKS -> STRING(CONTEXT) -> (USERQUERY+CONTEXT+INSTRUCTION)(INPUT) -> LLM -> RESPONSE

INSTURCTION -> THIS IS THE USER QUERY , AND CONTEXT , RESPONSE ACCRUATELY


MATRIX - MATRIX -> COSINE SIMILARITY-> 0.1-1 ->

###THIS IS CONTEXT
TAIMOOOR KHAN IS A GOOD BOY HE IS LIVING IN UNIT#2

###THIS IS USER QUERY
WHO IS TAIMOOR KHAN?

NOW RESPONSE ACCORDING TO THE CONTEXT