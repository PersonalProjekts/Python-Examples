# Diretório de Exemplos da Bilioteca Pytube

  Este diretório possui exemplos de códigos em Python utilizando a biblioteca `pytube`.

  Para utilizar os exemplos deste diretório, é necessário instalar a biblioteca `pytube`. Isso pode ser feito utilizando o gerenciador de pacotes `pip` com o seguinte comando:

  ```bash
    pip install pytube
   ```

  A biblioteca `pytube` depende da API do YouTube para funcionar. Caso a API do YouTube seja alterada, a biblioteca pode parar de funcionar temporariamente até que seja atualizada. Recomenda-se verificar o repositório oficial da biblioteca `pytube` para obter atualizações ou soluções alternativas caso ocorram problemas.

  Para mais informações sobre a biblioteca `pytube`, consulte a [documentação oficial](https://pytube.io/en/latest/).


  A seguir temos as descrições de cada um dos exemplos disponibilizados:

---

<details>
  <summary><b>audio_downloader.py</b></summary>

  Este programa foi desenvolvido para realizar o download de áudio de vídeos do YouTube a partir de uma URL fornecida pelo usuário. Ele utiliza a biblioteca `pytube` para acessar o vídeo, filtrar o áudio e efetuar o download.

  **Funcionalidades:**

  - ***Download de Áudio***:
    - Realiza o download apenas do áudio de um vídeo do YouTube.
    - Obtém automaticamente a melhor qualidade de áudio disponível.

  - ***Salvamento do Áudio***:
    - Salva o arquivo de áudio no diretório onde o script está localizado.

  **Como funciona:**

  O programa solicita ao usuário que insira a URL do vídeo do YouTube do qual deseja baixar o áudio. Em seguida, ele utiliza a biblioteca `pytube` para criar um objeto do vídeo, filtrar o áudio e efetuar o download. O arquivo de áudio é salvo no diretório do script.
</details>

---

<details>
  <summary><b>video_downloader.py</b></summary>

  Este programa foi desenvolvido para baixar vídeos do YouTube a partir de uma URL fornecida pelo usuário. Ele utiliza a biblioteca `pytube` para listar os formatos disponíveis do vídeo e realizar o download do formato selecionado pelo usuário.

  **Funcionalidades:**

  - ***Listagem de Formatos Disponíveis***:
    - Lista todos os formatos de vídeo e áudio disponíveis para o vídeo especificado.
    - Exibe os formatos de maneira indexada para facilitar a seleção pelo usuário.

  - ***Download do Vídeo***:
    - Realiza o download do vídeo no formato selecionado pelo usuário.
    - Salva o vídeo no diretório onde o script está localizado.

  **Como funciona:**

  O programa solicita ao usuário que insira a URL do vídeo do YouTube que deseja baixar. Em seguida, ele utiliza a biblioteca `pytube` para listar todos os formatos disponíveis do vídeo. O usuário seleciona o formato desejado, e o programa realiza o download do vídeo no diretório do script.
</details>

---

<details>
  <summary><b>video_hd_downloader.py</b></summary>

  Este programa foi desenvolvido para baixar vídeos do YouTube a partir de uma URL fornecida pelo usuário, utilizando a biblioteca `pytube`. Ele realiza o download do vídeo na maior resolução disponível e o salva no diretório onde o script está localizado.

  **Funcionalidades:**

  - ***Download de Vídeos***:
    - Realiza o download de vídeos do YouTube a partir de uma URL fornecida pelo usuário, baixando o vídeo na maior resolução disponível.

  - ***Salvamento do Vídeo***:
    - Salva o vídeo baixado no diretório onde o script está localizado.

  **Como funciona:**

  O programa solicita ao usuário que insira a URL do vídeo que deseja baixar. Em seguida, ele utiliza a biblioteca `pytube` para criar um objeto `YouTube` com base na URL fornecida. O vídeo é então baixado na maior resolução disponível e salvo no diretório do script.
</details>