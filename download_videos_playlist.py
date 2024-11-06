import yt_dlp
import os

# URL do vídeo ou playlist que você deseja baixar
url = input("Digite a URL do vídeo ou da playlist do YouTube: ")

# Cria uma pasta "downloads" no mesmo diretório do script
download_folder = os.path.join(os.path.dirname(__file__), 'downloads')
os.makedirs(download_folder, exist_ok=True)

# Configurações do yt-dlp
ydl_opts = {
    'format': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',  # 1080p ou melhor disponível até 1080p
    'outtmpl': os.path.join(download_folder, '%(playlist_index)s - %(title)s.%(ext)s'),  # Numerando o arquivo com o índice da playlist
    'ignoreerrors': True  # Ignora vídeos com erro (como privados ou indisponíveis)
}

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print("Baixando o vídeo ou playlist em 1080p...")
        ydl.download([url])
        print("Download concluído!")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
