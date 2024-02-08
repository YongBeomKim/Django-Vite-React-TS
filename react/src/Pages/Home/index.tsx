import { useState } from 'react'

const reactLogo = "react.svg"
const viteLogo = "vite.svg"
const reactLogoPath = `/static/logo/${reactLogo}` as string
const viteLogoPath = `/static/logo/${viteLogo}` as string


const Home = () => {
  const [count, setCount] = useState(0)
  return (
    <div>
      <a href="https://vitejs.dev" target="_blank">
        <img src={viteLogoPath} className="logo" alt="Vite logo" />
      </a>
      <a href="https://react.dev" target="_blank">
        <img src={reactLogoPath} className="logo react" alt="React logo" />
      </a>
      <h1>Vite + React</h1>
      <div className="bg-red-500">
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
  )
}

export default Home