import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
    <h1>Refine Your Email!</h1>
    <form className="form" id="form">
        <div>
            <label htmlFor='tone'>Tone</label>
            <select id="tone" name="tone">
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
        <textarea id="email" name="email" rows="20" cols="100" placeholder="paste your email"></textarea>
        <div>
            <button id="submit">Submit</button>
            <button id="checkOutput">Check Output</button>
            
        </div>
    </form>
    </>
  )
}

export default App
