import yt_dlp

# URL do vídeo que você deseja baixar
url = input("Digite a URL do vídeo do YouTube: ")

# Configurações do yt-dlp
ydl_opts = {
    'format': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',  # Apenas 1080p
    'outtmpl': '%(title)s.%(ext)s',  # Nome do arquivo
}

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print("Baixando o vídeo em 1080p...")
        ydl.download([url])
        print("Download concluído!")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
