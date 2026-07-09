#!/usr/bin/env python3
"""Generate all Theme B diagrams as SVGs"""
import os

OUT = "/Users/a1/Desktop/studying_BiologyHL/lessons/diagrams"
os.makedirs(OUT, exist_ok=True)

def save(name, svg):
    with open(os.path.join(OUT, name), 'w') as f:
        f.write(svg)
    print(f"  Created: {name}")

# ============== LESSON 12 ==============

save("L12_fischer_glucose.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 420">
  <rect width="600" height="420" fill="#fff"/>
  <text x="300" y="28" text-anchor="middle" font-family="Arial" font-size="16" fill="#1a6b3c" font-weight="bold">D-Glucose Fischer Projection</text>
  <!-- backbone line -->
  <line x1="300" y1="60" x2="300" y2="350" stroke="#333" stroke-width="2"/>
  <!-- C1 aldehyde -->
  <text x="235" y="72" font-family="Arial" font-size="14" fill="#333">H—C=O</text>
  <text x="410" y="72" font-family="Arial" font-size="12" fill="#e53935">C-1 (aldehyde)</text>
  <!-- C2 -->
  <text x="235" y="115" font-family="Arial" font-size="14" fill="#333">H—C—OH</text>
  <text x="410" y="115" font-family="Arial" font-size="12" fill="#1565c0">C-2 (−OH RIGHT)</text>
  <!-- C3 -->
  <text x="235" y="158" font-family="Arial" font-size="14" fill="#333">HO—C—H</text>
  <text x="410" y="158" font-family="Arial" font-size="12" fill="#1565c0">C-3 (−OH LEFT)</text>
  <!-- C4 -->
  <text x="235" y="201" font-family="Arial" font-size="14" fill="#333">H—C—OH</text>
  <text x="410" y="201" font-family="Arial" font-size="12" fill="#1565c0">C-4 (−OH RIGHT)</text>
  <!-- C5 -->
  <text x="235" y="244" font-family="Arial" font-size="14" fill="#333">H—C—OH</text>
  <text x="410" y="244" font-family="Arial" font-size="12" fill="#6a1b9a">C-5 (−OH RIGHT → D-sugar!)</text>
  <!-- C6 -->
  <text x="235" y="282" font-family="Arial" font-size="14" fill="#333">CH₂OH</text>
  <text x="410" y="282" font-family="Arial" font-size="12" fill="#e53935">C-6 (primary alcohol)</text>
  <!-- vertical bonds between carbons -->
  <line x1="270" y1="82" x2="270" y2="105" stroke="#333" stroke-width="1.5"/>
  <line x1="270" y1="125" x2="270" y2="148" stroke="#333" stroke-width="1.5"/>
  <line x1="270" y1="168" x2="270" y2="191" stroke="#333" stroke-width="1.5"/>
  <line x1="270" y1="211" x2="270" y2="234" stroke="#333" stroke-width="1.5"/>
  <line x1="270" y1="254" x2="270" y2="272" stroke="#333" stroke-width="1.5"/>
  <text x="300" y="330" text-anchor="middle" font-family="Arial" font-size="13" fill="#6a1b9a" font-weight="bold">Rule: C-5 −OH on RIGHT = D-sugar</text>
  <text x="300" y="356" text-anchor="middle" font-family="Arial" font-size="12" fill="#555">Right → Down in Haworth | Left → Up in Haworth</text>
  <!-- aldehyde circle -->
  <ellipse cx="232" cy="66" rx="42" ry="14" fill="none" stroke="#e53935" stroke-width="1.5" stroke-dasharray="4,3"/>
  <!-- D-sugar circle -->
  <ellipse cx="232" cy="238" rx="42" ry="14" fill="none" stroke="#6a1b9a" stroke-width="1.5" stroke-dasharray="4,3"/>
</svg>""")

save("L12_alpha_beta_glucose.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 440">
  <rect width="600" height="440" fill="#fff"/>
  <text x="300" y="26" text-anchor="middle" font-family="Arial" font-size="16" fill="#1a6b3c" font-weight="bold">α-Glucose vs β-Glucose — Haworth Projections</text>
  <!-- Left: Alpha-glucose -->
  <text x="160" y="50" text-anchor="middle" font-family="Arial" font-size="15" fill="#1565c0" font-weight="bold">α-D-Glucose</text>
  <g transform="translate(30,65)">
    <polygon points="100,15 175,65 175,145 100,195 25,145 25,65" fill="#e8f5e9" stroke="#333" stroke-width="2.5"/>
    <text x="100" y="0" font-family="Arial" font-size="10" fill="#555">O</text>
    <!-- C labels -->
    <text x="115" y="50" font-family="Arial" font-size="9" fill="#e53935">1</text>
    <text x="180" y="90" font-family="Arial" font-size="9" fill="#333">2</text>
    <text x="155" y="145" font-family="Arial" font-size="9" fill="#333">3</text>
    <text x="45" y="145" font-family="Arial" font-size="9" fill="#333">4</text>
    <text x="15" y="90" font-family="Arial" font-size="9" fill="#333">5</text>
    <!-- CH2OH on C5 -->
    <line x1="25" y1="80" x2="10" y2="42" stroke="#333" stroke-width="1.5"/>
    <text x="0" y="38" font-family="Arial" font-size="8" fill="#555">CH₂OH</text>
    <!-- OH groups - C1 OH DOWN (alpha) -->
    <text x="120" y="30" font-family="Arial" font-size="10" fill="#e53935" font-weight="bold">OH↓</text>
    <text x="185" y="82" font-family="Arial" font-size="9" fill="#333">OH</text>
    <text x="160" y="152" font-family="Arial" font-size="9" fill="#333">OH</text>
    <text x="18" y="152" font-family="Arial" font-size="9" fill="#333">OH</text>
    <!-- Arrow for C1 OH -->
    <line x1="115" y1="35" x2="115" y2="55" stroke="#e53935" stroke-width="2" marker-end="url(#arrowRed)"/>
  </g>
  <!-- Right: Beta-glucose -->
  <text x="440" y="50" text-anchor="middle" font-family="Arial" font-size="15" fill="#e53935" font-weight="bold">β-D-Glucose</text>
  <g transform="translate(320,65)">
    <polygon points="100,15 175,65 175,145 100,195 25,145 25,65" fill="#e8f5e9" stroke="#333" stroke-width="2.5"/>
    <text x="100" y="0" font-family="Arial" font-size="10" fill="#555">O</text>
    <text x="115" y="50" font-family="Arial" font-size="9" fill="#e53935">1</text>
    <text x="180" y="90" font-family="Arial" font-size="9" fill="#333">2</text>
    <text x="155" y="145" font-family="Arial" font-size="9" fill="#333">3</text>
    <text x="45" y="145" font-family="Arial" font-size="9" fill="#333">4</text>
    <text x="15" y="90" font-family="Arial" font-size="9" fill="#333">5</text>
    <line x1="25" y1="80" x2="10" y2="42" stroke="#333" stroke-width="1.5"/>
    <text x="0" y="38" font-family="Arial" font-size="8" fill="#555">CH₂OH</text>
    <!-- C1 OH UP (beta) -->
    <text x="120" y="18" font-family="Arial" font-size="10" fill="#e53935" font-weight="bold">OH↑</text>
    <text x="185" y="82" font-family="Arial" font-size="9" fill="#333">OH</text>
    <text x="160" y="152" font-family="Arial" font-size="9" fill="#333">OH</text>
    <text x="18" y="152" font-family="Arial" font-size="9" fill="#333">OH</text>
    <line x1="115" y1="24" x2="115" y2="44" stroke="#e53935" stroke-width="2"/>
  </g>
  <!-- Equilibrium arrow -->
  <text x="300" y="200" text-anchor="middle" font-family="Arial" font-size="14" fill="#6a1b9a">⇌ mutarotation (via open-chain form)</text>
  <!-- Bottom info -->
  <rect x="40" y="240" width="520" height="90" rx="6" fill="#f5f5f5" stroke="#ddd"/>
  <text x="300" y="262" text-anchor="middle" font-family="Arial" font-size="12" fill="#555">α-glucose: C-1 −OH DOWN (opposite CH₂OH) → found in STARCH &amp; GLYCOGEN</text>
  <text x="300" y="284" text-anchor="middle" font-family="Arial" font-size="12" fill="#555">β-glucose: C-1 −OH UP (same side as CH₂OH) → found in CELLULOSE</text>
  <text x="300" y="310" text-anchor="middle" font-family="Arial" font-size="11" fill="#e53935" font-weight="bold">This single −OH orientation determines digestibility!</text>
  <!-- Key uses -->
  <text x="160" y="365" text-anchor="middle" font-family="Arial" font-size="13" fill="#1565c0">α-1,4 → starch (helical, digestible)</text>
  <text x="440" y="365" text-anchor="middle" font-family="Arial" font-size="13" fill="#e53935">β-1,4 → cellulose (straight, indigestible)</text>
</svg>""")

