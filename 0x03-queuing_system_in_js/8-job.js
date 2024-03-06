const kue = require('kue');
const queue = kue.createQueue();
function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }
  for (var i = 0; i < jobs.length; i++) {
    var job = queue.create('push_notification_code_3', jobs[i])
      .save(() => console.log('Notification job created:', job.id))
      .on('complete', () => console.log(`Notification job ${job.id} completed`))
      .on('failed', (err) => console.log(`Notification job ${job.id} failed: ${err}`))
      .on('progress', (perc) => console.log(`Notification job ${job.id} ${perc}% complete`));
  }
}

module.exports = createPushNotificationsJobs;
