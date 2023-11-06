// const socket = new WebSocket('ws://localhost:8888'); 

// socket.addEventListener('open', (event) => { 
//   socket.send('Hello Server!'); 
// }); 

// socket.addEventListener('message', (event) => { 
//   console.log('Message from server ', event.data); 
// });

// socket.addEventListener('close', (event) => { 
//   console.log('The connection has been closed'); 
// });

const socket = new WebSocket('ws://localhost:8888/websocket');

socket.onopen = () => {
  console.log('Подключено к серверу WebSocket');

  // Отправка сообщения на сервер
  socket.send('Привет, сервер!');
};
// Обработка сообщений от сервера
socket.onmessage = (event) => {
  console.log('Получено сообщение от сервера:', event.data);
};

socket.onclose = () => {
  console.log('Отключено от сервера WebSocket');
};