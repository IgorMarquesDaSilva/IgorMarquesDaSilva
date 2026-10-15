"""Gera as artes SVG do README sem dependências externas."""

from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
ASSETS.mkdir(exist_ok=True)


HERO = """<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="330" viewBox="0 0 1200 330" role="img" aria-labelledby="title desc">
  <title id="title">Igor Marques da Silva</title>
  <desc id="desc">Desenvolvimento back-end, APIs e aplicações web</desc>
  <defs>
    <linearGradient id="background" x2="1" y2="1">
      <stop stop-color="#0A1221"/>
      <stop offset=".55" stop-color="#0E1A2D"/>
      <stop offset="1" stop-color="#10243A"/>
    </linearGradient>
    <linearGradient id="accent" x2="1" y2="0">
      <stop stop-color="#38BDF8"/>
      <stop offset="1" stop-color="#818CF8"/>
    </linearGradient>
    <radialGradient id="glow">
      <stop stop-color="#38BDF8" stop-opacity=".20"/>
      <stop offset="1" stop-color="#38BDF8" stop-opacity="0"/>
    </radialGradient>
    <pattern id="grid" width="36" height="36" patternUnits="userSpaceOnUse">
      <path d="M36 0H0V36" fill="none" stroke="#B8D9F2" stroke-opacity=".07"/>
    </pattern>
    <clipPath id="clip"><rect width="1200" height="330" rx="26"/></clipPath>
  </defs>
  <style>
    text { font-family: 'Segoe UI', Arial, sans-serif; }
    .flow { stroke-dasharray: 8 12; animation: move 16s linear infinite; }
    .pulse { animation: pulse 3.2s ease-in-out infinite; }
    @keyframes move { to { stroke-dashoffset: -200; } }
    @keyframes pulse { 50% { opacity: .45; } }
    @media (prefers-reduced-motion: reduce) {
      .flow, .pulse { animation: none; }
    }
  </style>
  <g clip-path="url(#clip)">
    <rect width="1200" height="330" fill="url(#background)"/>
    <rect width="1200" height="330" fill="url(#grid)"/>
    <circle cx="1020" cy="150" r="245" fill="url(#glow)"/>
    <path d="M0 329H1200" stroke="url(#accent)" stroke-width="3"/>
    <path d="M805 0V330" stroke="#A7C8E3" stroke-opacity=".12"/>
    <path d="M820 49H1180M820 282H1180" stroke="#A7C8E3" stroke-opacity=".12"/>
    <circle cx="1000" cy="165" r="106" fill="none" stroke="#5E82A4" stroke-opacity=".26"/>
    <circle cx="1000" cy="165" r="74" fill="none" stroke="#5E82A4" stroke-opacity=".20"/>
    <path class="flow" d="M900 162H1102M1000 65V265" stroke="url(#accent)" stroke-opacity=".50" stroke-width="2"/>
    <path d="M907 162L1000 104L1093 162L1000 226Z" fill="#0D2137" stroke="#4F7899" stroke-opacity=".7" stroke-width="2"/>
    <circle cx="1000" cy="104" r="25" fill="#12314C" stroke="#38BDF8" stroke-width="2"/>
    <circle cx="907" cy="162" r="25" fill="#12314C" stroke="#38BDF8" stroke-width="2"/>
    <circle cx="1093" cy="162" r="25" fill="#12314C" stroke="#38BDF8" stroke-width="2"/>
    <circle cx="1000" cy="226" r="25" fill="#12314C" stroke="#38BDF8" stroke-width="2"/>
    <circle class="pulse" cx="1000" cy="165" r="9" fill="#38BDF8"/>
    <text x="1000" y="109" text-anchor="middle" fill="#DFF6FF" font-size="11" font-weight="700">API</text>
    <text x="907" y="167" text-anchor="middle" fill="#DFF6FF" font-size="11" font-weight="700">WEB</text>
    <text x="1093" y="167" text-anchor="middle" fill="#DFF6FF" font-size="11" font-weight="700">DB</text>
    <text x="1000" y="231" text-anchor="middle" fill="#DFF6FF" font-size="11" font-weight="700">UX</text>
    <rect x="70" y="48" width="9" height="9" rx="2" fill="#38BDF8"/>
    <text x="95" y="58" fill="#82CDEC" font-size="15" font-weight="700" letter-spacing="3">DESENVOLVIMENTO DE SOFTWARE</text>
    <text x="68" y="151" fill="#F4F8FC" font-size="59" font-weight="700" letter-spacing="-2">Igor Marques da Silva</text>
    <text x="72" y="201" fill="#BCD0E2" font-size="23">Back-end  ·  APIs  ·  aplicações web</text>
    <path d="M72 226H719" stroke="#7594AE" stroke-opacity=".4"/>
    <rect x="72" y="252" width="105" height="35" rx="17.5" fill="#17364E" stroke="#37617D"/>
    <rect x="189" y="252" width="83" height="35" rx="17.5" fill="#17364E" stroke="#37617D"/>
    <rect x="284" y="252" width="101" height="35" rx="17.5" fill="#17364E" stroke="#37617D"/>
    <text x="124" y="275" text-anchor="middle" fill="#D6EBF5" font-size="15">Node.js</text>
    <text x="230" y="275" text-anchor="middle" fill="#D6EBF5" font-size="15">PHP</text>
    <text x="334" y="275" text-anchor="middle" fill="#D6EBF5" font-size="15">MySQL</text>
  </g>
</svg>
"""


