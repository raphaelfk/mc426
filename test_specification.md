# Especificação de Testes - MC426

## Funcionalidades Críticas e Casos de Teste

### 1. Autenticação de Usuário

#### Entradas
- Email
- Senha
- Nome (para registro)
- Confirmação de senha (para registro)

#### Resultados Esperados
- Login/Registro bem-sucedido: Redirecionamento para dashboard
- Login/Registro mal-sucedido: Mensagem de erro

#### Restrições/Requisitos
- Email válido
- Senha válida
- Email único no sistema
- Usuário não pode estar logado para registro

#### Casos de Teste
1. **CT-001: Login com credenciais válidas**
   - Pré-condição: Usuário registrado no sistema
   - Entrada: Email e senha válidos
   - Resultado esperado: Redirecionamento para dashboard
   - Status: Implementado

2. **CT-002: Login com credenciais inválidas**
   - Pré-condição: Usuário registrado no sistema
   - Entrada: Email válido, senha incorreta
   - Resultado esperado: Mensagem "Credenciais inválidas"
   - Status: Implementado

3. **CT-003: Registro com email já existente**
   - Pré-condição: Email já cadastrado no sistema
   - Entrada: Dados de registro com email existente
   - Resultado esperado: Mensagem "Email já cadastrado"
   - Status: Implementado

### 2. Criação de Rota

#### Entradas
- Ponto de partida
- Ponto de chegada
- Data e hora
- Tipo de atividade (caminhada/ciclismo)
- Nível de dificuldade
- Descrição opcional

#### Resultados Esperados
- Rota criada: Redirecionamento para visualização da rota
- Erro na criação: Mensagem de erro específica

#### Restrições/Requisitos
- Usuário deve estar logado
- Pontos de partida e chegada não podem ser iguais
- Data e hora devem ser futuras
- Local válido

#### Casos de Teste
1. **CT-004: Criação de rota válida**
   - Pré-condição: Usuário logado
   - Entrada: Dados completos de rota válida
   - Resultado esperado: Rota criada e redirecionamento
   - Status: Em desenvolvimento

2. **CT-005: Criação de rota com data passada**
   - Pré-condição: Usuário logado
   - Entrada: Data e hora no passado
   - Resultado esperado: Mensagem "Data deve ser futura"
   - Status: Em desenvolvimento

### 3. Sistema de Matching

#### Entradas
- Rota do usuário
- Preferências de matching

#### Resultados Esperados
- Match encontrado: Lista de usuários compatíveis
- Sem matches: Mensagem apropriada

#### Restrições/Requisitos
- Usuário deve ter rota criada
- Preferências devem ser configuradas
- Rotas compatíveis

#### Casos de Teste
1. **CT-006: Encontrar matches compatíveis**
   - Pré-condição: Usuário com rota e preferências configuradas
   - Entrada: Busca por matches
   - Resultado esperado: Lista de usuários compatíveis
   - Status: Não implementado

2. **CT-007: Sem matches disponíveis**
   - Pré-condição: Usuário com rota e preferências configuradas
   - Entrada: Busca por matches
   - Resultado esperado: Mensagem "Nenhum match encontrado"
   - Status: Não implementado

### 4. Sistema de Feedback

#### Entradas
- Avaliação (1-5 estrelas)
- Comentário

#### Resultados Esperados
- Feedback registrado: Confirmação de sucesso
- Erro no registro: Mensagem de erro
- Atualização da média de avaliações

#### Restrições/Requisitos
- Usuário deve estar logado
- Usuário só pode avaliar após atividade concluída
- Uma avaliação por par de usuários

#### Casos de Teste
1. **CT-008: Enviar feedback válido**
   - Pré-condição: Usuário logado e atividade concluída
   - Entrada: Avaliação e comentário
   - Resultado esperado: Feedback registrado
   - Status: Não implementado

2. **CT-009: Tentativa de avaliação duplicada**
   - Pré-condição: Usuário já avaliou o parceiro
   - Entrada: Nova avaliação
   - Resultado esperado: Mensagem "Avaliação já realizada"
   - Status: Não implementado

## Instruções para Execução dos Testes

1. Para funcionalidades implementadas:
   - Execute os testes automatizados
   - Verifique a cobertura de código
   - Documente bugs encontrados

2. Para funcionalidades em desenvolvimento:
   - Use os casos de teste como guia
   - Implemente testes unitários
   - Valide requisitos antes da implementação

3. Para funcionalidades não implementadas:
   - Mantenha os casos de teste atualizados
   - Use como referência para planejamento
   - Priorize implementação baseada em criticidade 