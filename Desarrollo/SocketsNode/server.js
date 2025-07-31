const { Server } = require('net');

const host = "0.0.0.0";
const END = 'END';

const connections = new Map();

const error = (message) => {
    console.error(message);
    process.exit(1);
}

const sendMessage = (message, origin) => {
    // Mandar a todos menos origin el message
}

const listen = (port) => {
    const server = new Server();
    server.on("connection", (socket) => {
        const remoteSocket = `${socket.remoteAddress}:${socket.remotePort}`;
        console.log(`New connection from ${remoteSocket}`);
        socket.setEncoding('utf-8');
        
        socket.on("data", (message) => {
            if(!connections.has(socket)){
                console.log(`Username ${message} set for connection ${remoteSocket}`);
                connections.set(socket, message);
            }else if(message === END){
                socket.end();
            }else{
                // Enviar el message al resto de usuarios
                console.log(`${remoteSocket} -> ${message}`);
            }
            });
            
            socket.on("close", () => {
                console.log(`Connection with ${remoteSocket} closed`)
            });
        });

        server.listen({ port, host }, () =>{
            console.log(`Listening on port ${port}`)
        });

        server.on("error", (err) => error(err.message));
}

const main = () => {
    if(process.argv.length !== 3) {
        error(`Usage: node ${__filename} port`);
    }

    let port = process.argv[2];
    if(NaN(port)) {
        error(`Invalid port ${port}`);
    }

    port = Number(port);

    listen(port);
}

if( require.main === module){
        main();
}