save("L12_monosaccharides.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 520">
  <rect width="600" height="520" fill="#fff"/>
  <text x="300" y="25" text-anchor="middle" font-family="Arial" font-size="16" fill="#1a6b3c" font-weight="bold">Monosaccharides: Galactose, Fructose, Ribose, Deoxyribose</text>
  <!-- GALACTOSE -->
  <text x="140" y="52" text-anchor="middle" font-family="Arial" font-size="13" fill="#1565c0" font-weight="bold">β-D-Galactose</text>
  <g transform="translate(15,62)">
    <polygon points="95,12 165,55 165,130 95,172 25,130 25,55" fill="#fce4ec" stroke="#333" stroke-width="2"/>
    <text x="95" y="-2" font-family="Arial" font-size="9" fill="#555">O</text>
    <text x="110" y="45" font-family="Arial" font-size="8" fill="#333">1</text>
    <text x="170" y="80" font-family="Arial" font-size="8" fill="#333">2</text>
    <text x="145" y="138" font-family="Arial" font-size="8" fill="#333">3</text>
    <text x="35" y="138" font-family="Arial" font-size="8" fill="#333">4</text>
    <text x="8" y="80" font-family="Arial" font-size="8" fill="#333">5</text>
    <line x1="25" y1="70" x2="10" y2="38" stroke="#333" stroke-width="1.2"/>
    <text x="0" y="34" font-family="Arial" font-size="7" fill="#555">CH₂OH</text>
    <text x="68" y="42" font-family="Arial" font-size="9" fill="#1565c0">OH↑</text>
    <text x="148" y="50" font-family="Arial" font-size="8" fill="#333">OH</text>
    <text x="78" y="150" font-family="Arial" font-size="9" fill="#e53935" font-weight="bold">OH↑</text>
    <text x="165" y="80" font-family="Arial" font-size="8" fill="#333">OH</text>
    <circle cx="78" cy="150" r="14" fill="none" stroke="#e53935" stroke-width="1.5" stroke-dasharray="3,2"/>
  </g>
  <text x="140" y="242" text-anchor="middle" font-family="Arial" font-size="10" fill="#e53935">C-4 OH UP (vs glucose DOWN)</text>
  <text x="140" y="256" text-anchor="middle" font-family="Arial" font-size="10" fill="#555">C-4 epimer of glucose</text>

  <!-- FRUCTOSE (furanose 5-ring) -->
  <text x="420" y="52" text-anchor="middle" font-family="Arial" font-size="13" fill="#1565c0" font-weight="bold">β-D-Fructose (furanose)</text>
  <g transform="translate(320,62)">
    <polygon points="95,5 145,55 115,110 45,110 15,55" fill="#fff3e0" stroke="#333" stroke-width="2"/>
    <text x="95" y="-5" font-family="Arial" font-size="9" fill="#555">O</text>
    <text x="110" y="50" font-family="Arial" font-size="8" fill="#e53935">2</text>
    <text x="130" y="100" font-family="Arial" font-size="8" fill="#333">3</text>
    <text x="50" y="100" font-family="Arial" font-size="8" fill="#333">4</text>
    <text x="10" y="50" font-family="Arial" font-size="8" fill="#333">5</text>
    <!-- two CH2OH groups -->
    <line x1="145" y1="52" x2="172" y2="32" stroke="#333" stroke-width="1.2"/>
    <text x="170" y="28" font-family="Arial" font-size="7" fill="#555">CH₂OH</text>
    <text x="100" y="122" font-family="Arial" font-size="7" fill="#555">CH₂OH (C-6)</text>
    <text x="80" y="50" font-family="Arial" font-size="8" fill="#333">OH</text>
  </g>
  <text x="420" y="242" text-anchor="middle" font-family="Arial" font-size="10" fill="#555">5-membered furanose ring</text>
  <text x="420" y="256" text-anchor="middle" font-family="Arial" font-size="10" fill="#555">Anomeric carbon = C-2 (ketose)</text>

  <!-- RIBOSE -->
  <text x="140" y="285" text-anchor="middle" font-family="Arial" font-size="13" fill="#1565c0" font-weight="bold">β-D-Ribose (RNA)</text>
  <g transform="translate(30,295)">
    <polygon points="80,5 120,45 100,95 30,95 5,50" fill="#e8eaf6" stroke="#333" stroke-width="2"/>
    <text x="80" y="-5" font-family="Arial" font-size="9" fill="#555">O</text>
    <text x="95" y="40" font-family="Arial" font-size="8" fill="#333">1</text>
    <text x="110" y="80" font-family="Arial" font-size="8" fill="#1565c0">2</text>
    <text x="45" y="80" font-family="Arial" font-size="8" fill="#333">3</text>
    <text x="0" y="40" font-family="Arial" font-size="8" fill="#333">4</text>
    <line x1="80" y1="10" x2="70" y2="-8" stroke="#333" stroke-width="1.2"/>
    <text x="55" y="-10" font-family="Arial" font-size="7" fill="#555">CH₂OH</text>
    <!-- OH groups all down -->
    <text x="90" y="32" font-family="Arial" font-size="8" fill="#333">OH</text>
    <text x="108" y="72" font-family="Arial" font-size="8" fill="#1565c0" font-weight="bold">OH↓</text>
    <text x="48" y="72" font-family="Arial" font-size="8" fill="#333">OH</text>
    <circle cx="108" cy="72" r="10" fill="none" stroke="#1565c0" stroke-width="1.5" stroke-dasharray="3,2"/>
  </g>
  <text x="140" y="410" text-anchor="middle" font-family="Arial" font-size="10" fill="#1565c0">C-2 has −OH → RNA</text>

  <!-- DEOXYRIBOSE -->
  <text x="420" y="285" text-anchor="middle" font-family="Arial" font-size="13" fill="#e53935" font-weight="bold">2-Deoxyribose (DNA)</text>
  <g transform="translate(320,295)">
    <polygon points="80,5 120,45 100,95 30,95 5,50" fill="#ffebee" stroke="#333" stroke-width="2"/>
    <text x="80" y="-5" font-family="Arial" font-size="9" fill="#555">O</text>
    <text x="95" y="40" font-family="Arial" font-size="8" fill="#333">1</text>
    <text x="110" y="80" font-family="Arial" font-size="8" fill="#e53935">2</text>
    <text x="45" y="80" font-family="Arial" font-size="8" fill="#333">3</text>
    <text x="0" y="40" font-family="Arial" font-size="8" fill="#333">4</text>
    <line x1="80" y1="10" x2="70" y2="-8" stroke="#333" stroke-width="1.2"/>
    <text x="55" y="-10" font-family="Arial" font-size="7" fill="#555">CH₂OH</text>
    <text x="90" y="32" font-family="Arial" font-size="8" fill="#333">OH</text>
    <text x="108" y="72" font-family="Arial" font-size="8" fill="#e53935" font-weight="bold">H↓</text>
    <text x="48" y="72" font-family="Arial" font-size="8" fill="#333">OH</text>
    <circle cx="108" cy="72" r="10" fill="none" stroke="#e53935" stroke-width="1.5" stroke-dasharray="3,2"/>
  </g>
  <text x="420" y="410" text-anchor="middle" font-family="Arial" font-size="10" fill="#e53935">C-2 has −H only → DNA (more stable)</text>

  <!-- Bottom note -->
  <text x="300" y="450" text-anchor="middle" font-family="Arial" font-size="12" fill="#555">The "missing oxygen" (deoxy) at C-2 makes DNA chemically more stable than RNA.</text>
</svg>""")

save("L12_disaccharides.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 500">
  <rect width="600" height="500" fill="#fff"/>
  <text x="300" y="25" text-anchor="middle" font-family="Arial" font-size="16" fill="#1a6b3c" font-weight="bold">Disaccharides: Maltose, Sucrose, Lactose</text>

  <!-- MALTOSE -->
  <text x="300" y="52" text-anchor="middle" font-family="Arial" font-size="13" fill="#1565c0" font-weight="bold">Maltose: α-Glucose + Glucose (α-1,4 glycosidic bond)</text>
  <g transform="translate(150,65)">
    <!-- Left glucose -->
    <polygon points="70,8 125,42 125,105 70,138 15,105 15,42" fill="#e8f5e9" stroke="#333" stroke-width="1.8"/>
    <text x="70" y="0" font-family="Arial" font-size="8" fill="#555">O</text>
    <text x="82" y="38" font-family="Arial" font-size="7" fill="#333">α</text>
    <!-- Glycosidic bond -->
    <line x1="125" y1="42" x2="140" y2="42" stroke="#e53935" stroke-width="2.5"/>
    <text x="132" y="35" font-family="Arial" font-size="7" fill="#e53935">O</text>
    <!-- Right glucose -->
    <polygon points="140,8 195,42 195,105 140,138 85,105 85,42" fill="#e8f5e9" stroke="#333" stroke-width="1.8"/>
    <text x="140" y="0" font-family="Arial" font-size="8" fill="#555">O</text>
  </g>
  <text x="300" y="210" text-anchor="middle" font-family="Arial" font-size="10" fill="#e53935">α-1,4 bond | Reducing sugar | Produced during starch digestion</text>

  <!-- SUCROSE -->
  <text x="300" y="245" text-anchor="middle" font-family="Arial" font-size="13" fill="#6a1b9a" font-weight="bold">Sucrose: α-Glucose + β-Fructose (α-1,2 glycosidic bond)</text>
  <g transform="translate(155,258)">
    <polygon points="70,8 125,42 125,105 70,138 15,105 15,42" fill="#e8f5e9" stroke="#333" stroke-width="1.8"/>
    <text x="70" y="0" font-family="Arial" font-size="7" fill="#555">O (Glc)</text>
    <line x1="125" y1="42" x2="138" y2="42" stroke="#6a1b9a" stroke-width="2.5"/>
    <polygon points="138,12 168,45 150,90 108,90 90,45" fill="#fff3e0" stroke="#333" stroke-width="1.8"/>
    <text x="138" y="5" font-family="Arial" font-size="7" fill="#555">O (Fru)</text>
  </g>
  <text x="300" y="400" text-anchor="middle" font-family="Arial" font-size="10" fill="#6a1b9a">α-1,2 bond | NON-reducing (both anomeric carbons locked) | Table sugar</text>

  <!-- LACTOSE -->
  <text x="300" y="428" text-anchor="middle" font-family="Arial" font-size="13" fill="#ff8f00" font-weight="bold">Lactose: β-Galactose + Glucose (β-1,4 glycosidic bond)</text>
  <g transform="translate(152,440)">
    <polygon points="68,8 120,42 120,100 68,130 16,100 16,42" fill="#fce4ec" stroke="#333" stroke-width="1.5"/>
    <text x="68" y="0" font-family="Arial" font-size="7" fill="#555">O (Gal)</text>
    <line x1="120" y1="42" x2="132" y2="42" stroke="#ff8f00" stroke-width="2"/>
    <polygon points="132,8 185,42 185,100 132,130 79,100 79,42" fill="#e8f5e9" stroke="#333" stroke-width="1.5"/>
    <text x="132" y="0" font-family="Arial" font-size="7" fill="#555">O (Glc)</text>
  </g>
</svg>""")

