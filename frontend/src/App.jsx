import { useState } from 'react'
import './App.css'



function App() {
  const [uuid, setUuid] = useState("");
  const [firstFetchSuccess, setFirstFetchSuccess] = useState(false);
  const [tone, setTone] = useState("friendly");
  const [emailText, setEmailText] = useState("");
  const [result, setResult] = useState("");

  }

  return (
    <>
    <h1>Refine Your Email!</h1> 
    <form className="form" id="form">
        <div>
            <label htmlFor='tone'>Tone</label>
            
            <select id="tone" name="tone" value={tone} onChange={(t) => setTone(t.target.value)}>
                <option value="enticing">Enticing</option>
                <option value="formal">Formal</option>
                <option value="friendly">Friendly</option>
                <option value="apologetic">Apologetic</option>
                <option value="enthusiastic">Enthusiastic</option>
                <option value="angry">Angry</option>
                <option value="funny">Funny</option>
                <option value="childish">Childish</option>
            </select>


        </div>

        <label id="your-email">Your Email:</label><br/>
        <textarea id="email" name="email" rows="20" cols="100" placeholder="paste your email" value={emailText} onChange={(e) => setEmailText(e.target.value)}></textarea>

        <div>
            <button id="submit" onClick={callFetch}>Submit</button>
            <button id="checkOutput" onClick={extractNewEmail}>Check Output</button>
            
        </div>
    </form>

    {
    result && //means --> if result has a value do x
      ( 
        <div className="output">
          <h2>Improved Email:</h2>
          <p>{result}</p>
        </div>
      )
    }

    </>
  )
}

export default App




async function extractNewEmail(e) {
  e.preventDefault();
  if (!firstFetchSuccess) {
    console.log("not ready yet");
    return;
  }

  try {
    const res = await fetch('http://127.0.0.1:5000/api/output', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ uuid }),
    });

    if (!res.ok) throw new Error(`HTTP error! status: ${res.status}`);
    const json_email = await res.json();
    alert(json_email.new_email);
    setResult(json_email.new_email);
  } catch (err) {
    console.error("Fetch error:", err);
  }
}


// form.addEventListener('submit',main);
// output_button.addEventListener('click',extract_new_email)


async function callFetch() {
  const fullEmail = `${tone}\n${emailText}`;
  try {
    const res = await fetch('http://127.0.0.1:5000/api/main-input', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email: fullEmail }),
    });

    if (!res.ok) throw new Error(`HTTP error! status: ${res.status}`);
    const data = await res.json();
    setUuid(data.id);
    setFirstFetchSuccess(true);
    console.log("main-input finished");
  } catch (err) {
    console.error('Fetch error:', err);
  }
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
        throw new Error(`HTTP error status ${response.status}`)
    }
      
    console.log("response verified");
    return response;
}

const handle_fetch_error = (error) =>
{
    console.error('Fetch error: ', error);
}
