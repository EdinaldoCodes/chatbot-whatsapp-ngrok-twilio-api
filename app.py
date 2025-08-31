from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

def exibir_menu():
    return (
        "✨👗 Bem-vindo(a) à Fulano Modas! 👕✨\n"
        "\n"
        "🕒 *Horário de funcionamento:*\n"
        "Segunda a sexta: *08:30 - 11:30* e *15:30 - 18:00*\n"
        "Sábado: *08:30 - 11:30*\n"
        "\n"
        "É um prazer ter você por aqui! 💖\n"
        "Sou o assistente virtual da loja e vou te ajudar.\n"
        "\n*Escolha uma das opções abaixo para continuar:*\n"
        "\n"
        "1️⃣ Novidades\n"
        "2️⃣ Promoções 🔥\n"
        "3️⃣ Catálogo Feminino 👗\n"
        "4️⃣ Catálogo Masculino 👕\n"
        "5️⃣ Falar com atendente 🧑\n"
    )

@app.route("/whatsapp", methods=['POST'])

def whatsapp_reply():
    incoming_msg = request.values.get('Body', '').lower().strip()  # Remove espaços em branco
    resp = MessagingResponse()
    msg = resp.message()

    if incoming_msg in ['1', 'novidades']:
        msg.body('Aqui estão as novidades da semana! [link]')
    elif incoming_msg in ['2', 'promocoes', 'promo']:
        msg.body('Confira nossas promoções imperdíveis! [link]')
    elif incoming_msg in ['3', 'catalogo feminino', 'catálago feminino']:
        msg.body('Veja nosso catálogo feminino completo! [link]')
    elif incoming_msg in ['4', 'catalogo masculino', 'catálago masculino']:
        msg.body('Veja nosso catálogo masculino completo! [link]')
    elif incoming_msg in ['5', 'falar com atendente']:
        msg.body('Um de nossos atendentes entrará em contato com você em breve.')
    elif 'ajuda' in incoming_msg:
        msg.body('Claro! Me diga o que você precisa.')
    else:
        msg.body(exibir_menu())

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
