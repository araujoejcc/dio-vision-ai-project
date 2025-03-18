import pytesseract
from PIL import Image
import os
import json
from datetime import datetime

# Configurar o caminho para o executável do Tesseract (se necessário)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Para Windows

def extract_text_from_image(image_path):
    """Extrai texto de uma imagem usando Tesseract OCR."""
    try:
        # Abre a imagem
        img = Image.open(image_path)
        
        # Extrai o texto
        text = pytesseract.image_to_string(img, lang='por+eng')
        
        return text.strip()
    except Exception as e:
        return f"Erro ao processar a imagem: {str(e)}"

def process_all_images():
    """Processa todas as imagens na pasta inputs e salva os resultados."""
    input_dir = "inputs"
    output_dir = "outputs"
    
    # Cria a pasta de saída se não existir
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    results = {}
    
    # Processa cada imagem na pasta de inputs
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
            image_path = os.path.join(input_dir, filename)
            
            # Extrai texto da imagem
            text = extract_text_from_image(image_path)
            
            # Salva o resultado em um arquivo de texto
            output_filename = f"{os.path.splitext(filename)[0]}_result.txt"
            output_path = os.path.join(output_dir, output_filename)
            
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(text)
            
            # Adiciona ao dicionário de resultados
            results[filename] = {
                'text': text,
                'processed_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
    
    # Salva um resumo de todos os resultados em JSON
    summary_path = os.path.join(output_dir, 'summary.json')
    with open(summary_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=4)
    
    return results

if __name__ == "__main__":
    print("Iniciando o processamento de imagens para reconhecimento de texto...")
    results = process_all_images()
    print(f"Processamento concluído! Foram processadas {len(results)} imagens.")
    print(f"Os resultados foram salvos na pasta 'outputs'.")
