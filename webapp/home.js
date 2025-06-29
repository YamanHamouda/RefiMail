const form = document.getElementById('form')
const output_button = document.getElementById('checkOutput')
let email;
let new_email;
let first_fetch_success = false;
const main = (event) => 
{
    event.preventDefault();
    email = document.getElementById('email').value;
    const length = email.length;
    console.log("email length: " + length);
    if (length > 1500)
    {
        alert("Email exceeds character limit of 1000 characters, current length: " + length);
        return;
    }
    
    call_fetch();

}


const extract_new_email = (event) =>
{
    event.preventDefault();
    if (!first_fetch_success)
    {
        console.log("not ready yet");
        return;
    }
    console.log("calling 2nd fetch");
    fetch('http://127.0.0.1:5000/api/output',
        {
            method: 'POST',
            headers: {'Content-Type' : 'application/json'},
        }
    )
    .then(jsonify)
    .then(handle_new_email)
    .catch(handle_fetch_error);
}

form.addEventListener('submit',main);
output_button.addEventListener('click',extract_new_email)


const call_fetch = () =>
{
    const tone =  document.getElementById("tone").value;
    console.log("the tone is " + tone + "\n" + email);
    console.log("calling fetch");   
    fetch('http://127.0.0.1:5000/api/main-input',
                {
                method: 'POST',
                headers: {'Content-Type' : 'application/json'},
                body: JSON.stringify({email: (tone + "\n" + email)}) ///// <--- here change enticing with dropdown variable name
                }
            )
        .then(isOk)
        .then(res => res.json())
        .then(response =>{ 
            console.log("/api/main-input finished");
            first_fetch_success=true;})
        .catch(handle_fetch_error);
}



const handle_new_email = (json_email) =>
{
    console.log("handling email");
    new_email = json_email.new_email;
    console.log(new_email);
    alert(new_email);
    console.log("email handled");
}

const jsonify = (response) =>
{
   isOk(response);
   const json_response = response.json();
   console.log("jsonified");
   return json_response;
   
}


const isOk = (response) =>
{
    console.log("verifying reponse...");
    if (!response.ok) 
    {
        console.log("verify failed...");
        throw new Error(`HTTP error status ${resonse.status}`)
    }
      
    console.log("response verified");
    return response;
}

const handle_fetch_error = (error) =>
{
    console.error('Fetch error: ', error);
}
