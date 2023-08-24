
## 📫 Contribuir

Para contribuir com o projeto, siga estas etapas:

1. Bifurque este repositório.
2. Crie um branch: `git checkout -b dev`.
3. Faça suas alterações e confirme-as: `git commit -m '<mensagem_commit>'`
4. Envie para o branch: `git push origin dev`
5. Crie a solicitação de pull.

Como alternativa, consulte a documentação do GitHub em [como criar uma solicitação pull](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).


## ☑️ Recomendações

- Adicione um título consistente com o título do conteúdo;
- Recomendamos que na primeira linha deve ter no máximo 4 palavras;
- Para descrever com detalhes, usar a descrição do commit;
- Usar um emoji no início da mensagem de commit representando sobre o commit;
- Um link precisa ser adicionado em sua forma mais autêntica, ou seja: sem encurtadores de link e links afiliados;
- Documente seu código afinal 
<code>“Code is more often read than written.”<code>

<code>— Guido van Rossum<code>

## 💻 Exemplos
<table>
  <thead>
    <tr>
      <th>Comando git</th>
      <th>Resultado no GitHub</th>
    </tr>
  </thead>
 <tbody>
    <tr>
      <td>
        <code>git commit -m ":tada: Commit inicial"</code>
      </td>
      <td>🎉 Commit inicial</td>
    </tr>
    <tr>
      <td>
        <code>git commit -m ":books: [ DOC ] - Atualizaçao do README"</code>
      </td>
      <td>📚 [ DOC ] - Atualizaçao do README</td>
    </tr>
    <tr>
      <td>
        <code>git commit -m ":bug: [ FIXED ] - Loop infinito na linha 50"</code>
      </td>
      <td>🐛 [ FIXED ] - Loop infinito na linha 50</td>
    </tr>
    <tr>
      <td>
        <code>git commit -m ":sparkles: [ FEATURE ] - Pagina de login"</code>
      </td>
      <td>✨ [ FEATURE ] - Pagina de login</td>
    </tr>
    <tr>
      <td>
        <code>git commit -m ":recycle: [ REFACTOR ] - Passando para arrow functions"</code>
      </td>
      <td>♻️ [ REFACTOR ] - Passando para arrow functions</td>
    </tr>
    <tr>
      <td>
        <code>git commit -m ":zap: [ PERFORM ] - Melhoria no tempo de resposta"</code>
      </td>
      <td>⚡ [ PERFORM ] - Melhoria no tempo de resposta</td>
    </tr>
    <tr>
      <td>
        <code>git commit -m ":boom: [ FIXED ] - Revertendo mudanças ineficientes"</code>
      </td>
      <td>💥 [ FIXED ] - Revertendo mudanças ineficientes</td>
    </tr>
    <tr>
      <td>
        <code>git commit -m ":lipstick: [ FEATURE ] - Estilizaçao CSS do formulario"</code>
      </td>
      <td>💄 [ FEATURE ] - Estilizaçao CSS do formulario</td>
    </tr>
    <tr>
      <td>
        <code>git commit -m ":test_tube: [ TEST ] - Criando novo teste"</code>
      </td>
      <td>🧪 [ TEST ] - Criando novo teste</td>
    </tr>
    <tr>
      <td>
        <code>git commit -m ":bulb: [ DOC ] - Comentários sobre a função LoremIpsum( )"</code>
      </td>
      <td>💡 [ DOC ] - Comentários sobre a função LoremIpsum( )</td>
    </tr>
  </tbody>
</table>

---

## 📝 Licença

Esse projeto está sob licença. Veja o arquivo [LICENCE](LICENSE) para mais detalhes.

---

## 🤝 Colaboradores

Agradecemos às seguintes pessoas que contribuíram para este projeto:

<table>
  <tr>
      <td align="center">
      <a href="#">
        <img src="https://avatars.githubusercontent.com/u/76502001?v=4" width="70px;" alt="Foto do Vinícius Tasso no GitHub"/><br>
        <sub>
          <b>Vinícius Tasso</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="#">
        <img src="https://avatars.githubusercontent.com/u/87236158?v=4" width="70px;" alt="Foto do Heitor Tasso no GitHub"/><br>
        <sub>
          <b>Heitor Tasso</b>
        </sub>
      </a>
    </td>
  </tr>
</table>

---

Para ver quantidade de linhas do código no Visual Studio Code:
 - `(gci -include *.kv,*.py -recurse | select-string .).Count`

---

# Build to PYPI

 - `python setup.py sdist`
 - `twine upload dist/*`

