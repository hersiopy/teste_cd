/*
[QSF] RESPOSTA QUEBRA BACEN
[QSF] SOLICITA��O DE QUEBRA BACEN
*/
SELECT
C.NUMCOOPERATIVA
FROM COOPERATIVA C
INNER JOIN VIW_BANCO_SERVIDOR W ON C.NUMCOOPERATIVA = W.NUMCOOPERATIVA
WHERE ( NUMPAC = 0
AND CODTIPOINSTITUICAO = 3
AND NUMCOOPPAI NOT IN (9999)
AND DATAIMPLANTACAOSICOOB <= GETDATE()
AND C.NUMCOOPERATIVA NOT IN (3350,4440,4025,4156,4202,4363,4401,4472,4479,4503,4506,4566,
4615,5142,9806,4524,3321,5002,3354, 3061,4378,5059,4050,4333,3279,4547,
3340,3355,2015,2001,4291,4278,3210,3200,4554,4545,4508,4501,4488,4485,
4339,1001,5082,4595,4578,4203,4361,4348,4183,3168,3285,3269,3062,3019,3174,
4276,4442,3315,4064,3121,3060,3020,4439,4587,3064,4126,
3356,5014,4001,5024,3339,3043,4280,4236,3271,3125,3233,4491,4539,3288,
4491,4431,4539,5631,4431,4539,4491,5631))
OR ( C.NUMCOOPERATIVA = 1 AND NUMPAC = 0 )
ORDER BY IDINSTITUICAO