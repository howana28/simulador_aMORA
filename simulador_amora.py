from flask import Flask, render_template, request

app = Flask(__name__)

IGPM_ANUAL = 0.06  # 6%

def format_currency(value):
    return f"R$ {value:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')

def calcular_juros_compostos(valor_base, taxa, ano):
    return valor_base * ((1 + taxa) ** (ano - 1))

def calcular_igpm(valor_base, igpm, ano):
    return valor_base * ((1 + igpm) ** (ano - 1))

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    if request.method == 'POST':
        try:
            valor_imovel = float(request.form['valor_imovel'].replace('.', '').replace(',', '.'))
            percentual_entrada = float(request.form['percentual_entrada'].replace(',', '.'))
            anos_contrato = int(request.form['anos_contrato'])
            taxa_juros = float(request.form['taxa_juros'].replace(',', '.')) / 100

            valor_entrada = valor_imovel * (percentual_entrada / 100)
            total_a_guardar = valor_imovel * 0.15
            valor_mensal_base = total_a_guardar / (anos_contrato * 12)

            igpm_corrigido = []
            juros_corrigido = []

            for ano in range(1, anos_contrato + 1):
                igpm_valor = calcular_igpm(valor_mensal_base, IGPM_ANUAL, ano)
                juros_valor = calcular_juros_compostos(valor_mensal_base, taxa_juros, ano)
                igpm_corrigido.append(format_currency(igpm_valor))
                juros_corrigido.append(format_currency(juros_valor))

            resultado = {
                'valor_entrada': format_currency(valor_entrada),
                'total_a_guardar': format_currency(total_a_guardar),
                'valor_mensal_base': format_currency(valor_mensal_base),
                'anos_contrato': anos_contrato,
                'igpm_corrigido': igpm_corrigido,
                'juros_corrigido': juros_corrigido,
                'taxa_juros_percent': f"{taxa_juros*100:.2f}",
                'igpm_percent': f"{IGPM_ANUAL*100:.2f}",
                'valor_imovel': format_currency(valor_imovel),
                'percentual_entrada': percentual_entrada
            }
        except Exception as e:
            resultado = {'erro': str(e)}

    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)