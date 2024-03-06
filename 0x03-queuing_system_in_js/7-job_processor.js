var blacklist = ['4153518780', '4153518781'];

function sendNotification(phoneNumber, message, job, done) {
  for (var i = 0; i <= 100; i++) {
    if (i == 0) {
      job.progress(0, 100);
      if (blacklist.includes(phoneNumber)) {
        return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
      }
    } else if (i == 50){
      job.progress(50, 100);
      console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    }
  }
  done();
}

const kue = require('kue');
const queue = kue.createQueue();
queue.process('push_notification_code_2', 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
