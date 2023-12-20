<p align="center">
  <img src="https://user-images.githubusercontent.com/23036697/179610525-9ee37437-9302-4681-a5e7-7ce84cd6776a.png" alt="accessibility text">
</p>

![Badge Linguagem](http://img.shields.io/static/v1?label=LINGUAGEM&message=PYTHON&color=informational&style=plastic) ![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=yellowgreen&style=plastic) ![Badge Commits](https://img.shields.io/github/commit-activity/w/PersonalProjekts/Python-Examples?label=COMMITS&style=plastic)

<hr/>

<p>Este repositório serve de suporte ao estudo da linguagem Python fornecendo diversos exemplos nas mais diversas aplicações.</p>

<p>A depender do exemplo a ser estudado, algumas bibliotecas deverão ser instaladas. Para isso deverá ser utilizado o instalador de pacotes PIP. Vejamos como utilizá-lo.</p>

<hr/>

<h3>PIP</h3>

<p>Primeiro devemos verificar o PIP está instalado.</p>

<pre><code>pip --version</code></pre>

<p>Caso ele não esteja instalado,ele pode ser baixado e instalado a partir da URL a seguir:</p>

<pre><a target="_blank" href="https://pypi.org/project/pip/">https://pypi.org/project/pip/</a></pre>

<p>Caso ele já esteja instalado é sempre aconselhável atualizar a versão do PIP:</p>

<pre><code>python -m pip install --upgrade pip</code></pre>

<p>Uma vez atualizado, utilizamos o comando PIP para instalar a biblioteca desejada:</p>

<pre><code>pip install <i>nome_biblioteca</i></code></pre>

Onde <i>nome_biblioteca</i> é o nome da biblioteca que se deseja instalar.

<p>Caso haja algum controle de permissão de usuário que impossibilite a instalação da biblioteca, devemos adicionar o argumento <i>--user</i>:</p>

<pre><code>pip install <i>nome_biblioteca</i> --user</code></pre>

A seguir iremos listar as bibliotecas que precisarão ser instaladas.

<hr/>

<h3>BIBLIOTECAS</h3>

<details><summary><h4>Pytube</h4></summary>
  <p>Esta biblioteca permite baixar vídeos do Youtube</p>

  <p>A sua documentação pode ser vista em:</p>

  <pre><a target="_blank" href="https://pypi.org/project/pytube/">https://pypi.org/project/pytube/</a></pre>

  <p>Será necessário fazer um ajuste na linha 30 do arquivo <b>cipher.py</b></p>

  ```python
  var_regex = re.compile("^\$*\w+\W")
  ```
  
  <p>Uma vez que o ajuste foi feito, basta no início do seu código importar a bilbioteca Pytube.</p>

  ```python
  from pytube import YouTube
  ```
</details>

<details><summary><h4>MoviePy</h4></summary>
  <p>Esta biblioteca habilita recursos para edição de vídeo: corte, concatenação, inserções de títulos, composição de vídeo (também   conhecida como edição não linear), processamento de vídeo e criação de efeitos personalizados.</p>

  <p>A sua documentação pode ser vista em:</p>

  <pre><a target="_blank" href="https://pypi.org/project/moviepy/">https://pypi.org/project/moviepy/</a></pre>

  <p>Para usá-la basta no início do seu código importar a bilbioteca MoviePy.</p>

  ```python
  import moviepy.editor
  ```
</details>

<details><summary><h4>QRCode</h4></summary>
  <p>Esta biblioteca é utilizada para a geração de QrCodes.</p>

  <p>A sua documentação pode ser vista em:</p>

  <pre><a target="_blank" href="https://pypi.org/project/qrcode/">https://pypi.org/project/qrcode/</a></pre>

  <p>Para usá-la basta no início do seu código importar a bilbioteca QRCode.</p>

  ```python
  import qrcode
  ```
  
  <p>A instalação padrão inclui a biblioteca <i>Pillow</i>:</p>

  <p>A documentação da biblioteca <i>Pillow</i> pode ser vista em:</p>

  <pre><a target="_blank" href="https://pypi.org/project/Pillow/">https://pypi.org/project/Pillow/</a></pre>
</details>

<details><summary><h4>PyQRCode</h4></summary>
  <p>Esta biblioteca é um gerador de código QR simples.</p>
  
  <p>Ao contrário de outras bibliotecas, todos osparâmetros podem ser ajustados manualmente.</p>

  <p>A sua documentação pode ser vista em:</p>

  <pre><a target="_blank" href="https://pypi.org/project/PyQRCode/">https://pypi.org/project/PyQRCode/</a></pre>

  <p>Para usá-la basta no início do seu código importar a bilbioteca PyQRCode.</p>

  ```python
  import pyqrcode
  ```
</details>

<details><summary><h4>GeoPy</h4></summary>
  <p>Esta biblioteca é um cliente para vários serviços web de geocodificação (<i>Geocoders</i>).</p>
  
  <p>Ela inclui classes para:</p>

  <ul>
    <li>OpenStreetMap Nominatim;</li>
    <li>Google Geocoding API (V3);</i>
    <li>e outros serviços de geocodificação.
  </ul>
  
  <p>A lista completa está em </p>

  <pre><a target="_blank" href="https://geopy.readthedocs.io/en/latest/#geocoders">https://geopy.readthedocs.io/en/latest/#geocoders</a></pre>
  
  <p>A sua documentação pode ser vista em:</p>
  
  <pre><a target="_blank" href="https://pypi.org/project/geopy/">https://pypi.org/project/geopy/</a></pre>
  
  <p>Ou em...</p>
  
  <pre><a target="_blank" href="https://geopy.readthedocs.io/en/stable/">https://geopy.readthedocs.io/en/stable/</a></pre>

  <p>Para usá-la basta no início do seu código importar a bilbioteca GeoPy informando qual o <i>Geocoder</i> que você irá trabalhar.</p>

  ```python
  from geopy.geocoders import Nominatim
  ```
  
  <p>Um exemplo dessa biblioteca utilizando como API para geração de mapa o <a target="_blank" href="https://www.openstreetmap.org/#map=4/-23.56/-46.67">OpenStreetMap</a> com o Geocoder <i>Nominatim</i> pode ser visto em:</p>
  
  <pre><a target="_blank" href="https://nominatim.openstreetmap.org/ui/search.html">https://nominatim.openstreetmap.org/ui/search.html</a></pre>  
</details>

<hr/>
