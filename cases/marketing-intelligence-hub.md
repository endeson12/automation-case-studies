# Marketing Intelligence Hub

## Problema

Conhecimento obtido de vídeos, documentos e experiências de campanhas costuma ficar disperso, sem proveniência, critérios de uso ou histórico de revisão.

## Solução

Painel interno em Python/Flask que transforma fontes autorizadas em uma biblioteca pesquisável de regras, hipóteses, experimentos e aprendizados. O sistema separa fatos, inferências e testes sugeridos.

## Automações

- ingestão validada de JSONL e Markdown;
- normalização de URLs e rejeição de duplicidades;
- checksums e UPSERT idempotente;
- busca textual e opção de busca híbrida com fallback;
- trilha de auditoria com redação de campos sensíveis;
- planejamento de experimentos e fila de revisão;
- migrações Supabase/PostgreSQL com RLS deny-by-default.

## Segurança e supervisão

Anexos são privados e validados por assinatura/tipo. Chaves ficam fora do navegador e do Git. O sistema não publica campanhas, não altera orçamento e não executa gastos: produz diagnósticos e rascunhos sujeitos a aprovação humana.

## Publicação

O código permanece privado porque contém contexto operacional. Este estudo apresenta somente arquitetura e controles sanitizados; não expõe contas, campanhas, credenciais ou dados empresariais.
