**ELICITAÇÃO DE REQUISITOS** 

Primeiramente, foi realizado um benchmarking de aplicativos e plataformas com usabilidade parecida do que tínhamos em mente, procurando nos guiar através das funcionalidades e requisitos básicos para o funcionamento do nosso aplicativo. 

**1º Passo: Benchmarking** 

Foram analisados diferentes tipos de aplicativos que fazem parte do nosso escopo: 

- Apps de roteamento como Komoot e Bikemap; 
  - Essas plataformas oferecem **roteamento personalizado para ciclistas**, levando em conta tipos de terreno, elevação, preferências de vias e níveis de habilidade. Elas usam dados colaborativos e mapas detalhados, gerando rotas mais seguras e agradáveis, muitas vezes ignoradas por apps de navegação comuns. 
- Soluções focadas em segurança, como dashcam.bike e OurStreets, que permitem reportar trechos perigosos; 
  - Permitem que usuários reportem **situações de risco em tempo real**, como direção agressiva, má iluminação ou buracos, criando um **banco de dados colaborativo de perigos urbanos**. Isso capacita ciclistas e pedestres a evitarem áreas problemáticas e pressiona autoridades a tomarem providências. 
- Plataformas de match social, como WalkClub e WalkPal; 
  - Esses serviços conectam pessoas com interesses semelhantes para caminharem juntas com base em **horário, local e ritmo**, promovendo **socialização, segurança e incentivo à atividade física**. O uso de algoritmos de compatibilidade melhora a experiência e reduz barreiras para caminhadas regulares. 
- Apps crowdsourcing de incidentes de trânsito como o Waze; 
  - Waze transforma cada motorista em um sensor, criando um sistema em tempo real de alertas sobre acidentes, congestionamentos, blitz, entre outros. A **inteligência coletiva** permite desviar rotas de forma eficiente e dinâmica. 
- Apps de deslocamento com base em rotas como a Uber. 

○  O Uber utiliza **algoritmos de roteamento em tempo real**, considerando 

trânsito, histórico de demanda e até comportamento dos motoristas, para oferecer o **caminho mais eficiente**. Além disso, o sistema aprende com 

o uso contínuo. 

Foi muito útil para a gente entender o que já existe e onde ainda há espaço para reaproveitamento e inovação. Com esse panorama em mãos, fica claro que podemos criar algo diferente ao misturar essas ideias num só lugar e nos guiar para ter um ponta-pé inicial no brainstorming. 

**2º Passo: Brainstorming** 

Tendo em vista a pesquisa feita e uma noção básica de requisitos para a nossa plataforma, utilizando o Figma (FigJam), utilizamos um quadro branco e post-its para cada um jogar suas ideias e entendermos os requisitos necessário: 

![](figma.jpeg)

Após rounds de 5 minutos para cada um escrever o que vinha em mente, dividimos todos os post-its em subcategorias, de acordo com a finalidade dos requisitos elencados: 

![](figma_2.jpeg)

![](figma_3.jpeg)

**3º Passo: Consolidação e resumo das ideias** 

Por fim, consolidamos e detalhamos os requisitos levantados: 

1. **Requisitos Funcionais**
1. Autenticação e Perfil 
   1. Cadastro/login 
   1. Criar conta via e-mail/senha ou social login (Google/Facebook/Icloud) 
   1. Recuperação de senha por e-mail 
   1. Verificação em múltiplas etapas  
1. Gestão de perfil 
   1. Editar nome, foto, tipo de atividade (bike/caminhada) 
   1. Definir preferências: distância, horários, nível de experiência, visibilidade (público/amigos/privado) 
1. Rotas, Histórico e Offline 
   1. Criação e edição de rotas 
   1. Edição de rotas (integração com o Google Maps para traçar as rotas recomendadas) 
   1. Editar e adicionar POIs - Pontos de Interesse (água, oficina, farmácia, delegacia, etc.) 
   1. Editar/excluir rotas salvas 
