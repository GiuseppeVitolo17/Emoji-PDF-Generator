from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.pdfgen.canvas import Canvas
import textwrap

# Percorso al font NotoColorEmoji.ttf che hai scaricato
FONT_PATH = "NotoColorEmoji.ttf"
OUTPUT_FILE = "guida_SU_Danimarca_emoji.pdf"

# Contenuto del PDF con emoji
text = """
📘 Guida pratica per studenti UE in Danimarca che vogliono ottenere l'SU

1️⃣ Arrivo e registrazione
- 🎓 Iscriviti formalmente all'università (avrai la Letter of Admission → serve come prova).
- 🏠 Trova un alloggio (contratto d'affitto, student housing, ecc.).
- 🏢 Vai al SIRI (o International Citizen Service) con i documenti → ottieni il documento di residenza UE.
- 🆔 Con quello vai al Borgerservice → ottieni CPR number.
- 🔑 Una volta che hai il CPR, richiedi anche il MitID (identità digitale).

2️⃣ Lavoro part-time
- 🛠️ L'università non ti assegna il lavoro: devi trovarlo tu (bar, ristoranti, cleaning, magazzino, food delivery, ecc.).
- ⏱️ Molti studenti internazionali lavorano 10–12 ore a settimana, che è proprio la soglia minima per essere considerati "worker" secondo le regole SU.
- 💼 L'importante è che il lavoro sia contrattualizzato e tassato in Danimarca → serve busta paga e tasse regolarmente versate.

3️⃣ Richiesta SU
- Dopo che hai:
  • 🆔 CPR
  • 🔑 MitID
  • 🎓 iscrizione universitaria
  • 💼 contratto di lavoro regolare
- 🌐 Puoi fare la domanda online su minSU.
- 📄 Devi anche compilare il modulo per lo "equal status" (che certifica che come studente UE-lavoratore hai gli stessi diritti dei danesi).
- 💰 Una volta approvata, ricevi circa 6.300 DKK/mese (~850 €), pagati sul conto danese.

📌 Tempistiche realistiche
- 🕒 Arrivi → in 2–4 settimane hai CPR + MitID.
- 🔍 Trovi lavoro → 1–2 mesi (dipende da città e lingua, ma ad Aarhus è fattibile).
- 📝 Applichi a SU → serve la prova che stai già lavorando.
- 💳 I pagamenti SU partono dal mese di domanda approvata, non retroattivi.

👉 Quindi: non è l'università che ti "dà" il lavoro, ma sei tu a doverlo trovare.
L'università però ha spesso job portals e uffici di career guidance che ti aiutano a cercare.
"""

# Creazione PDF con ReportLab
c = Canvas(OUTPUT_FILE, pagesize=A4)
width, height = A4

# Prova a registrare e usare Liberation Sans che supporta le emoji
try:
    # Prova a registrare Liberation Sans
    pdfmetrics.registerFont(TTFont('LiberationSans', '/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf'))
    c.setFont('LiberationSans', 12)
    print("Usando font LiberationSans registrato")
except Exception as e:
    print(f"Errore con LiberationSans registrato: {e}")
    try:
        # Prova con font di sistema che supporta emoji
        c.setFont('LiberationSans', 12)
        print("Usando font LiberationSans di sistema")
    except:
        try:
            c.setFont('DejaVuSans', 12)
            print("Usando font DejaVuSans")
        except:
            try:
                c.setFont('Arial', 12)
                print("Usando font Arial")
            except:
                c.setFont('Helvetica', 12)
                print("Usando font Helvetica")

# Posizione iniziale
y_position = height - 2*cm
line_height = 15
margin = 2*cm

# Scrivo il testo
for line in text.split('\n'):
    if line.strip():
        # Wrapping del testo per adattarlo alla pagina
        wrapped_lines = textwrap.wrap(line, width=80)
        for wrapped_line in wrapped_lines:
            if y_position < 2*cm:  # Nuova pagina se necessario
                c.showPage()
                c.setFont('NotoColorEmoji', 12)
                y_position = height - 2*cm
            
            c.drawString(margin, y_position, wrapped_line)
            y_position -= line_height
    else:
        y_position -= line_height/2  # Spazio extra per righe vuote

# Salvo il PDF
c.save()

print(f"PDF creato: {OUTPUT_FILE}")