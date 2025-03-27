import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Form from './components/Form'
import WorkExperienceList from './components/WorkExperience'

function App() {
  const [count, setCount] = useState(0)
  const [experience, setExperience] = useState([])

  return (
    <>
    <h1>CV Builder</h1>
      <Form />
      <WorkExperienceList />
    </>
  )
}



export default App
