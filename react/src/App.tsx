import React, { useState, Suspense } from 'react'
import './App.css'
const Login = React.lazy(() => import('./Components/Login'));

const reactLogo = "react.svg"
const viteLogo = "vite.svg"
const reactLogoPath = `/static/logo/${reactLogo}` as string
const viteLogoPath = `/static/logo/${viteLogo}` as string

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <Suspense fallback={<div>Loading ...</div>}>
        <section>
          <Login />
          <div>
            <a href="https://vitejs.dev" target="_blank">
              <img src={viteLogoPath} className="logo" alt="Vite logo" />
            </a>
            <a href="https://react.dev" target="_blank">
              <img src={reactLogoPath} className="logo react" alt="React logo" />
            </a>
            <h1>Vite + React</h1>
            <div className="card">
              <button onClick={() => setCount((count) => count + 1)}>
                count is {count}
              </button>
              <p>
                Edit <code>src/App.tsx</code> and save to test HMR
              </p>
            </div>
            <p className="read-the-docs">
              Click on the Vite and React logos to learn more
            </p>
          </div>
        </section>
      </Suspense>
    </>
  )
}

export default App