CARDS = [
    {
        "slug": "fincontrol",
        "number": "01",
        "tag": "APLICAÇÃO WEB",
        "title": "FINCONTROL",
        "lines": (
            "Controle financeiro com receitas, despesas",
            "e autenticação para cada usuário.",
        ),
        "stack": "Node.js  ·  Express  ·  MySQL",
        "accent": "#38BDF8",
        "icon": '<path d="M446 104v-20m19 20V65m19 39V78m19 26V51" /><path d="M438 112h75" />',
    },
    {
        "slug": "beehive",
        "number": "02",
        "tag": "TEMPO REAL",
        "title": "Beehive",
        "lines": (
            "Comunicação em equipe com chat em tempo real,",
            "canais privados e chamadas de voz.",
        ),
        "stack": "Socket.IO  ·  WebRTC  ·  MySQL",
        "accent": "#A78BFA",
        "icon": '<path d="M466 50l28 16v32l-28 16-28-16V66z" /><path d="M438 66l28 16 28-16M466 82v32" />',
    },
    {
        "slug": "aeed-bruno",
        "number": "03",
        "tag": "EDUCAÇÃO",
        "title": "AEED-Bruno",
        "lines": (
            "Ensino de estruturas de dados com quizzes,",
            "progresso e recursos de gamificação.",
        ),
        "stack": "PHP  ·  MySQL  ·  Testes",
        "accent": "#34D399",
        "icon": '<path d="M435 64l31-16 31 16-31 16zM435 80l31 16 31-16M435 96l31 16 31-16" />',
    },
    {
        "slug": "bug-hunters",
        "number": "04",
        "tag": "JOGO EDUCATIVO",
        "title": "Bug Hunters",
        "lines": (
            "Jogo de lógica em Portugol com missões,",
            "feedback imediato e recursos acessíveis.",
        ),
        "stack": "JavaScript  ·  Canvas 2D  ·  Acessibilidade",
        "accent": "#FBBF24",
        "icon": '<path d="M446 64l-12 12 12 12M486 64l12 12-12 12M474 55l-16 42" />',
    },
]


def card_svg(card):
    title = escape(card["title"])
    tag = escape(card["tag"])
    line_one, line_two = (escape(line) for line in card["lines"])
    stack = escape(card["stack"])
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="560" height="225" viewBox="0 0 560 225" role="img" aria-labelledby="title desc">
  <title id="title">{title}</title>
  <desc id="desc">{line_one} {line_two}</desc>
  <defs>
    <linearGradient id="surface" x2="1" y2="1">
      <stop stop-color="#111E2C"/>
      <stop offset="1" stop-color="#0D1117"/>
    </linearGradient>
    <clipPath id="clip"><rect width="560" height="225" rx="18"/></clipPath>
  </defs>
  <style>text {{ font-family: 'Segoe UI', Arial, sans-serif; }}</style>
  <g clip-path="url(#clip)">
    <rect x="1" y="1" width="558" height="223" rx="18" fill="url(#surface)" stroke="#2B3C50" stroke-width="2"/>
    <rect width="6" height="225" fill="{card['accent']}"/>
    <circle cx="490" cy="78" r="62" fill="{card['accent']}" opacity=".06"/>
    <g fill="none" stroke="{card['accent']}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" opacity=".9">{card['icon']}</g>
    <text x="28" y="42" fill="{card['accent']}" font-size="13" font-weight="700" letter-spacing="2.2">{tag}</text>
    <text x="520" y="42" fill="#698299" font-size="14" text-anchor="end">{card['number']} / 04</text>
    <text x="28" y="88" fill="#F0F5FA" font-size="31" font-weight="700">{title}</text>
    <text x="28" y="126" fill="#AFBECD" font-size="16.5">{line_one}</text>
    <text x="28" y="150" fill="#AFBECD" font-size="16.5">{line_two}</text>
    <path d="M28 179H532" stroke="#33465B"/>
    <circle cx="34" cy="201" r="4" fill="{card['accent']}"/>
    <text x="49" y="206" fill="#D7E3EC" font-size="14">{stack}</text>
  </g>
</svg>
"""


(ASSETS / "hero.svg").write_text(HERO, encoding="utf-8")
for card in CARDS:
    (ASSETS / f"{card['slug']}.svg").write_text(card_svg(card), encoding="utf-8")
