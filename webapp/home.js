const form = document.getElementById('form')
let email;
const main = (event) => 
{
    event.preventDefault();
    email = document.getElementById('email').value;
    const length = email.length;
    console.log("works " + length);
    if (length> 1500)
    {
        alert("Email exceeds character limit of 1000 characters, current length: " + length);
        return;
    }

    call_fetch();
}

form.addEventListener('submit',main);

const call_fetch = () =>
{
fetch('http://localhost:5000/api/home',
            {
            method: 'POST',
            headers: {'Content-Type' : 'application/json'},
            body: JSON.stringify({email: email})
            }
        )
    .then(jsonify)
    .then(use_data)
    .catch(handle_fetch_error);
}

const use_data = (data) =>
{
   
    console.log('Success: ', data);
    alert(data.new_email);
}

const jsonify = (response) =>
{
    if (!response.ok) 
        throw new Error("Something went wrong: " + response.status);
    return response.json();
}

const handle_fetch_error = (error) =>
{
    console.error('Fetch error: ', error);
}
