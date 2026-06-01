from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML, CSS

# para instalar o WeasyPrint: pip install WeasyPrint
# verifique se o weasyPrint esta instalado: weasyprint --version
# No caso de erro: no windows o gtk3(uma biblioteca que o weasyprint precisa) não vem instalado e não pode ser baixado por meio do pip, então é so baixar por esse link-> https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases
def gerar_pdf(request):
    html_string = render_to_string('pei/relatorio.html')
    #resposta HTTP que será enviada ao navegador informando que sera um pdf
    envio = HttpResponse(content_type= 'application/pdf')
    #Define como o navegador lida com o pdf. Inline: abre o pdf no navegador. attachment: baixa o pdf automaticamente
    envio['Content-Disposition'] = 'inline; filename= "relatorio.pdf"'

    #Pega a string HTML gerada, converte para PDF usando o WeasyPrint e depois escreve o PDF dentro da resposta HTTP (envio)
    HTML(string=html_string).write_pdf(envio)
    return envio