const redis = require('redis');
import { createClient } from 'redis';
import { promisify } from 'util';

const client = createClient();

client.on('error', err => console.log('Redis client not connected to the server:', err));

client.on('connect', () => console.log('Redis client connected to the server'));

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

const asyncGet = promisify(client.get).bind(client);
async function displaySchoolValue(schoolName) {
  asyncGet(schoolName).then((res) => {
    console.log(res);
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
