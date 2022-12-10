# Distaste
### Backend do app Wandinha, a lua e um gato preto
***
Frontend feito pela 
[Jailane](https://github.com/Jailane-barboza), vulgo Nina,
em um app desktop feito com Electron.js.

## Projeto
O Distaste é uma API com o objetivo de retornar ao usuário
informações a respeito do horário baseado na região
fornecida.

## Tecnologias Utilizadas
- Python
- FastAPI
- Deta (deploy)

## Uso
**Url: _https://distaste.deta.dev_**

Fazer requisição do tipo POST para essa url na rota __*/time*__.

### Importante:
- Essa API precisa de uma senha de acesso passada no header na chave "AuthDistaste",
que vai ser utilizada pelo app.

```json
{
  "Content-Type": "application/json",
  "Accept": "application/json",
  "AuthDistaste": "*****"
}
```

- No corpo da requisição, passar a região para conseguir as informações de horário
corretas.

Ex.:

```json
{
  "region": "America/Manaus"
}
```

## Exemplo
Exemplo de uso usando a linguagem JavaScript:

```javascript
async function getTime(region, auth) {
    const headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'AuthDistaste': auth
    };
    
    const data = {
        'region': region
    };
    
    const options = {
        method: 'POST',
        headers: headers,
        body: JSON.stringify(data)
    };

    const res = await fetch('https://distaste.deta.dev/time', options);
    const json = await res.json();
    
    console.log(json.body);
} 
```

Executando essa função às 18h01m27s do dia 9 de dezembro em Manaus, passando
os parâmetros certos, a saída no console será:

```json
{
  "ano": 2022,
  "dia": 9,
  "hora": 18,
  "mes": 12,
  "minuto": 1,
  "segundo": 27
}
```
