# 🛡️ Projeto Educacional: Keylogger e Ransomware em Python

> ⚠️ **Aviso Legal Importante**

Este projeto foi desenvolvido **exclusivamente para fins educacionais**, como parte de estudos em cibersegurança. O uso indevido deste código — como aplicação em sistemas de terceiros sem consentimento — **constitui crime** previsto no **Art. 154-A do Código Penal Brasileiro**, que trata da **invasão de dispositivo informático**.

> **Art. 154-A**: Invadir dispositivo informático alheio, conectado ou não à rede de computadores, mediante violação indevida de mecanismo de segurança e com o fim de obter, adulterar ou destruir dados ou informações sem autorização do titular do dispositivo.

---

## ❗ Termos de Uso

- Este projeto **não deve ser utilizado em ambientes reais ou contra terceiros**.
- O autor **não se responsabiliza por qualquer uso indevido** do código aqui disponibilizado.
- O código **não está pronto para uso imediato** — requer ajustes, testes e configuração adequada para funcionar corretamente.

---

## 🧪 Objetivo

Este repositório contém dois scripts em Python:

1. **Keylogger**: Captura teclas digitadas e envia por e-mail.
2. **Ransomware Simples**: Criptografa arquivos locais como simulação de ataque.

Ambos os scripts foram desenvolvidos para fins **didáticos**, com foco em entender técnicas ofensivas para melhor desenvolver defesas.

---

## 🛠️ Requisitos

Antes de executar os scripts, instale as bibliotecas necessárias com:

```bash
pip install pynput cryptography
```

⚙️ Observações
Testado em ambiente Kali Linux via VirtualBox.

O envio de e-mails pode exigir configuração de senha de app no Gmail.

O ransomware simula criptografia com Fernet e não realiza propagação ou persistência.

Talvez seu anti-vírus não deixe o projeto ser executado ou mostre erros/ameaças.

📚 Referências
Documentação oficial do Python: https://docs.python.org/3/

Cryptography.io: https://cryptography.io/

pynput: https://pypi.org/project/pynput/

Art. 154-A do Código Penal: https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2012/lei/l12737.htm

👨‍💻 Autor
Projeto desenvolvido por Vagner Guimarães Carneiro como parte de Estudos em Cibersegurança.
