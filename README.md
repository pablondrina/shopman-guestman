# shopman-guestman

CRM completo para Django. Gestão de clientes com múltiplos pontos de contato, endereços, grupos com pricing diferenciado, programa de fidelidade com tiers, insights RFM, merge de duplicatas, consentimento LGPD, e integração ManyChat.

Part of the [Django Shopman](https://github.com/pablondrina/django-shopman) commerce framework.

## Domínio

- **Customer** — cliente com nome, phone, email. Identificação por telefone (phone-first).
- **ContactPoint** — ponto de contato adicional (email secundário, WhatsApp, etc.).
- **CustomerAddress** — endereço estruturado com geolocalização.
- **CustomerGroup** — grupo de clientes com listing_ref para pricing diferenciado.
- **ExternalIdentity** — identidade em sistema externo (iFood, Rappi, etc.).

## Contribs (9 módulos)

| Contrib | O que faz |
|---------|-----------|
| `loyalty` | Programa de fidelidade: pontos, stamps, tiers (Bronze→Silver→Gold→Platinum). Ledger imutável. |
| `insights` | Análise RFM (Recency, Frequency, Monetary). CustomerInsight por cliente. |
| `preferences` | Preferências do cliente (alergia, sem lactose, etc.). |
| `identifiers` | Identificadores customizáveis (CPF, cartão fidelidade, matrícula). |
| `consent` | Consentimento de comunicação (LGPD). Canal + base legal + status. |
| `merge` | Merge de clientes duplicados com audit trail. |
| `timeline` | Timeline de interações do cliente (pedidos, contatos, eventos). |
| `manychat` | Integração ManyChat para notificações via WhatsApp. |
| `admin_unfold` | Admin com Unfold theme. |

## Services

- **CustomerService** — CRUD, busca por phone, resolução de identidade.
- **LoyaltyService** — enroll, earn_points, redeem_points, add_stamp, auto-tier upgrade.
- **InsightService** — cálculo RFM, segmentação.
- **MergeService** — merge de duplicatas com resolução de conflitos.
- **ConsentService** — registro e consulta de consentimento.

## Instalação

```bash
pip install shopman-guestman
```

```python
INSTALLED_APPS = [
    "shopman.guestman",
    "shopman.guestman.contrib.loyalty",      # programa de fidelidade
    "shopman.guestman.contrib.insights",     # análise RFM
    "shopman.guestman.contrib.preferences",  # preferências
    "shopman.guestman.contrib.identifiers",  # CPF, cartão, etc.
    "shopman.guestman.contrib.consent",      # LGPD
    "shopman.guestman.contrib.merge",        # merge de duplicatas
    "shopman.guestman.contrib.timeline",     # timeline
]
```

## Development

```bash
git clone https://github.com/pablondrina/django-shopman.git
cd django-shopman && pip install -e packages/guestman
make test-guestman  # ~369 testes
```

## License

MIT — Pablo Valentini
