const btn = document.getElementById('button');
const notify = document.getElementById('status');

document.getElementById('form')
 .addEventListener('submit', function(event) {
   event.preventDefault();

   btn.value = 'Sending...';

   const serviceID = 'vv';
   const templateID = 'template_pink';

   emailjs.sendForm(serviceID, templateID, this)
    .then(() => {
      btn.value = 'Send';
      alert('Mail is sent successfully');
    }, (err) => {
      btn.value = 'Send';
      alert(JSON.stringify(err));
    });
});