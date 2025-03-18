# Projeto de Reconhecimento de Texto em Imagens

## 📝 Descrição
Este projeto implementa um sistema de reconhecimento óptico de caracteres (OCR) para extrair texto de imagens. Desenvolvido como parte do bootcamp de Inteligência Artificial da DIO, o projeto demonstra a aplicação prática de tecnologias de visão computacional.

## 🚀 Tecnologias Utilizadas
- Python 3.x
- Tesseract OCR
- Biblioteca pytesseract
- PIL (Python Imaging Library)

## 📁 Estrutura do Projeto
```
ocr-image-text-recognition/
│
├── inputs/               # Pasta com as imagens originais
│   ├── imagem1.jpg
│   ├── imagem2.png
│   └── ...
│
├── outputs/              # Pasta com os resultados do OCR
│   ├── imagem1_result.txt
│   ├── imagem2_result.txt
│   ├── summary.json
│   └── ...
│
├── src/                  # Código fonte do projeto
│   └── ocr_processor.py
│
├── requirements.txt      # Dependências do projeto
└── README.md             # Este arquivo
```

## 🔧 Instalação e Configuração

### Pré-requisitos
- Python 3.6 ou superior
- Tesseract OCR instalado no sistema

### Passos para instalação

1. Clone este repositório:
```bash
git clone https://github.com/seu-usuario/ocr-image-text-recognition.git
cd ocr-image-text-recognition
```

2. Instale o Tesseract OCR:
   - **Windows**: Baixe o instalador em [https://github.com/UB-Mannheim/tesseract/wiki](https://github.com/UB-Mannheim/tesseract/wiki)
   - **Linux**: `sudo apt install tesseract-ocr`
   - **macOS**: `brew install tesseract`

3. Instale as dependências Python:
```bash
pip install -r requirements.txt
```

## 💻 Como Usar

1. Coloque suas imagens na pasta `inputs/`
2. Execute o script principal:
```bash
python src/ocr_processor.py
```
3. Os resultados serão salvos na pasta `outputs/`

## 📊 Resultados e Insights

### Exemplos de Processamento

#### Imagem Original
![Imagem Original](inputs/exemplo.jpg)

#### Texto Reconhecido
```
Este é um exemplo de texto que foi 
reconhecido pela nossa ferramenta OCR.
O sistema conseguiu extrair corretamente 
o conteúdo desta imagem.
```

### Insights e Aprendizados

Durante o desenvolvimento deste projeto, descobri vários aspectos interessantes sobre OCR:

1. **Qualidade da imagem**: A precisão do reconhecimento de texto depende muito da qualidade da imagem original. Imagens com alto contraste entre texto e fundo tendem a produzir melhores resultados.

2. **Pré-processamento**: Técnicas como binarização, remoção de ruído e correção de perspectiva podem melhorar significativamente os resultados do OCR.

3. **Multilinguagem**: O Tesseract suporta mais de 100 idiomas, sendo necessário especificar o idioma correto para obter resultados mais precisos.

4. **Casos de uso**: Essa tecnologia pode ser aplicada em diversos cenários, como:
   - Digitalização de documentos
   - Extração de texto de placas em sistemas de visão computacional
   - Acessibilidade para deficientes visuais
   - Indexação de conteúdo em imagens para sistemas de busca

## 🔮 Possibilidades Futuras

Algumas melhorias que poderiam ser implementadas:

- Adicionar pré-processamento de imagem para melhorar a qualidade do OCR
- Implementar reconhecimento de tabelas em documentos
- Criar uma interface web para upload e processamento de imagens
- Integrar com APIs de tradução para processar textos em múltiplos idiomas
- Usar técnicas de deep learning para melhorar a precisão do reconhecimento

## 📫 Como Contribuir

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Faça commit das suas alterações (`git commit -m 'Adiciona nova feature'`)
4. Faça push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## 📄 Licença
Este projeto está sob a licença MIT - veja o arquivo [LICENSE.md](LICENSE.md) para mais detalhes.