save("L12_starch_glycogen_cellulose.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 480">
  <rect width="600" height="480" fill="#fff"/>
  <text x="300" y="25" text-anchor="middle" font-family="Arial" font-size="16" fill="#1a6b3c" font-weight="bold">Polysaccharides: Starch (Amylose + Amylopectin), Glycogen, Cellulose</text>

  <!-- AMYLOSE -->
  <text x="105" y="55" text-anchor="middle" font-family="Arial" font-size="12" fill="#1565c0" font-weight="bold">Amylose</text>
  <text x="105" y="70" text-anchor="middle" font-family="Arial" font-size="9" fill="#555">α-1,4 only, helical</text>
  <g transform="translate(15,80)">
    <!-- Helical coil -->
    <path d="M10,70 Q20,50 30,70 Q40,90 50,70 Q60,50 70,70 Q80,90 90,70 Q100,50 110,70 Q120,90 130,70 Q140,50 150,70" fill="none" stroke="#43a047" stroke-width="3"/>
    <path d="M10,70 Q20,90 30,70 Q40,50 50,70 Q60,90 70,70 Q80,50 90,70 Q100,90 110,70 Q120,50 130,70 Q140,90 150,70" fill="none" stroke="#81c784" stroke-width="2" stroke-dasharray="5,3"/>
    <!-- Iodine inside -->
    <g fill="#6a1b9a">
      <circle cx="30" cy="70" r="2.5"/>
      <circle cx="36" cy="68" r="2.5"/>
      <circle cx="42" cy="67" r="2.5"/>
      <circle cx="48" cy="68" r="2.5"/>
      <circle cx="54" cy="70" r="2.5"/>
    </g>
    <text x="5" y="55" font-family="Arial" font-size="7" fill="#6a1b9a">I₃⁻→</text>
  </g>
  <text x="105" y="120" text-anchor="middle" font-family="Arial" font-size="8" fill="#6a1b9a">Blue-black with iodine</text>

  <!-- AMYLOPECTIN -->
  <text x="300" y="55" text-anchor="middle" font-family="Arial" font-size="12" fill="#1565c0" font-weight="bold">Amylopectin (starch) &amp; Glycogen</text>
  <text x="300" y="70" text-anchor="middle" font-family="Arial" font-size="9" fill="#555">α-1,4 backbone + α-1,6 branches</text>
  <g transform="translate(170,80)">
    <!-- Main chain -->
    <path d="M0,70 L180,70" stroke="#43a047" stroke-width="3"/>
    <!-- Branch 1 -->
    <path d="M40,70 L40,30" stroke="#43a047" stroke-width="2"/>
    <circle cx="40" cy="70" r="5" fill="#e53935"/>
    <text x="45" y="65" font-family="Arial" font-size="7" fill="#e53935">α-1,6</text>
    <!-- Branch 2 -->
    <path d="M100,70 L100,30" stroke="#43a047" stroke-width="2"/>
    <circle cx="100" cy="70" r="5" fill="#e53935"/>
    <!-- Branch 3 -->
    <path d="M140,70 L140,95" stroke="#43a047" stroke-width="2"/>
    <circle cx="140" cy="70" r="5" fill="#e53935"/>
    <text x="150" y="105" font-family="Arial" font-size="7" fill="#555">Amylopectin: ~1 branch / 20 glu</text>
  </g>
  <text x="300" y="120" text-anchor="middle" font-family="Arial" font-size="8" fill="#e53935">Glycogen: ~1 branch / 10 glu (more highly branched)</text>

  <!-- CELLULOSE -->
  <text x="470" y="55" text-anchor="middle" font-family="Arial" font-size="12" fill="#e53935" font-weight="bold">Cellulose</text>
  <text x="470" y="70" text-anchor="middle" font-family="Arial" font-size="9" fill="#555">β-1,4 straight chains</text>
  <g transform="translate(380,80)">
    <!-- 3 parallel straight chains -->
    <line x1="0" y1="50" x2="120" y2="50" stroke="#e53935" stroke-width="2"/>
    <line x1="0" y1="65" x2="120" y2="65" stroke="#e53935" stroke-width="2"/>
    <line x1="0" y1="80" x2="120" y2="80" stroke="#e53935" stroke-width="2"/>
    <!-- H-bonds between chains -->
    <line x1="20" y1="50" x2="20" y2="65" stroke="#1565c0" stroke-width="1" stroke-dasharray="4,3"/>
    <line x1="50" y1="50" x2="50" y2="65" stroke="#1565c0" stroke-width="1" stroke-dasharray="4,3"/>
    <line x1="80" y1="50" x2="80" y2="65" stroke="#1565c0" stroke-width="1" stroke-dasharray="4,3"/>
    <line x1="20" y1="65" x2="20" y2="80" stroke="#1565c0" stroke-width="1" stroke-dasharray="4,3"/>
    <line x1="50" y1="65" x2="50" y2="80" stroke="#1565c0" stroke-width="1" stroke-dasharray="4,3"/>
    <line x1="80" y1="65" x2="80" y2="80" stroke="#1565c0" stroke-width="1" stroke-dasharray="4,3"/>
  </g>
  <text x="470" y="120" text-anchor="middle" font-family="Arial" font-size="8" fill="#1565c0">H-bonds → microfibrils</text>

  <!-- COMPARISON TABLE -->
  <rect x="30" y="150" width="540" height="320" rx="6" fill="#fafafa" stroke="#ddd"/>
  <text x="300" y="175" text-anchor="middle" font-family="Arial" font-size="13" fill="#333" font-weight="bold">Critical Comparison</text>
  <!-- Table header -->
  <line x1="30" y1="188" x2="570" y2="188" stroke="#ddd" stroke-width="1"/>
  <text x="100" y="202" font-family="Arial" font-size="9" fill="#555">Bond Type</text>
  <text x="255" y="202" font-family="Arial" font-size="9" fill="#555">3D Shape</text>
  <text x="380" y="202" font-family="Arial" font-size="9" fill="#555">Digestible?</text>
  <text x="500" y="202" font-family="Arial" font-size="9" fill="#555">Function</text>
  <line x1="30" y1="210" x2="570" y2="210" stroke="#ddd" stroke-width="1"/>
  <!-- Row 1 -->
  <text x="100" y="227" font-family="Arial" font-size="9" fill="#1565c0">α-1,4 (only)</text>
  <text x="255" y="227" font-family="Arial" font-size="9" fill="#333">Helical (6 glu/turn)</text>
  <text x="380" y="227" font-family="Arial" font-size="9" fill="#43a047">Yes (amylase)</text>
  <text x="500" y="227" font-family="Arial" font-size="9" fill="#333">Energy storage (plants)</text>
  <line x1="30" y1="232" x2="570" y2="232" stroke="#eee"/>
  <!-- Row 2 -->
  <text x="100" y="248" font-family="Arial" font-size="9" fill="#1565c0">α-1,4 + α-1,6</text>
  <text x="255" y="248" font-family="Arial" font-size="9" fill="#333">Branched tree</text>
  <text x="380" y="248" font-family="Arial" font-size="9" fill="#43a047">Yes (amylase)</text>
  <text x="500" y="248" font-family="Arial" font-size="9" fill="#333">Quick glucose release</text>
  <line x1="30" y1="253" x2="570" y2="253" stroke="#eee"/>
  <!-- Row 3 -->
  <text x="100" y="269" font-family="Arial" font-size="9" fill="#1565c0">α-1,4 + α-1,6</text>
  <text x="255" y="269" font-family="Arial" font-size="9" fill="#333">Dense shrub (many branches)</text>
  <text x="380" y="269" font-family="Arial" font-size="9" fill="#43a047">Yes (amylase)</text>
  <text x="500" y="269" font-family="Arial" font-size="9" fill="#333">Energy storage (animals)</text>
  <line x1="30" y1="274" x2="570" y2="274" stroke="#eee"/>
  <!-- Row 4 -->
  <text x="100" y="290" font-family="Arial" font-size="9" fill="#e53935" font-weight="bold">β-1,4 (only)</text>
  <text x="255" y="290" font-family="Arial" font-size="9" fill="#333">Straight (alternating flip)</text>
  <text x="380" y="290" font-family="Arial" font-size="9" fill="#e53935" font-weight="bold">No (need cellulase)</text>
  <text x="500" y="290" font-family="Arial" font-size="9" fill="#333">Structural (plant cell walls)</text>

  <!-- Key insight -->
  <text x="300" y="340" text-anchor="middle" font-family="Arial" font-size="12" fill="#e53935" font-weight="bold">β-1,4 makes ALL the difference — straight chains → H-bonds → microfibrils → tensile strength</text>
  <text x="300" y="360" text-anchor="middle" font-family="Arial" font-size="11" fill="#555">Every other glucose flipped 180° prevents helical coiling</text>
  <text x="300" y="385" text-anchor="middle" font-family="Arial" font-size="12" fill="#333">α-1,4 → helical → amylase can digest | β-1,4 → straight → needs cellulase</text>
  <text x="300" y="410" text-anchor="middle" font-family="Arial" font-size="11" fill="#555">Ruminants have symbiotic bacteria producing cellulase; humans do not.</text>
</svg>""")

save("L12_glycoprotein_membrane.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 380">
  <rect width="600" height="380" fill="#fff"/>
  <text x="300" y="25" text-anchor="middle" font-family="Arial" font-size="16" fill="#1a6b3c" font-weight="bold">Glycoproteins &amp; Glycolipids on the Cell Membrane</text>
  <!-- Membrane bilayer -->
  <g transform="translate(30,160)">
    <!-- Top leaflet -->
    <circle cx="30" cy="10" r="8" fill="#81c784" stroke="#333" stroke-width="1"/>
    <circle cx="70" cy="10" r="8" fill="#81c784" stroke="#333" stroke-width="1"/>
    <circle cx="110" cy="10" r="8" fill="#81c784" stroke="#333" stroke-width="1"/>
    <circle cx="150" cy="10" r="8" fill="#81c784" stroke="#333" stroke-width="1"/>
    <circle cx="190" cy="10" r="8" fill="#81c784" stroke="#333" stroke-width="1"/>
    <circle cx="230" cy="10" r="8" fill="#81c784" stroke="#333" stroke-width="1"/>
    <circle cx="270" cy="10" r="8" fill="#81c784" stroke="#333" stroke-width="1"/>
    <circle cx="310" cy="10" r="8" fill="#81c784" stroke="#333" stroke-width="1"/>
    <circle cx="350" cy="10" r="8" fill="#81c784" stroke="#333" stroke-width="1"/>
    <circle cx="390" cy="10" r="8" fill="#81c784" stroke="#333" stroke-width="1"/>
    <circle cx="430" cy="10" r="8" fill="#81c784" stroke="#333" stroke-width="1"/>
    <circle cx="470" cy="10" r="8" fill="#81c784" stroke="#333" stroke-width="1"/>
    <circle cx="510" cy="10" r="8" fill="#81c784" stroke="#333" stroke-width="1"/>
    <!-- tails -->
    <line x1="30" y1="16" x2="25" y2="35" stroke="#333" stroke-width="1.5"/>
    <line x1="30" y1="16" x2="35" y2="35" stroke="#333" stroke-width="1.5"/>
    <line x1="70" y1="16" x2="65" y2="35" stroke="#333" stroke-width="1.5"/>
    <line x1="70" y1="16" x2="75" y2="35" stroke="#333" stroke-width="1.5"/>
    <line x1="110" y1="16" x2="105" y2="35" stroke="#333" stroke-width="1.5"/>
    <line x1="110" y1="16" x2="115" y2="35" stroke="#333" stroke-width="1.5"/>
    <line x1="150" y1="16" x2="145" y2="35" stroke="#333" stroke-width="1.5"/>
    <line x1="150" y1="16" x2="155" y2="35" stroke="#333" stroke-width="1.5"/>
    <!-- Bottom leaflet -->
    <line x1="30" y1="55" x2="25" y2="36" stroke="#333" stroke-width="1.5"/>
    <line x1="30" y1="55" x2="35" y2="36" stroke="#333" stroke-width="1.5"/>
    <circle cx="30" cy="60" r="8" fill="#81c784" stroke="#333" stroke-width="1"/>
    <line x1="70" y1="55" x2="65" y2="36" stroke="#333" stroke-width="1.5"/>
    <line x1="70" y1="55" x2="75" y2="36" stroke="#333" stroke-width="1.5"/>
    <circle cx="70" cy="60" r="8" fill="#81c784" stroke="#333" stroke-width="1"/>
  </g>
  <!-- Glycoprotein with branching carbohydrate -->
  <g transform="translate(180,60)">
    <rect x="45" y="0" width="30" height="130" rx="4" fill="#1565c0" opacity="0.3" stroke="#1565c0" stroke-width="2"/>
    <!-- carbohydrate branches -->
    <line x1="40" y1="2" x2="25" y2="-30" stroke="#e53935" stroke-width="2"/>
    <line x1="25" y1="-30" x2="10" y2="-55" stroke="#e53935" stroke-width="1.5"/>
    <line x1="25" y1="-30" x2="35" y2="-50" stroke="#e53935" stroke-width="1.5"/>
    <line x1="60" y1="0" x2="55" y2="-25" stroke="#e53935" stroke-width="2"/>
    <line x1="55" y1="-25" x2="45" y2="-45" stroke="#e53935" stroke-width="1.5"/>
    <line x1="55" y1="-25" x2="65" y2="-40" stroke="#e53935" stroke-width="1.5"/>
    <line x1="80" y1="2" x2="90" y2="-20" stroke="#e53935" stroke-width="2"/>
    <line x1="90" y1="-20" x2="80" y2="-38" stroke="#e53935" stroke-width="1.5"/>
    <line x1="90" y1="-20" x2="105" y2="-30" stroke="#e53935" stroke-width="1.5"/>
    <text x="60" y="-62" text-anchor="middle" font-family="Arial" font-size="10" fill="#e53935" font-weight="bold">Carbohydrate chains (glycocalyx)</text>
    <text x="60" y="145" text-anchor="middle" font-family="Arial" font-size="10" fill="#1565c0" font-weight="bold">Transmembrane Protein</text>
  </g>
  <!-- Glycolipid -->
  <g transform="translate(430,100)">
    <line x1="20" y1="-30" x2="10" y2="-55" stroke="#ff8f00" stroke-width="2"/>
    <line x1="20" y1="-30" x2="35" y2="-50" stroke="#ff8f00" stroke-width="1.5"/>
    <circle cx="20" cy="-20" r="6" fill="#ffcc80" stroke="#ff8f00" stroke-width="1.5"/>
    <text x="20" y="-62" text-anchor="middle" font-family="Arial" font-size="10" fill="#ff8f00" font-weight="bold">Glycolipid</text>
  </g>
  <text x="300" y="145" text-anchor="middle" font-family="Arial" font-size="11" fill="#555">EXTRACELLULAR</text>
  <text x="300" y="310" text-anchor="middle" font-family="Arial" font-size="11" fill="#555">CYTOPLASM</text>
  <rect x="50" y="335" width="500" height="35" rx="5" fill="#f5f5f5" stroke="#ddd"/>
  <text x="300" y="357" text-anchor="middle" font-family="Arial" font-size="11" fill="#333">Carbohydrates → cell recognition, adhesion • ABO blood groups • Glycocalyx protects cell surface</text>
</svg>""")

print("Lesson 12 done!")
