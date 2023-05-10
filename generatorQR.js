// Importa a biblioteca
const QRCode = require('qrcode-generator');

// Define o texto que será codificado no QR Code
const texto = 'Exemplo de texto';

// Cria um novo QR Code com o nível de correção Q e o modo de codificação Byte
const qr = QRCode(0, 'Q');
qr.addData(texto);
qr.make();

// Imprime a imagem do QR Code em ASCII art
console.log(qr.createASCII(2));
