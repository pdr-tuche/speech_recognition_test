# speech_recognition_test

🗣 Transcrição de audio para texto

## Depedencias do windows

- ffmpeg e ffprobe [site](https://ffmpeg.org/)

### [Como instalar](https://www.gyan.dev/ffmpeg/builds/)

- instalando pelo Chocolatey windows package manager:

[clique para saber como fazer o download do chocolatey](https://chocolatey.org/install) ou faça download do [script](./install_chocolatey.ps1) e o execute como administrador =)

Após instalar o chocolatey, faça download do pacote ffmpeg para windows abrindo o powershell como administrador e digitando o comando:

```ps1
choco install ffmpeg
```

## Executar o codigo

- monte um ambiente virtual:

```ps1
python -m venv venv
```

- ative o ambiente virtual:

```ps1
.\venv\Scripts\activate
```

- instale as depedencias do codigo:

```ps1
pip install -r requirements.txt
```

agora execute o codigo =)
