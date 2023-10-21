select 
    matriculaId,
    dataNascimento,
    dataAssinatura,
    dataInicioVigencia,
    prazoCobertura,
    t1.prazoPagamento,
    t4.nome as tabua,
    t6.juros
from matricula t1
inner join segurado t2 on t2.cpf = t1.cpfSegurado
inner join produtotabua t3 on t1.produtoId = t3.produtoId and t3.sexo = t2.sexo
inner join tabua t4 on t3.tabuaId = t4.tabuaId
inner join produtojuros t5 on t1.produtoId = t5.produtoId and t1.prazoPagamento = t5.prazoPagamento
inner join juros t6 on t5.jurosId = t6.jurosId
where matriculaId = 1