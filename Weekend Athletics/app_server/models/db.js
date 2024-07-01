const mongoose = require('mongoose');
const host = process.env.DB_HOST || '127.0.0.1';
const dbURI = `mongodb://${host}/weekend_athletics`;
const readLine = require('readline');

//build the connection string and set connection timeout
const connect = ()=>{
    setTimeout(() => mongoose.connect(dbURI, {}), 1000);
}

//Monitor connection events
mongoose.connection.on('connected', ()=>{
    console.log(`Mongoose connected to ${dbURI}`);
});

mongoose.connection.on('error', err=>{
    console.log('Mongoose connection error: ', err);
});

mongoose.connection.on('disconnected', ()=>{
    console.log('Mongoose disconnected');
});

//Windows listener
if(process.platform === 'win32'){
    const r1 = readLine.createInterface({
        input: process.stdin,
        output: process.stdout
    });
    r1.on('SIGINT', ()=>{
        process.emit("SIGINT");
    });
}

//Configure Graceful Shutdown
const gracefulShutdown = (msg) =>{
    mongoose.connection.close(()=>{
        console.log(`Mongoose disconnected through ${msg}`);
    });
};

//Event listeners for Graceful Shutdown
process.once('SIGUSR2', ()=>{
    gracefulShutdown('nodemon restart');
    process.kill(process.pid, 'SIGUSR2');
});

//Shutdown invoked by app termination
process.on('SIGINT', ()=>{
    gracefulShutdown('app termination');
    process.exit(0);
});

//Shutdown invoked by container termination
process.on('SIGTERM', ()=>{
    gracefulShutdown('app shutdown');
    process.exit(0);
});

//Make initial connection
connect();

//Import Mongoose Schema
require('./articles');
module.exports = mongoose;
