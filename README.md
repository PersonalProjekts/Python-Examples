<h1>Python-Examples</h1>

![Badge Linguagem](http://img.shields.io/static/v1?label=LINGUAGEM&message=PYTHON&color=informational&style=plastic)
![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=yellowgreen&style=plastic)

<hr/>

<p>Este repositório serve de suporte ao estudo da linguagem Python fornecendo diversos exemplos nasmais diversas aplicações.</p>

<p>A depender do exemplo a ser estudado, algumas bibliotecas deverão ser instaladas. Para isso deverá ser utilizado o instalador de pacotes PIP. Vejamos como utilizá-lo.</p>

<hr/>

<h3>PIP</h3>

<p>Primeiro devemos verificar o PIP está instalado.</p>

<pre><code>pip --version</code></pre>

<p>Caso ele não esteja instalado,ele pode ser baixado e instalado a partir da URL a seguir:</p>

<pre><a target="_blank" href="https://pypi.org/project/pip/">https://pypi.org/project/pip/</a></pre>

<p>Caso ele já esteja instalado é sempre aconselhável atualizar a versão do PIP:</p>

```bash
python -m pip install --upgrade pip
```

<p>Uma vez atualizado, utilizamos o comando PIP para instalar a biblioteca desejada:</p>

<pre><code>pip install <i>nome_biblioteca</i></code></pre>

Onde <i>nome_biblioteca</i> é o nome da biblioteca que se deseja instalar.

A seguir iremos listar as bibliotecas que precisarão ser instaladas.

<hr/>

<h3>BIBLIOTECAS</h3>

<div style="margin-left:45px; width:50%;">
<h4>Pytube</h4>

<p>Esta biblioteca permite baixar vídeos do Youtube</p>

<pre><a target="_blank" href="https://pypi.org/project/pytube/">https://pypi.org/project/pytube/</a></pre>

<p>Será necessário fazer um ajuste na linha 30 do arquivo <b>cipher.py</b></p>

<pre><code>var_regex = re.compile("^\$*\w+\W")</code></pre>

</div>
<hr/>
