
<!-- .github/copilot-instructions.md
     Propósito: orientação curta e prática para agentes de IA trabalharem neste repositório Django.
-->

# Guia rápido para agentes de IA

Este repositório é um site Django simples (um projeto, uma app). O objetivo: fornecer fatos acionáveis para um agente ser produtivo rapidamente.

## Visão geral
- Raiz do projeto: `manage.py`; configurações em `jj_investimento/`.
- App única: `page_app/` — contém views, templates, assets estáticos e rotas.
- Banco de dados SQLite incluído: `db.sqlite3` (sem configuração externa).

Estrutura explicada: site server-rendered; UI organizada em templates dentro de `page_app/templates/`. As rotas do app são incluídas em `jj_investimento/urls.py` via `include('page_app.urls')`.

## Arquivos-chave e exemplos concretos
- `manage.py` — entrypoint Django (usar para runserver, migrate, test).
- `jj_investimento/settings.py` — verifique `INSTALLED_APPS`, `TEMPLATES` e `STATIC` antes de mudar comportamento.
- `jj_investimento/urls.py` — inclui `page_app.urls` na raiz.
- `page_app/urls.py` — rotas do app. Exemplos:
  - `path('', index)` → `page_app.views.index` (home)
  - `path('contato/', contato)` → `page_app.views.contato`
- `page_app/views.py` — views simples que renderizam templates:
  - `index(request)` renderiza `page_app/partial/home.html`
  - `contato(request)` renderiza `page_app/partial/contato.html`
- Templates importantes: `page_app/templates/page_app/partial/` e `.../global/` (partials como header/footer).
- Assets estáticos: `page_app/static/page_app/img/` (imagens usadas pelo template).

## Como executar e testar (comandos concretos)
- Instalar Django (não há `requirements.txt`): `pip install django` (considere pedir versão se precisar de pin). 
- Subir o servidor de desenvolvimento: `python manage.py runserver`.
- Aplicar migrações: `python manage.py migrate`.
- Criar superuser (se necessário): `python manage.py createsuperuser`.
- Executar testes da app: `python manage.py test page_app` (ou `python manage.py test`).

## Convenções e padrões observados neste projeto
- Foco em uma única app: alterações geralmente em `page_app/` (views, templates, urls, static).
- Organização de templates por partials: editar `page_app/templates/page_app/partial/` e reutilizar com `{% include %}`.
- Views são função (function-based), sem `name` nas URLs — se adicionar nomes (`name=`), mantenha consistência com as views.
- Texto e README em português — preserve a localização.

## Integrações e dependências externas
- Não há serviços externos, chaves de API ou integrações externas detectadas.
- Banco de dados local: `db.sqlite3`. Mudanças em modelos exigem migrações e atualização do arquivo incluído.

## Guia prático para editar (faça isto primeiro)
1. Abra `jj_investimento/urls.py`, `page_app/urls.py` e `page_app/views.py` para localizar a rota e o template afetado.
2. Prefira editar templates em `page_app/templates/page_app/partial/`; ao adicionar imagens/CSS, coloque em `page_app/static/page_app/`.
3. Após alterar modelos, rode: `python manage.py makemigrations` e `python manage.py migrate`.
4. Execute `python manage.py test page_app` para validar alterações de comportamento.

## O que NÃO existe / perguntas úteis ao mantenedor
- Não há `requirements.txt` ou arquivos de versão fixados (peça versão de Django se necessário).
- Não há CI/CD, Dockerfile ou configurações de produção neste repositório.

## Checklist rápido para PRs gerados por IA
- Preserve textos em português a menos que solicitado o contrário.
- Prefira modificar partials em vez de duplicar header/footer.
- Ao adicionar endpoints, acrescente `name=` às rotas para facilitar reverse lookup em templates.
- Inclua migrações no PR se modelos foram alterados; execute testes locais antes de abrir PR.

Se quiser, eu adapto este arquivo para português mais formal, adiciono exemplos passo-a-passo (ex: criar nova view + rota + template) ou crio um `requirements.txt` com uma versão sugerida do Django — diga o que prefere.

