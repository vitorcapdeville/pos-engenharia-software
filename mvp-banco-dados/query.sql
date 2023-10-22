select 
    t1.matriculaId,
    t2.dataNascimento,
    t1.dataAssinatura,
    t1.dataInicioVigencia,
    t1.prazoCobertura,
    t1.prazoPagamento,
    t4.nome as tabua,
    t6.juros
from matricula t1
    inner join segurado t2 on t2.cpf = t1.cpfSegurado
    left join produtotabua t3 on t1.produtoId = t3.produtoId
    and t3.sexo = t2.sexo
    left join tabua t4 on t3.tabuaId = t4.tabuaId
    left join produtoprazo t7 on t1.produtoId = t7.produtoId
    and t1.prazoCobertura = t7.prazoCobertura
    and t1.prazoPagamento = t7.prazoPagamento
    left join juros t6 on t7.jurosId = t6.jurosId
where matriculaId = 1;
