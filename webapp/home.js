const form = document.getElementById('form')
let email;
const get_email = (event) => 
{
    event.preventDefault();
   
    email = document.getElementById('email').value;

    console.log(email);

    alert("email submitted: " + email);
}

form.addEventListener('submit',get_email);