1. Acompanhamento em tempo real 
   1. Localização via GPS 
   1. Botão de SOS: compartilha localização aos contatos de confiança 
   1. Check-in/check-out automático para contato de segurança 
1. Histórico e estatísticas 
   1. Armazenar trajeto, data, distância, tempo e elevação 
   1. Exibir camadas de calor (rotas populares, áreas de risco) 
   1. Mapas offline: download de regiões e sincronização posterior 
1. Busca e navegação 
   1. Pesquisar rotas públicas por localização, distância, avaliação 
1. Compartilhamento social 
   1. Compartilhar rota via app, WhatsApp, Instagram, Facebook 
1. Match  
- Algoritmo de match 
- Sugerir parceiros por rota, horário, velocidade; filtros por gênero e avaliação 
9. Convites e agendamento 
   1. Enviar/aceitar convites (push/e-mail) e agendar saídas únicas ou recorrentes 
9. Grupos  
   1. Criar grupos de rota (bike ou a pé) públicos ou privados  
9. Interações Sociais & Gamificação 
   1. Feed de atividades 
   1. Linha do tempo: conclusões de rotas, reports de trechos, badges 
9. Sistema de conquistas 
   1. Medalhas por km pedalados, matches realizados, reports úteis 
9. Feedback & Segurança 
   1. Avaliação de parceiros (tanto nota quanto comentários - destacar incidentes relacionados ao parceiro) 
   1. Estrelas + comentários pós-atividade 
9. Report de incidentes 
   1. Marcar locais inseguros ou infra estrutura ruim com foto e descrição 
   1. Exibir avisos em tempo real sobre problemas relatados 
9. Bloqueio de usuários 
   1. Bloquear parceiros com avaliação abaixo de limiar 
9. Comunicação & Integrações 
   1. Chat privado (futuro) 
   1. Mensagens 1:1 entre usuários que deram match 
9. Notificações 
   1. Push/e-mail para convites, mensagens, avisos de risco 
9. Integração externa 
   1. Sincronizar/importar atividades de Strava, Garmin Connect, Apple Health 
   1. API REST pública (rotas, usuários, avaliações) 
9. Administração e Auditoria 
- Dashboards e relatórios 
- Métricas de uso (usuários ativos, matches, incidentes) 
20. Moderação de conteúdo 
- Filtrar/remover feedbacks indevidos 
- Logs de auditoria (banimento, exclusões, alterações críticas) 
2. **Requisitos Não Funcionais Externos** 
1. Cumprimento das Normas nacionais 
1. Privacidade 
   1. Coletar dados apenas com consentimento explícito 
   1. Políticas de retenção e anonimização 
1. Interoperabilidade 
- Protocolos padrão: OAuth2 para login social, REST/JSON e OpenAPI para APIs 
3. **Requisitos Não Funcionais do Produto** 
1. Desempenho 
   1. Requisições de API comportando até 1 000 usuários simultâneos (pensando no tamanho da Unicamp e sem pensar na escalabilidade do APP) 
1. Disponibilidade  
   1. Operação contínua 24/7 
1. Usabilidade 
   1. Usuário sem treino completa onboarding+match+início de rota em baixo tempo com facilidade 
1. Compatibilidade  
   1. Suporte a Chrome, Firefox, Edge, Safari (versões atuais); iOS/Android  
1. Segurança 
   1. Senhas criptografadas; compliance OWASP ***(futuro)*** 
1. Monitoramento  
   1. Métricas; logs centralizados; alertas  
1. Confiabilidade  
- Retry automático em timeouts; snapshots do banco de dados periodicamente para evitar colapsar caso de algum problema 
4. **Requisitos Não Funcionais Organizacionais** 
1. Segurança de acesso 
   1. Fluxo de criação de conta com MFA e validação de e-mail 
1. Governança e Qualidade 
   1. Cobertura mínima de testes, revisão de código e documentação obrigatórias 
1. Operação e Suporte 
- Equipe de operações 24/7; procedimentos de backup e recuperação de desastre ***(futuro)*** 
5. **Outras técnicas**
