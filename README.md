# Projeto MC426

## Membros

- Erika Tiemi Santos Hacimoto (RA 244953)
- Gabriel Jeronimo da Silva (RA 247112)
- Raphael Ferezin Kitahara (RA 244839)
- Luiza Coelho de Souza (RA 247257)
- Guilherme Henrique Ichiro Seto Ito (RA 238706)
- Pedro Henrique Peraçoli Pereira Ceccon (RA 247327)

## Descrição do Projeto
O software a ser desenvolvido é uma plataforma integrada de sistemas de compatibilidade e mapas colaborativos. Essa plataforma terá como objetivo principal conectar pessoas interessadas em caminhar ou pedalar ao mesmo tempo, fornecendo uma experiência mais segura ao realizarem um ato de socialização. Os principais recursos incluem um meio de realizar "matches" entre os usuários com rotas similares, possibilidade de avaliação de outros usuários por meio de feedbacks e informações detalhadas sobre locais inseguros e infraestruturas ruins.

Além disso, a plataforma oferecerá funcionalidades de interação, que com a posterior escalabilidade do sistema, possivelmente haverá uma implementação de um chat com outros usuários e integração com outros aplicativos para aumentar o engajamento dos usuários em relação às devidas atividades físicas. A segurança e a confiabilidade serão prioridades, garantindo que os dados sejam protegidos e que o usuário também se sinta seguro ao iniciar uma atividade juntamente com outro usuário, muitas vezes, desconhecido, através de um sistema de avaliação. O software será desenvolvido utilizando uma abordagem ágil, permitindo adaptações rápidas às necessidades dos usuários.

## Arquitetura do Sistema

### Diagrama de Componentes (C4 - Nível 3)

```mermaid
graph TB
    subgraph "Frontend"
        Template[Template HTML]
        Static[Static Files]
        JS[JavaScript]
        CSS[CSS]
    end

    subgraph "Backend"
        subgraph "Controllers"
            UserController[UserController]
            RouteController[RouteController]
            MatchController[MatchController]
            FeedbackController[FeedbackController]
        end

        subgraph "Models"
            User[User Model]
            Route[Route Model]
            Match[Match Model]
            Feedback[Feedback Model]
        end

        subgraph "Services"
            AuthService[Authentication Service]
            MatchService[Match Service]
            MapService[Map Service]
        end
    end

    subgraph "Database"
        DB[(Database)]
    end

    Template --> UserController
    Template --> RouteController
    Template --> MatchController
    Template --> FeedbackController
    Static --> Template
    JS --> Template
    CSS --> Template

    UserController --> User
    RouteController --> Route
    MatchController --> Match
    FeedbackController --> Feedback

    UserController --> AuthService
    MatchController --> MatchService
    RouteController --> MapService

    User --> DB
    Route --> DB
    Match --> DB
    Feedback --> DB
```

### Estilo Arquitetural

O sistema adota o padrão arquitetural **MVC (Model-View-Controller)** com uma camada adicional de serviços:

1. **Model (Modelo)**
   - Representa os dados e a lógica de negócio
   - Contém as regras de validação
   - Gerencia o estado dos dados
   - Responsável pela persistência dos dados no banco de dados

2. **View (Visão)**
   - Interface com o usuário
   - Templates HTML para renderização dinâmica
   - Arquivos estáticos (CSS, JavaScript)
   - Responsável pela apresentação dos dados

3. **Controller (Controlador)**
   - Processa as requisições HTTP
   - Coordena a interação entre Model e View
   - Implementa a lógica de aplicação
   - Gerencia o fluxo de dados

4. **Services (Serviços)**
   - Implementa lógica de negócio complexa
   - Fornece funcionalidades reutilizáveis
   - Gerencia integrações externas
   - Separa responsabilidades específicas

### Componentes Principais

1. **Models**
   - **User**: Gerencia dados e validações de usuários
   - **Route**: Controla informações de rotas e trajetos
   - **Match**: Gerencia compatibilidade entre usuários
   - **Feedback**: Controla avaliações e feedbacks

2. **Controllers**
   - **UserController**: Operações de usuário (registro, login, perfil)
   - **RouteController**: Gerenciamento de rotas e trajetos
   - **MatchController**: Lógica de matching entre usuários
   - **FeedbackController**: Sistema de avaliações

3. **Services**
   - **Authentication Service**: Gerenciamento de autenticação
   - **Match Service**: Algoritmos de compatibilidade
   - **Map Service**: Integração com serviços de mapa

4. **View**
   - **Templates**: Interface do usuário
   - **Static**: Recursos estáticos (CSS, JavaScript)
   - **Components**: Componentes reutilizáveis

### Padrão de Projeto

Para o componente de gerenciamento de usuários, será implementado o padrão **Repository**. Este padrão será utilizado para:

- Abstrair a lógica de acesso a dados
- Centralizar a lógica de persistência
- Facilitar a manutenção e testes
- Melhorar a organização do código
- Permitir a troca fácil da implementação do banco de dados

A implementação deste padrão será realizada através de uma issue específica com o label "AvaliacaoA4".
